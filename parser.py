import json
import re


def _extract_json_candidates(text: str):
    """
    Find all substrings that look like top-level JSON objects,
    even if surrounded by other text. Handles nested braces correctly.
    """
    candidates = []
    depth = 0
    start = None

    for i, ch in enumerate(text):
        if ch == '{':
            if depth == 0:
                start = i
            depth += 1
        elif ch == '}':
            if depth > 0:
                depth -= 1
                if depth == 0 and start is not None:
                    candidates.append(text[start:i + 1])
                    start = None

    return candidates


def parse_tool_call(response: str):
    if not response:
        return None

    # Fast path: the whole response is clean JSON (ideal case)
    try:
        tool_request = json.loads(response.strip())
        if isinstance(tool_request, dict) and isinstance(tool_request.get("tool"), str):
            return tool_request
    except json.JSONDecodeError:
        pass
    except Exception:
        pass

    # Fallback: model added explanation text around the JSON —
    # scan for any embedded {...} block that parses as a valid tool call.
    for candidate in _extract_json_candidates(response):
        try:
            tool_request = json.loads(candidate)
        except Exception:
            continue

        if isinstance(tool_request, dict) and isinstance(tool_request.get("tool"), str):
            return tool_request

    return None


if __name__ == "__main__":
    # Clean JSON
    test_response = '{"tool": "calculator", "input": "2 + 2"}'
    print(parse_tool_call(test_response))

    # JSON with explanation text around it (the real-world messy case)
    messy_response = '''It appears there is no info available. Let me search the web.
    {
        "tool":"web_search",
        "query":"Cockroach Janta Party"
    }'''
    print(parse_tool_call(messy_response))

    # No tool call at all
    print(parse_tool_call("The capital of France is Paris."))