logging.basicConfig(level=logging.INFO)
import logging
from models.lstm_advanced import build_lstm_advanced
import xgboost as xgb
import numpy as np

def hybrid_model_predict(seq_data, tabular_data):
    """
    وظيفة: hybrid_model_predict
    """
    lstm_model = build_lstm_advanced(seq_data.shape[1:])
    lstm_model.fit(seq_data, np.mean(seq_data, axis=2), epochs=1, verbose=0)
    lstm_preds = lstm_model.predict(seq_data)

    xgb_model = xgb.XGBRegressor()
    xgb_model.fit(tabular_data, lstm_preds.flatten())
    final_preds = xgb_model.predict(tabular_data)

    return final_preds