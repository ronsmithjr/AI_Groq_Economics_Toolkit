"""
pricing.py

Single source of truth for Groq model pricing.
All prices are in USD.
"""


import json
import os
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



# Load pricing from config/model_prices.json
def _load_pricing():
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "model_prices.json")
    with open(config_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    pricing = {}
    for model, cfg in data.items():
        mtype = cfg["type"]
        price = cfg["price"]
        if mtype == "llm":
            price_obj = LLMPrice(
                input_per_m=price["input_per_m"],
                output_per_m=price["output_per_m"],
                cached_input_per_m=price.get("cached_input_per_m"),
            )
        elif mtype == "tts":
            price_obj = TTSPrice(
                per_m_characters=price["per_m_characters"]
            )
        elif mtype == "stt":
            price_obj = STTPrice(
                per_hour=price["per_hour"],
                min_billable_seconds=price.get("min_billable_seconds", 10.0)
            )
        elif mtype == "tool":
            price_obj = ToolPrice(
                per_1k_requests=price.get("per_1k_requests"),
                per_hour=price.get("per_hour")
            )
        else:
            raise ValueError(f"Unknown model type: {mtype}")
        pricing[model] = ModelConfig(type=mtype, price=price_obj)
    return pricing

PRICING: Dict[str, ModelConfig] = _load_pricing()
