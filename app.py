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

    choices_list = dc.get_choices_list(df)
    choice = st.selectbox(
        "Válaszd ki az ID-kat tartalmazó oszlopot!",
        (["Válassz!"] + choices_list)
    )

    st.markdown("---")

    if choice == "Válassz!":
        st.warning("Nem válaszottál oszlopot")
    else:
        choices_list_length = dc.number_of_items(choice, df)
        company_id_list = dc.get_id_list(choice, df)
        values_for_query = []
        for id in company_id_list
            values_for_query.append(f"({id})")
        st.info(f"select * from (values {",".join(values_for_query)}) as t(company_id)"")

st.markdown("---")
st.write("@author: _E. *Martin* Maho_")
