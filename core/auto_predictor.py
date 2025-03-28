
import numpy as np
import logging
from data.loader import load_data
from models.quantum.hybrid_model import hybrid_model_predict
from models.quantum.bayesian_lstm import build_bayesian_lstm
from models.quantum.auto_model_selector import select_best_model
import traceback

logging.basicConfig(level=logging.INFO)

class ModelWrapper:
    def __init__(self, name, predict_func, description=""):
        self.name = name
        self.predict_func = predict_func
        self.description = description

    def predict(self, X_seq, X_tabular):
        return self.predict_func(X_seq, X_tabular)

def run_prediction(symbol="AAPL", model_choice="auto"):
    try:
        logging.info(f"تشغيل التنبؤ للسهم {symbol} باستخدام النموذج {model_choice}")

        df = load_data(symbol)
        df = df.dropna()

        df["return"] = df["Close"].pct_change()
        df["volatility"] = df["Close"].rolling(window=5).std()
        df = df.dropna()

        if df.empty or df.shape[0] < 10:
            raise ValueError("البيانات غير كافية لإجراء التنبؤ.")

        X_seq = np.expand_dims(df[["Close"]].values, axis=-1)
        X_tabular = df[["return", "volatility"]].values
        y_true = df["Close"].values

        models = {
            "hybrid": ModelWrapper("hybrid", hybrid_model_predict, "نموذج هجين يستخدم بيانات متسلسلة وجدولية."),
            "bayesian": ModelWrapper("bayesian", lambda x, y: build_bayesian_lstm(x.shape[1:]).predict(x), "Bayesian LSTM لتوقع السلاسل الزمنية."),
        }

        if model_choice in models:
            model = models[model_choice]
            pred = model.predict(X_seq, X_tabular)
            mae = np.mean(np.abs(y_true - pred))
            direction_acc = np.mean(np.sign(np.diff(y_true)) == np.sign(np.diff(pred))) * 100

            return [{
                "model": model.name,
                "description": model.description,
                "mae": mae,
                "direction_accuracy": direction_acc
            }]
        else:
            return select_best_model(models, X_seq, X_tabular, y_true)

    except Exception as e:
        logging.error(f"حدث خطأ أثناء التنبؤ: {e}")
        traceback.print_exc()
        return [{"error": str(e)}]
