"""
reporting.py

Reporting utilities for scenario results.
"""

from typing import Dict, List, Tuple


def print_scenario_header(scenario: Dict) -> None:
    users = scenario["assumptions"]["users"]
    interactions = scenario["assumptions"]["interactions_per_user_per_month"]

    print(f"\n=== Scenario: {scenario['scenario_name']} ===")
    desc = scenario.get("description")
    if desc:
        print(desc)
    print(f"Users: {users:,}")
    print(f"Interactions per user per month: {interactions:,}\n")


def print_cost_breakdown(breakdown: List[Tuple[str, float]]) -> None:
    print("=== Cost Breakdown ===")
    for name, cost in breakdown:
        print(f"{name:<35} ${cost:,.2f}")
    print("")


def print_totals(
    total_cost: float,
    users: int,
    interactions_per_user_per_month: int,
) -> None:
    total_interactions = users * interactions_per_user_per_month

    print("=== Totals ===")
    print(f"Total Monthly Cost:      ${total_cost:,.2f}")
    print(f"Cost per User per Month: ${total_cost / users:,.4f}")
    print(f"Cost per Interaction:    ${total_cost / total_interactions:,.4f}\n")
