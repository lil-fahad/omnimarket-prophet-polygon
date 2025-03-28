logging.basicConfig(level=logging.INFO)
import logging
import openai
import os

def explain_prediction(symbol, prediction_summary, model_name=""):
    """
    وظيفة: explain_prediction
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "⚠️ لا يوجد مفتاح API لتفسير GPT"

    openai.api_key = api_key
    prompt = f"""
    سهم {symbol} تم تحليله باستخدام نموذج {model_name}.
    النتائج أظهرت التالي: {prediction_summary}.
    وضّح ما تعنيه هذه النتائج للمستثمر بشكل مبسط.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"حدث خطأ أثناء الاتصال بـ GPT: {str(e)}"