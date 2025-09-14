# 🧑‍🤝‍🧑 Multi-Agentic AI Systems with CrewAI & OpenAI LLM  

This repository contains two **multi-agent AI systems** built using [CrewAI](https://github.com/joaomdmoura/crewAI) and **OpenAI LLMs**.  
Both systems demonstrate **inter-agent collaboration**, asynchronous task execution, and practical use cases of multi-agent orchestration.  

---

## 📌 Projects Included
### 1️⃣ Event Planner Crew  
An AI-powered system where multiple agents collaborate to **plan and manage events**.  
- Agents handle **venue coordination, logistics, and marketing**.  
- Demonstrates **parallel execution** and **decision-making**.  

### 2️⃣ Resume Tailoring Crew  
A system where agents collaborate to **tailor resumes** based on job descriptions.  
- Agents analyze job postings.  
- Suggest improvements to resumes.  
- Output is a **job-specific resume draft**.  

---

## 📂 Repository Structure
├── utils.py # Shared utilities (logging, helpers, configs)
├── event_plan.py # Event Planner Crew implementation
├── resume_tailor.py # Resume Tailor Crew implementation
├── requirements.txt # Python dependencies
└── README.md # Project documentation

🔧 Example Workflow

Event Planner Crew

User defines event details (date, type, budget).

Agents collaborate to propose venue, logistics plan, and marketing strategy.

Final structured plan is output.

Resume Tailor Crew

User provides a base resume + job description.

Agents analyze job posting keywords and adjust resume accordingly.

Output: tailored resume draft.

📦 Dependencies

Python 3.10+

CrewAI

OpenAI

Pydantic

python-dotenv

(See requirements.txt for full list.)

📖 Learnings

Hands-on experience in multi-agent collaboration.

Usage of CrewAI with OpenAI LLMs.

Designing reusable utilities (utils.py) for agent workflows.

Handling asynchronous tasks and structured outputs.

🔗 References

DeepLearning.AI – Building Multi-Agentic AI Systems

CrewAI Documentation
