"""
pricing.py

Single source of truth for Groq model pricing.
All prices are in USD.
"""

from dataclasses import dataclass
from typing import Optional, Dict, Literal


ModelType = Literal["llm", "tts", "stt", "tool"]


@dataclass
class LLMPrice:
    input_per_m: float
    output_per_m: float
    cached_input_per_m: Optional[float] = None


@dataclass
class TTSPrice:
    per_m_characters: float


@dataclass
class STTPrice:
    per_hour: float
    min_billable_seconds: float = 10.0


@dataclass
class ToolPrice:
    per_1k_requests: Optional[float] = None
    per_hour: Optional[float] = None


@dataclass
class ModelConfig:
    type: ModelType
    price: object


PRICING: Dict[str, ModelConfig] = {
    # LLMs (from Groq pricing page)
    "openai/gpt-oss-20b": ModelConfig(
        type="llm",
        price=LLMPrice(
            input_per_m=0.075,
            output_per_m=0.30,
            cached_input_per_m=None,
        ),
    ),
    "openai/gpt-oss-safeguard-20b": ModelConfig(
        type="llm",
        price=LLMPrice(
            input_per_m=0.075,
            output_per_m=0.30,
            cached_input_per_m=None,
        ),
    ),
    "openai/gpt-oss-120b": ModelConfig(
        type="llm",
        price=LLMPrice(
            input_per_m=0.15,
            output_per_m=0.60,
            cached_input_per_m=None,
        ),
    ),
    "moonshotai/kimi-k2-instruct-0905": ModelConfig(
        type="llm",
        price=LLMPrice(
            input_per_m=1.00,
            output_per_m=3.00,
            cached_input_per_m=0.50,
        ),
    ),
    "llama-4-scout-17bx16e": ModelConfig(
        type="llm",
        price=LLMPrice(
            input_per_m=0.11,
            output_per_m=0.34,
            cached_input_per_m=None,
        ),
    ),
    "qwen3-32b": ModelConfig(
        type="llm",
        price=LLMPrice(
            input_per_m=0.29,
            output_per_m=0.59,
            cached_input_per_m=None,
        ),
    ),
    "llama-3.3-70b-versatile": ModelConfig(
        type="llm",
        price=LLMPrice(
            input_per_m=0.59,
            output_per_m=0.79,
            cached_input_per_m=None,
        ),
    ),
    "llama-3.1-8b-instant": ModelConfig(
        type="llm",
        price=LLMPrice(
            input_per_m=0.05,
            output_per_m=0.08,
            cached_input_per_m=None,
        ),
    ),
    # TTS (character-based)
    "canopy-labs/orpheus-english": ModelConfig(
        type="tts",
        price=TTSPrice(
            per_m_characters=22.00,
        ),
    ),
    "canopy-labs/orpheus-arabic-saudi": ModelConfig(
        type="tts",
        price=TTSPrice(
            per_m_characters=40.00,
        ),
    ),
    # STT (audio-hour-based)
    "whisper-v3-large": ModelConfig(
        type="stt",
        price=STTPrice(
            per_hour=0.111,
            min_billable_seconds=10.0,
        ),
    ),
    "whisper-large-v3-turbo": ModelConfig(
        type="stt",
        price=STTPrice(
            per_hour=0.04,
            min_billable_seconds=10.0,
        ),
    ),
    # Tools (example values)
    "tool/basic-search": ModelConfig(
        type="tool",
        price=ToolPrice(
            per_1k_requests=5.00,
        ),
    ),
    "tool/advanced-search": ModelConfig(
        type="tool",
        price=ToolPrice(
            per_1k_requests=8.00,
        ),
    ),
    "tool/visit-website": ModelConfig(
        type="tool",
        price=ToolPrice(
            per_1k_requests=1.00,
        ),
    ),
    "tool/code-execution": ModelConfig(
        type="tool",
        price=ToolPrice(
            per_hour=0.18,
        ),
    ),
    "tool/browser-automation": ModelConfig(
        type="tool",
        price=ToolPrice(
            per_hour=0.08,
        ),
    ),
}
