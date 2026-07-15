<div align="center">

# AGENTIC AI

### Autonomous AI Agent powered by Groq Llama 3.3

<img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask">
<img src="https://img.shields.io/badge/Groq-Llama%203.3-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Operational-success?style=for-the-badge">

<br><br>

<a href="https://shikhar-ai-agent-v2.vercel.app/">
<img src="https://img.shields.io/badge/Live%20Demo-Open-success?style=for-the-badge">
</a>

<a href="https://github.com/shikhar11x">
<img src="https://img.shields.io/badge/GitHub-shikhar11x-181717?style=for-the-badge&logo=github">
</a>

<a href="https://www.linkedin.com/in/shikhar11x/">
<img src="https://img.shields.io/badge/LinkedIn-Shikhar%20Bajpai-0A66C2?style=for-the-badge&logo=linkedin">
</a>

</div>

---

# Overview

Agentic AI is an autonomous AI assistant capable of understanding natural language, invoking tools dynamically, maintaining conversational memory, and interacting through a futuristic terminal-inspired web interface.

---

# Features

| Status | Feature |
|:------:|---------|
| ✓ | AI Chat Assistant |
| ✓ | Groq Llama 3.3 Integration |
| ✓ | Tool Calling |
| ✓ | Persistent Memory |
| ✓ | Calculator |
| ✓ | Weather Tool |
| ✓ | Currency Converter |
| ✓ | Wikipedia Search |
| ✓ | Date & Time |
| ✓ | Flask REST API |
| ✓ | Terminal UI |
| ✓ | Vercel Deployment |

---

# Architecture

```
User
   │
   ▼
Web Interface
   │
   ▼
Flask API
   │
   ▼
Agent
   │
 ┌─┼───────────────┐
 │ │ │ │ │
 ▼ ▼ ▼ ▼ ▼
LLM Memory Parser Tools
             │
      ┌──────┼──────────────┐
      ▼      ▼      ▼       ▼
 Calculator Weather Currency Wikipedia
```

---

# Technology Stack

| Layer | Technology |
|--------|------------|
| Language | Python |
| Backend | Flask |
| AI | Groq API |
| Model | Llama 3.3 70B |
| Frontend | HTML • CSS • JavaScript |
| Deployment | Vercel |

---

# Folder Structure

```text
api/
static/
tools/
data/

agent.py
app.py
config.py
llm.py
memory.py
parser.py
prompts.py
requirements.txt
vercel.json
```

---

# Installation

```bash
git clone https://github.com/shikhar11x/Ai-AGENT-II.git

cd Ai-AGENT-II

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python app.py
```

---

# Environment Variables

```env
GROQ_API_KEY=YOUR_API_KEY
```

---

# API

POST `/chat`

```json
{
  "message":"Weather in Delhi"
}
```

Response

```json
{
  "response":"Current weather..."
}
```

---

# Screenshots

Replace these with your screenshots.

<img src="images/home.png">

<img src="images/chat.png">

---

# Connect

<a href="https://github.com/shikhar11x">
<img src="https://img.shields.io/badge/GitHub-shikhar11x-181717?style=for-the-badge&logo=github">
</a>

<a href="https://www.linkedin.com/in/shikhar11x/">
<img src="https://img.shields.io/badge/LinkedIn-Shikhar%20Bajpai-0A66C2?style=for-the-badge&logo=linkedin">
</a>
