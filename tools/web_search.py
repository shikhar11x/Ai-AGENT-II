from ddgs import DDGS


def execute(arguments: dict) -> str:
    query = arguments.get("query") or arguments.get("q") or arguments.get("search")

    if not query:
        return "Web search error: query required"

    try:
        results = DDGS().text(query, max_results=5)

        if not results:
            return f"No web results found for '{query}'"

        formatted = []
        for i, r in enumerate(results, start=1):
            title = r.get("title", "No title")
            snippet = r.get("body", "")
            link = r.get("href", "")
            formatted.append(f"{i}. {title}\n{snippet}\nSource: {link}")

        return "\n\n".join(formatted)

    except Exception as e:
        return f"Web search error: {e}"


if __name__ == "__main__":
    print(execute({"query": "latest AI news today"}))