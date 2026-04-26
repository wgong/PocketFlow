import click
import yaml
from pocketflow import Node, Flow
from utils import call_llm, get_tools, call_tool


class GetToolsNode(Node):
    def prep(self, shared):
        click.echo("Getting available tools...")
        return "simple_server.py"

    def exec(self, server_path):
        return get_tools(server_path)

    def post(self, shared, prep_res, exec_res):
        shared["tools"] = exec_res
        tool_info = []
        for i, tool in enumerate(exec_res, 1):
            properties = tool.inputSchema.get("properties", {})
            required = tool.inputSchema.get("required", [])
            params = []
            for param_name, param_info in properties.items():
                param_type = param_info.get("type", "unknown")
                req_status = "(Required)" if param_name in required else "(Optional)"
                params.append(f"    - {param_name} ({param_type}): {req_status}")
            tool_info.append(
                f"[{i}] {tool.name}\n  Description: {tool.description}\n  Parameters:\n"
                + "\n".join(params)
            )
        shared["tool_info"] = "\n".join(tool_info)
        return "decide"


class DecideToolNode(Node):
    def prep(self, shared):
        tool_info = shared["tool_info"]
        question = shared["question"]
        prompt = f"""
### CONTEXT
You are an assistant that can use tools via Model Context Protocol (MCP).

### ACTION SPACE
{tool_info}

### TASK
Answer this question: "{question}"

## NEXT ACTION
Analyze the question, extract any numbers or parameters, and decide which tool to use.
Return your response in this format:

```yaml
thinking: |
    <your step-by-step reasoning about what the question is asking and what numbers to extract>
tool: <name of the tool to use>
reason: <why you chose this tool>
parameters:
    <parameter_name>: <parameter_value>
    <parameter_name>: <parameter_value>
```
IMPORTANT:
1. Extract numbers from the question properly
2. Use proper indentation (4 spaces) for multi-line fields
3. Use the | character for multi-line text fields
"""
        return prompt

    def exec(self, prompt):
        click.echo("Analyzing question and deciding which tool to use...")
        return call_llm(prompt)

    def post(self, shared, prep_res, exec_res):
        try:
            yaml_str = exec_res.split("```yaml")[1].split("```")[0].strip()
            decision = yaml.safe_load(yaml_str)
            shared["tool_name"] = decision["tool"]
            shared["parameters"] = decision["parameters"]
            shared["thinking"] = decision.get("thinking", "")
            click.echo(f"Selected tool: {decision['tool']}")
            click.echo(f"Extracted parameters: {decision['parameters']}")
            return "execute"
        except Exception as e:
            click.echo(f"Error parsing LLM response: {e}")
            click.echo(f"Raw response: {exec_res}")
            return None


class ExecuteToolNode(Node):
    def prep(self, shared):
        return shared["tool_name"], shared["parameters"]

    def exec(self, inputs):
        tool_name, parameters = inputs
        click.echo(f"Executing tool '{tool_name}' with parameters: {parameters}")
        return call_tool("simple_server.py", tool_name, parameters)

    def post(self, shared, prep_res, exec_res):
        shared["answer"] = exec_res
        click.echo(f"\nFinal Answer: {exec_res}")
        return "done"


def create_mcp_flow():
    get_tools_node = GetToolsNode()
    decide_node = DecideToolNode()
    execute_node = ExecuteToolNode()
    get_tools_node - "decide" >> decide_node
    decide_node - "execute" >> execute_node
    return Flow(start=get_tools_node)


@click.command()
@click.option("--question",
              default="What is 982713504867129384651 plus 73916582047365810293746529?",
              show_default=True, help="Question to answer using MCP tools")
@click.option("--out", default=None,
              help="File path to save the answer (e.g. output/answer.txt)")
def main(question, out):
    """Answer questions using MCP (Model Context Protocol) tools."""
    click.echo(f"Processing question: {question}")
    shared = {"question": question}
    create_mcp_flow().run(shared)

    if out and "answer" in shared:
        from pathlib import Path
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        Path(out).write_text(str(shared["answer"]), encoding="utf-8")
        click.echo(f"\nSaved to: {out}")


if __name__ == "__main__":
    main()
