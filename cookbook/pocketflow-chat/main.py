from pocketflow import Node, Flow
from utils import call_llm

NUM_MSG = 2

class ChatNode(Node):
    def prep(self, shared):
        # Initialize messages if this is the first run
        if "messages" not in shared:
            shared["messages"] = []
            print("Welcome to the chat! Type 'exit' to end the conversation.")
        
        num_msg = shared.get("num_msg", (2*NUM_MSG+1))
        # Get user input
        user_input = input("\nYou: ")
        
        # Check if user wants to exit
        if user_input.lower() in ['exit', 'bye', 'quit']:
            return None
        
        # Add user message to history
        shared["messages"].append({"role": "user", "content": user_input})
        
        # Return all messages for the LLM
        return shared["messages"][-num_msg:]

    def exec(self, messages):
        if messages is None:
            return None
        
        msg = "\n\t".join([str(m) for m in messages])
        print(f"""[messages]\n\t{msg}""")

        # Call LLM with the entire conversation history
        response = call_llm(messages)
        return response

    def post(self, shared, prep_res, exec_res):
        if prep_res is None or exec_res is None:
            print("\nGoodbye!")
            return None  # End the conversation
        
        # Print the assistant's response
        print(f"\nAssistant: {exec_res}")
        
        # Add assistant message to history
        shared["messages"].append({"role": "assistant", "content": exec_res})
        
        # Loop back to continue the conversation
        return "continue"

# Create the flow with self-loop
chat_node = ChatNode()
chat_node - "continue" >> chat_node  # Loop back to continue conversation

flow = Flow(start=chat_node)

# Start the chat
if __name__ == "__main__":
    shared = {"num_msg" : (2*NUM_MSG+1)}
    flow.run(shared)
