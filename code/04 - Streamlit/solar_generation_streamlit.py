import streamlit as st
import pandas as pd
import numpy as np
import h5py
import datetime as dt
import matplotlib.pyplot as plt


# Load data
@st.cache
def load_camp1():
    camp1 = pd.read_csv("../../data/predictions/camp1_pred.csv")
    camp1.index = pd.to_datetime(camp1["Timestamp"])
    return camp1

def load_camp2():
    camp2 = pd.read_csv("../../data/predictions/camp2_pred.csv")
    camp2.index = pd.to_datetime(camp2["Timestamp"])
    return camp2

def load_camp3():
    camp3 = pd.read_csv("../../data/predictions/camp3_pred.csv")
    camp3.index = pd.to_datetime(camp3["Timestamp"])
    return camp3

def load_camp4():
    camp4 = pd.read_csv("../../data/predictions/camp4_pred.csv")
    camp4.index = pd.to_datetime(camp4["Timestamp"])
    return camp4

def load_camp5():
    camp5 = pd.read_csv("../../data/predictions/camp5_pred.csv")
    camp5.index = pd.to_datetime(camp5["Timestamp"])
    return camp5

def load_site6():
    site6 = pd.read_csv("../../data/predictions/site6_pred.csv")
    site6.index = pd.to_datetime(site6["Timestamp"])
    return site6

def load_site8():
    site8 = pd.read_csv("../../data/predictions/site8_pred.csv")
    site8.index = pd.to_datetime(site8["Timestamp"])
    return site8

def load_site10():
    site10 = pd.read_csv("../../data/predictions/site10_pred.csv")
    site10.index = pd.to_datetime(site10["Timestamp"])
    return site10

def load_site12():
    site12 = pd.read_csv("../../data/predictions/site12_pred.csv")
    site12.index = pd.to_datetime(site12["Timestamp"])
    return site12

camp1 = load_camp1()
camp2 = load_camp2()
camp3 = load_camp3()
camp4 = load_camp4()
camp5 = load_camp5()
site6 = load_site6()
site8 = load_site8()
site10 = load_site10()
site12 = load_site12()


x = pd.date_range(start = camp1.index[0], end = camp1.index[-1], freq = '15T')

def plot_option_1():
    fig, ax = plt.subplots(figsize = (12,8))
    ax.plot(camp1[['Preds', 'True']])
    ax.set_xlabel('Time', fontsize = 20)
    for tick in ax.get_xticklabels():
        tick.set_rotation(30)
    ax.set_ylabel('Solar Generation (Min/Max Scaled)', fontsize = 20)
    ax.set_title('Campus 1', fontsize = 28);

def plot_option_2():
    fig, ax = plt.subplots(figsize = (12,8))
    ax.plot(camp2[['Preds', 'True']])
    ax.set_xlabel('Time', fontsize = 20)
    for tick in ax.get_xticklabels():
        tick.set_rotation(30)
    ax.set_ylabel('Solar Generation (Min/Max Scaled)', fontsize = 20)
    ax.set_title('Campus 2', fontsize = 28);

def plot_option_3():
    fig, ax = plt.subplots(figsize = (12,8))
    ax.plot(camp3[['Preds', 'True']])
    ax.set_xlabel('Time', fontsize = 20)
    for tick in ax.get_xticklabels():
        tick.set_rotation(30)
    ax.set_ylabel('Solar Generation (Min/Max Scaled)', fontsize = 20)
    ax.set_title('Campus 3', fontsize = 28);

def plot_option_4():
    fig, ax = plt.subplots(figsize = (12,8))
    ax.plot(camp4[['Preds', 'True']])
    ax.set_xlabel('Time', fontsize = 20)
    for tick in ax.get_xticklabels():
        tick.set_rotation(30)
    ax.set_ylabel('Solar Generation (Min/Max Scaled)', fontsize = 20)
    ax.set_title('Campus 4', fontsize = 28);

def plot_option_5():
    fig, ax = plt.subplots(figsize = (12,8))
    ax.plot(camp5[['Preds', 'True']])
    ax.set_xlabel('Time', fontsize = 20)
    for tick in ax.get_xticklabels():
        tick.set_rotation(30)
    ax.set_ylabel('Solar Generation (Min/Max Scaled)', fontsize = 20)
    ax.set_title('Campus 5', fontsize = 28);

def plot_option_6():
    fig, ax = plt.subplots(figsize = (12,8))
    ax.plot(site6[['Preds', 'True']])
    ax.set_xlabel('Time', fontsize = 20)
    for tick in ax.get_xticklabels():
        tick.set_rotation(30)
    ax.set_ylabel('Solar Generation (Min/Max Scaled)', fontsize = 20)
    ax.set_title('Site 6', fontsize = 28);

def plot_option_8():
    fig, ax = plt.subplots(figsize = (12,8))
    ax.plot(site8[['Preds', 'True']])
    ax.set_xlabel('Time', fontsize = 20)
    for tick in ax.get_xticklabels():
        tick.set_rotation(30)
    ax.set_ylabel('Solar Generation (Min/Max Scaled)', fontsize = 20)
    ax.set_title('Site 8', fontsize = 28);

def plot_option_10():
    fig, ax = plt.subplots(figsize = (12,8))
    ax.plot(site10[['Preds', 'True']])
    ax.set_xlabel('Time', fontsize = 20)
    for tick in ax.get_xticklabels():
        tick.set_rotation(30)
    ax.set_ylabel('Solar Generation (Min/Max Scaled)', fontsize = 20)
    ax.set_title('Site 10', fontsize = 28);

def plot_option_12():
    fig, ax = plt.subplots(figsize = (12,8))
    ax.plot(site12[['Preds', 'True']])
    ax.set_xlabel('Time', fontsize = 20)
    for tick in ax.get_xticklabels():
        tick.set_rotation(30)
    ax.set_ylabel('Solar Generation (Min/Max Scaled)', fontsize = 20)
    ax.set_title('Site 12', fontsize = 28);




def app():
    # Define the options
    options = {
        "Campus 1": plot_option_1,
        "Campus 2": plot_option_2,
        "Campus 3": plot_option_3,
        "Campus 4": plot_option_4,
        "Campus 5": plot_option_5,
        "Site 6": plot_option_6,
        "Site 8": plot_option_8,
        "Site 10": plot_option_10,
        "Site 10": plot_option_10,


    }
    option = st.sidebar.selectbox("Select an option", list(options.keys()))

    plot_func = options[option]

    # Call the plot function
    plot_func()

    # Define the zoom slider
    zoom_level = st.sidebar.slider("Zoom level", 0.1, 70.0, 1.0)

    # Set the x-axis limits based on the zoom level
    x_limits = plt.xlim()
    x_range = x_limits[1] - x_limits[0]
    x_middle = (x_limits[0] + x_limits[1]) / 2
    plt.xlim(x_middle - x_range / (2 * zoom_level), x_middle + x_range / (2 * zoom_level))

    # Define the x-axis slider
    x_slider = st.sidebar.slider("X-axis", float(x_limits[0]), float(x_limits[1]), float(x_middle), step=float(x_range/100))

    # Set the x-axis based on the slider value
    plt.xlim(x_slider - x_range / (2 * zoom_level), x_slider + x_range / (2 * zoom_level))

    fig = plt.gcf()
    st.pyplot(fig)


if __name__ == '__main__':
    app()
