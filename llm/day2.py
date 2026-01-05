# Day 2: Chain of Thought
# Learn how to use chain-of-thought reasoning in DSPy tasks.
#
# Task: Break down the classification process into steps.
# Experiment with different texts and observe the reasoning steps.

import dspy

class ChainOfThoughtClassifier(dspy.Task):
    def __init__(self, text):
        self.text = text
    def run(self):
        steps = []
        if 'transaction' in self.text:
            steps.append('Detected transaction keyword')
            result = 'Transaction Advice'
        elif 'investment' in self.text:
            steps.append('Detected investment keyword')
            result = 'Investment Report'
        elif 'loan' in self.text:
            steps.append('Detected loan keyword')
            result = 'Loan Agreement'
        else:
            steps.append('No keyword detected')
            result = 'Other'
        return steps, result

# Example usage
sample_text = "# Loan Details\nThis is your loan agreement."
classifier = ChainOfThoughtClassifier(sample_text)
steps, result = classifier.run()
print('Steps:', steps)
print('Result:', result)
