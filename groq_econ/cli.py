"""
cli.py

Groq Economics Toolkit CLI.

Commands:
  - llm
  - tts
  - stt
  - tool
  - run-scenario
"""

import argparse

from .estimator import (
    estimate_llm_cost,
    estimate_tts_cost,
    estimate_stt_cost,
    estimate_tool_cost,
    estimate_workflow_step_cost,
)
from .scenarios import load_scenario
from .reporting import (
    print_scenario_header,
    print_cost_breakdown,
    print_totals,
)


def cli_llm(args):
    cost = estimate_llm_cost(
        model=args.model,
        input_tokens=args.input_tokens,
        output_tokens=args.output_tokens,
        cached_input_tokens=args.cached_input_tokens,
    )
    print(f"\nLLM Cost Estimate for {args.model}")
    print("--------------------------------------")
    print(f"Input tokens:          {args.input_tokens:,}")
    print(f"Cached input tokens:   {args.cached_input_tokens:,}")
    print(f"Output tokens:         {args.output_tokens:,}")
    print("--------------------------------------")
    print(f"Total cost:            ${cost:,.4f}\n")


def cli_tts(args):
    cost = estimate_tts_cost(
        model=args.model,
        characters=args.characters,
    )
    print(f"\nTTS Cost Estimate for {args.model}")
    print("--------------------------------------")
    print(f"Characters:            {args.characters:,}")
    print("--------------------------------------")
    print(f"Total cost:            ${cost:,.4f}\n")


def cli_stt(args):
    cost = estimate_stt_cost(
        model=args.model,
        audio_seconds=args.audio_seconds,
    )
    print(f"\nSTT Cost Estimate for {args.model}")
    print("--------------------------------------")
    print(f"Audio seconds:         {args.audio_seconds:,}")
    print("--------------------------------------")
    print(f"Total cost:            ${cost:,.4f}\n")


def cli_tool(args):
    cost = estimate_tool_cost(
        tool_name=args.tool,
        requests=args.requests,
        hours=args.hours,
    )
    print(f"\nTool Cost Estimate for {args.tool}")
    print("--------------------------------------")
    print(f"Requests:              {args.requests:,}")
    print(f"Hours:                 {args.hours}")
    print("--------------------------------------")
    print(f"Total cost:            ${cost:,.4f}\n")


def cli_run_scenario(args):
    scenario = load_scenario(args.file)

    users = scenario["assumptions"]["users"]
    interactions = scenario["assumptions"]["interactions_per_user_per_month"]

    print_scenario_header(scenario)

    total_cost = 0.0
    breakdown = []

    for step in scenario["workflows"]:
        calls = step["calls_per_interaction"] * interactions * users
        cost = estimate_workflow_step_cost(step, calls)
        breakdown.append((step["name"], cost))
        total_cost += cost

    print_cost_breakdown(breakdown)
    print_totals(total_cost, users, interactions)


def build_parser():
    parser = argparse.ArgumentParser(
        description="Groq Economics Toolkit CLI"
    )
    subparsers = parser.add_subparsers(dest="command")

    # LLM
    llm = subparsers.add_parser("llm", help="Estimate LLM cost")
    llm.add_argument("--model", required=True)
    llm.add_argument("--input_tokens", type=int, required=True)
    llm.add_argument("--output_tokens", type=int, required=True)
    llm.add_argument("--cached_input_tokens", type=int, default=0)
    llm.set_defaults(func=cli_llm)

    # TTS
    tts = subparsers.add_parser("tts", help="Estimate TTS cost")
    tts.add_argument("--model", required=True)
    tts.add_argument("--characters", type=int, required=True)
    tts.set_defaults(func=cli_tts)

    # STT
    stt = subparsers.add_parser("stt", help="Estimate STT cost")
    stt.add_argument("--model", required=True)
    stt.add_argument("--audio_seconds", type=float, required=True)
    stt.set_defaults(func=cli_stt)

    # Tools
    tool = subparsers.add_parser("tool", help="Estimate tool cost")
    tool.add_argument("--tool", required=True)
    tool.add_argument("--requests", type=int, default=0)
    tool.add_argument("--hours", type=float, default=0.0)
    tool.set_defaults(func=cli_tool)

    # Run scenario
    run = subparsers.add_parser("run-scenario", help="Run a scenario file")
    run.add_argument("--file", required=True)
    run.set_defaults(func=cli_run_scenario)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if not getattr(args, "command", None):
        parser.print_help()
        return

    args.func(args)


if __name__ == "__main__":
    main()
