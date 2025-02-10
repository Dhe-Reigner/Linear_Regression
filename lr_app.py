import streamlit as st
import pandas as pd
import numpy as np
import sklearn 
import pickle

model  =pickle.load(open('linear_regression_model.pkl', 'rb'))

# let's create web app
st.title("Scikit-Learn Linear Regression Model")
