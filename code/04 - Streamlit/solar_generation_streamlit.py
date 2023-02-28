import streamlit as st
import pandas as pd
import numpy as np
import h5py
import datetime as dt
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.utils import timeseries_dataset_from_array
from matplotlib.backends.backend_agg import RendererAgg
_lock = RendererAgg.lock

# Load data
#@st.cache
#def load_data():
#    camp1 = pd.read_csv("../../data/cleaned/campus5.csv")
#    camp1["Date"] = pd.to_datetime(camp1["Date"])
#    return camp1.set_index("Date")

#camp1 = load_data()

model_campus5 = keras.models.load_model('df.h5')

def forecast(model, batch_size = 16, row):
    X = row[0:-1]
    X = X.reshape(1, 1, len(X))
    yhat = model.predict(X, batch_size=batch_size)
    return yhat[0,0]

# Define a function to make predictions
def predictions(start, end, choice):

    indx = pd.date_range(start = start, end = end, freq = '15T')
    if choice == 'Campus 1':
        model = model_campus5
        max_val = 488.088
    elif choice == 'Campus 2':
        model = model_campus5
    elif choice == 'Campus 3':
        model = model_campus5
    elif choice == 'Campus 4':
        model = model_campus5
    elif choice == 'Campus 5':
        model = model_campus5
    elif choice == 'Campus 3 - Site 6':
        model = model_campus5
    elif choice == 'Campus 3 - Site 8':
        model = model_campus5
    elif choice == 'Campus 3 - Site 10':
        model = model_campus5
    elif choice == 'Campus 3 - Site 12':
        model = model_campus5

#    indx = tf.keras.layers.Reshape(indx)
    seq_length = 16
    indx_seq = timeseries_dataset_from_array(
        indx,
        targets = indx[seq_length:],
        sequence_length = seq_length,
        batch_size = 96,
        shuffle = False,
        seed = 42
    )
    predicts = model.predict(indx_seq)
    preds = predicts*max_val
    preds_df = pd.DataFrame(data = preds, index = indx, columns = ['Preds'])

    return preds_df

#Streamlit app
def app():
    st.sidebar.title("Solar Energy Generation Prediction App")

    with st.sidebar.container():
        options = ['Campus 1', 'Campus 2', 'Campus 3', 'Campus 4', 'Campus 5', 'Campus 3 - Site 6',
        'Campus 3 - Site 8',  'Campus 3 - Site 10', 'Campus 3 - Site 12']
        choice = st.selectbox("Select Only One Option", options)


    #    date_range = st.slider("Select date range", min_value=data.index.min(), max_value=camp1.index.max(), value=(data.index.min(), data.index.max()))

    #    data_filtered = data.loc[date_range[0]:date_range[1]]





        start_date = st.date_input("Start Date")
        start_time = st.time_input("Start Time")
        end_date = st.date_input("End Date")
        end_time = st.time_input("End Time")

        start = dt.datetime.combine(start_date, start_time)
        end = dt.datetime.combine(end_date, end_time)

    # Create a time series plot
    #with _lock:
    #    fig, ax = plt.subplots(figsize=(8, 6))
    #    ax.plot(data_filtered.index, data_filtered["Value"])
    #    ax.set_xlabel("Date")
    #    ax.set_ylabel("Value")
    #    ax.set_title("Time Series Plot")
    #    st.pyplot(fig)

    # Preds
    preds_df = predictions(start, end, choice)

    # Write Predictions
    st.write(f"The predicted solar generation for the given timeframe is given below")
    st.write(preds_df)


    # Plot the preds
    fig, ax = plt.subplots()
    ax.bar(preds_df.index, preds_df['Preds'])
    ax.set_xticklabels([])
    ax.set_ylabel('Solar Generation (kWh)')
    ax.set_xlabel('Time')
    ax.set_title('Solar Generation Output (kWh)')
    st.pyplot(fig)

#    csv = preds_df.to_csv(index=False)
#    b64 = base64.b64encode(csv.encode()).decode()
#    href = f'<a href="data:file/csv;base64,{b64}" download="{choice}predictions.csv">Download CSV</a>'
#    st.markdown(href, unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    app()
