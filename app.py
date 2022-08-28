import streamlit as st
import decode as dc
import pandas as pd

# --------------------------------------

st.set_page_config(page_title="ID lista")

st.title("ID lista - vesszővel elválasztva")

uploaded_file = st.file_uploader("Töltsd fel a csv fájlt!")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.index += 1

    head_num = st.selectbox(
        "Hány elemet szeretnél látni?",
        ([10, "mindet!"])
    )
    head_num = 10 if head_num != "mindet!" else 1000000

    st.table(df.head(head_num))

    choice = st.selectbox(
        "Válaszd ki az ID-kat tartalmazó oszlopot!",
        (["Válassz!"] + dc.get_choices_list(df))
    )

    st.markdown("---")

    if choice == "Válassz!":
        st.warning("Nem válaszottál oszlopot")
    else:
        choices_list_length = dc.number_of_items(choice, df)
        st.success(f"Szuper! Letöltheted {choices_list_length} elemet tartalmazó listát ;D")
        output_field = dc.get_string_for_file(choice, df)
        st.download_button('Letöltés', output_field)

st.markdown("---")
st.write("@author: E. Martin Maho")
