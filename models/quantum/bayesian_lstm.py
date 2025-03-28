logging.basicConfig(level=logging.INFO)
import logging
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def build_bayesian_lstm(input_shape):
    """
    وظيفة: build_bayesian_lstm
    """
    model = Sequential()
    model.add(LSTM(64, return_sequences=True, input_shape=input_shape, dropout=0.3, recurrent_dropout=0.3))
    model.add(LSTM(64, dropout=0.3, recurrent_dropout=0.3))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model