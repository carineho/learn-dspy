# Day 1: DSPy Tasks
# Learn how to create and use DSPy tasks for basic text classification.
#
# Task: Classify markdown text into categories.
# Try changing `sample_text` and see how the output changes.

import dspy

class MarkdownClassifier(dspy.Task):
    def __init__(self, text):
        self.text = text
    def run(self):
        # Replace with your logic
        if 'transaction' in self.text:
            return 'Transaction Advice'
        elif 'investment' in self.text:
            return 'Investment Report'
        elif 'loan' in self.text:
            return 'Loan Agreement'
        else:
            return 'Other'

# Example usage
sample_text = "# Investment Portfolio\nThis is your investment report."
classifier = MarkdownClassifier(sample_text)
print(classifier.run())
