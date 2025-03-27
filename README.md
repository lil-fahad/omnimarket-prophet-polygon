# OmniMarket Prophet - Quantum AI Edition

**OmniMarket Prophet** هو نظام تنبؤ وتحليل أسواق متكامل يعمل بالذكاء الاصطناعي على مستوى احترافي، يستخدم أحدث النماذج الهجينة والتقنيات الحديثة لتقديم توقعات دقيقة ومفسرة للأسواق المالية (أسهم + خيارات).

---

## المميزات الأساسية:

- **نماذج هجينة متقدمة**: LSTM + Transformer + XGBoost
- **تنبؤ غير يقيني (Bayesian LSTM)**: لمعرفة درجة الثقة
- **تفسير ذكي للتنبؤات**: باستخدام SHAP
- **توصيات تداول ذكية مرتبة حسب نسبة الربحية**
- **استخدام Polygon API كمصدر رسمي للبيانات**
- **واجهة Streamlit تفاعلية**

---

## مصدر البيانات: Polygon.io

المشروع يستخدم [Polygon.io](https://polygon.io) كمصدر رئيسي لجلب بيانات الأسهم.

### لتفعيل ذلك:
- أنشئ حساب على Polygon.io للحصول على API Key
- ثم أضف المفتاح باستخدام:

```bash
export POLYGON_API_KEY="your_key_here"
```

أو على Streamlit Cloud:

```toml
# secrets.toml
POLYGON_API_KEY = "your_key_here"
```

---

## طريقة التشغيل:

```bash
pip install -r requirements.txt
streamlit run streamlit_ui/app.py
```

---

## الملفات المهمة:

| المسار | الوظيفة |
|--------|----------|
| `data/polygon_api.py` | الاتصال بـ Polygon API |
| `data/loader.py` | تحميل البيانات المعتمدة على Polygon |
| `core/auto_predictor.py` | تنفيذ التنبؤ المتكامل |
| `models/quantum/` | نماذج الذكاء المطور |
| `streamlit_ui/` | واجهة المستخدم |
| `evaluation/` | تقييم النموذج ورسوم بيانية |

---

## الترخيص
تم تطوير هذا المشروع لأغراض البحث والتطوير فقط، ولا يُعتبر توصية استثمارية مباشرة.