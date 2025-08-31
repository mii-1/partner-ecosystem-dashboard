import streamlit as st
import pandas as pd

st.title("🤝 Partner Ecosystem Dashboard (Mock)")

df = pd.read_json("data/partner_usage.json")

st.subheader("Raw Data")
st.dataframe(df, use_container_width=True)

st.subheader("KPIs")
kpi = df.groupby("partner").agg(
    total_requests=("requests","sum"),
    avg_users=("users","mean"),
    p50_latency=("latency_ms_p50","mean"),
    p95_latency=("latency_ms_p95","mean"),
    value_usd=("value_usd","sum")
).reset_index()
st.dataframe(kpi, use_container_width=True)

st.subheader("Requests by Partner")
st.bar_chart(kpi.set_index("partner")["total_requests"])

st.subheader("Value by Partner (USD)")
st.bar_chart(kpi.set_index("partner")["value_usd"])

