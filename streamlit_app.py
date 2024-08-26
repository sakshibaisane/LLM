import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Additional UI elements
st.header("Welcome to the App")
st.subheader("Here are some quick options to get started:")
st.button("Click me!")
st.text_input("Enter your text here:")

# Displaying a sample chart
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(data)
