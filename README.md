```markdown
# 🔬 Multi-Agent Research Assistant

A production-ready AI research assistant powered by LangGraph that orchestrates multiple specialized agents to conduct comprehensive research on any topic. The system automatically plans research, searches the web, synthesizes information, and generates detailed reports with critical analysis.

---

## 🎯 What is This Project?

This is an autonomous multi-agent system that mimics how human researchers work:

1. **Plans** the research by breaking down complex topics into searchable subtasks
2. **Searches** the web using advanced search APIs to gather information
3. **Synthesizes** findings into coherent summaries
4. **Critiques** the final report to ensure quality and completeness

Unlike simple chatbots, this system uses a **graph-based workflow** where multiple AI agents collaborate, each with specialized roles, to produce high-quality research reports automatically.

### Key Features

- 🤖 **Multi-agent orchestration** with LangGraph
- 🔍 **Advanced web search** via Tavily API
- 🧠 **LLM-powered** planning, summarization, and critique
- 📊 **State management** for complex workflows
- 🎨 **Interactive UI** with Streamlit
- 🐳 **Docker support** for easy deployment
- 📝 **Structured output** with citations and feedback

---

## 🏗️ Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     User Input (Topic)                       │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Planner Agent      │
              │  (GPT-4/Claude)      │
              │                      │
              │ Breaks topic into    │
              │ 3-5 subtasks         │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Research Plan      │
              │  [Q1, Q2, Q3, ...]   │
              └──────────┬───────────┘
                         │
                         ▼
         ┌───────────────┴───────────────┐
         │      For Each Subtask:        │
         │                               │
         │  ┌─────────────────────┐     │
         │  │  Search Agent       │     │
         │  │  (Tavily API)       │     │
         │  │                     │     │
         │  │  Web search for     │     │
         │  │  current query      │     │
         │  └──────────┬──────────┘     │
         │             │                 │
         │             ▼                 │
         │  ┌─────────────────────┐     │
         │  │  Summarizer Agent   │     │
         │  │  (GPT-4/Claude)     │     │
         │  │                     │     │
         │  │  Synthesize results │     │
         │  │  into summary       │     │
         │  └──────────┬──────────┘     │
         │             │                 │
         └─────────────┼─────────────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │  All Summaries       │
            │  Combined            │
            └──────────┬───────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │   Critic Agent       │
            │   (GPT-4/Claude)     │
            │                      │
            │ Evaluates report     │
            │ Provides feedback    │
            └──────────┬───────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │   Final Report       │
            │   + Critique         │
            └──────────────────────┘

### State Flow Diagram


START
  │
  ├─→ [Planner Node] ──→ research_plan created
  │
  ├─→ [Search Node] ──→ search_results[i] added
  │
  ├─→ [Summarize Node] ──→ summaries[i] added
  │
  ├─→ [Decision: More subtasks?]
  │     │
  │     ├─→ YES ──→ [Increment Step] ──→ back to Search Node
  │     │
  │     └─→ NO ──→ [Finalize Node] ──→ final_report generated
  │
END

---

## 🚀 How to
```markdown
# 🔬 Multi-Agent Research Assistant

A production-ready AI research assistant powered by LangGraph that orchestrates multiple specialized agents to conduct comprehensive research on any topic.

---

## 🎯 What is This Project?

This project is an autonomous multi-agent system that simulates a real research workflow using AI agents.

The system:

- Breaks a topic into research subtasks
- Searches the web for relevant information
- Summarizes findings
- Generates a final research report
- Critiques the report quality automatically

### Example Workflow

```text
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

### Features

- Multi-agent orchestration with LangGraph
- Web research using Tavily API
- GPT-4 / Claude integration
- Stateful workflow execution
- Streamlit UI
- Docker support
- Modular architecture

---

# 🏗️ Architecture Diagram

text
┌──────────────────────────────┐
│         User Topic           │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│        Planner Agent         │
│  Creates research subtasks   │
└──────────────┬───────────────┘
               │
               ▼
      ┌──────────────────┐
      │  Research Plan   │
      └────────┬─────────┘
               │
               ▼
┌──────────────────────────────┐
│         Search Agent         │
│     Searches the web         │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       Summarizer Agent       │
│   Synthesizes information    │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│         Critic Agent         │
│ Evaluates final report       │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      Final Research Report   │
└──────────────────────────────┘

---

# 🚀 How to Run

## 1. Clone the repository

bash
git clone https://github.com/yourusername/multi-agent-research-assistant.git

cd multi-agent-research-assistant

---

## 2. Create virtual environment

bash
python -m venv venv

Activate it:

### Linux / macOS

bash
source venv/bin/activate

### Windows

bash
venv\Scripts\activate

---

## 3. Install dependencies

bash
pip install -r requirements.txt

---

## 4. Configure environment variables

Create a `.env` file:

env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key

---

## 5. Run the application

### CLI Mode

bash
python main.py

### Streamlit UI

bash
streamlit run app.py

---

# 📸 Screenshot / Demo

## Streamlit Interface

markdown
Add screenshot here:
assets/demo-ui.png

## Example GIF

markdown
Add demo GIF here:
assets/demo.gif

Suggested tools:
- ScreenToGif
- Kap
- OBS Studio

---

# 🧪 Sample Output

## Input

text
Future of AI agents in software engineering

---

## Generated Research Plan

text
1. Current AI coding assistants
2. AI-driven software testing
3. Autonomous software agents
4. Risks and limitations
5. Future trends

---

## Final Report Snippet

text
AI agents are increasingly transforming software engineering workflows.
Tools such as GitHub Copilot and autonomous coding agents are improving
developer productivity through code generation, testing, and debugging.

However, challenges remain regarding reliability, hallucinations,
security vulnerabilities, and maintainability.

Industry trends suggest future development environments will include
collaborative AI agents capable of end-to-end software delivery.

---

# 🛠️ Tech Stack

## Core Frameworks

- LangGraph
- LangChain

## LLM Providers

- OpenAI GPT-4
- Anthropic Claude

## Search & Retrieval

- Tavily Search API

## Backend

- Python 3.11+

## UI

- Streamlit

## Utilities

- Rich
- Pydantic
- python-dotenv

## DevOps

- Docker

---

# 📂 Project Structure

text
multi-agent-research-assistant/
│
├── src/
│   ├── agents/
│   │   ├── planner.py
│   │   ├── searcher.py
│   │   ├── summarizer.py
│   │   └── critic.py
│   │
│   ├── utils/
│   │   └── logger.py
│   │
│   ├── state.py
│   └── workflow.py
│
├── app.py
├── main.py
├── requirements.txt
├── Dockerfile
└── README.md

---

# 🗺️ Roadmap

## Phase 1 — Core System ✅

- [x] Multi-agent workflow
- [x] Web search integration
- [x] Report generation
- [x] Streamlit UI

---

## Phase 2 — Improvements 🚧

- [ ] Async agent execution
- [ ] Better state persistence
- [ ] Retry & error recovery
- [ ] Structured JSON outputs
- [ ] Citation generation

---

## Phase 3 — Advanced Features 🔮

- [ ] Vector database memory
- [ ] Human-in-the-loop review
- [ ] Multi-LLM routing
- [ ] PDF export
- [ ] Autonomous agent collaboration
- [ ] Real-time streaming responses

---

# 🐳 Docker Support

Build image:

bash
docker build -t research-assistant .

Run container:

bash
docker run --env-file .env research-assistant

---

# 📜 License

MIT License
