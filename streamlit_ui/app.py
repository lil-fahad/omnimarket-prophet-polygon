import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging
logging.basicConfig(level=logging.INFO)

import streamlit as st
from core.auto_predictor import run_prediction
from core.recommender import recommend_options
from core.explainable_ai import explain_prediction

st.set_page_config(page_title="OmniMarket Prophet")

symbol = st.text_input("أدخل رمز السهم", value="AAPL")

if st.button("ابدأ التحليل"):
    results = run_prediction(symbol)
    for r in results:
        mae = r.get('mae')
        acc = r.get('direction_accuracy')
        if isinstance(mae, (int, float)) and isinstance(acc, (int, float)):
            st.write(f"النموذج: {r['model']}, MAE: {mae:.2f}, دقة الاتجاه: {acc:.2f}%")
        else:
            st.write(f"النموذج: {r.get('model')} — لا توجد نتائج كمية.")
        recommendation = recommend_options(100, 105)
        explanation = explain_prediction(symbol, f"تغير متوقع بنسبة {recommendation['expected_change_pct']}%", r['model'])
        st.markdown("### التوصية:")
        st.write(recommendation)
        st.markdown("### التفسير:")
        st.info(explanation)
