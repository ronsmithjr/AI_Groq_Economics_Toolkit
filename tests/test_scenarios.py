from groq_econ.scenarios import load_scenario

def test_load_scenario():
    data = load_scenario("scenarios/scenario_support.yaml")
    assert "workflows" in data
    assert len(data["workflows"]) > 0
