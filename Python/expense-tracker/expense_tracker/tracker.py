import os
import csv
import time
from expense_tracker import storage as db
from expense_tracker import models as md
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

def add_expense(args):
    amount = args.amount
    description = args.description

    if amount <= 0:
        console.print("[bold red]Invalid amount. Must be greater than 0.[/]")
        return

    expenses = db.load_expenses()

    new_id = max([e["id"] for e in expenses], default=0) + 1

    new_expense = md.Expense(
        id=new_id,
        amount=amount,
        description=description,
    )

    expenses.append(new_expense.to_dict())
    db.save_expenses(expenses)

    console.print(f"[bold green]Expense added successfully! ID: {new_expense.id}[/]")
    console.print(f"[bold yellow]Amount:[/] $ {amount}")
    console.print(f"[bold yellow]Description:[/] {description}")

def list_expense(args=None):
    expenses = db.load_expenses()

    if not expenses:
        console.print("[bold red]No expenses available.[/]")
        return

    table = Table(show_header=True, header_style="bold yellow", box=box.ROUNDED)
    table.add_column("ID", justify="center")
    table.add_column("Date")
    table.add_column("Description")
    table.add_column("Amount", justify="center")

    for expense in expenses:
        table.add_row(
            str(expense["id"]),
            expense["createdAt"],
            expense["description"],
            f"$ {str(expense['amount'])}0",
            style="bold white",
        )

    console.print(table)

def delete_expense(args):
    expense_id = args.id
    expenses = db.load_expenses()

    if not expenses:
        console.print("[bold red]No expenses to delete.[/]")
        return

    expense_to_delete = next((e for e in expenses if e["id"] == expense_id), None)

    if expense_to_delete:
        expenses.remove(expense_to_delete)
        db.save_expenses(expenses)
        console.print(f"[bold green]Expense ID {expense_id} deleted successfully![/]")
        console.print("[bold yellow]Reindexing expenses...[/]")
        reindex_expenses()
        time.sleep(1)
        console.print("[bold green]Reindexing complete.[/]")
        time.sleep(0.5)
        console.print("[bold blue]Current Expenses -->[/]")
        list_expense()
    else:
        console.print(f"[bold red]Expense ID {expense_id} not found.[/]")

def summary_expense(args):
    expenses = db.load_expenses()

    if not expenses:
        console.print("[bold red]No expenses available.[/]")
        return

    if args.month:
        month = args.month
        expenses = [e for e in expenses if e["month"] == month]
    title = f"[bold yellow]{'Monthly Summary for ' + month_name(args.month) if args.month else 'Total Summary'}[/]".center(50)
    console.print(f"[bold yellow]{title}[/]")
    if not expenses:
        console.print("[bold red]No expenses found for the selected month.[/]")
        return

    total = sum(e["amount"] for e in expenses)
    average = total / len(expenses) if expenses else 0

    table = Table(show_header=True, header_style="bold yellow", box=box.ROUNDED)
    table.add_column("Total Amount", justify="center")
    table.add_column("Average Amount", justify="center")

    table.add_row(
        f"$ {total:.2f}",
        f"$ {average:.2f}",
        style="bold white",
    )

    console.print(table)

def export_expense(args=None):
    expenses = db.load_expenses()

    if not expenses:
        console.print("[bold red]No expenses available to export.[/]")
        return

    console.print("[bold yellow]By continuing, you agree to export the expenses as a CSV file.[/]")
    console.print("[bold yellow]Press Enter to continue, or 'q' to cancel.[/]")
    user_input = input().strip().lower()

    if user_input == "q":
        console.print("[bold red]Export canceled.[/]")
        return

    FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    FILE_NAME = os.path.join(os.path.dirname(FILE_PATH), "data/exported_expenses.csv")

    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Date", "Description", "Amount", "Created By", "Updated At", "Month"])
        for expense in expenses:
            writer.writerow([
                expense["id"],
                expense["createdAt"],
                expense["description"],
                expense["amount"],
                expense["createdBy"],
                expense["updatedAt"],
                expense["month"],
            ])

    console.print(f"[bold green]Expenses exported successfully to {FILE_NAME}[/]")

def reindex_expenses():
    expenses = db.load_expenses()
    expenses.sort(key=lambda e: e["id"])

    for idx, expense in enumerate(expenses, start=1):
        expense["id"] = idx

    db.save_expenses(expenses)


def month_name(month_number):
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return month_names.get(month_number, "Invalid month")