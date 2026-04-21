from db import get_conn
from evaluator import hallucination_score, bias_score, risk_score

def log_run(prompt_id, prompt, response, model="gpt-4"):
    h = hallucination_score(response)
    b = bias_score(prompt)
    r = risk_score(h, b)

    conn = get_conn()
    c = conn.cursor()

    c.execute("""
    INSERT INTO runs VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (prompt_id, prompt, response, model, h, b, r))

    conn.commit()
    conn.close()

    return r