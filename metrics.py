import pandas as pd
import numpy as np

def compute_metrics(df):
    total = len(df)
    hallucination_rate = df["hallucination_flag"].mean()
    bias_rate = df["bias_flag"].mean()
    accuracy = df["correct"].mean()
    avg_confidence = df["confidence"].mean()

    return {
        "total": total,
        "hallucination_rate": hallucination_rate,
        "bias_rate": bias_rate,
        "accuracy": accuracy,
        "avg_confidence": avg_confidence
    }

def hallucination_by_category(df):
    return df.groupby("category")["hallucination_flag"].mean()

def faithfulness_distribution(df):
    return pd.cut(df["faithfulness_score"], bins=8).value_counts().sort_index()

def calibration_data(df):
    df = df.copy()
    df["confidence_bucket"] = pd.cut(df["confidence"], bins=[0,50,70,90,100])
    return df.groupby("confidence_bucket")["correct"].mean()

def variance_analysis(df):
    variance = df.groupby("prompt_id")["response"].nunique()
    high_variance = variance[variance > 1]
    return variance, high_variance