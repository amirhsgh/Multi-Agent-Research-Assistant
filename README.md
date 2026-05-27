# 🔬 Multi-Agent Research Assistant

A production-ready AI research assistant powered by **LangGraph** that orchestrates multiple specialized agents to conduct comprehensive research on any topic.

The system automatically plans research, searches the web, synthesizes information, and generates detailed reports with critical analysis.

---

## 🎯 What is This Project?

This project is an autonomous multi-agent system that simulates how human researchers work.

The system:

- Plans the research by breaking complex topics into searchable subtasks
- Searches the web using advanced search APIs
- Synthesizes findings into coherent summaries
- Critiques the final report to ensure quality and completeness

Unlike simple chatbots, this system uses a graph-based workflow where multiple AI agents collaborate, each with a specialized role, to produce high-quality research reports automatically.

---

## ✨ Key Features

- 🤖 Multi-agent orchestration with LangGraph
- 🔍 Advanced web search via Tavily API
- 🧠 LLM-powered planning, summarization, and critique
- 📊 Stateful workflow execution
- 🎨 Interactive UI with Streamlit
- 🐳 Docker support for easy deployment
- 📝 Structured output with summaries, citations, and feedback
- 🧩 Modular architecture

---

## 🧠 Example Workflow

```
User Topic
   ↓
Planner Agent
   ↓
Search Agent
   ↓
Summarizer Agent
   ↓
Critic Agent
   ↓
Final Research Report
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      User Input / Topic                     │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │    Planner Agent     │
              │   GPT-4 / Claude     │
              │                      │
              │  Breaks topic into   │
              │  research subtasks   │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Research Plan      │
              │  [Q1, Q2, Q3, ...]   │
              └──────────┬───────────┘
                         │
                         ▼
            ┌────────────┴────────────┐
            │   For Each Subtask      │
            │                         │
            │  ┌────────────────────┐ │
            │  │   Search Agent     │ │
            │  │     Tavily API     │ │
            │  └─────────┬──────────┘ │
            │            │            │
            │            ▼            │
            │  ┌────────────────────┐ │
            │  │ Summarizer Agent   │ │
            │  │   GPT-4 / Claude   │ │
            │  └─────────┬──────────┘ │
            └────────────┼────────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │  Combined Summaries  │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │    Critic Agent      │
              │   GPT-4 / Claude     │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │    Final Report      │
              │    + Critique        │
              └──────────────────────┘
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/amirhsgh/Multi-Agent-Research-Assistant.git
cd Multi-Agent-Research-Assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 5. Run the Application

```bash
# CLI mode
python main.py

# Streamlit UI
streamlit run app.py
```

---

## 🧪 Sample Output

**Input:** *Future of AI agents in software engineering*

**Generated Research Plan:**

1. Current AI coding assistants
2. AI-driven software testing
3. Autonomous software agents
4. Risks and limitations
5. Future trends

**Final Report (snippet):**

> AI agents are increasingly transforming software engineering workflows. Tools such as GitHub Copilot and autonomous coding agents are improving developer productivity through code generation, testing, and debugging. However, challenges remain regarding reliability, hallucinations, security vulnerabilities, and maintainability.

---

## 🛠️ Tech Stack

- **Core Frameworks:** LangGraph · LangChain
- **LLM Providers:** OpenAI GPT-4 · Anthropic Claude
- **Search & Retrieval:** Tavily Search API
- **Backend:** Python 3.11+
- **UI:** Streamlit
- **Utilities:** Rich · Pydantic · python-dotenv
- **DevOps:** Docker

---

## 📂 Project Structure

```
multi-agent-research-assistant/
├── src/
│   ├── agents/
│   │   ├── planner.py
│   │   ├── searcher.py
│   │   ├── summarizer.py
│   │   └── critic.py
│   ├── utils/
│   │   └── logger.py
│   ├── state.py
│   └── workflow.py
├── app.py
├── main.py
├── requirements.txt
├── Dockerfile
├── .env.example
└── README.md
```

---

## 🗺️ Roadmap

**Phase 1 — Core System ✅**
- Multi-agent workflow
- Web search integration
- Report generation
- Streamlit UI

**Phase 2 — Improvements 🚧**
- Async agent execution
- Better state persistence
- Retry and error recovery
- Structured JSON outputs
- Citation generation

**Phase 3 — Advanced Features 🔮**
- Vector database memory
- Human-in-the-loop review
- Multi-LLM routing
- PDF export
- Real-time streaming responses

---

## 🐳 Docker Support

```bash
docker build -t research-assistant .
docker run --env-file .env research-assistant
```

---

## 📜 License

MIT License.

---

## 👤 Author

**Amirhossein Ghavi** — AI Engineer
📧 amiqavi2601@gmail.com · 💼 [LinkedIn](https://www.linkedin.com/in/amirhossein-ghavi/) · 🌍 Open to remote roles (EU)
