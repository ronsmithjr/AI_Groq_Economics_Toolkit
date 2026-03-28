AI_Groq_Economics_Toolkit/
├─ README.md
├─ pyproject.toml              # or setup.cfg / requirements.txt
├─ .gitignore
│
├─ groq_econ/
│  ├─ __init__.py
│  ├─ pricing.py               # core pricing tables + dataclasses
│  ├─ estimator.py             # pure cost functions (LLM/TTS/STT/tools)
│  ├─ scenarios.py             # load/validate scenario files
│  ├─ reporting.py             # text/CSV/JSON report generators
│  └─ cli.py                   # main CLI entrypoint (run-scenario, llm, tts, stt, tool)
│
├─ scenarios/
│  ├─ scenario_support.yaml    # Tier-1 support workflow
│  ├─ scenario_rag.yaml        # RAG workflow
│  ├─ scenario_agent.yaml      # agentic automation
│  └─ examples.json            # optional JSON variants
│
├─ docs/
│  ├─ overview.md              # executive summary of Groq pricing model
│  ├─ modeling-guide.md        # how to design scenarios & unit economics
│  ├─ cli-usage.md             # CLI commands, examples, patterns
│  └─ changelog.md             # pricing/version changes over time
│
├─ notebooks/
│  ├─ 01_scenario_explorer.ipynb   # interactive what-if modeling
│  └─ 02_margin_analysis.ipynb     # price → margin → breakeven curves
│
└─ tests/
   ├─ test_pricing.py
   ├─ test_estimator.py
   ├─ test_scenarios.py
   └─ test_cli.py
