import subprocess

def test_cli_help():
    result = subprocess.run(["groq-econ", "--help"], capture_output=True)
    assert result.returncode == 0
