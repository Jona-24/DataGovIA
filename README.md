# TFM - Intelligent Decision Support System for Data Governance

## Overview

This project is an **Intelligent Decision Support System** designed to assess organizational data management capabilities, identify maturity gaps, detect risks, and generate contextualized recommendations for data governance improvement.

The system uses a multi-agent reasoning architecture built with **LangGraph** to provide explainable, capability-driven insights.

## Core Concept

The system reasons about organizational context to identify symptoms, capability gaps, risks, and recommendations. It leverages a frozen knowledge model based on frameworks like DAMA-DMBOK, DCAM, ISO 11179, and COBIT.

**Reasoning Flow:**
```
Context → Symptoms → Capability Gaps → Risks → Recommendations → Expected Outcomes
```

## Project Structure

```
TFM/
├── project/                          # Main application
│   ├── main.py                      # Entry point with example usage
│   ├── requirements.txt             # Python dependencies
│   ├── agents/                      # Multi-agent system
│   │   ├── intake_agent.py         # Collects organizational context
│   │   ├── diagnostic_agent.py     # Identifies capability gaps and risks
│   │   ├── retrieval_agent.py      # Retrieves relevant knowledge
│   │   └── reasoning_agent.py      # Generates recommendations
│   ├── models/                      # Data structures
│   │   ├── state.py                # Graph state definition
│   │   ├── diagnosis.py            # Diagnosis model
│   │   └── intake_result.py        # Intake results model
│   ├── llm/                         # LLM provider configuration
│   │   └── provider.py             # LLM provider setup
│   └── prompts/                    # Agent prompt templates
│
├── knowledge_bases/                 # Domain knowledge
│   ├── Knowledge_Model_v1_FROZEN.md # Core knowledge model (FROZEN)
│   ├── capabilities/                # Capability definitions
│   │   └── KU_METADATA_MANAGEMENT_v1.0.md
│   ├── data_governance/             # Data governance knowledge
│   │   └── KU_DATA_GOVERNANCE_DAMA.md
│   └── vectorstore/                 # Vector database utilities
│       ├── build_db.py             # Build knowledge vector store
│       ├── debug_chroma.py         # Debug Chroma database
│       └── query_db.py             # Query vector database
│
├── chroma_db/                       # Vector store (Chroma)
│   └── chroma.sqlite3              # SQLite vector database
│
├── Estado del arte/                 # Research and reference materials
├── .gitignore                       # Git ignore file
└── venv/                           # Python virtual environment
```

## Key Components

### Multi-Agent System

The system uses a pipeline orchestrated by LangGraph:
***Actual(Work in Process)
1. **Intake Agent** - Collects organizational context and current state
2. **Diagnostic Agent** - Analyzes gaps and identifies risks
3. **Retrieval Agent** - Fetches relevant knowledge from the vector store
4. **Reasoning Agent** - Generates actionable recommendations

### Knowledge Base

- **Frozen Knowledge Model v1.0** - Core domain knowledge (as of 2026-05-31)
- **Vector Store** - Chroma-based embedding and retrieval system
- **Capability Units** - Structured knowledge on metadata management, data governance, etc.

### State Management

The `GraphState` carries the following information through the pipeline:

```python
- user_input: str                    # Initial organizational context
- organization_context: dict         # Structured context
- capability_gaps: list             # Identified gaps
- retrieved_knowledge: list         # Relevant knowledge chunks
- recommendations: list             # Generated recommendations
- diagnosis: dict                   # Complete diagnosis output
```

## Setup & Installation

### Prerequisites

- Python 3.8+
- Virtual environment (venv)

### Installation

1. **Clone/Open the project**
   ```bash
   cd e:\TFM
   ```

2. **Activate virtual environment**
   ```bash
   # Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r project/requirements.txt
   ```

4. **Build knowledge vector store** (if needed)
   ```bash
   python knowledge_bases/vectorstore/build_db.py
   ```

## Usage

### Basic Example

```bash
python project/main.py
```

The default example analyzes an SME retail company with:
- Excel and Power BI usage
- Inconsistent reports
- Missing data catalog

### Example Input Format

```python
{
    "user_input": """
    We are a SME retail company.
    We use Excel and Power BI.
    Reports are inconsistent.
    We do not have a data catalog.
    """
}
```

### Output

The system returns:

- **retrieved_knowledge** - Relevant knowledge chunks from the base
- **diagnosis** - Complete diagnostic analysis with recommendations

## Environment Variables

Create a `.env` file for configuration (ignored by git):

```bash
# .env
LLM_API_KEY=your_key_here
LLM_MODEL=gpt-4
# Additional configuration as needed
```

## Development

### Running Debug Tools

```bash
# Query the knowledge base
python knowledge_bases/vectorstore/query_db.py

# Debug Chroma vector store
python knowledge_bases/vectorstore/debug_chroma.py
```

## Knowledge Model Status

- **Version:** 1.0
- **Status:** FROZEN (as of 2026-05-31)
- **Approval Date:** 2026-05-31
- **Language:** English

The knowledge model is frozen and should not be modified without formal approval.

## Architecture Notes

- Built with **LangGraph** for agent orchestration
- Uses **Chroma** vector database for knowledge retrieval
- Implements **multi-agent reasoning** for explainability
- Capability-driven rather than framework-driven analysis

## License & Status

This is a TFM (Trabajo Fin de Máster / Master's Thesis) project.

---

**Last Updated:** 2026-06-08
