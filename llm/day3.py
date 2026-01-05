# Day 3: Optimizers
# Learn how to use DSPy optimizers to improve classification accuracy.
#
# Task: Use a simple optimizer to tune classification logic.
# Tune the `keywords` dictionary and see how it affects classification.

import dspy

class OptimizedClassifier(dspy.Task):
    def __init__(self, text, keywords):
        self.text = text
        self.keywords = keywords
    def run(self):
        for category, kw in self.keywords.items():
            if kw in self.text:
                return category
        return 'Other'

# Optimizer: update keywords
keywords = {
    'Transaction Advice': 'transaction',
    'Investment Report': 'investment',
    'Loan Agreement': 'loan'
}

# Example usage
sample_text = "# Transaction Notice\nThis is a transaction advice."
classifier = OptimizedClassifier(sample_text, keywords)
print(classifier.run())

# Try changing keywords for better results
keywords['Transaction Advice'] = 'notice'
print(classifier.run())
