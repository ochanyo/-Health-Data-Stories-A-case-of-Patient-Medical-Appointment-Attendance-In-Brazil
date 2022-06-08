import pandas as pd

import pandas_profiling

import streamlit as st

from streamlit_pandas_profiling import st_profile_report

from pandas_profiling import ProfileReport




df = pd.read_csv('brazil_data.csv')




profile = ProfileReport(df,

                        title="Appointment Attendance Register",

        dataset={

        "description": "This profiling report was generated for #HealthDataStories",

    },

)




st.title("Pandas Profiling of Brazil Patient Medical Appointment Attendance in Streamlit")

st.write(df)
st_profile_report(profile)
