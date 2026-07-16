from llm import chat
from memory import load_memory, save_memory
from prompts import SYSTEM_PROMPT
from parser import parse_tool_call
from tools.registry import execute_tool

MAX_TOOL_STEPS = 4  # safety limit so the agent can't loop forever


class Agent:
    def run(self, user_input):
        memory = load_memory()

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]
        messages.extend(memory)
        messages.append({
            "role": "user",
            "content": user_input
        })

        llm_response = chat(messages)

        steps_taken = 0

        # Keep going as long as the model keeps requesting tools,
        # up to MAX_TOOL_STEPS times (prevents infinite loops).
        while steps_taken < MAX_TOOL_STEPS:
            tool_request = parse_tool_call(llm_response)

            if tool_request is None:
                # Model gave a final plain-text answer — we're done.
                break

            steps_taken += 1

            tool_name = tool_request.get("tool")
            arguments = tool_request.copy()
            arguments.pop("tool", None)

            print(f"\nTool_requested: {tool_name}")
            print(f"Arguments: {arguments}")

            tool_result = execute_tool(tool_name, arguments)
            print(f"Tool Result: {tool_result}")

            messages.append({
                "role": "assistant",
                "content": llm_response
            })
            messages.append({
                "role": "user",
                "content": (
                    f"Tool Result: {tool_result}\n"
                    "If this result answers the user's original question, "
                    "reply with a normal plain-text answer now. "
                    "If it does not (for example the tool found nothing), "
                    "you may request ONE more tool call in the same JSON "
                    "format to try a different approach (e.g. web_search)."
                )
            })

            llm_response = chat(messages)

        # llm_response is now the final natural-language answer
        memory.append({
            "role": "user",
            "content": user_input
        })
        memory.append({
            "role": "assistant",
            "content": llm_response
        })
        save_memory(memory)

        return llm_response


if __name__ == "__main__":
    agent = Agent()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = agent.run(user_input)
        print(f"Bot: {response}")