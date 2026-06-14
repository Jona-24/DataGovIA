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
│   ├── main.py                       # Entry point with example usage
│   ├── agents/                       # Multi-agent system
│   │   ├── intake_agent.py           # Collects organizational context
│   │   ├── diagnostic_agent.py       # Identifies capability gaps and risks
│   │   ├── retrieval_agent.py        # Retrieves relevant knowledge
│   │   ├── reasoning_agent.py        # Generates recommendations
│   │   ├── dss_agent.py              # Orchestrates decision support outputs
│   │   ├── strategy_agent.py         # Generates strategic actions
│   │   └── technology_assessment_agent.py # Assesses technology profiles
│   ├── models/                       # Data structures
│   │   ├── state.py                  # Graph state definition
│   │   ├── diagnosis.py              # Diagnosis model
│   │   ├── intake_result.py          # Intake results model
│   │   ├── organization_context.py   # Organization context model
│   │   ├── capability_gap.py         # Capability gap model
│   │   ├── dss_report.py             # DSS report model
│   │   ├── recommendation.py         # Recommendation model
│   │   ├── strategy.py               # Strategy model
│   │   ├── strategic_action.py       # Strategic action model
│   │   └── technology_profile.py     # Technology profile model
│   ├── llm/                          # LLM provider configuration
│   │   └── provider.py               # LLM provider setup
│   └── prompts/                      # Agent prompt templates

├── knowledge_bases/                  # Domain knowledge
│   ├── capabilities/                 # Capability definitions
│   │   ├── Knowledge_Model_v2.md     # Core knowledge model (FROZEN / v2 draft)
│   │   ├── KU_DATA GOVERNANCE_v1.0.md
│   │   ├── KU_DATA_ARCHITECTURE_v1.0.md
│   │   └── KU_METADATA_MANAGEMENT_v2.md
│   └── vectorstore/                  # Vector database utilities
│       ├── build_db.py               # Build knowledge vector store
│       ├── debug_chroma.py           # Debug Chroma database
│       └── query_db.py               # Query vector database

├── chroma_db/                        # Vector store (Chroma)
│   └── chroma.sqlite3                # SQLite vector database

├── Estado del arte/                  # Research and reference materials
├── chroma_db/                        # Vector DB artifacts
├── requirements.txt                  # Project dependencies (root)
├── .gitignore                        # Git ignore file
└── venv/                             # Python virtual environment
```

## Key Components

### Multi-Agent System

The system uses a pipeline orchestrated by LangGraph. Current agents included in `project/agents/`:

- **Intake Agent** - Collects organizational context and current state
- **Diagnostic Agent** - Analyzes capability gaps and identifies risks
- **Retrieval Agent** - Fetches relevant knowledge from the vector store
- **Reasoning Agent** - Generates actionable recommendations
- **DSS Agent** - Orchestrates output formatting and DSS workflows
- **Strategy Agent** - Produces strategic actions and roadmaps
- **Technology Assessment Agent** - Evaluates technology profiles and fit

Agents are modular and communicate via the `GraphState` passed through the pipeline.

### Knowledge Base

- **Frozen Knowledge Model v2 (draft)** - Core domain knowledge (updated)
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

### Model Mapping

The Python data models in `project/models/` are implemented following the Knowledge Model defined in `knowledge_bases/capabilities/Knowledge_Model_v2.md`. Ensure that updates to the knowledge model are propagated to the corresponding Python models and validation rules.

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
   pip install -r requirements.txt
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

- **Version:** 2.0 (draft)
- **Status:** FROZEN / draft updates (2026)
- **Approval Date:** 2026-05-31
- **Language:** English

## Architecture Notes

- Built with **LangGraph** for agent orchestration
- Uses **Chroma** vector database for knowledge retrieval
- Implements **multi-agent reasoning** for explainability
- Capability-driven rather than framework-driven analysis

## License & Status

This is a TFM (Trabajo Fin de Máster / Master's Thesis) project.

---

**Last Updated:** 2026-06-13
