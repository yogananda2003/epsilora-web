"""
AI-generated expense tracker with category breakdown and monthly summaries.
"""

from datetime import datetime
from collections import defaultdict


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add(self, amount: float, category: str, description: str = ""):
        self.expenses.append({
            "amount": amount,
            "category": category.lower(),
            "description": description,
            "date": datetime.now().isoformat(),
        })

    def total(self) -> float:
        return sum(e["amount"] for e in self.expenses)

    def by_category(self) -> dict:
        breakdown = defaultdict(float)
        for e in self.expenses:
            breakdown[e["category"]] += e["amount"]
        return dict(sorted(breakdown.items(), key=lambda x: x[1], reverse=True))

    def monthly_summary(self) -> dict:
        summary = defaultdict(float)
        for e in self.expenses:
            month = e["date"][:7]  # YYYY-MM
            summary[month] += e["amount"]
        return dict(sorted(summary.items()))

    def report(self):
        print(f"\n{'='*40}")
        print(f"  Total spent: ${self.total():,.2f}")
        print(f"{'='*40}")
        print("\nBy category:")
        for cat, amt in self.by_category().items():
            pct = (amt / self.total() * 100) if self.total() else 0
            print(f"  {cat:<20} ${amt:>8,.2f}  ({pct:.1f}%)")
        print("\nMonthly breakdown:")
        for month, amt in self.monthly_summary().items():
            print(f"  {month}  ${amt:,.2f}")
        print()


if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.add(120.00, "Food", "Groceries")
    tracker.add(45.50, "Transport", "Uber rides")
    tracker.add(9.99, "Subscriptions", "Netflix")
    tracker.add(200.00, "Food", "Dinner out")
    tracker.add(60.00, "Utilities", "Electricity")
    tracker.add(14.99, "Subscriptions", "Spotify")
    tracker.add(85.00, "Transport", "Fuel")
    tracker.report()
