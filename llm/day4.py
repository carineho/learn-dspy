# Day 4: Advanced DSPy Features
# Explore more advanced DSPy features and recent updates.
#
# Task: Use DSPy with external business logic for classification.
# Create a `logic.json` file and experiment with different rules.

import dspy
import json

class ExternalLogicClassifier(dspy.Task):
    def __init__(self, text, logic_file):
        self.text = text
        with open(logic_file) as f:
            self.logic = json.load(f)
    def run(self):
        for category, kw in self.logic.items():
            if kw in self.text:
                return category
        return 'Other'

# Example usage
# Create a logic.json file with your rules
# Example: {"Transaction Advice": "transaction", "Investment Report": "investment", "Loan Agreement": "loan"}

sample_text = "# Investment Portfolio\nThis is your investment report."
classifier = ExternalLogicClassifier(sample_text, 'logic.json')
print(classifier.run())
