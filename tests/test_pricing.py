from groq_econ.pricing import PRICING, ModelConfig

def test_pricing_structure():
    assert isinstance(PRICING, dict)
    for name, cfg in PRICING.items():
        assert isinstance(cfg, ModelConfig)
