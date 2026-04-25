import os
from pathlib import Path # Import the Path class
import re

from openai import OpenAI

def call_llm(prompt):    
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "your-api-key"))
    r = client.chat.completions.create(
        model="gpt-4o-mini",  # "gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return r.choices[0].message.content

def write_file(topic="", content="", style="draft", out_dir="output"):
    """
    Write <content> data to an output file named as:
        "<out_dir>/<style>-<reformated-topic>.md"

    where <reformated-topic> string has any special character replaced with "-".
    """
    if not content:
        print(f"No content provided for topic: {topic}. Skipping file write.")
        return

    # 1. Reformat the topic string (logic remains the same)
    reformated_topic = topic.lower()
    reformated_topic = reformated_topic.replace(" ", "-")
    reformated_topic = re.sub(r'[^\w-]+', '-', reformated_topic)
    reformated_topic = re.sub(r'-+', '-', reformated_topic)
    reformated_topic = reformated_topic.strip('-')

    if not reformated_topic:
        reformated_topic = "untitled" # Provide a default name
        topic = "Untitled"

    # 2. Construct the filename and the full path using pathlib
    filename = f"{style}-{reformated_topic}.md"
    output_dir_path = Path(out_dir)
    full_path = output_dir_path / filename

    # 3. Ensure the output directory exists using pathlib
    try:
        output_dir_path.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory {output_dir_path}: {e}")
        return # Exit if directory cannot be created

    # 4. Write the content to the file using pathlib's write_text
    try:
        full_path.write_text(f"# {topic}\n\n{content}", encoding='utf-8')
        print(f"Successfully wrote content for '{topic}' to {full_path}")
    except (IOError, OSError) as e: # Catch potential file system errors
        print(f"[Error] failed to write {full_path}:\n {e}")

# Example usage
if __name__ == "__main__":
    print(call_llm("Tell me a short joke")) 