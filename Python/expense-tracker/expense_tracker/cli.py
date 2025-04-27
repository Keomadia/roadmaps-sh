# expense_tracker/cli.py

import argparse
from expense_tracker import tracker

def handle_command():
    parser = argparse.ArgumentParser(
        prog="expense-tracker",
        description="A simple CLI Expense Tracker",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add expense
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--amount", type=float, required=True, help="Amount spent")
    add_parser.add_argument("--description", type=str, required=True, help="Description of the expense")

    # List expenses
    subparsers.add_parser("list", help="List all expenses")

    # Delete expense
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", type=int, required=True, help="ID of the expense to delete")

    # Summary
    summary_parser = subparsers.add_parser("summary", help="Show expenses summary")
    summary_parser.add_argument("--month", type=int, help="Month (1-12) to filter summary")

    # Export
    subparsers.add_parser("export", help="Export all expenses to a CSV file")

    args = parser.parse_args()

    if args.command == "add":
        tracker.add_expense(args)
    elif args.command == "list":
        tracker.list_expense()
    elif args.command == "delete":
        tracker.delete_expense(args)
    elif args.command == "summary":
        tracker.summary_expense(args)
    elif args.command == "export":
        tracker.export_expense(args)
