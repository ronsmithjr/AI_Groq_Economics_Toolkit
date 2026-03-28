# Repo Map

```text
AI_Groq_Economics_Toolkit/
├─ README.md
├─ pyproject.toml              # or setup.cfg / requirements.txt
├─ .gitignore
│
+---config
|       model_prices.json
|
+---docs
|       overview.md
|       repomap.md
|
+---groq_econ
|   |   cli.py
|   |   estimator.py
|   |   pricing.py
|   |   reporting.py
|   |   scenarios.py
|   |   __init__.py
|   |
|   \---__pycache__
|           cli.cpython-313.pyc
|           estimator.cpython-313.pyc
|           pricing.cpython-313.pyc
|           reporting.cpython-313.pyc
|           scenarios.cpython-313.pyc
|           __init__.cpython-313.pyc
|
+---scenarios
|       scenario_agent.yaml
|       scenario_rag.yaml
|       scenario_support.yaml
|
\---tests
        test_cli.py
        test_estimator.py
        test_pricing.py
        test_scenarios.py
```
