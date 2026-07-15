import sys
import traceback
from flask import Flask, request, jsonify, send_from_directory

from agent import Agent

app = Flask(__name__, static_folder="static", static_url_path="")

agent = Agent()


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(force=True)

        user_input = (data.get("message") or "").strip()

        if not user_input:
            return jsonify({"response": "Empty message"}), 400

        response = agent.run(user_input)

        return jsonify({
            "response": response
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "traceback": traceback.format_exc()
        }), 500


def run_cli():
    print("=" * 60)
    print("AI Agent")
    print("=" * 60)

    cli_agent = Agent()

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            break

        try:
            response = cli_agent.run(user_input)
            print(f"Bot: {response}")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    if "--cli" in sys.argv:
        run_cli()
    else:
        app.run(host="0.0.0.0", port=5000)