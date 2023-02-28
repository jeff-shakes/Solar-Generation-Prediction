import streamlit as st
import pandas as pd
import numpy as np
import h5py
import datetime as dt
import matplotlib.pyplot as plt


#model = h5py.File('model.h5', 'r')

# Define a function to make predictions
def predictions(start, end, choice):

    indx = pd.date_range(start = start, end = end, freq = '15T')
    if choice == 'Campus 1':
        weights = model['weights_1']
    elif choice == 'Campus 2':
        weights = model['weights_2']
    elif choice == 'Campus 3':
        weights = model['weights_3']
    elif choice == 'Campus 4':
        weights = model['weights_4']
    elif choice == 'Campus 5':
        weights = model['weights_5']
    elif choice == 'Campus 3 - Site 6':
        weights = model['weights_5']
    elif choice == 'Campus 3 - Site 8':
        weights = model['weights_5']
    elif choice == 'Campus 3 - Site 10':
        weights = model['weights_5']
    elif choice == 'Campus 3 - Site 12':
        weights = model['weights_5']

    preds = model_selection.predict(indx)
    preds_df = pd.DataFrame(data = preds, index = indx, columns = ['Preds'])
    # Return the predictions
    return preds_df

#Streamlit app
def app():
    st.sidebar.title("Solar Energy Generation Prediction App")

    with st.sidebar.container():

        options = ['Campus 1', 'Campus 2', 'Campus 3', 'Campus 4', 'Campus 5', 'Campus 3 - Site 6',
        'Campus 3 - Site 8',  'Campus 3 - Site 10', 'Campus 3 - Site 12']
        choice = st.selectbox("Select Only One Option", options)

        start_date = st.date_input("Start Date")
        start_time = st.time_input("Start Time")
        end_date = st.date_input("End Date")
        end_time = st.time_input("End Time")

        start = dt.datetime.combine(start_date, start_time)
        end = dt.datetime.combine(end_date, end_time)



    # Preds
    preds_df = predictions(start, end, choice)

    # Write Predictions
    st.write(f"The predicted solar generation for the given timeframe is given below")
    st.write(preds_df)


    # Plot the timedelta
    fig, ax = plt.subplots()
    ax.bar(preds_df.index, preds_df['Preds'])
    ax.set_xticklabels([])
    ax.set_ylabel('Solar Generation (kWh)')
    ax.set_xlabel('Time')
    ax.set_title('Solar Generation Output (kWh)')
    st.pyplot(fig)

    csv = preds_df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{choice}predictions.csv">Download CSV</a>'
    st.markdown(href, unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    app()
