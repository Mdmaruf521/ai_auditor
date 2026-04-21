import pandas as pd

def load_data():
    prompts = pd.read_csv("prompts.csv")
    responses = pd.read_csv("responses.csv")
    evaluation = pd.read_csv("evaluation.csv")

    df = responses.merge(evaluation, on="response_id")
    df = df.merge(prompts, on="prompt_id")

    return df