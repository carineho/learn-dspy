# Day 5: Experimentation & Extensions
# Experiment with DSPy and extend your classifier.
# Try extending the logic or integrating with an actual LLM API.

import dspy
# Placeholder for LLM integration
class LLMClassifier(dspy.Task):
    def __init__(self, text):
        self.text = text
    def run(self):
        # Imagine calling an LLM here
        # For now, use simple logic
        if 'agreement' in self.text:
            return 'Loan Agreement'
        return 'Other'

# Example usage
sample_text = "# Loan Agreement\nThis is a loan agreement."
classifier = LLMClassifier(sample_text)
print(classifier.run())
