import asyncio
import click
from pocketflow import AsyncNode, AsyncFlow
from utils import call_llm


class AsyncHinter(AsyncNode):
    async def prep_async(self, shared):
        guess = await shared["hinter_queue"].get()
        if guess == "GAME_OVER":
            return None
        return shared["target_word"], shared["forbidden_words"], shared.get("past_guesses", [])

    async def exec_async(self, inputs):
        if inputs is None:
            return None
        target, forbidden, past_guesses = inputs
        prompt = f"Generate hint for '{target}'\nForbidden words: {forbidden}"
        if past_guesses:
            prompt += f"\nPrevious wrong guesses: {past_guesses}\nMake hint more specific."
        prompt += "\nUse at most 5 words."
        hint = call_llm(prompt)
        click.echo(f"\nHinter: Here's your hint - {hint}")
        return hint

    async def post_async(self, shared, prep_res, exec_res):
        if exec_res is None:
            return "end"
        await shared["guesser_queue"].put(exec_res)
        return "continue"


class AsyncGuesser(AsyncNode):
    async def prep_async(self, shared):
        hint = await shared["guesser_queue"].get()
        return hint, shared.get("past_guesses", [])

    async def exec_async(self, inputs):
        hint, past_guesses = inputs
        prompt = f"Given hint: {hint}, past wrong guesses: {past_guesses}, make a new guess. Directly reply a single word:"
        guess = call_llm(prompt)
        click.echo(f"Guesser: I guess it's - {guess}")
        return guess

    async def post_async(self, shared, prep_res, exec_res):
        if exec_res.lower() == shared["target_word"].lower():
            click.echo("Game Over - Correct guess!")
            await shared["hinter_queue"].put("GAME_OVER")
            return "end"
        if "past_guesses" not in shared:
            shared["past_guesses"] = []
        shared["past_guesses"].append(exec_res)
        await shared["hinter_queue"].put(exec_res)
        return "continue"


async def run_game(word, forbidden):
    shared = {
        "target_word": word,
        "forbidden_words": forbidden,
        "hinter_queue": asyncio.Queue(),
        "guesser_queue": asyncio.Queue(),
    }

    click.echo("=========== Taboo Game Starting! ===========")
    click.echo(f"Target word: {shared['target_word']}")
    click.echo(f"Forbidden words: {shared['forbidden_words']}")
    click.echo("============================================")

    await shared["hinter_queue"].put("")

    hinter = AsyncHinter()
    guesser = AsyncGuesser()
    hinter_flow = AsyncFlow(start=hinter)
    guesser_flow = AsyncFlow(start=guesser)
    hinter - "continue" >> hinter
    guesser - "continue" >> guesser

    await asyncio.gather(
        hinter_flow.run_async(shared),
        guesser_flow.run_async(shared),
    )

    click.echo("=========== Game Complete! ===========")


@click.command()
@click.option("--word", default="nostalgic", show_default=True,
              help="Target word the guesser must guess")
@click.option("--forbidden", default="memory,past,remember,feeling,longing",
              show_default=True, help="Comma-separated list of forbidden words")
def main(word, forbidden):
    """Play an async Taboo word-guessing game with two LLM agents."""
    forbidden_list = [w.strip() for w in forbidden.split(",")]
    asyncio.run(run_game(word, forbidden_list))


if __name__ == "__main__":
    main()
