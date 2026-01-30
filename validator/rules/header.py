from validator.result import ValidationResult
from datetime import datetime

def h01_company_id(tree):
    company_id = tree.findtext(".//CompanyID")
    if not company_id:
        return ValidationResult(
            "H01",
            "ERROR",
            "CompanyID (CUI) lipsă în Header"
        )

def h02_period_exists(tree):
    start = tree.findtext(".//StartDate")
    end = tree.findtext(".//EndDate")
    if not start or not end:
        return ValidationResult(
            "H02",
            "ERROR",
            "Perioada StartDate / EndDate lipsă"
        )

def h03_single_month(tree):
    try:
        start = datetime.fromisoformat(tree.findtext(".//StartDate"))
        end = datetime.fromisoformat(tree.findtext(".//EndDate"))
        if start.year != end.year or start.month != end.month:
            return ValidationResult(
                "H03",
                "ERROR",
                "SAF-T trebuie raportat pentru o singură lună"
            )
    except Exception:
        pass

def h04_currency_ron(tree):
    currency = tree.findtext(".//CurrencyCode")
    if currency != "RON":
        return ValidationResult(
            "H04",
            "ERROR",
            "CurrencyCode trebuie să fie RON"
        )

HEADER_RULES = [
    h01_company_id,
    h02_period_exists,
    h03_single_month,
    h04_currency_ron
]
