# Groq Economics Toolkit


### Disclaimer:  90% of this code was generated using AI

A modular, scenario‑driven cost modeling toolkit for Groq workloads.

## Features

- Token, character, and audio‑hour cost estimation
- Scenario‑based unit economics modeling
- CLI for quick analysis
- YAML/JSON scenario formats
- Reporting layer with cost breakdowns
- Extensible pricing table

## Install

```powershell
pip install -e.
```

## CLI Usage

```powershell
groq-econ run-scenario scenarios/scenario_support.yaml
```

## Python Usage

```python
from groq_econ.estimator import estimate_llm_cost

cost = estimate_llm_cost(
    model="openai/gpt-oss-20b",
    input_tokens=50000,
    output_tokens=10000
)
print(cost)
```

## Scenarios

See the scenarios/ folder for ready‑to‑use examples.
