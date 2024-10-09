# %%
import streamlit as st
import numpy as np
import pandas as pd
import openmatrix as omx

# %%


def parse_omx(file):
    # Parse the OMX file
    with open("temp.omx", "wb") as f:
        f.write(file.getbuffer())

    data = {}
    with omx.open_file("temp.omx", "r") as omx_file:
        for key in omx_file.list_matrices():
            data[key] = np.array(omx_file[key])

    return data


def main():
    st.title("OMX File Upload and Display")

    # File uploader
    uploaded_file = st.file_uploader("Choose an OMX file", type=["omx"])

    if uploaded_file is not None:
        # Parse the uploaded OMX file
        data = parse_omx(uploaded_file)

        kernels = list(data.keys())
        kernel = st.selectbox("Select Kernel", kernels)
        # Create a DataFrame and display it
        df = pd.DataFrame(data[kernel])
        st.write("## Matrix Data")
        st.dataframe(df)


if __name__ == "__main__":
    main()
