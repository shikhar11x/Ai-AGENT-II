import json
import os

# Vercel ka filesystem read-only hota hai, sirf /tmp writable hai.
# Local pe data/ folder use hoga, Vercel pe /tmp
if os.environ.get("VERCEL"):
    MEMORY_FILE = "/tmp/memory.json"
else:
    MEMORY_FILE = "data/memory.json"


def load_memory() -> list:
    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except Exception:
        return []


def save_memory(memory: list) -> None:
    folder = os.path.dirname(MEMORY_FILE)
    if folder:
        os.makedirs(folder, exist_ok=True)

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, ensure_ascii=False, indent=4)


def add_message(memory: list, role: str, content: str) -> None:
    memory.append(
        {
            "role": role,
            "content": content
        }
    )
    return memory


if __name__ == "__main__":
    print("Loading memory...")
    memory = load_memory()

    print(memory)

    print("\nAdding messages...")

    memory = add_message(memory, "user", "Hello, how are you?")
    memory = add_message(memory, "assistant", "I'm good, thank you!")

    save_memory(memory)
    print(load_memory())