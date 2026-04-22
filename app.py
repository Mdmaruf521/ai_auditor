import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import io
import json
import hashlib

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="AI CAUGHT // AI OBSERVABILITY OS",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# PREMIUM STYLE ENGINE
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;700;800&family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background: #030712 !important;
    color: #e2e8f0 !important;
}
.block-container { padding: 1.5rem 2rem 3rem 2rem !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { background: #050d1a !important; border-right: 1px solid #0f2540; }
.stApp { background: radial-gradient(ellipse at 20% 50%, #0a1628 0%, #030712 60%) !important; }

.aegis-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(1.4rem, 3vw, 2.4rem);
    font-weight: 800;
    background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #34d399 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.2;
    margin-bottom: 0.2rem;
    padding-top: 0.5rem;
    word-break: break-word;
}
.aegis-subtitle {
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    color: #475569;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
}
.section-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem;
    color: #38bdf8;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}
.metric-card {
    background: linear-gradient(145deg, #0d1f3c, #091629);
    border: 1px solid #1e3a5f;
    border-radius: 16px;
    padding: 20px 24px;
    position: relative;
    overflow: hidden;
    transition: transform 0.2s ease, border-color 0.2s ease;
    margin-bottom: 8px;
}
.metric-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #38bdf8, #818cf8, #34d399);
}
.metric-card .label {
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    margin-bottom: 8px;
}
.metric-card .value {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    color: #f1f5f9;
    line-height: 1;
}
.metric-card .delta { font-size: 0.75rem; color: #34d399; margin-top: 6px; font-weight: 500; }
.metric-card .delta.bad { color: #f87171; }

.card { background: #0d1f3c; border: 1px solid #1e3a5f; padding: 20px; border-radius: 14px; margin-bottom: 12px; }

.risk-badge {
    display: inline-block; padding: 4px 12px; border-radius: 20px;
    font-family: 'Space Mono', monospace; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.08em;
}
.risk-low  { background: rgba(52,211,153,0.15); color: #34d399; border: 1px solid rgba(52,211,153,0.3); }
.risk-mid  { background: rgba(251,191,36,0.15);  color: #fbbf24; border: 1px solid rgba(251,191,36,0.3); }
.risk-high { background: rgba(248,113,113,0.15); color: #f87171; border: 1px solid rgba(248,113,113,0.3); }
.risk-critical {
    background: rgba(239,68,68,0.2); color: #ef4444; border: 1px solid rgba(239,68,68,0.5);
    animation: pulse-red 2s infinite;
}
@keyframes pulse-red {
    0%,100% { box-shadow: 0 0 0 0 rgba(239,68,68,0.4); }
    50%      { box-shadow: 0 0 0 6px rgba(239,68,68,0); }
}

.article-card {
    background: linear-gradient(160deg, #0d1f3c, #071525);
    border: 1px solid #1e3a5f; border-radius: 16px; padding: 28px 32px; margin-bottom: 16px;
}
.article-card h3 { font-family: 'Syne', sans-serif; font-size: 1.25rem; font-weight: 700; color: #38bdf8; margin-bottom: 12px; }
.article-card p, .article-card li { font-size: 0.95rem; color: #94a3b8; line-height: 1.75; }
.article-card strong { color: #e2e8f0; }
.article-card code { background: #0a1628; color: #34d399; padding: 2px 8px; border-radius: 4px; font-family: 'Space Mono', monospace; font-size: 0.8rem; }
.article-tag {
    display: inline-block; padding: 3px 10px; border-radius: 12px; font-size: 0.65rem;
    font-family: 'Space Mono', monospace;
    background: rgba(129,140,248,0.15); color: #818cf8; border: 1px solid rgba(129,140,248,0.3);
    margin-right: 6px; margin-bottom: 12px;
}
.article-key-insight {
    background: rgba(56,189,248,0.08); border-left: 3px solid #38bdf8;
    padding: 14px 18px; border-radius: 0 10px 10px 0; margin: 16px 0;
    font-size: 0.9rem; color: #bae6fd; font-style: italic;
}

.sidebar-logo {
    font-family: 'Syne', sans-serif; font-size: 1.4rem; font-weight: 800;
    background: linear-gradient(135deg, #38bdf8, #818cf8);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
    padding: 12px 0 4px 0;
}
.sidebar-tagline {
    font-family: 'Space Mono', monospace; font-size: 0.6rem; color: #475569;
    letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 16px;
    padding-bottom: 16px; border-bottom: 1px solid #1e3a5f;
}
.nav-chip {
    display: inline-block; background: rgba(56,189,248,0.1); color: #38bdf8;
    border: 1px solid rgba(56,189,248,0.25); border-radius: 6px; padding: 2px 8px;
    font-family: 'Space Mono', monospace; font-size: 0.6rem; margin-left: 6px; vertical-align: middle;
}
.aegis-divider { height: 1px; background: linear-gradient(90deg, transparent, #1e3a5f, transparent); margin: 24px 0; }

.alert-critical {
    background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.3);
    border-radius: 10px; padding: 14px 18px; margin-bottom: 10px; font-size: 0.88rem; color: #fca5a5;
}
.alert-warning {
    background: rgba(251,191,36,0.08); border: 1px solid rgba(251,191,36,0.3);
    border-radius: 10px; padding: 14px 18px; margin-bottom: 10px; font-size: 0.88rem; color: #fde68a;
}
.alert-ok {
    background: rgba(52,211,153,0.08); border: 1px solid rgba(52,211,153,0.3);
    border-radius: 10px; padding: 14px 18px; margin-bottom: 10px; font-size: 0.88rem; color: #6ee7b7;
}
.alert-info {
    background: rgba(56,189,248,0.08); border: 1px solid rgba(56,189,248,0.3);
    border-radius: 10px; padding: 14px 18px; margin-bottom: 10px; font-size: 0.88rem; color: #bae6fd;
}

.compliance-row {
    display: flex; align-items: center; justify-content: space-between;
    padding: 12px 16px; border-radius: 10px; margin-bottom: 8px;
    background: #091629; border: 1px solid #1e3a5f; font-size: 0.9rem;
}
.compliance-pass { border-left: 3px solid #34d399; }
.compliance-fail  { border-left: 3px solid #f87171; }
.compliance-warn  { border-left: 3px solid #fbbf24; }

div[data-testid="metric-container"] {
    background: #0d1f3c !important; border: 1px solid #1e3a5f !important;
    border-radius: 12px !important; padding: 16px !important;
}
div[data-testid="metric-container"] label {
    color: #64748b !important; font-family: 'Space Mono', monospace !important; font-size: 0.7rem !important;
}
div[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #f1f5f9 !important; font-family: 'Syne', sans-serif !important;
    font-size: 1.8rem !important; font-weight: 700 !important;
}

.stButton > button {
    background: linear-gradient(135deg, #0369a1, #1e40af) !important;
    color: white !important; border: 1px solid rgba(56,189,248,0.3) !important;
    border-radius: 10px !important; font-family: 'Space Mono', monospace !important;
    font-size: 0.75rem !important; letter-spacing: 0.08em !important;
    padding: 0.5rem 1.5rem !important; transition: all 0.2s ease !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #0284c7, #2563eb) !important;
    border-color: #38bdf8 !important; transform: translateY(-1px) !important;
    box-shadow: 0 4px 15px rgba(56,189,248,0.2) !important;
}

.stSelectbox > div > div, .stTextArea textarea, .stNumberInput input {
    background: #091629 !important; border-color: #1e3a5f !important;
    color: #e2e8f0 !important; border-radius: 10px !important; font-family: 'Inter', sans-serif !important;
}
.stProgress > div > div > div {
    background: linear-gradient(90deg, #38bdf8, #818cf8) !important; border-radius: 4px !important;
}
div[data-testid="stExpander"] {
    background: #0d1f3c !important; border: 1px solid #1e3a5f !important; border-radius: 12px !important;
}

.compare-table { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
.compare-table th {
    background: #0a1628; color: #38bdf8; font-family: 'Space Mono', monospace;
    font-size: 0.65rem; letter-spacing: 0.1em; text-transform: uppercase;
    padding: 12px 16px; text-align: left; border-bottom: 1px solid #1e3a5f;
}
.compare-table td { padding: 11px 16px; border-bottom: 1px solid #0f2540; color: #cbd5e1; }
.compare-table tr:hover td { background: rgba(56,189,248,0.04); }
.compare-table .best  { color: #34d399; font-weight: 600; }
.compare-table .worst { color: #f87171; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# DATA ENGINE
# ─────────────────────────────────────────────
@st.cache_data
def generate(n=1200):
    np.random.seed(42)
    models  = ["GPT-4o", "Claude", "Gemini", "Llama"]
    domains = ["Legal", "Medical", "Code", "Finance", "Support"]
    df = pd.DataFrame({
        "model":       np.random.choice(models, n),
        "domain":      np.random.choice(domains, n),
        "confidence":  np.random.uniform(0.4, 0.99, n),
        "correctness": np.random.uniform(0.2, 1.0, n),
        "hallucination": np.random.binomial(1, 0.12, n),
        "latency":     np.random.uniform(100, 2200, n),
        "toxicity":    np.random.uniform(0, 0.3, n),
    })
    df["truth_gap"] = df["confidence"] - df["correctness"]
    df["risk"] = (
        (1 - df["correctness"]) * 0.3 +
        df["hallucination"]     * 0.35 +
        df["toxicity"]          * 0.15 +
        (1 - df["confidence"])  * 0.2
    )
    return df

df = generate()

# ─────────────────────────────────────────────
# PLOTLY THEME
# ─────────────────────────────────────────────
PLOTLY_THEME = dict(
    paper_bgcolor="rgba(9,22,41,0.95)",
    plot_bgcolor="rgba(9,22,41,0.95)",
    font=dict(color="#94a3b8", family="Inter"),
    title_font=dict(color="#e2e8f0", family="Syne", size=15),
    xaxis=dict(gridcolor="#1e3a5f", zerolinecolor="#1e3a5f", showline=False),
    yaxis=dict(gridcolor="#1e3a5f", zerolinecolor="#1e3a5f", showline=False),
    colorway=["#38bdf8","#818cf8","#34d399","#fbbf24","#f87171"],
    margin=dict(t=50, b=40, l=40, r=20),
)

def style_fig(fig):
    fig.update_layout(**PLOTLY_THEME)
    return fig

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def plain_explainer(title, text):
    st.markdown(
        f'<div style="background:rgba(56,189,248,0.06);border:1px solid rgba(56,189,248,0.18);'
        f'border-radius:12px;padding:16px 20px;margin-bottom:16px;">'
        f'<div style="font-family:\'Space Mono\',monospace;font-size:0.6rem;color:#38bdf8;'
        f'letter-spacing:0.15em;text-transform:uppercase;margin-bottom:6px;">What does this mean?</div>'
        f'<div style="font-size:0.9rem;color:#bae6fd;line-height:1.65;">{text}</div></div>',
        unsafe_allow_html=True
    )

def section_header(title, badge=None):
    badge_html = f'<span class="nav-chip">{badge}</span>' if badge else ""
    st.markdown(f'<div class="aegis-title">{title}{badge_html}</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-logo">AI CAUGHT</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-tagline">AI Observability OS // Enterprise Grade</div>', unsafe_allow_html=True)

    health = round((1 - df["risk"].mean()) * 100, 1)
    health_color = "#34d399" if health >= 70 else "#fbbf24" if health >= 50 else "#f87171"
    st.markdown(
        f'<div style="background:#091629;border:1px solid #1e3a5f;border-radius:12px;padding:14px 16px;margin-bottom:16px;">'
        f'<div style="font-family:\'Space Mono\',monospace;font-size:0.6rem;color:#475569;text-transform:uppercase;'
        f'letter-spacing:0.1em;margin-bottom:6px;">System Health</div>'
        f'<div style="font-family:\'Syne\',sans-serif;font-size:1.8rem;font-weight:800;color:{health_color};">{health}%</div>'
        f'<div style="height:4px;background:#1e3a5f;border-radius:2px;margin-top:8px;">'
        f'<div style="height:4px;width:{health}%;background:{health_color};border-radius:2px;"></div></div></div>',
        unsafe_allow_html=True
    )

    page = st.radio(
        "Navigate",
        [
            "Dashboard",
            "Prompt Lab",
            "Model Forensics",
            "Incident Timeline",
            "AI Health Score",
            "Model Benchmark",
            "Compliance Checker",
            "Risk Simulator",
            "Learning Hub",
            "Economics",
            "Export Report",
        ],
        label_visibility="collapsed"
    )

    st.markdown('<div class="aegis-divider"></div>', unsafe_allow_html=True)
    st.markdown(
        '<div style="font-family:\'Space Mono\',monospace;font-size:0.6rem;color:#334155;line-height:1.8;">'
        'DATA: 1,200 synthetic audit events<br>'
        'MODELS: GPT-4o / Claude / Gemini / Llama<br>'
        'DOMAINS: Legal / Medical / Finance / Code / Support<br>'
        'VERSION: 14.0.0 // 2026</div>',
        unsafe_allow_html=True
    )


# ═══════════════════════════════════════════════════════════
#  DASHBOARD
# ═══════════════════════════════════════════════════════════
if page == "Dashboard":

    # ── Fixed title with padding so it clears the sidebar toggle bar ──
    st.markdown(
        '<div style="padding-top:0.25rem;">'
        '<div class="aegis-title">AI Observability Command Center'
        '<span class="nav-chip">LIVE</span></div>'
        '<div class="aegis-subtitle">Real-time surveillance across all model behaviours, failure modes and risk surfaces</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # ── Model selector for dashboard ──────────────────────
    all_models = ["All Models"] + sorted(df["model"].unique().tolist())
    dash_model = st.selectbox("Filter Dashboard by Model", all_models, key="dash_model_select")
    ddf = df if dash_model == "All Models" else df[df["model"] == dash_model]

    c1, c2, c3, c4, c5 = st.columns(5)
    avg_risk  = ddf["risk"].mean()
    hall_rate = ddf["hallucination"].mean()
    risk_color = "#f87171" if avg_risk > 0.4 else "#fbbf24" if avg_risk > 0.25 else "#34d399"

    with c1:
        st.markdown(
            f'<div class="metric-card"><div class="label">Avg System Risk</div>'
            f'<div class="value" style="color:{risk_color}">{avg_risk:.3f}</div>'
            f'<div class="delta bad">+0.012 vs last week</div></div>',
            unsafe_allow_html=True
        )
    with c2:
        st.markdown(
            f'<div class="metric-card"><div class="label">Truth Gap</div>'
            f'<div class="value">{ddf["truth_gap"].mean():.3f}</div>'
            f'<div class="delta">Confidence vs Reality</div></div>',
            unsafe_allow_html=True
        )
    with c3:
        st.markdown(
            f'<div class="metric-card"><div class="label">Hallucination Rate</div>'
            f'<div class="value" style="color:#fbbf24">{hall_rate:.2%}</div>'
            f'<div class="delta bad">1 in {int(1/hall_rate)} responses</div></div>',
            unsafe_allow_html=True
        )
    with c4:
        st.markdown(
            f'<div class="metric-card"><div class="label">Avg Latency</div>'
            f'<div class="value">{ddf["latency"].mean():.0f}ms</div>'
            f'<div class="delta">P95: {ddf["latency"].quantile(0.95):.0f}ms</div></div>',
            unsafe_allow_html=True
        )
    with c5:
        toxic_pct = (ddf["toxicity"] > 0.15).mean()
        st.markdown(
            f'<div class="metric-card"><div class="label">Toxicity Flags</div>'
            f'<div class="value" style="color:#f87171">{toxic_pct:.2%}</div>'
            f'<div class="delta bad">Responses above threshold</div></div>',
            unsafe_allow_html=True
        )

    st.markdown('<div class="aegis-divider"></div>', unsafe_allow_html=True)
    plain_explainer("Dashboard Overview",
        "This dashboard watches all your AI models 24/7. Think of it as a security camera for your AI — "
        "it catches when models make things up (hallucinations), when they sound confident but are wrong, "
        "and flags which industry areas carry the highest risk."
    )

    # Smart Alerts
    st.markdown('<div class="section-label">Live Alerts</div>', unsafe_allow_html=True)
    worst_domain = ddf.groupby("domain")["risk"].mean().idxmax()
    worst_model  = ddf.groupby("model")["risk"].mean().idxmax() if dash_model == "All Models" else dash_model

    st.markdown(
        f'<div class="alert-critical">CRITICAL: {worst_domain} domain has the highest risk exposure '
        f'({ddf[ddf.domain==worst_domain]["risk"].mean():.3f}). Immediate review recommended.</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="alert-warning">WARNING: {worst_model} shows elevated hallucination patterns '
        f'({ddf[ddf.model==worst_model]["hallucination"].mean():.2%} rate). '
        f'Consider additional validation layers.</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="alert-ok">OK: Average toxicity is within acceptable bounds '
        f'({ddf["toxicity"].mean():.3f} avg).</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="alert-info">INFO: Truth Gap of {ddf["truth_gap"].mean():.3f} indicates models are '
        f'moderately overconfident. Standard for production LLMs.</div>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="aegis-divider"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        fig = style_fig(px.histogram(ddf, x="risk", nbins=40, title="1. Risk Distribution",
                                     color_discrete_sequence=["#38bdf8"]))
        st.plotly_chart(fig, use_container_width=True)
        st.caption("How often your system enters unsafe output territory. Left = safe. Right = dangerous.")
    with col2:
        fig2 = style_fig(px.scatter(ddf, x="confidence", y="correctness", color="domain",
                                    title="2. Confidence vs Reality", opacity=0.6))
        fig2.add_shape(type="line", x0=0, y0=0, x1=1, y1=1,
                       line=dict(color="#f87171", dash="dash", width=2))
        st.plotly_chart(fig2, use_container_width=True)
        st.caption("Red diagonal = perfect calibration. Points below the line = confident but wrong.")

    col3, col4 = st.columns(2)
    with col3:
        fig3 = style_fig(px.density_heatmap(ddf, x="confidence", y="correctness",
                                             title="3. Failure Heatmap", color_continuous_scale="Blues"))
        st.plotly_chart(fig3, use_container_width=True)
        st.caption("Bright clusters = systematic failure zones.")
    with col4:
        fig4 = style_fig(px.box(ddf, x="model", y="risk", title="4. Model Risk Profile", color="model"))
        st.plotly_chart(fig4, use_container_width=True)
        st.caption("Each model has a unique failure fingerprint. Taller boxes = more unpredictable.")

    col5, col6 = st.columns(2)
    with col5:
        fig5 = style_fig(px.scatter(ddf, x="latency", y="risk", title="5. Latency vs Risk",
                                    color="model", opacity=0.5))
        st.plotly_chart(fig5, use_container_width=True)
        st.caption("Slow models are not automatically safer.")
    with col6:
        domain_risk = ddf.groupby("domain")["risk"].mean().reset_index().sort_values("risk", ascending=False)
        fig6 = style_fig(px.bar(domain_risk, x="domain", y="risk", title="6. Domain Risk Exposure",
                                color="risk", color_continuous_scale="Reds"))
        st.plotly_chart(fig6, use_container_width=True)
        st.caption("Which industries carry the most risk when AI is deployed there.")

    col7, col8 = st.columns(2)
    with col7:
        hall_counts = ddf["hallucination"].value_counts().reset_index()
        hall_counts.columns = ["hallucinated", "count"]
        hall_counts["hallucinated"] = hall_counts["hallucinated"].map(
            {0: "No Hallucination", 1: "Hallucinated"})
        fig7 = style_fig(px.pie(hall_counts, names="hallucinated", values="count",
                                title="7. Hallucination Split",
                                color_discrete_sequence=["#34d399", "#f87171"]))
        st.plotly_chart(fig7, use_container_width=True)
        st.caption("What fraction of all AI responses contained fabricated information.")
    with col8:
        fig8 = style_fig(px.violin(ddf, x="model", y="risk", title="8. Risk Distribution Shape",
                                   color="model", box=True))
        st.plotly_chart(fig8, use_container_width=True)
        st.caption("Wide violin = inconsistent. Narrow violin = predictable. You want narrow.")

    fig9 = style_fig(px.scatter_3d(ddf.sample(min(400, len(ddf))), x="confidence", y="correctness", z="latency",
                                   color="model", title="9. 3D Behavior Space", opacity=0.7))
    st.plotly_chart(fig9, use_container_width=True)
    st.caption("Full behavior fingerprint: confidence, correctness, and latency in a single view.")

    col9, col10 = st.columns(2)
    with col9:
        fig10 = style_fig(px.line(ddf.sort_values("confidence"), y="risk", title="10. Risk Curve",
                                  color_discrete_sequence=["#818cf8"]))
        st.plotly_chart(fig10, use_container_width=True)
        st.caption("How total risk evolves as model confidence increases.")
    with col10:
        corr = ddf[["risk","confidence","correctness","latency"]].corr()
        fig11 = style_fig(px.imshow(corr, title="11. Correlation Matrix",
                                    color_continuous_scale="RdBu_r", zmin=-1, zmax=1))
        st.plotly_chart(fig11, use_container_width=True)
        st.caption("Hidden relationships between system metrics.")

    fig12 = style_fig(px.histogram(ddf, x="truth_gap", nbins=40, title="12. Truth Gap Distribution",
                                   color_discrete_sequence=["#fbbf24"]))
    fig12.add_vline(x=0, line_dash="dash", line_color="#f87171", annotation_text="Perfect Calibration")
    st.plotly_chart(fig12, use_container_width=True)
    st.caption("Right of red line = overconfident. Left = underconfident.")


# ═══════════════════════════════════════════════════════════
#  PROMPT LAB  — enriched logic, no LLM required
# ═══════════════════════════════════════════════════════════
elif page == "Prompt Lab":

    section_header("Prompt Audit Engine")
    st.markdown('<div class="aegis-subtitle">Paste any prompt and response to get an instant hallucination and quality audit</div>', unsafe_allow_html=True)

    plain_explainer("How This Works",
        "This tool scans your AI prompt and the response it generated. It checks: Is the prompt clear enough? "
        "Does the response use overconfident language? Does it have RAG grounding? "
        "You get a detailed risk breakdown — no technical knowledge required."
    )

    col_a, col_b = st.columns(2)
    with col_a:
        prompt = st.text_area("Prompt (what you asked the AI)", height=160,
                              placeholder="e.g. What are the legal requirements for forming a company in the UK?")
    with col_b:
        response = st.text_area("Response (what the AI said)", height=160,
                                placeholder="Paste the AI response here...")

    opt_cols = st.columns(3)
    with opt_cols[0]:
        domain_sel = st.selectbox("Domain Context", ["General","Legal","Medical","Finance","Code","Support"])
    with opt_cols[1]:
        model_sel = st.selectbox("Model Used", ["GPT-4o","Claude","Gemini","Llama","Other"])
    with opt_cols[2]:
        rag_enabled = st.selectbox("RAG / Knowledge Grounding", ["No RAG (open generation)","RAG enabled — internal docs","RAG enabled — verified external","Fine-tuned domain model"])

    adv_col1, adv_col2, adv_col3 = st.columns(3)
    with adv_col1:
        temperature = st.slider("Model Temperature", 0.0, 1.0, 0.7, 0.05,
                                help="Higher = more creative/risky. Lower = more deterministic.")
    with adv_col2:
        system_prompt_quality = st.selectbox("System Prompt Quality",
            ["None / Default", "Basic role instruction", "Detailed with constraints", "Production-grade with guardrails"])
    with adv_col3:
        use_case_sensitivity = st.selectbox("Use Case Sensitivity",
            ["Low (internal draft)", "Medium (customer-facing)", "High (regulated output)", "Critical (life/legal/financial)"])

    if st.button("Run Audit"):
        if prompt.strip() and response.strip():

            # ── Deterministic but varied scoring engine ─────
            # Seed based on prompt+response hash so the SAME inputs always give the SAME result
            # but DIFFERENT inputs give different results
            seed_val = int(hashlib.md5((prompt + response + model_sel + domain_sel).encode()).hexdigest(), 16) % (2**31)
            rng = np.random.default_rng(seed_val)

            prompt_words   = len(prompt.split())
            response_words = len(response.split())
            prompt_chars   = len(prompt)
            response_chars = len(response)

            # --- Clarity ---
            clarity = min(prompt_words / 35, 1.0)
            # Reward question marks, penalise very short prompts
            if "?" in prompt: clarity = min(clarity + 0.08, 1.0)
            if prompt_words < 5: clarity = max(clarity - 0.25, 0.0)
            if prompt_words > 60: clarity = min(clarity + 0.12, 1.0)

            # --- Overconfidence flags ---
            dangerous_words = ["guarantee","always","never","definitely","certainly","100%",
                               "proven","impossible","absolutely","without doubt","confirmed fact",
                               "scientifically proven","guaranteed","no exceptions","irrefutably"]
            hedge_words     = ["possibly","might","could","may","approximately","around","likely",
                               "suggests","indicates","appears","seems","based on available","unclear",
                               "uncertain","varies","consult","verify","double-check"]
            citation_words  = ["according to","source:","reference:","study shows","research indicates",
                               "published","per the","as per","cited in","from the"]

            danger_count   = sum(1 for w in dangerous_words if w in response.lower())
            hedge_count    = sum(1 for w in hedge_words     if w in response.lower())
            citation_count = sum(1 for w in citation_words  if w in response.lower())

            # --- RAG adjustment ---
            rag_risk_reduction = {
                "No RAG (open generation)": 0.0,
                "RAG enabled — internal docs": -0.12,
                "RAG enabled — verified external": -0.18,
                "Fine-tuned domain model": -0.10,
            }
            rag_reduction = rag_risk_reduction.get(rag_enabled, 0.0)

            # --- Temperature effect ---
            temp_risk_add = temperature * 0.18  # high temp = higher hallucination risk

            # --- System prompt quality ---
            sys_prompt_mod = {
                "None / Default": 0.10,
                "Basic role instruction": 0.04,
                "Detailed with constraints": -0.05,
                "Production-grade with guardrails": -0.12,
            }
            sys_mod = sys_prompt_mod.get(system_prompt_quality, 0.0)

            # --- Use case sensitivity ---
            sensitivity_mod = {
                "Low (internal draft)": -0.04,
                "Medium (customer-facing)": 0.02,
                "High (regulated output)": 0.08,
                "Critical (life/legal/financial)": 0.15,
            }
            sens_mod = sensitivity_mod.get(use_case_sensitivity, 0.0)

            # --- Domain base risk ---
            domain_risk_adj = {"Legal":0.08,"Medical":0.10,"Finance":0.07,"Code":0.03,"General":0,"Support":0.02}
            domain_add = domain_risk_adj.get(domain_sel, 0)

            # --- Model baseline variance ---
            model_baselines = {
                "GPT-4o":  {"risk": 0.0,   "hall": 0.11, "latency": 820,  "calibration": 0.78},
                "Claude":  {"risk": -0.03, "hall": 0.09, "latency": 960,  "calibration": 0.82},
                "Gemini":  {"risk": 0.02,  "hall": 0.13, "latency": 740,  "calibration": 0.75},
                "Llama":   {"risk": 0.05,  "hall": 0.16, "latency": 1100, "calibration": 0.70},
                "Other":   {"risk": 0.04,  "hall": 0.14, "latency": 950,  "calibration": 0.72},
            }
            model_b = model_baselines.get(model_sel, model_baselines["Other"])

            # --- Core risk computation ---
            base_risk = (
                (1 - clarity) * 0.25 +
                min(response_chars / 3000, 1) * 0.15 +
                (danger_count / max(len(dangerous_words), 1)) * 0.30 +
                (1 - min(hedge_count / 5, 1)) * 0.15 +
                model_b["risk"] * 0.15
            )
            risk = base_risk + domain_add + rag_reduction + temp_risk_add + sys_mod + sens_mod
            risk = float(np.clip(risk + rng.uniform(-0.04, 0.04), 0.0, 1.0))

            # --- Truth gap proxy ---
            truth_gap = abs(prompt_chars - response_chars) / max(prompt_chars, 1)
            truth_gap = min(truth_gap, 5.0)

            # --- Hallucination likelihood ---
            hall_prob = model_b["hall"] + (domain_add * 0.5) + (temp_risk_add * 0.4) + (danger_count * 0.03)
            hall_prob = float(np.clip(hall_prob + rng.uniform(-0.02, 0.02), 0.0, 1.0))

            # --- Calibration score ---
            calibration_score = model_b["calibration"] - (danger_count * 0.05) + (hedge_count * 0.02) + (citation_count * 0.03)
            calibration_score = float(np.clip(calibration_score + rng.uniform(-0.03, 0.03), 0.0, 1.0))

            # --- Estimated latency ---
            latency_est = int(model_b["latency"] * (0.8 + temperature * 0.4) * (0.5 + response_words / 200))

            # --- Complexity score ---
            complexity_score = min((prompt_words / 20) * 0.4 + (response_words / 100) * 0.6, 1.0)

            # --- Store for export ---
            st.session_state["last_audit"] = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "prompt": prompt,
                "response": response,
                "model": model_sel,
                "domain": domain_sel,
                "rag": rag_enabled,
                "temperature": temperature,
                "system_prompt_quality": system_prompt_quality,
                "use_case_sensitivity": use_case_sensitivity,
                "clarity_score": round(clarity, 3),
                "hallucination_risk": round(risk, 3),
                "hallucination_likelihood_pct": round(hall_prob * 100, 1),
                "truth_gap_proxy": round(truth_gap, 3),
                "hedge_ratio": f"{hedge_count}/{response_words}",
                "calibration_score": round(calibration_score, 3),
                "danger_words_found": [w for w in dangerous_words if w in response.lower()],
                "hedge_words_found": [w for w in hedge_words if w in response.lower()],
                "citation_signals": citation_count,
                "estimated_latency_ms": latency_est,
                "complexity_score": round(complexity_score, 3),
            }
            audit = st.session_state["last_audit"]

            st.markdown('<div class="aegis-divider"></div>', unsafe_allow_html=True)
            st.markdown("#### Core Metrics")
            r1, r2, r3, r4, r5, r6 = st.columns(6)
            r1.metric("Clarity Score",          f"{clarity:.2f}")
            r2.metric("Hallucination Risk",     f"{risk:.2f}")
            r3.metric("Hall. Likelihood",       f"{hall_prob:.1%}")
            r4.metric("Truth Gap Proxy",        f"{truth_gap:.2f}")
            r5.metric("Calibration",            f"{calibration_score:.2f}")
            r6.metric("Hedge Ratio",            f"{hedge_count}/{response_words}")

            st.markdown("#### Extended Metrics")
            e1, e2, e3, e4 = st.columns(4)
            e1.metric("Danger Words",     str(danger_count))
            e2.metric("Citation Signals", str(citation_count))
            e3.metric("Est. Latency",     f"{latency_est} ms")
            e4.metric("Complexity",       f"{complexity_score:.2f}")

            st.markdown("**Overall Risk Level:**")
            st.progress(min(risk, 1.0))

            if risk > 0.7:
                st.markdown(
                    '<div class="alert-critical">CRITICAL RISK: This response is very likely to contain '
                    'hallucinated content. Do NOT use without expert verification.</div>',
                    unsafe_allow_html=True
                )
            elif risk > 0.4:
                st.markdown(
                    '<div class="alert-warning">MODERATE RISK: Some hallucination signals detected. '
                    'Cross-reference key claims before relying on this response.</div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    '<div class="alert-ok">LOW RISK: This response shows reasonable calibration. '
                    'Standard verification practices are sufficient.</div>',
                    unsafe_allow_html=True
                )

            # ── RAG impact callout ─────────────────────────
            if rag_reduction < 0:
                st.markdown(
                    f'<div class="alert-info">RAG GROUNDING: {rag_enabled} reduced estimated risk by '
                    f'{abs(rag_reduction):.0%}. Grounded responses are significantly more reliable.</div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    '<div class="alert-warning">NO RAG: Response is based on open generation with no '
                    'document grounding. Consider enabling RAG to reduce hallucination risk by 12–18%.</div>',
                    unsafe_allow_html=True
                )

            # ── Model-specific insight ─────────────────────
            model_insights = {
                "GPT-4o":  "GPT-4o is well-calibrated for most tasks but shows elevated hallucination in niche legal/medical citations.",
                "Claude":  "Claude typically hedges well and has lower hallucination rates, especially in longer analytical tasks.",
                "Gemini":  "Gemini performs well on factual retrieval but can overstate confidence in low-frequency knowledge areas.",
                "Llama":   "Open-source Llama models have higher baseline hallucination rates. RAG grounding is strongly recommended.",
                "Other":   "Unknown model — apply conservative risk thresholds and verify all factual claims independently.",
            }
            st.markdown(
                f'<div class="alert-info">MODEL INSIGHT [{model_sel}]: {model_insights.get(model_sel, "")}</div>',
                unsafe_allow_html=True
            )

            if danger_count > 0:
                found = [w for w in dangerous_words if w in response.lower()]
                st.markdown(
                    f'<div class="alert-warning">Overconfident language detected: '
                    f'<strong>{", ".join(found)}</strong>. Real-world AI systems rarely have absolute certainties.</div>',
                    unsafe_allow_html=True
                )

            if citation_count > 0:
                st.markdown(
                    f'<div class="alert-ok">Citation signals detected ({citation_count} instance(s)). '
                    f'Verify that cited sources actually exist — LLMs can fabricate plausible-sounding references.</div>',
                    unsafe_allow_html=True
                )

            # ── Temperature warning ────────────────────────
            if temperature > 0.8:
                st.markdown(
                    f'<div class="alert-warning">HIGH TEMPERATURE ({temperature}): Elevated creativity setting '
                    f'increases hallucination risk by ~{temp_risk_add:.0%}. Consider reducing to 0.3–0.5 for '
                    f'factual tasks.</div>',
                    unsafe_allow_html=True
                )

            # ── Use case warning ──────────────────────────
            if use_case_sensitivity in ["High (regulated output)", "Critical (life/legal/financial)"]:
                st.markdown(
                    f'<div class="alert-critical">USE CASE ALERT: {use_case_sensitivity} — This output '
                    f'requires mandatory human review by a qualified professional before use. AI output '
                    f'in this context carries legal and/or safety liability.</div>',
                    unsafe_allow_html=True
                )

            st.markdown("#### Audit Recommendations")
            recs = []
            if clarity < 0.5:
                recs.append("**Prompt clarity is low.** Make your prompt more specific — include context, constraints, and the exact format needed.")
            if truth_gap > 2:
                recs.append("**Response length mismatch.** The response is far longer than the prompt suggests is needed. Long responses carry more hallucination surface area.")
            if danger_count > 0:
                recs.append("**Challenge absolute statements.** Ask the AI to cite sources or express uncertainty instead of using definitive language.")
            if domain_sel in ["Medical","Legal","Finance"]:
                recs.append(f"**High-stakes domain.** This is a {domain_sel} context. Always have a licensed professional validate AI output before acting on it.")
            if hedge_count < 2:
                recs.append("**Insufficient hedging.** The response lacks uncertainty language. Well-calibrated AI should express doubt where appropriate.")
            if rag_enabled == "No RAG (open generation)" and domain_sel in ["Legal","Medical","Finance"]:
                recs.append("**Enable RAG grounding.** For this domain, connecting the model to a verified document store can reduce hallucination risk by 12–18%.")
            if temperature > 0.7:
                recs.append(f"**Lower the temperature.** Current setting ({temperature}) is high for factual tasks. Target 0.2–0.5 for accuracy-critical use cases.")
            if system_prompt_quality in ["None / Default", "Basic role instruction"] and use_case_sensitivity != "Low (internal draft)":
                recs.append("**Improve system prompt.** A production-grade system prompt with guardrails can reduce risk by up to 12 percentage points.")
            if citation_count > 0:
                recs.append("**Verify all citations.** The response contains citation-like language — check that every referenced source actually exists.")

            if recs:
                for rec in recs:
                    st.markdown(f"- {rec}")
            else:
                st.success("Prompt and response appear well-formed. Standard review processes apply.")

            # ── Risk radar chart ───────────────────────────
            st.markdown("#### Risk Radar")
            radar_vals = [
                1 - clarity,
                risk,
                hall_prob,
                min(truth_gap / 5, 1),
                1 - calibration_score,
                min(danger_count / 5, 1),
                temp_risk_add,
            ]
            radar_labels = ["Low Clarity","Risk Score","Hall. Likelihood","Truth Gap","Miscalibration","Danger Words","Temp Risk"]
            radar_closed = radar_vals + [radar_vals[0]]
            label_closed = radar_labels + [radar_labels[0]]
            rfig = go.Figure(go.Scatterpolar(
                r=radar_closed, theta=label_closed,
                fill='toself', fillcolor='rgba(248,113,113,0.15)',
                line=dict(color='#f87171', width=2)
            ))
            rfig.update_layout(
                polar=dict(
                    bgcolor="#091629",
                    radialaxis=dict(visible=True, range=[0,1], gridcolor="#1e3a5f",
                                   tickfont=dict(color="#475569")),
                    angularaxis=dict(gridcolor="#1e3a5f")
                ),
                paper_bgcolor="#091629", font=dict(color="#94a3b8"),
                margin=dict(t=40, b=30), height=350
            )
            st.plotly_chart(rfig, use_container_width=True)
            st.caption("Larger filled area = higher overall risk profile. Aim for a small, compact shape.")

        else:
            st.warning("Please enter both a prompt and a response to run the audit.")


# ═══════════════════════════════════════════════════════════
#  MODEL FORENSICS
# ═══════════════════════════════════════════════════════════
elif page == "Model Forensics":

    section_header("Model Fingerprints")
    st.markdown('<div class="aegis-subtitle">Deep-dive into the behavioural DNA of any individual model</div>', unsafe_allow_html=True)

    plain_explainer("What Are Model Fingerprints?",
        "Every AI model has a unique pattern of strengths and weaknesses. "
        "One model might be great at code but dangerous in medical contexts. "
        "This page exposes those patterns so you can make smarter deployment decisions."
    )

    model = st.selectbox("Select Model to Inspect", df.model.unique())
    fdf   = df[df.model == model]

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Risk Score",       f"{fdf['risk'].mean():.3f}")
    m2.metric("Hallucination",    f"{fdf['hallucination'].mean():.2%}")
    m3.metric("Avg Correctness",  f"{fdf['correctness'].mean():.2%}")
    m4.metric("Truth Gap",        f"{fdf['truth_gap'].mean():.3f}")

    model_risks = df.groupby("model")["risk"].mean().rank()
    rank  = int(model_risks[model])
    total = len(model_risks)
    rank_color = "#34d399" if rank == 1 else "#fbbf24" if rank == 2 else "#f87171"
    st.markdown(
        f'<div style="background:#091629;border:1px solid #1e3a5f;border-radius:10px;padding:12px 16px;margin:12px 0;">'
        f'<span style="font-family:\'Space Mono\',monospace;font-size:0.7rem;color:#64748b;">RISK RANKING: </span>'
        f'<span style="font-family:\'Syne\',sans-serif;font-size:1.1rem;font-weight:700;color:{rank_color};">'
        f'#{rank} of {total} models</span></div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)
    with c1:
        fig = style_fig(px.box(fdf, x="domain", y="risk",
                               title=f"{model} — Risk by Domain", color="domain"))
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Which domains this model struggles with most.")
    with c2:
        fig2 = style_fig(px.scatter(fdf, x="confidence", y="correctness",
                                    color="domain", title=f"{model} — Confidence vs Correctness", opacity=0.6))
        fig2.add_shape(type="line", x0=0, y0=0, x1=1, y1=1,
                       line=dict(color="#f87171", dash="dash", width=2))
        st.plotly_chart(fig2, use_container_width=True)
        st.caption("Points below red line = model was confident but wrong.")

    fig3 = style_fig(px.violin(fdf, x="domain", y="truth_gap",
                               title=f"{model} — Truth Gap by Domain", color="domain", box=True))
    st.plotly_chart(fig3, use_container_width=True)
    st.caption("How badly confidence diverges from reality, by domain.")


# ═══════════════════════════════════════════════════════════
#  INCIDENT TIMELINE
# ═══════════════════════════════════════════════════════════
elif page == "Incident Timeline":

    section_header("AI Failure Timeline")
    st.markdown('<div class="aegis-subtitle">Track how risk evolves over time — catch regressions before they reach production</div>', unsafe_allow_html=True)

    plain_explainer("Why Time Matters",
        "AI models change over time — updates, fine-tuning, and shifting usage patterns all affect quality. "
        "This timeline lets you spot exactly when something went wrong. "
        "Think of it like a stock chart — but for your AI's safety."
    )

    df_time = df.copy()
    df_time["time"] = pd.date_range("2024-01-01", periods=len(df_time))

    filter_cols = st.columns(2)
    with filter_cols[0]:
        selected_models  = st.multiselect("Filter by Model",  df_time["model"].unique(),
                                          default=list(df_time["model"].unique()))
    with filter_cols[1]:
        selected_domains = st.multiselect("Filter by Domain", df_time["domain"].unique(),
                                          default=list(df_time["domain"].unique()))

    filtered = df_time[
        df_time["model"].isin(selected_models) &
        df_time["domain"].isin(selected_domains)
    ]

    trend = filtered.groupby(filtered["time"].dt.date)["risk"].mean().reset_index()
    trend.columns = ["date", "risk"]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=trend["date"], y=trend["risk"],
        fill="tozeroy", fillcolor="rgba(56,189,248,0.08)",
        line=dict(color="#38bdf8", width=2), name="Avg Risk"
    ))
    fig.add_hline(y=0.4, line_dash="dash", line_color="#f87171",
                  annotation_text="Risk Threshold", annotation_position="right")
    fig.update_layout(title="System Risk Over Time", **PLOTLY_THEME)
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Peaks above the red line require immediate investigation.")

    model_trend = (
        filtered.groupby([filtered["time"].dt.to_period("M").astype(str), "model"])["risk"]
        .mean().reset_index()
    )
    model_trend.columns = ["month","model","risk"]
    fig2 = style_fig(px.line(model_trend, x="month", y="risk", color="model",
                             title="Monthly Risk Per Model", markers=True))
    st.plotly_chart(fig2, use_container_width=True)
    st.caption("Compare model risk trajectories month by month.")

    st.markdown("#### Detected Anomalies")
    anomaly_dates = trend[trend["risk"] > trend["risk"].mean() + trend["risk"].std()].head(3)
    if len(anomaly_dates) > 0:
        for _, row in anomaly_dates.iterrows():
            st.markdown(
                f'<div class="alert-warning">Anomaly on <strong>{row["date"]}</strong> — '
                f'Risk spike to <strong>{row["risk"]:.3f}</strong> (above 1-sigma threshold).</div>',
                unsafe_allow_html=True
            )
    else:
        st.markdown(
            '<div class="alert-ok">No significant anomalies detected in the current selection.</div>',
            unsafe_allow_html=True
        )


# ═══════════════════════════════════════════════════════════
#  AI HEALTH SCORE  — with model selector
# ═══════════════════════════════════════════════════════════
elif page == "AI Health Score":

    section_header("AI Health Score", "NEW")
    st.markdown('<div class="aegis-subtitle">Your AI system translated into a single board-ready health rating</div>', unsafe_allow_html=True)

    plain_explainer("The Health Score",
        "Your AI Health Score is like a credit score — but for your AI system. "
        "It combines risk, hallucination rates, latency, toxicity and calibration into a single number from 0 to 100. "
        "Above 75 is healthy. Below 50 means immediate action is required. "
        "This is the number you show your board, your VCs, and your compliance team."
    )

    # ── Model selector ─────────────────────────────────────
    hs_model_options = ["All Models"] + sorted(df["model"].unique().tolist())
    hs_model = st.selectbox("View Health Score For", hs_model_options, key="hs_model_sel")
    hsdf = df if hs_model == "All Models" else df[df["model"] == hs_model]

    risk_score    = max(0, (1 - hsdf["risk"].mean()) * 100)
    hall_score    = max(0, (1 - hsdf["hallucination"].mean()) * 100)
    calibration   = max(0, (1 - abs(hsdf["truth_gap"].mean())) * 100)
    latency_score = max(0, (1 - hsdf["latency"].mean() / 2200) * 100)
    toxicity_score= max(0, (1 - hsdf["toxicity"].mean() / 0.3) * 100)
    overall = (
        risk_score     * 0.30 +
        hall_score     * 0.25 +
        calibration    * 0.20 +
        latency_score  * 0.10 +
        toxicity_score * 0.15
    )

    gauge = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=round(overall, 1),
        delta={"reference": 75, "valueformat": ".1f"},
        gauge={
            "axis": {"range": [0, 100], "tickcolor": "#475569"},
            "bar":  {"color": "#38bdf8", "thickness": 0.25},
            "bgcolor": "#091629",
            "bordercolor": "#1e3a5f",
            "steps": [
                {"range": [0,  40], "color": "rgba(239,68,68,0.2)"},
                {"range": [40, 65], "color": "rgba(251,191,36,0.15)"},
                {"range": [65, 80], "color": "rgba(56,189,248,0.1)"},
                {"range": [80,100], "color": "rgba(52,211,153,0.15)"},
            ],
            "threshold": {"line": {"color": "#34d399","width": 3}, "thickness": 0.75, "value": 75}
        },
        title={"text": f"Overall AI Health Score — {hs_model}",
               "font": {"family": "Syne", "color": "#e2e8f0", "size": 16}},
        number={"font": {"family": "Syne", "size": 56, "color": "#38bdf8"}, "suffix": " / 100"}
    ))
    gauge.update_layout(paper_bgcolor="#091629", plot_bgcolor="#091629",
                        font=dict(color="#94a3b8"), margin=dict(t=60, b=30))
    st.plotly_chart(gauge, use_container_width=True)

    st.markdown("#### Score Breakdown")
    labels  = ["Risk","Hallucination","Calibration","Speed","Toxicity"]
    scores  = [risk_score, hall_score, calibration, latency_score, toxicity_score]
    weights = ["30%","25%","20%","10%","15%"]
    sub_cols = st.columns(5)
    for col, label, score, w in zip(sub_cols, labels, scores, weights):
        color = "#34d399" if score >= 75 else "#fbbf24" if score >= 55 else "#f87171"
        col.markdown(
            f'<div class="metric-card" style="text-align:center;">'
            f'<div class="label">{label} ({w})</div>'
            f'<div class="value" style="color:{color};font-size:1.5rem">{score:.1f}</div>'
            f'<div style="height:3px;background:#1e3a5f;border-radius:2px;margin-top:8px;">'
            f'<div style="height:3px;width:{min(score,100):.0f}%;background:{color};border-radius:2px;"></div>'
            f'</div></div>',
            unsafe_allow_html=True
        )

    st.markdown('<div class="aegis-divider"></div>', unsafe_allow_html=True)
    grade = "A" if overall >= 85 else "B" if overall >= 70 else "C" if overall >= 55 else "D" if overall >= 40 else "F"
    grade_color = "#34d399" if grade in ["A","B"] else "#fbbf24" if grade == "C" else "#f87171"
    grade_label = {"A":"Excellent","B":"Good","C":"Acceptable","D":"Needs Improvement","F":"Critical"}[grade]
    grade_desc = (
        "Your AI system is operating at a high standard. Risk is well-controlled and models are appropriately calibrated."
        if grade in ["A","B"] else
        "Your system is functional but has identifiable risk areas. Targeted interventions are recommended."
        if grade == "C" else
        "Your AI system poses significant risk. Urgent review of hallucination rates is required."
    )
    st.markdown(
        f'<div style="background:#091629;border:1px solid #1e3a5f;border-radius:16px;padding:24px 28px;'
        f'display:flex;align-items:center;gap:24px;">'
        f'<div style="font-family:\'Syne\',sans-serif;font-size:4rem;font-weight:800;'
        f'color:{grade_color};min-width:80px;text-align:center">{grade}</div>'
        f'<div><div style="font-family:\'Syne\',sans-serif;font-size:1.1rem;color:#e2e8f0;'
        f'font-weight:700;margin-bottom:6px;">System Grade: {grade_label}</div>'
        f'<div style="font-size:0.9rem;color:#94a3b8;line-height:1.65;">{grade_desc}</div>'
        f'</div></div>',
        unsafe_allow_html=True
    )

    st.markdown("#### Health Score by Model")
    model_health = []
    for m in df["model"].unique():
        mdf = df[df["model"] == m]
        ms = (
            max(0, (1 - mdf["risk"].mean()) * 100)          * 0.30 +
            max(0, (1 - mdf["hallucination"].mean()) * 100)  * 0.25 +
            max(0, (1 - abs(mdf["truth_gap"].mean())) * 100) * 0.20 +
            max(0, (1 - mdf["latency"].mean() / 2200) * 100) * 0.10 +
            max(0, (1 - mdf["toxicity"].mean() / 0.3) * 100) * 0.15
        )
        model_health.append({"Model": m, "Health Score": round(ms, 1)})
    mh_df = pd.DataFrame(model_health).sort_values("Health Score", ascending=False)

    # highlight selected model
    colors = ["#38bdf8" if m == hs_model else "#4a6fa5" for m in mh_df["Model"]]
    fig_mh = go.Figure(go.Bar(
        x=mh_df["Model"], y=mh_df["Health Score"],
        marker_color=colors,
        text=mh_df["Health Score"].astype(str),
        textposition="outside"
    ))
    fig_mh.add_hline(y=75, line_dash="dash", line_color="#34d399", annotation_text="Target (75)")
    fig_mh.update_layout(title="Model Health Scores", **PLOTLY_THEME)
    st.plotly_chart(fig_mh, use_container_width=True)

    # ── Per-model detailed breakdown table ────────────────
    st.markdown("#### Detailed Model Comparison")
    rows_html = ""
    for row in model_health:
        m = row["Model"]
        mdf = df[df["model"] == m]
        r_s  = max(0, (1 - mdf["risk"].mean()) * 100)
        h_s  = max(0, (1 - mdf["hallucination"].mean()) * 100)
        c_s  = max(0, (1 - abs(mdf["truth_gap"].mean())) * 100)
        l_s  = max(0, (1 - mdf["latency"].mean() / 2200) * 100)
        t_s  = max(0, (1 - mdf["toxicity"].mean() / 0.3) * 100)
        hs   = row["Health Score"]
        g    = "A" if hs >= 85 else "B" if hs >= 70 else "C" if hs >= 55 else "D" if hs >= 40 else "F"
        gc   = "#34d399" if g in ["A","B"] else "#fbbf24" if g == "C" else "#f87171"
        highlight = 'background:rgba(56,189,248,0.08);' if m == hs_model else ''
        rows_html += (
            f'<tr style="{highlight}">'
            f'<td style="font-family:\'Space Mono\',monospace;font-size:0.8rem;color:#38bdf8">{m}</td>'
            f'<td style="color:{gc};font-weight:700">{g}</td>'
            f'<td>{hs:.1f}</td>'
            f'<td>{r_s:.1f}</td>'
            f'<td>{h_s:.1f}</td>'
            f'<td>{c_s:.1f}</td>'
            f'<td>{l_s:.1f}</td>'
            f'<td>{t_s:.1f}</td>'
            f'</tr>'
        )
    table_html = (
        '<table class="compare-table"><thead><tr>'
        '<th>Model</th><th>Grade</th><th>Health</th><th>Risk</th>'
        '<th>Hallucination</th><th>Calibration</th><th>Speed</th><th>Toxicity</th>'
        f'</tr></thead><tbody>{rows_html}</tbody></table>'
    )
    st.markdown(f'<div class="card">{table_html}</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
#  MODEL BENCHMARK
# ═══════════════════════════════════════════════════════════
elif page == "Model Benchmark":

    section_header("Model Benchmark", "NEW")
    st.markdown('<div class="aegis-subtitle">Head-to-head comparison across every quality dimension</div>', unsafe_allow_html=True)

    plain_explainer("Why Compare Models?",
        "Different AI models excel in different areas. GPT-4o might be faster but hallucinate more in legal contexts. "
        "Claude might be better calibrated but slower. "
        "This comparison lets you pick the right model for the right job."
    )

    metrics_cols  = ["risk","hallucination","truth_gap","latency","toxicity","correctness","confidence"]
    model_summary = df.groupby("model")[metrics_cols].mean().reset_index()

    st.markdown("#### Radar: Multi-Dimensional Comparison")
    categories = ["Low Risk","Low Hallucination","Low Truth Gap","Low Latency","Low Toxicity","Correctness","Confidence"]
    radar_fig  = go.Figure()
    for _, row in model_summary.iterrows():
        vals = [
            1 - row["risk"],
            1 - row["hallucination"],
            1 - abs(row["truth_gap"]),
            1 - row["latency"] / 2200,
            1 - row["toxicity"],
            row["correctness"],
            row["confidence"],
        ]
        vals_closed = vals + [vals[0]]
        cats_closed = categories + [categories[0]]
        radar_fig.add_trace(go.Scatterpolar(
            r=vals_closed, theta=cats_closed, fill="toself", name=row["model"], opacity=0.75
        ))
    radar_fig.update_layout(
        polar=dict(
            bgcolor="#091629",
            radialaxis=dict(visible=True, range=[0,1], gridcolor="#1e3a5f",
                            linecolor="#1e3a5f", tickfont=dict(color="#475569")),
            angularaxis=dict(gridcolor="#1e3a5f", linecolor="#1e3a5f")
        ),
        title=dict(text="Model Performance Radar",
                   font=dict(family="Syne", color="#e2e8f0", size=15)),
        paper_bgcolor="#091629", plot_bgcolor="#091629",
        font=dict(color="#94a3b8"),
        legend=dict(bgcolor="#0d1f3c", bordercolor="#1e3a5f"),
        margin=dict(t=60, b=30)
    )
    st.plotly_chart(radar_fig, use_container_width=True)

    st.markdown("#### Full Benchmark Table")
    min_risk = model_summary["risk"].min()
    max_risk = model_summary["risk"].max()
    min_hall = model_summary["hallucination"].min()
    max_hall = model_summary["hallucination"].max()

    rows_html = ""
    for _, row in model_summary.iterrows():
        r_cls = "best" if row["risk"] == min_risk else "worst" if row["risk"] == max_risk else ""
        h_cls = "best" if row["hallucination"] == min_hall else "worst" if row["hallucination"] == max_hall else ""
        rows_html += (
            f'<tr>'
            f'<td style="font-family:\'Space Mono\',monospace;font-size:0.8rem;color:#38bdf8">{row["model"]}</td>'
            f'<td class="{r_cls}">{row["risk"]:.3f}</td>'
            f'<td class="{h_cls}">{row["hallucination"]:.2%}</td>'
            f'<td>{row["truth_gap"]:.3f}</td>'
            f'<td>{row["latency"]:.0f}</td>'
            f'<td>{row["toxicity"]:.3f}</td>'
            f'<td>{row["correctness"]:.2%}</td>'
            f'</tr>'
        )
    table_html = (
        '<table class="compare-table"><thead><tr>'
        '<th>Model</th><th>Risk</th><th>Hallucination</th>'
        '<th>Truth Gap</th><th>Latency (ms)</th><th>Toxicity</th><th>Correctness</th>'
        f'</tr></thead><tbody>{rows_html}</tbody></table>'
    )
    st.markdown(f'<div class="card">{table_html}</div>', unsafe_allow_html=True)
    st.caption("Green = best in category. Red = worst in category.")

    st.markdown("#### Best Model Per Domain")
    domain_leaders  = df.groupby(["domain","model"])["risk"].mean().reset_index()
    best_per_domain = domain_leaders.loc[domain_leaders.groupby("domain")["risk"].idxmin()]
    for _, row in best_per_domain.iterrows():
        st.markdown(
            f'<div class="compliance-row compliance-pass">'
            f'<span style="font-family:\'Space Mono\',monospace;font-size:0.75rem;color:#94a3b8">{row["domain"]}</span>'
            f'<span style="font-family:\'Syne\',sans-serif;font-weight:700;color:#34d399">{row["model"]}</span>'
            f'<span style="font-family:\'Space Mono\',monospace;font-size:0.7rem;color:#475569">Risk: {row["risk"]:.3f}</span>'
            f'</div>',
            unsafe_allow_html=True
        )


# ═══════════════════════════════════════════════════════════
#  COMPLIANCE CHECKER
# ═══════════════════════════════════════════════════════════
elif page == "Compliance Checker":

    section_header("AI Compliance Checker", "NEW")
    st.markdown('<div class="aegis-subtitle">Validate your AI deployment against EU AI Act, GDPR and enterprise governance standards</div>', unsafe_allow_html=True)

    plain_explainer("Why Compliance Matters",
        "The EU AI Act legally requires organisations to audit AI systems in high-risk areas like healthcare, "
        "legal, and finance. Non-compliance can result in fines up to EUR 30 million or 6% of global revenue. "
        "This checker maps your current system metrics to those legal requirements — automatically."
    )

    framework = st.selectbox("Select Compliance Framework",
                             ["EU AI Act (2025)","GDPR Article 22","Enterprise AI Governance","ISO 42001"])

    st.markdown(f"#### Compliance Report: {framework}")

    avg_risk  = df["risk"].mean()
    hall_rate = df["hallucination"].mean()
    truth_gap = df["truth_gap"].mean()
    avg_tox   = df["toxicity"].mean()
    worst_d   = df.groupby("domain")["risk"].mean().idxmax()
    worst_r   = df.groupby("domain")["risk"].mean().max()

    if framework == "EU AI Act (2025)":
        checks = [
            ("Article 9 — Risk Management System",
             worst_r < 0.5, worst_r < 0.4,
             f"Highest domain risk ({worst_d}): {worst_r:.3f}. Threshold: 0.4 for PASS."),
            ("Article 10 — Training Data Quality",
             hall_rate < 0.10, hall_rate < 0.08,
             f"Hallucination rate: {hall_rate:.2%}. Target below 10%."),
            ("Article 13 — Transparency & Explainability",
             True, True,
             "AI CAUGHT audit trail satisfies transparency logging requirements."),
            ("Article 14 — Human Oversight Capability",
             True, True,
             "Platform provides override and escalation pathways."),
            ("Article 15 — Accuracy & Robustness",
             avg_risk < 0.35, avg_risk < 0.25,
             f"Average system risk: {avg_risk:.3f}. High-risk systems require below 0.25."),
            ("Annex III — High Risk Domain Monitoring",
             worst_r < 0.45, worst_r < 0.35,
             f"{worst_d} is monitored. Risk: {worst_r:.3f}."),
        ]
    elif framework == "GDPR Article 22":
        checks = [
            ("Right to Explanation — Decision Logic",
             True, True,
             "AI CAUGHT provides audit trails for automated decisions."),
            ("Data Minimization in Prompts",
             hall_rate < 0.15, hall_rate < 0.10,
             f"Hallucination rate {hall_rate:.2%} indicates data quality concern."),
            ("Accuracy Principle",
             avg_risk < 0.40, avg_risk < 0.25,
             f"System risk {avg_risk:.3f} maps to accuracy compliance concern."),
            ("Automated Decision Risk (Art 22)",
             truth_gap < 0.15, truth_gap < 0.10,
             f"Truth gap {truth_gap:.3f}. Overconfident models cannot self-certify decisions."),
        ]
    elif framework == "Enterprise AI Governance":
        checks = [
            ("Model Risk Policy — Risk Ceiling",
             avg_risk < 0.35, avg_risk < 0.25,
             f"Enterprise risk policy threshold: 0.25. Current: {avg_risk:.3f}"),
            ("Hallucination SLA",
             hall_rate < 0.12, hall_rate < 0.08,
             f"Standard enterprise SLA: <12%. Current: {hall_rate:.2%}"),
            ("Toxicity Policy",
             avg_tox < 0.10, avg_tox < 0.05,
             f"Toxicity mean: {avg_tox:.3f}. Enterprise policy: below 0.10."),
            ("Model Monitoring — Continuous Audit",
             True, True,
             "AI CAUGHT provides continuous observability. Requirement satisfied."),
            ("Incident Response Protocol",
             True, True,
             "Timeline and alert features provide incident tracking capability."),
            ("Board-Level Reporting",
             True, True,
             "Health Score and Export features satisfy board reporting requirements."),
        ]
    else:  # ISO 42001
        checks = [
            ("Clause 6.1 — AI Risk Assessment",
             avg_risk < 0.40, avg_risk < 0.30,
             f"ISO 42001 requires formal risk assessment. Current risk: {avg_risk:.3f}"),
            ("Clause 8.4 — AI System Lifecycle Monitoring",
             True, True,
             "Incident timeline satisfies lifecycle monitoring requirement."),
            ("Clause 9.1 — Performance Evaluation",
             True, True,
             "All 12 dashboard metrics satisfy performance evaluation clause."),
            ("Clause 10.2 — Nonconformity & Corrective Action",
             hall_rate < 0.12, hall_rate < 0.08,
             f"Hallucination rate {hall_rate:.2%} is a nonconformity trigger at >12%."),
        ]

    passed         = sum(1 for _, p, _, _ in checks if p)
    total_checks   = len(checks)
    compliance_pct = passed / total_checks * 100
    comp_color     = "#34d399" if compliance_pct >= 80 else "#fbbf24" if compliance_pct >= 60 else "#f87171"

    st.markdown(
        f'<div style="background:#091629;border:1px solid #1e3a5f;border-radius:12px;padding:18px 22px;'
        f'margin-bottom:20px;display:flex;align-items:center;justify-content:space-between;">'
        f'<div><div style="font-family:\'Space Mono\',monospace;font-size:0.65rem;color:#475569;margin-bottom:4px;">'
        f'COMPLIANCE SCORE</div>'
        f'<div style="font-family:\'Syne\',sans-serif;font-size:2rem;font-weight:800;color:{comp_color}">'
        f'{compliance_pct:.0f}% ({passed}/{total_checks} checks passed)</div></div>'
        f'<div style="text-align:right;font-family:\'Space Mono\',monospace;font-size:0.7rem;color:#475569;">'
        f'Framework: {framework}<br>Assessed: {datetime.now().strftime("%Y-%m-%d")}</div></div>',
        unsafe_allow_html=True
    )

    for check_name, passes, strict_pass, detail in checks:
        row_class = "compliance-pass" if passes else "compliance-fail"
        if passes and not strict_pass:
            badge = '<span class="risk-badge risk-mid">MARGINAL</span>'
        elif passes:
            badge = '<span class="risk-badge risk-low">PASS</span>'
        else:
            badge = '<span class="risk-badge risk-high">FAIL</span>'
        st.markdown(
            f'<div class="compliance-row {row_class}">'
            f'<span style="font-size:0.88rem;color:#cbd5e1;flex:2">{check_name}</span>'
            f'<span style="font-size:0.78rem;color:#64748b;flex:2">{detail}</span>'
            f'{badge}</div>',
            unsafe_allow_html=True
        )

    if compliance_pct < 100:
        st.markdown('<div class="aegis-divider"></div>', unsafe_allow_html=True)
        st.markdown("#### Remediation Actions")
        for check_name, passes, _, detail in checks:
            if not passes:
                st.markdown(
                    f"- **{check_name}**: {detail} — "
                    f"Reduce risk through improved prompt engineering, RAG grounding, and model fine-tuning."
                )


# ═══════════════════════════════════════════════════════════
#  RISK SIMULATOR
# ═══════════════════════════════════════════════════════════
elif page == "Risk Simulator":

    section_header("Risk Simulator", "NEW")
    st.markdown('<div class="aegis-subtitle">Model the real-world impact of AI risk at your organisation\'s scale</div>', unsafe_allow_html=True)

    plain_explainer("What Is the Risk Simulator?",
        "This simulator translates abstract AI risk numbers into concrete business impact: "
        "How many customers could be affected? How many legal incidents might occur? "
        "What is the expected financial exposure? Designed for executives, investors, and product teams."
    )

    sc1, sc2, sc3 = st.columns(3)
    with sc1:
        daily_requests = st.number_input("Daily AI Requests", 100, 10_000_000, 10_000, step=1000)
    with sc2:
        avg_value = st.number_input("Avg Value Per Request ($)", 0.01, 500.0, 2.50)
    with sc3:
        domain_sel = st.selectbox("Primary Domain",
                                  ["General","Legal","Medical","Finance","Code","Support"])

    domain_multiplier = {"Legal":3.5,"Medical":4.0,"Finance":2.8,"Code":1.2,"Support":1.0,"General":1.5}
    multiplier = domain_multiplier[domain_sel]

    hall_rate = df["hallucination"].mean()
    avg_risk  = df["risk"].mean()

    daily_hall   = daily_requests * hall_rate
    daily_risky  = daily_requests * avg_risk
    daily_cost   = daily_risky * avg_value * multiplier
    annual_cost  = daily_cost * 365
    monthly_affected = daily_hall * 30

    r1, r2, r3 = st.columns(3)
    r1.metric("Daily Hallucinated Responses", f"{daily_hall:,.0f}")
    r2.metric("Monthly Affected Users",       f"{monthly_affected:,.0f}")
    r3.metric("Est. Annual Risk Exposure",    f"${annual_cost:,.0f}")

    st.markdown('<div class="aegis-divider"></div>', unsafe_allow_html=True)

    scale_range  = np.arange(100, max(daily_requests * 2, 1000), max(daily_requests // 50, 1))
    scenario_df  = pd.DataFrame({
        "Daily Requests":      scale_range,
        "Daily Hallucinations": scale_range * hall_rate,
        "Annual Cost ($)":     scale_range * avg_risk * avg_value * multiplier * 365
    })

    c1, c2 = st.columns(2)
    with c1:
        fig1 = style_fig(px.line(scenario_df, x="Daily Requests", y="Daily Hallucinations",
                                 title="Hallucinations Scale with Request Volume",
                                 color_discrete_sequence=["#f87171"]))
        fig1.add_vline(x=daily_requests, line_dash="dash", line_color="#38bdf8",
                       annotation_text="Your Volume")
        st.plotly_chart(fig1, use_container_width=True)
    with c2:
        fig2 = style_fig(px.line(scenario_df, x="Daily Requests", y="Annual Cost ($)",
                                 title="Annual Risk Exposure vs Scale",
                                 color_discrete_sequence=["#fbbf24"]))
        fig2.add_vline(x=daily_requests, line_dash="dash", line_color="#38bdf8",
                       annotation_text="Your Volume")
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("#### What-If: Risk Reduction Scenarios")
    reduction = st.slider("If we reduce hallucination rate by (%) via better prompting / RAG:", 0, 80, 30, step=5)
    new_hall      = hall_rate * (1 - reduction / 100)
    saved_annually = (hall_rate - new_hall) * daily_requests * avg_value * multiplier * 365

    st.markdown(
        f'<div style="background:#091629;border:1px solid #1e3a5f;border-radius:12px;padding:20px 24px;margin-top:8px;">'
        f'<div style="font-family:\'Space Mono\',monospace;font-size:0.65rem;color:#475569;margin-bottom:8px;">'
        f'PROJECTED SAVINGS WITH {reduction}% HALLUCINATION REDUCTION</div>'
        f'<div style="font-family:\'Syne\',sans-serif;font-size:2.2rem;font-weight:800;color:#34d399;">'
        f'${saved_annually:,.0f} / year</div>'
        f'<div style="font-size:0.85rem;color:#64748b;margin-top:6px;">'
        f'New hallucination rate: {new_hall:.2%} (down from {hall_rate:.2%})</div></div>',
        unsafe_allow_html=True
    )


# ═══════════════════════════════════════════════════════════
#  LEARNING HUB
# ═══════════════════════════════════════════════════════════
elif page == "Learning Hub":

    section_header("AI Observability Learning Hub")
    st.markdown('<div class="aegis-subtitle">Deep knowledge articles — from zero to expert on AI auditing</div>', unsafe_allow_html=True)

    plain_explainer("Who Is This For?",
        "Whether you are a business executive, product manager, legal professional, or AI engineer, "
        "these articles give you the exact mental models you need to understand and govern AI systems effectively. "
        "No jargon. No fluff. Just the most important things to know."
    )

    ARTICLES = {}

    ARTICLES["Why LLMs Hallucinate"] = {
        "tags": ["Fundamentals","Risk","Non-Technical"],
        "read_time": "5 min",
        "level": "Beginner",
        "body": (
            "**The Core Problem**\n\n"
            "When you ask ChatGPT a question, it does not open an encyclopedia. It predicts, word by word, "
            "which characters are statistically most likely to follow the previous ones — based on patterns "
            "learned during training. The model has no concept of truth, only likelihood.\n\n"
            "Hallucination emerges from this architecture. The model optimises for fluency, not accuracy. "
            "A confident-sounding wrong answer scores better during training than a hesitant correct one.\n\n"
            "**The Three Types of Hallucination**\n\n"
            "1. **Fabrication Hallucination** — The model invents citations, statistics, events, or people "
            "that do not exist. Most dangerous in legal, medical, and financial contexts.\n\n"
            "2. **Conflation Hallucination** — The model merges information from two different real sources, "
            "creating a plausible but inaccurate hybrid response.\n\n"
            "3. **Outdatedness Hallucination** — The model states something that was true at training time "
            "but is now false.\n\n"
            "**Key Insight**\n\n"
            "The higher the model's confidence, the more dangerous its hallucinations. A model that expresses "
            "uncertainty is actually safer than one that presents fabrications with authoritative certainty.\n\n"
            "**What You Can Do**\n\n"
            "- Always ask high-stakes AI to cite sources and cross-check them\n"
            "- Use Retrieval-Augmented Generation (RAG) to ground responses in verified documents\n"
            "- Monitor hallucination rates — a 12% rate means 1 in 8 responses contains fabricated content\n"
            "- Treat AI output in regulated domains as a first draft, not a final authority"
        )
    }

    ARTICLES["The Truth Gap Explained"] = {
        "tags": ["Core Concept","Metrics","Non-Technical"],
        "read_time": "4 min",
        "level": "Beginner",
        "body": (
            "**Defining the Truth Gap**\n\n"
            "The Truth Gap is the difference between a model's expressed confidence and its actual correctness. "
            "A model that says '90% confident' and is right 90% of the time has zero truth gap — perfectly calibrated. "
            "A model that says '90% confident' but is right only 60% of the time has a 30-point truth gap.\n\n"
            "Most production LLMs have a positive truth gap — they are systematically overconfident.\n\n"
            "**Why This Matters More Than Raw Error Rates**\n\n"
            "If a model says 'I'm not sure, but this might be the answer,' a human will verify it. "
            "If a model says 'The answer is definitively X,' a human might not — especially under time pressure. "
            "This is why overconfident wrong answers cause more real-world harm than uncertain wrong answers.\n\n"
            "**Industry Benchmarks**\n\n"
            "- Below 0.05: Excellent — suitable for autonomous decision support\n"
            "- 0.05 to 0.15: Acceptable — human review should be standard\n"
            "- Above 0.15: High risk — mandatory human oversight for all outputs"
        )
    }

    ARTICLES["Why Confidence is Dangerous"] = {
        "tags": ["Risk","Psychology","Non-Technical"],
        "read_time": "4 min",
        "level": "Beginner",
        "body": (
            "**The Confidence Trap**\n\n"
            "Humans are wired to trust confident sources. We evolved in environments where confidence often "
            "correlated with expertise. AI systems exploit this instinct without intending to — they produce "
            "authoritative-sounding output because that is what the training data consisted of.\n\n"
            "**RLHF and the Helpful-Confident Feedback Loop**\n\n"
            "Reinforcement Learning from Human Feedback (RLHF) trains models to maximise human approval ratings. "
            "Humans tend to rate confident, fluent, authoritative responses more highly — even when those responses "
            "are wrong. This creates a training signal that systematically rewards overconfidence.\n\n"
            "**Practical Implication**\n\n"
            "Never treat AI confidence as ground truth. A model that says it is '95% sure' may actually be right "
            "only 60% of the time on that class of question. The confidence score reflects training distribution, "
            "not actual reliability."
        )
    }

    ARTICLES["RAG: The Hallucination Cure"] = {
        "tags": ["Technical","Solutions","Engineering"],
        "read_time": "6 min",
        "level": "Intermediate",
        "body": (
            "**What Is RAG?**\n\n"
            "Retrieval-Augmented Generation (RAG) is a technique that connects an LLM to a verified knowledge base. "
            "Instead of generating answers purely from training memory, the model first retrieves relevant documents "
            "and then generates a response grounded in those documents.\n\n"
            "**Why RAG Reduces Hallucination**\n\n"
            "When a model has access to a retrieved document, it can quote, paraphrase, or reason from a real source "
            "rather than reconstructing information from statistical patterns. This reduces fabrication hallucination "
            "dramatically — by 40–70% in controlled benchmarks.\n\n"
            "**RAG Limitations**\n\n"
            "- RAG cannot fix hallucination if the retrieval step returns irrelevant documents\n"
            "- The model may still confabulate when the retrieved context is insufficient\n"
            "- RAG adds latency — typically 200–800ms for retrieval\n"
            "- Requires maintaining a high-quality, up-to-date knowledge base\n\n"
            "**Implementation Checklist**\n\n"
            "1. Define your knowledge corpus (internal docs, regulations, product data)\n"
            "2. Chunk documents into 300–500 token segments\n"
            "3. Embed and index using a vector database (Pinecone, Weaviate, pgvector)\n"
            "4. Retrieve top-K relevant chunks at query time\n"
            "5. Inject retrieved chunks into the model's context window\n"
            "6. Monitor retrieval relevance scores alongside hallucination rates"
        )
    }

    ARTICLES["AI in High-Stakes Domains"] = {
        "tags": ["Industry","Risk","Compliance"],
        "read_time": "7 min",
        "level": "Intermediate",
        "body": (
            "**Legal Domain: The Citation Crisis**\n\n"
            "In 2023, lawyers filed court documents with AI-generated citations to cases that did not exist. "
            "The model had fabricated plausible-sounding case names, docket numbers, and judicial quotes. "
            "The brief passed initial review because the citations looked authentic.\n\n"
            "Key risks in legal AI:\n"
            "- Fabricated case law and statutes\n"
            "- Misquoted contract terms\n"
            "- Jurisdiction confusion\n"
            "- Confidentiality breaches in document processing\n\n"
            "**Medical Domain: The Highest Stakes**\n\n"
            "LLMs are particularly dangerous in clinical settings because:\n"
            "- Medical knowledge changes rapidly (post-training cutoff blindness)\n"
            "- Drug interaction complexity exceeds most models' reliable reasoning depth\n"
            "- Rare conditions are underrepresented in training data\n"
            "- Models may confidently recommend inappropriate treatments\n\n"
            "**Financial Domain: Compounding Error Risk**\n\n"
            "In financial AI, errors compound. An incorrect risk assessment might lead to a position that, "
            "when wrong, causes further downstream errors in dependent models.\n\n"
            "**The EU AI Act Classification**\n\n"
            "High-risk AI requiring mandatory conformity assessment includes:\n"
            "- Healthcare: any AI assisting clinical decisions\n"
            "- Legal: AI used in law enforcement or legal advice\n"
            "- Finance: AI for credit scoring and financial decisions\n"
            "- Employment: AI for candidate screening"
        )
    }

    ARTICLES["The EU AI Act: A Practical Guide"] = {
        "tags": ["Compliance","Legal","Non-Technical"],
        "read_time": "9 min",
        "level": "Advanced",
        "body": (
            "**The Risk Pyramid**\n\n"
            "The EU AI Act classifies AI systems into four tiers:\n\n"
            "1. **Unacceptable Risk** — Banned outright. Social scoring systems, real-time biometric "
            "surveillance, manipulative subliminal AI.\n\n"
            "2. **High Risk** — Legally permitted but subject to strict requirements. Includes AI in "
            "healthcare, legal services, financial decisions, critical infrastructure, and employment.\n\n"
            "3. **Limited Risk** — Lighter obligations. Chatbots must disclose they are AI.\n\n"
            "4. **Minimal Risk** — No regulation. Spam filters, AI in video games.\n\n"
            "**Penalties**\n\n"
            "- Up to EUR 30 million or 6% of global revenue for prohibited AI violations\n"
            "- Up to EUR 20 million or 4% for high-risk AI obligation violations\n"
            "- Up to EUR 10 million or 2% for other violations\n\n"
            "**How AI CAUGHT Helps**\n\n"
            "AI CAUGHT directly addresses Articles 9 (risk management), 10 (data quality), 13 (transparency), "
            "and 15 (accuracy and robustness). The Health Score, Compliance Checker, and Export Report "
            "features populate the technical documentation that regulators may request."
        )
    }

    ARTICLES["Model Calibration Deep Dive"] = {
        "tags": ["Technical","Metrics","Engineering"],
        "read_time": "7 min",
        "level": "Advanced",
        "body": (
            "**Formal Definition**\n\n"
            "A model is perfectly calibrated if: for all confidence levels p, the model is correct exactly "
            "p fraction of the time on inputs where it expresses confidence p. "
            "A 70% confident prediction should be right 70% of the time — no more, no less.\n\n"
            "**Expected Calibration Error (ECE)**\n\n"
            "ECE is the primary metric for measuring calibration quality. It computes the weighted average "
            "of the gap between predicted confidence and actual accuracy across confidence buckets. "
            "Lower ECE is better. State-of-the-art calibrated models achieve ECE below 0.02.\n\n"
            "**Temperature Scaling**\n\n"
            "The most common post-training calibration technique. A single scalar parameter T (temperature) "
            "is applied to the model's logits before the softmax operation. T > 1 softens the distribution "
            "(reduces overconfidence). T < 1 sharpens it.\n\n"
            "**Why Most LLMs Are Poorly Calibrated**\n\n"
            "- RLHF training rewards confident-sounding responses\n"
            "- Chain-of-thought prompting can improve or worsen calibration depending on implementation\n"
            "- Calibration degrades in out-of-distribution domains\n"
            "- Instruction fine-tuning often increases overconfidence even as it improves task performance"
        )
    }

    article_names = list(ARTICLES.keys())
    article_choice = st.selectbox("Choose Article", article_names)

    if article_choice in ARTICLES:
        art = ARTICLES[article_choice]
        tag_html = "".join(f'<span class="article-tag">{t}</span>' for t in art["tags"])
        level_color = (
            "#34d399" if art["level"] == "Beginner"
            else "#fbbf24" if art["level"] == "Intermediate"
            else "#f87171"
        )
        st.markdown(
            f'<div class="article-card">'
            f'<div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px;">'
            f'<div>{tag_html}</div>'
            f'<div style="font-family:\'Space Mono\',monospace;font-size:0.65rem;color:#475569;text-align:right;">'
            f'{art["read_time"]} read &nbsp;|&nbsp; '
            f'<span style="color:{level_color}">{art["level"]}</span></div></div>'
            f'<h3>{article_choice}</h3></div>',
            unsafe_allow_html=True
        )
        st.markdown(art["body"])

    st.markdown('<div class="aegis-divider"></div>', unsafe_allow_html=True)
    st.markdown("#### Quick Reference Glossary")
    glossary = {
        "Hallucination":      "When an AI model generates information that is factually incorrect or completely fabricated, presented with confidence.",
        "Truth Gap":          "The difference between a model's expressed confidence and its actual correctness rate. Positive values indicate overconfidence.",
        "Calibration":        "How well a model's confidence scores match its true accuracy rates across many predictions.",
        "RAG":                "Retrieval-Augmented Generation — a technique that grounds AI responses in retrieved documents from a verified knowledge base.",
        "RLHF":               "Reinforcement Learning from Human Feedback — the training process that makes LLMs conversational but introduces confidence bias.",
        "Token Prediction":   "The fundamental mechanism of LLMs — they predict the next most likely word/token, not retrieve factual answers.",
        "System Prompt":      "Instructions given to an AI model before the user's message, used to set behaviour, role, and constraints.",
        "Context Window":     "The maximum amount of text (in tokens) an LLM can consider at once — typically 8,000 to 200,000 tokens for modern models.",
        "ECE":                "Expected Calibration Error — the primary metric for measuring how well a model's confidence matches its accuracy.",
        "EU AI Act":          "EU regulation classifying AI by risk level (unacceptable / high / limited / minimal) with binding compliance requirements.",
    }
    for term, definition in glossary.items():
        with st.expander(term):
            st.markdown(definition)


# ═══════════════════════════════════════════════════════════
#  ECONOMICS  — with model selector
# ═══════════════════════════════════════════════════════════
elif page == "Economics":

    section_header("Shadow Cost Analysis")
    st.markdown('<div class="aegis-subtitle">Quantify the hidden financial cost of AI unreliability in your organisation</div>', unsafe_allow_html=True)

    plain_explainer("What Is Shadow Cost?",
        "Every hallucination your AI produces costs money — in employee time spent verifying or correcting AI output, "
        "in legal exposure from incorrect advice, and in customer trust eroded by bad responses. "
        "This calculator makes that invisible cost visible."
    )

    # ── Model selector ─────────────────────────────────────
    econ_model_options = ["All Models"] + sorted(df["model"].unique().tolist())
    econ_model = st.selectbox("Analyse Economics For", econ_model_options, key="econ_model_sel")
    edf = df if econ_model == "All Models" else df[df["model"] == econ_model]

    # ── Cost Calculator inputs ─────────────────────────────
    st.markdown("#### Shadow Cost Calculator")
    ec1, ec2, ec3 = st.columns(3)
    with ec1:
        daily_volume = st.number_input("Daily AI Queries", 500, 5_000_000, 50_000, step=1000, key="econ_vol")
    with ec2:
        hourly_rate  = st.number_input("Avg Employee Hourly Rate ($)", 10, 500, 65, key="econ_rate")
    with ec3:
        verify_mins  = st.number_input("Minutes to Verify 1 AI Response", 1, 60, 8, key="econ_mins")

    econ_domain = st.selectbox("Primary Deployment Domain",
                               ["General","Legal","Medical","Finance","Code","Support"], key="econ_domain")

    domain_multiplier_econ = {"Legal":3.8,"Medical":4.2,"Finance":3.0,"Code":1.2,"Support":1.0,"General":1.5}
    dmult = domain_multiplier_econ[econ_domain]

    hall_rate_e  = edf["hallucination"].mean()
    avg_risk_e   = edf["risk"].mean()
    truth_gap_e  = edf["truth_gap"].mean()

    daily_hall_count     = daily_volume * hall_rate_e
    verification_cost_d  = daily_hall_count * (verify_mins / 60) * hourly_rate * dmult
    legal_exposure_d     = daily_volume * avg_risk_e * 0.001 * dmult * 500   # $500 avg legal incident
    trust_erosion_d      = daily_volume * hall_rate_e * 0.05 * 25            # $25 avg customer churn cost
    total_shadow_cost_d  = verification_cost_d + legal_exposure_d + trust_erosion_d
    annual_shadow         = total_shadow_cost_d * 365

    st.markdown('<div class="aegis-divider"></div>', unsafe_allow_html=True)
    st.markdown(f"#### Shadow Cost Breakdown — **{econ_model}**")

    sc1, sc2, sc3, sc4 = st.columns(4)
    sc1.metric("Daily Verification Cost",  f"${verification_cost_d:,.0f}")
    sc2.metric("Daily Legal Exposure",     f"${legal_exposure_d:,.0f}")
    sc3.metric("Daily Trust Erosion",      f"${trust_erosion_d:,.0f}")
    sc4.metric("Est. Annual Shadow Cost",  f"${annual_shadow:,.0f}")

    # ── Cost breakdown chart ───────────────────────────────
    breakdown_fig = go.Figure(go.Pie(
        labels=["Verification Labour","Legal Exposure","Trust Erosion"],
        values=[verification_cost_d, legal_exposure_d, trust_erosion_d],
        hole=0.55,
        marker=dict(colors=["#38bdf8","#f87171","#fbbf24"]),
    ))
    breakdown_fig.update_layout(
        title="Daily Shadow Cost Composition",
        paper_bgcolor="#091629", plot_bgcolor="#091629",
        font=dict(color="#94a3b8", family="Inter"),
        legend=dict(bgcolor="#0d1f3c", bordercolor="#1e3a5f"),
        margin=dict(t=50, b=20)
    )
    st.plotly_chart(breakdown_fig, use_container_width=True)

    # ── Per-model shadow cost comparison ──────────────────
    st.markdown("#### Shadow Cost by Model")
    model_costs = []
    for m in df["model"].unique():
        mdf = df[df["model"] == m]
        mhr  = mdf["hallucination"].mean()
        mar  = mdf["risk"].mean()
        mvc  = daily_volume * mhr * (verify_mins / 60) * hourly_rate * dmult
        mle  = daily_volume * mar * 0.001 * dmult * 500
        mte  = daily_volume * mhr * 0.05 * 25
        mtot = (mvc + mle + mte) * 365
        model_costs.append({"Model": m, "Annual Shadow Cost ($)": round(mtot, 0),
                            "Hall Rate": round(mhr * 100, 1)})
    mc_df = pd.DataFrame(model_costs).sort_values("Annual Shadow Cost ($)", ascending=True)

    bar_colors = ["#38bdf8" if m == econ_model else "#4a6fa5" for m in mc_df["Model"]]
    cost_fig = go.Figure(go.Bar(
        x=mc_df["Annual Shadow Cost ($)"], y=mc_df["Model"],
        orientation="h",
        marker_color=bar_colors,
        text=[f"${v:,.0f}" for v in mc_df["Annual Shadow Cost ($)"]],
        textposition="outside"
    ))
    cost_fig.update_layout(title="Estimated Annual Shadow Cost by Model", **PLOTLY_THEME)
    st.plotly_chart(cost_fig, use_container_width=True)
    st.caption("Based on your entered volume, rate, and domain. Lower bar = cheaper to operate.")

    # ── ROI of reducing hallucination ─────────────────────
    st.markdown("#### ROI Simulator: Cost of Reducing Hallucination")
    roi_reduction = st.slider("Hallucination reduction via RAG / better prompting (%)", 0, 80, 40, step=5, key="econ_roi")
    rag_cost_annual = 12_000 * (roi_reduction / 40)   # rough RAG infrastructure cost
    saved = annual_shadow * (roi_reduction / 100)
    net_roi = saved - rag_cost_annual

    r1, r2, r3 = st.columns(3)
    r1.metric("Annual Savings", f"${saved:,.0f}")
    r2.metric("RAG / Improvement Cost", f"${rag_cost_annual:,.0f}")
    r3.metric("Net Annual ROI", f"${net_roi:,.0f}", delta="Positive" if net_roi > 0 else "Negative")

    if net_roi > 0:
        st.markdown(
            f'<div class="alert-ok">POSITIVE ROI: Investing in hallucination reduction delivers an estimated '
            f'<strong>${net_roi:,.0f}</strong> net annual benefit at your current scale.</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="alert-warning">MARGINAL ROI: At current scale, the improvement cost may outweigh savings. '
            f'Re-evaluate at higher query volumes or in higher-stakes domains.</div>',
            unsafe_allow_html=True
        )

    # ── Key model stats for selected model ────────────────
    st.markdown('<div class="aegis-divider"></div>', unsafe_allow_html=True)
    st.markdown(f"#### Key Risk Indicators — {econ_model}")
    ki1, ki2, ki3, ki4 = st.columns(4)
    ki1.metric("Hallucination Rate",  f"{hall_rate_e:.2%}")
    ki2.metric("Avg Risk Score",      f"{avg_risk_e:.3f}")
    ki3.metric("Truth Gap",           f"{truth_gap_e:.3f}")
    ki4.metric("Avg Latency",         f"{edf['latency'].mean():.0f} ms")

    domain_cost_df = edf.groupby("domain")["risk"].mean().reset_index()
    domain_cost_df["Est. Daily Cost ($)"] = domain_cost_df["risk"] * daily_volume * 0.001 * dmult * 500 / 5
    domain_cost_df = domain_cost_df.sort_values("Est. Daily Cost ($)", ascending=False)
    fig_dc = style_fig(px.bar(domain_cost_df, x="domain", y="Est. Daily Cost ($)",
                              title=f"Daily Risk Cost by Domain — {econ_model}",
                              color="Est. Daily Cost ($)", color_continuous_scale="Reds"))
    st.plotly_chart(fig_dc, use_container_width=True)
    st.caption("Which domains are costing you the most due to AI risk exposure.")


# ═══════════════════════════════════════════════════════════
#  EXPORT REPORT  — fully working
# ═══════════════════════════════════════════════════════════
elif page == "Export Report":

    section_header("Export Report")
    st.markdown('<div class="aegis-subtitle">Download your full audit trail, prompt lab results, and system health data</div>', unsafe_allow_html=True)

    plain_explainer("What Can You Export?",
        "Export your AI audit data in multiple formats for board presentations, compliance submissions, "
        "and engineering reviews. Prompt Lab audit results are included when you have run an audit in this session."
    )

    # ── System summary stats ───────────────────────────────
    avg_risk  = df["risk"].mean()
    hall_rate = df["hallucination"].mean()
    truth_gap = df["truth_gap"].mean()
    avg_tox   = df["toxicity"].mean()
    health    = round((1 - avg_risk) * 100, 1)
    grade     = "A" if health >= 85 else "B" if health >= 70 else "C" if health >= 55 else "D" if health >= 40 else "F"

    st.markdown("#### Current System Snapshot")
    snap1, snap2, snap3, snap4, snap5 = st.columns(5)
    snap1.metric("Health Score", f"{health}")
    snap2.metric("Grade", grade)
    snap3.metric("Avg Risk", f"{avg_risk:.3f}")
    snap4.metric("Hall. Rate", f"{hall_rate:.2%}")
    snap5.metric("Truth Gap", f"{truth_gap:.3f}")

    st.markdown('<div class="aegis-divider"></div>', unsafe_allow_html=True)

    # ── Export 1: Full dataset CSV ─────────────────────────
    st.markdown("#### Export 1 — Full Audit Dataset (CSV)")
    st.markdown("Complete 1,200-row dataset with all model metrics, risk scores, and domain breakdowns.")
    csv_data = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇ Download Full Dataset (CSV)",
        data=csv_data,
        file_name=f"ai_caught_full_dataset_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv",
        key="dl_csv_full"
    )

    # ── Export 2: Model Summary CSV ───────────────────────
    st.markdown("#### Export 2 — Model Summary Report (CSV)")
    st.markdown("Aggregated per-model metrics: risk, hallucination, truth gap, latency, toxicity, correctness.")
    metrics_cols  = ["risk","hallucination","truth_gap","latency","toxicity","correctness","confidence"]
    model_summary = df.groupby("model")[metrics_cols].mean().round(4).reset_index()
    model_summary.columns = ["Model","Avg Risk","Hallucination Rate","Truth Gap","Avg Latency (ms)","Avg Toxicity","Correctness","Confidence"]

    model_health_list = []
    for m in df["model"].unique():
        mdf = df[df["model"] == m]
        ms = (
            max(0, (1 - mdf["risk"].mean()) * 100)          * 0.30 +
            max(0, (1 - mdf["hallucination"].mean()) * 100)  * 0.25 +
            max(0, (1 - abs(mdf["truth_gap"].mean())) * 100) * 0.20 +
            max(0, (1 - mdf["latency"].mean() / 2200) * 100) * 0.10 +
            max(0, (1 - mdf["toxicity"].mean() / 0.3) * 100) * 0.15
        )
        g = "A" if ms >= 85 else "B" if ms >= 70 else "C" if ms >= 55 else "D" if ms >= 40 else "F"
        model_health_list.append({"Model": m, "Health Score": round(ms, 1), "Grade": g})
    mh_df2 = pd.DataFrame(model_health_list)
    model_export = model_summary.merge(mh_df2, on="Model")

    model_csv = model_export.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇ Download Model Summary (CSV)",
        data=model_csv,
        file_name=f"ai_caught_model_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv",
        key="dl_csv_model"
    )

    # ── Export 3: Domain Risk CSV ──────────────────────────
    st.markdown("#### Export 3 — Domain Risk Breakdown (CSV)")
    domain_summary = df.groupby(["domain","model"])[["risk","hallucination","truth_gap","toxicity","correctness"]].mean().round(4).reset_index()
    domain_csv = domain_summary.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇ Download Domain Risk Report (CSV)",
        data=domain_csv,
        file_name=f"ai_caught_domain_risk_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv",
        key="dl_csv_domain"
    )

    # ── Export 4: Prompt Lab Audit (JSON + TXT) ────────────
    st.markdown('<div class="aegis-divider"></div>', unsafe_allow_html=True)
    st.markdown("#### Export 4 — Prompt Lab Audit Results")

    if "last_audit" in st.session_state and st.session_state["last_audit"]:
        audit = st.session_state["last_audit"]

        st.markdown(
            f'<div class="alert-ok">Prompt Lab audit available from <strong>{audit["timestamp"]}</strong> — '
            f'Model: <strong>{audit["model"]}</strong>, Domain: <strong>{audit["domain"]}</strong>, '
            f'Hallucination Risk: <strong>{audit["hallucination_risk"]}</strong></div>',
            unsafe_allow_html=True
        )

        # ── JSON export ───────────────────────────────────
        audit_json = json.dumps(audit, indent=2, ensure_ascii=False).encode("utf-8")
        st.download_button(
            label="⬇ Download Prompt Audit (JSON)",
            data=audit_json,
            file_name=f"ai_caught_prompt_audit_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json",
            key="dl_audit_json"
        )

        # ── Plain-text report ─────────────────────────────
        txt_lines = [
            "=" * 60,
            "AI CAUGHT — PROMPT AUDIT REPORT",
            "=" * 60,
            f"Generated : {audit['timestamp']}",
            f"Model     : {audit['model']}",
            f"Domain    : {audit['domain']}",
            f"RAG       : {audit['rag']}",
            f"Temperature: {audit['temperature']}",
            f"System Prompt Quality: {audit['system_prompt_quality']}",
            f"Use Case Sensitivity : {audit['use_case_sensitivity']}",
            "",
            "─" * 60,
            "SCORES",
            "─" * 60,
            f"Clarity Score          : {audit['clarity_score']}",
            f"Hallucination Risk     : {audit['hallucination_risk']}",
            f"Hallucination Likelihood: {audit['hallucination_likelihood_pct']}%",
            f"Truth Gap Proxy        : {audit['truth_gap_proxy']}",
            f"Calibration Score      : {audit['calibration_score']}",
            f"Hedge Ratio            : {audit['hedge_ratio']}",
            f"Danger Words Found     : {', '.join(audit['danger_words_found']) or 'None'}",
            f"Citation Signals       : {audit['citation_signals']}",
            f"Estimated Latency      : {audit['estimated_latency_ms']} ms",
            f"Complexity Score       : {audit['complexity_score']}",
            "",
            "─" * 60,
            "PROMPT",
            "─" * 60,
            audit['prompt'],
            "",
            "─" * 60,
            "RESPONSE",
            "─" * 60,
            audit['response'],
            "",
            "=" * 60,
            "AI CAUGHT // AI Observability OS // 2026",
            "=" * 60,
        ]
        txt_report = "\n".join(txt_lines).encode("utf-8")
        st.download_button(
            label="⬇ Download Prompt Audit (TXT Report)",
            data=txt_report,
            file_name=f"ai_caught_prompt_audit_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            key="dl_audit_txt"
        )

        # ── Preview ───────────────────────────────────────
        with st.expander("Preview Audit Data"):
            st.json(audit)

    else:
        st.markdown(
            '<div class="alert-warning">No Prompt Lab audit available yet. '
            'Go to <strong>Prompt Lab</strong>, enter a prompt and response, and click <strong>Run Audit</strong>. '
            'Then return here to download the results.</div>',
            unsafe_allow_html=True
        )

    # ── Export 5: Full system text report ─────────────────
    st.markdown('<div class="aegis-divider"></div>', unsafe_allow_html=True)
    st.markdown("#### Export 5 — Full System Health Report (TXT)")

    worst_domain = df.groupby("domain")["risk"].mean().idxmax()
    worst_model  = df.groupby("model")["risk"].mean().idxmax()
    best_model   = df.groupby("model")["risk"].mean().idxmin()

    system_lines = [
        "=" * 60,
        "AI CAUGHT — SYSTEM HEALTH REPORT",
        "=" * 60,
        f"Generated : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Dataset   : 1,200 synthetic audit events",
        "",
        "─" * 60,
        "SYSTEM OVERVIEW",
        "─" * 60,
        f"Overall Health Score   : {health} / 100",
        f"System Grade           : {grade}",
        f"Average Risk           : {avg_risk:.4f}",
        f"Hallucination Rate     : {hall_rate:.2%}",
        f"Truth Gap              : {truth_gap:.4f}",
        f"Average Toxicity       : {avg_tox:.4f}",
        f"Average Latency        : {df['latency'].mean():.0f} ms",
        f"P95 Latency            : {df['latency'].quantile(0.95):.0f} ms",
        "",
        "─" * 60,
        "MODEL SUMMARY",
        "─" * 60,
    ]
    for _, row in model_export.iterrows():
        system_lines.append(
            f"{row['Model']:10s} | Health: {row['Health Score']:5.1f} | Grade: {row['Grade']} | "
            f"Risk: {row['Avg Risk']:.3f} | Hall: {row['Hallucination Rate']:.2%} | "
            f"Latency: {row['Avg Latency (ms)']:.0f}ms"
        )
    system_lines += [
        "",
        "─" * 60,
        "KEY FINDINGS",
        "─" * 60,
        f"Highest Risk Domain    : {worst_domain}",
        f"Highest Risk Model     : {worst_model}",
        f"Lowest Risk Model      : {best_model}",
        "",
        "─" * 60,
        "DOMAIN RISK",
        "─" * 60,
    ]
    for domain, grp in df.groupby("domain"):
        system_lines.append(f"{domain:10s} | Risk: {grp['risk'].mean():.3f} | Hall: {grp['hallucination'].mean():.2%}")

    system_lines += [
        "",
        "=" * 60,
        "AI CAUGHT // AI Observability OS // 2026",
        "=" * 60,
    ]
    sys_txt = "\n".join(system_lines).encode("utf-8")
    st.download_button(
        label="⬇ Download System Health Report (TXT)",
        data=sys_txt,
        file_name=f"ai_caught_system_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
        mime="text/plain",
        key="dl_sys_txt"
    )

    st.markdown('<div class="aegis-divider"></div>', unsafe_allow_html=True)
    st.markdown(
        '<div style="font-family:\'Space Mono\',monospace;font-size:0.65rem;color:#334155;text-align:center;padding:8px 0;">'
        'AI CAUGHT // AI Observability OS // All exports contain synthetic data for demonstration purposes.</div>',
        unsafe_allow_html=True
    )
