import sqlite3

def get_conn():
    conn = sqlite3.connect("ai_audit.db")
    return conn


def init_db():
    conn = get_conn()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS runs (
        response_id INTEGER,
        prompt TEXT,
        response TEXT,
        model TEXT,
        hallucination_score REAL,
        bias_score REAL,
        risk_score REAL
    )
    """)

    conn.commit()
    conn.close()