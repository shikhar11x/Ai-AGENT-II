from tools.calculator import execute as calculator
from tools.time_tool import execute as time_tool
from tools.weather import execute as weather
from tools.currency import execute as currency
from tools.wikipedia import execute as wikipedia
from tools.web_search import execute as web_search

TOOLS = {
    "calculator": calculator,
    "time": time_tool,
    "weather": weather,
    "currency": currency,
    "wikipedia": wikipedia,
    "web_search": web_search,
}


def execute_tool(tool_name: str, arguments: dict):
    tool = TOOLS.get(tool_name)
    if tool is None:
        return f"Unknown Tool: {tool_name}"
    return tool(arguments)


def list_tools():
    return list(TOOLS.keys())


if __name__ == "__main__":
    print("Registered Tools\n")
    print(execute_tool("calculator", {"expression": "25*18"}))
    print("\n")
    print(execute_tool("time", {}))
    print("\n")
    print(execute_tool("weather", {"city": "delhi"}))