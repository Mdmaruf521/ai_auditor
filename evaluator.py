import numpy as np

def hallucination_score(text):
    triggers = ["always", "never", "guarantee", "100%"]
    return min(sum(t in text.lower() for t in triggers) / 3, 1)


def bias_score(prompt):
    keywords = ["female", "male", "women", "men"]
    return 0.3 if any(k in prompt.lower() for k in keywords) else 0.05


def risk_score(h, b):
    return round((h * 0.6) + (b * 0.4), 3)