# Define your business logic for classification here
# You can also use a JSON file for categories and rules

CATEGORIES = [
    "Transaction Advice",
    "Investment Report",
    "Loan Agreement",
    "Other"
]

def classify_text(text):
    """
    Simple rule-based classification. Replace with DSPy logic as you learn.
    """
    text_lower = text.lower()
    if "transaction" in text_lower:
        return "Transaction Advice"
    elif "investment" in text_lower:
        return "Investment Report"
    elif "loan" in text_lower:
        return "Loan Agreement"
    else:
        return "Other"
