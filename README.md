# Intelligent-Task-Mnanger
An Intelligent Agent developed for the CSA2001 (Fundamentals of AI and ML) course at VIT Bhopal.

 Project Overview
This project is an Intelligent Task Management Agent  that leverages Large Language Models (LLMs) and heuristic-based search strategies to help users maintain productivity through "Rational Recommendations."

Key Features
Knowledge Representation:  Uses a structured CSV-based Knowledge Base (Pandas) for data persistence.
Inference Engine:  A heuristic-based recommendation system that identifies the most urgent tasks based on proximity to deadlines.
NLP Integration: Integrated with the Groq API (Llama 3) to provide context-aware motivational feedback and task analysis.
Minimalist CLI:  A high-efficiency Command Line Interface for direct agent interaction.

Technical Stack:
Language:  Python 3.13
Data Management:  Pandas library
AI Engine:  Groq Cloud API (Llama-3.3-70b-versatile)
Logic Model: Rational Decision-Making 

 How to Run:
1. Clone the repository: `git clone [your-link]`
2. Install dependencies: `pip install pandas groq`
3. Add your Groq API key in the `Task` class.
4. Run the agent: `python task_manager.py`

  Syllabus Mapping :
The agent operates in a discrete, static, and observable environment (the CSV file).
Implements a Greedy Heuristic to recommend the "Optimal Next State."
Demonstrates real-world application of LLMs in productivity software
