"""
estimator.py

Pure cost estimation functions for Groq models.
"""

from typing import Dict, Tuple

from .pricing import PRICING, LLMPrice, TTSPrice, STTPrice, ToolPrice, ModelConfig


def estimate_llm_cost(
    model: str,
    input_tokens: int,
    output_tokens: int,
    cached_input_tokens: int = 0,
) -> float:
    cfg: ModelConfig = PRICING.get(model)  # type: ignore
    if cfg is None or cfg.type != "llm":
        raise ValueError(f"Model {model} is not configured as an LLM.")

    price: LLMPrice = cfg.price  # type: ignore

    in_m = input_tokens / 1_000_000
    out_m = output_tokens / 1_000_000
    cached_in_m = cached_input_tokens / 1_000_000

    uncached_in_m = max(in_m - cached_in_m, 0.0)

    cost = 0.0
    cost += uncached_in_m * price.input_per_m
    cost += out_m * price.output_per_m

    if price.cached_input_per_m is not None and cached_in_m > 0:
        cost += cached_in_m * price.cached_input_per_m

    return cost


def estimate_tts_cost(
    model: str,
    characters: int,
) -> float:
    cfg: ModelConfig = PRICING.get(model)  # type: ignore
    if cfg is None or cfg.type != "tts":
        raise ValueError(f"Model {model} is not configured as TTS.")

    price: TTSPrice = cfg.price  # type: ignore
    chars_m = characters / 1_000_000
    return chars_m * price.per_m_characters


def estimate_stt_cost(
    model: str,
    audio_seconds: float,
) -> float:
    cfg: ModelConfig = PRICING.get(model)  # type: ignore
    if cfg is None or cfg.type != "stt":
        raise ValueError(f"Model {model} is not configured as STT.")

    price: STTPrice = cfg.price  # type: ignore

    billable_seconds = max(audio_seconds, price.min_billable_seconds)
    billable_hours = billable_seconds / 3600.0

    return billable_hours * price.per_hour


def estimate_tool_cost(
    tool_name: str,
    requests: int = 0,
    hours: float = 0.0,
) -> float:
    cfg: ModelConfig = PRICING.get(tool_name)  # type: ignore
    if cfg is None or cfg.type != "tool":
        raise ValueError(f"Tool {tool_name} is not configured as a tool.")

    price: ToolPrice = cfg.price  # type: ignore
    cost = 0.0

    if price.per_1k_requests is not None and requests > 0:
        cost += (requests / 1000.0) * price.per_1k_requests

    if price.per_hour is not None and hours > 0:
        cost += hours * price.per_hour

    return cost


def estimate_workflow_step_cost(step: Dict, calls: int) -> float:
    """
    Helper used by scenario runner.
    `step` is a workflow dict from a scenario file.
    """
    step_type = step["type"]

    if step_type == "llm":
        per_call = estimate_llm_cost(
            model=step["model"],
            input_tokens=step["input_tokens"],
            output_tokens=step["output_tokens"],
            cached_input_tokens=step.get("cached_input_tokens", 0),
        )
    elif step_type == "tts":
        per_call = estimate_tts_cost(
            model=step["model"],
            characters=step["characters"],
        )
    elif step_type == "stt":
        per_call = estimate_stt_cost(
            model=step["model"],
            audio_seconds=step["audio_seconds"],
        )
    elif step_type == "tool":
        per_call = estimate_tool_cost(
            tool_name=step["tool"],
            requests=step.get("requests", 0),
            hours=step.get("hours", 0.0),
        )
    else:
        raise ValueError(f"Unknown workflow step type: {step_type}")

    return per_call * calls
