"""
scenarios.py

Loading and validating scenario files (YAML or JSON).
"""

import json
from pathlib import Path
from typing import Any, Dict

import yaml


REQUIRED_ROOT_KEYS = {"scenario_name", "assumptions", "workflows"}
REQUIRED_ASSUMPTIONS_KEYS = {"users", "interactions_per_user_per_month"}
REQUIRED_WORKFLOW_KEYS = {"name", "type", "calls_per_interaction"}


def load_scenario(path: str) -> Dict[str, Any]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Scenario file not found: {path}")

    text = p.read_text()

    if p.suffix.lower() in [".yaml", ".yml"]:
        data = yaml.safe_load(text)
    elif p.suffix.lower() == ".json":
        data = json.loads(text)
    else:
        raise ValueError("Scenario file must be .yaml, .yml, or .json")

    validate_scenario(data)
    return data


def validate_scenario(data: Dict[str, Any]) -> None:
    missing_root = REQUIRED_ROOT_KEYS - data.keys()
    if missing_root:
        raise ValueError(f"Scenario missing root keys: {missing_root}")

    assumptions = data.get("assumptions", {})
    missing_assumptions = REQUIRED_ASSUMPTIONS_KEYS - assumptions.keys()
    if missing_assumptions:
        raise ValueError(f"Scenario assumptions missing keys: {missing_assumptions}")

    if not isinstance(data.get("workflows"), list) or not data["workflows"]:
        raise ValueError("Scenario must contain a non-empty 'workflows' list.")

    for i, step in enumerate(data["workflows"]):
        missing_step = REQUIRED_WORKFLOW_KEYS - step.keys()
        if missing_step:
            raise ValueError(
                f"Workflow step {i} ('{step.get('name', 'unnamed')}') missing keys: {missing_step}"
            )

        step_type = step["type"]
        if step_type == "llm":
            for k in ["model", "input_tokens", "output_tokens"]:
                if k not in step:
                    raise ValueError(f"LLM step '{step['name']}' missing key: {k}")
        elif step_type == "tts":
            for k in ["model", "characters"]:
                if k not in step:
                    raise ValueError(f"TTS step '{step['name']}' missing key: {k}")
        elif step_type == "stt":
            for k in ["model", "audio_seconds"]:
                if k not in step:
                    raise ValueError(f"STT step '{step['name']}' missing key: {k}")
        elif step_type == "tool":
            if "tool" not in step:
                raise ValueError(f"Tool step '{step['name']}' missing key: tool")
        else:
            raise ValueError(f"Unknown workflow step type: {step_type}")
