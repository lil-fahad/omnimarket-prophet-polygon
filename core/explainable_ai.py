
from dotenv import load_dotenv
load_dotenv()

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def explain_prediction(symbol, context, model_name):
    """
    توضح هذه الدالة التنبؤ الذي قام به النموذج بلغة مفهومة.
    """
    prompt = f"""فسر للمستثمر سبب التوصية بسهم {symbol} باستخدام النموذج {model_name}.
معلومات إضافية:
{context}
الرجاء تقديم تفسير مبسط يمكن فهمه من قبل غير المتخصصين.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )

    return response["choices"][0]["message"]["content"]
