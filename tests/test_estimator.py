from groq_econ.estimator import estimate_llm_cost

def test_llm_cost_basic():
    cost = estimate_llm_cost(
        model="openai/gpt-oss-20b",
        input_tokens=1000,
        output_tokens=500
    )
    assert cost > 0
