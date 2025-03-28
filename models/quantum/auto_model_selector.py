logging.basicConfig(level=logging.INFO)
import logging
from sklearn.metrics import mean_absolute_error
import numpy as np

def select_best_model(model_dict, X_seq, X_tabular, y_true):
    """
    وظيفة: select_best_model
    """
    results = []
    for name, model_func in model_dict.items():
        preds = model_func(X_seq, X_tabular)
        mae = mean_absolute_error(y_true, preds)
        direction_acc = np.mean(np.sign(np.diff(y_true)) == np.sign(np.diff(preds))) * 100
        results.append({"model": name, "mae": mae, "direction_accuracy": direction_acc})
    return sorted(results, key=lambda x: x["mae"])