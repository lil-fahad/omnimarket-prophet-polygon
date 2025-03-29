import logging
logging.basicConfig(level=logging.INFO)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

def build_lstm_advanced(input_shape, units=64, dropout_rate=0.2):
    """
    وظيفة: build_lstm_advanced
    """
    model = Sequential()
    model.add(LSTM(units, input_shape=input_shape, return_sequences=True))
    model.add(Dropout(dropout_rate))
    model.add(LSTM(units))
    model.add(Dropout(dropout_rate))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model