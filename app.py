import streamlit as st
import decode as dc
import pandas as pd

# --------------------------------------

st.set_page_config(page_title="ID lista vesszővel")

st.title("ID lista vesszővel")

uploaded_file = st.file_uploader("Töltsd fel a csv fájlt!")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

    choice = st.selectbox(
        "Válaszd ki az ID-kat tartalmazó oszlopot!",
        (["Válassz!"] + dc.get_choices_list(df))
    )

    st.markdown("---")

    if choice == "Válassz!":
        st.warning("Nem válaszottál oszlopot")
    else:
        st.success("Szuper! Letöltheted a listát ;D")
        output_file = dc.text_file_generator(choice, df)
        with open(output_file) as o:
            st.download_button('Letöltés', o)

st.markdown("---")
st.write("@author: E. Martin Maho")
