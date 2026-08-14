import os

from managers import ExpenseManager
from storage import Storage


def test_storage_uses_project_folder_paths():
    assert os.path.basename(Storage.FILE_JSON) == "data.json"
    assert os.path.basename(Storage.FILE_CSV) == "data.csv"
    assert os.path.dirname(Storage.FILE_JSON).endswith("expense_project")


def test_manager_tracks_income_and_expense():
    manager = ExpenseManager()
    manager.add_transaction(2500, "Salary")
    manager.add_transaction(-120, "Groceries")

    assert len(manager.expenses) == 2
    assert manager.expenses[0].amount == 2500
    assert manager.expenses[1].category == "Groceries"


def test_transaction_history_is_lazy_and_iterable():
    manager = ExpenseManager()
    manager.add_transaction(100, "Freelance")

    history = list(manager.transaction_history())
    assert len(history) == 1
    assert history[0].amount == 100
