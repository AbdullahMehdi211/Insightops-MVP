# InsightOps MVP

## About This Project
**InsightOps** is an AI-powered business investigation assistant backend and interactive dashboard designed as a robust proof-of-concept. It transforms natural language business questions—such as inquiries regarding customer churn or metric fluctuations—into structured, reproducible data analysis, root-cause findings, and actionable recommendations.

The project bridges business queries to multi-source enterprise evidence using a modular stack featuring a FastAPI asynchronous backend, an embedded dark-mode UI dashboard, and an architecture tailored for multi-agent tool orchestration (including SQL execution, vector search, and document parsing).

---

## Architecture Overview

InsightOps coordinates business queries across multiple data layers:
* **API Layer**: FastAPI handling asynchronous request routing and CORS.
* **Frontend Layer**: Built-in interactive dark-mode dashboard for instant agentic investigation queries.
* **Orchestration & Tools (Mocked in MVP)**: Designed for agent loops interacting with PostgreSQL (SQL execution), Qdrant (vector similarity search), and Docling (unstructured document parsing).

You can review the complete visual multi-agent workflow and layer breakdown in the [System Architecture Diagram](./insightops_architecture_diagram.pdf).

---

## Project Structure

```text
insightops-mvp/
│
├── Insightops_MVP.py                 # FastAPI backend server & integrated UI
├── requirements.txt                  # Core project dependencies
├── insightops_architecture_diagram.pdf # High-level system architecture & data flow
└── .gitignore                        # Ignored files for version control
```

---

## Getting Started & Installation Guide

Follow these step-by-step instructions to set up and run the project locally on your machine.

### 1. Cloning the Repository
Open your terminal and clone the repository to your local machine, then navigate into the project folder:
```bash
git clone https://github.com/AbdullahMehdi211/Insightops-MVP.git
cd insightops-mvp
```

### 2. Setting Up a Python Virtual Environment
It is recommended to use a virtual environment to manage dependencies cleanly. Run the command corresponding to your operating system:

* **For Windows:**
  ```bash
  python -m venv .venv
  .venv\Scripts\activate
  ```

* **For macOS / Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Installing Dependencies
Install all required Python packages using the requirements file:
```bash
pip install -r requirements.txt
```

### 4. Running the FastAPI Server
Start the backend application server locally:
```bash
python Insightops_MVP.py
```

### 5. Accessing the Application in the Browser
Once the server is running, open your web browser to explore the interfaces:
* **Interactive UI Dashboard**: Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) to use the investigation control panel.
* **Swagger API Documentation**: Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to inspect and test the API endpoints directly.