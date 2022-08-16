import streamlit as st
import decode
from datetime import datetime
from io import StringIO
import pandas as pd

# --------------------------------------

now = datetime.now()
dt_string = now.strftime("%Y-%m-%d_%H-%M-%S")  # YYYY-mm-dd_HH-MM-SS

st.set_page_config(page_title="ID lista vesszővel")

st.title("ID lista vesszővel")

uploaded_file = st.file_uploader("Töltsd fel a csv fájlt!")


#adding a file uploader

file = st.file_uploader("Please choose a file")

if file is not None:
    #To read file as bytes:
    bytes_data = file.getvalue()
    st.write(bytes_data)

    #To convert to a string based IO:
    stringio = StringIO(file.getvalue().decode("utf-8"))
    st.write(stringio)

    #To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    #Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(file)
    st.write(df)


if uploaded_file is not None:
    lst = decode.file_parser(uploaded_file)

    choice = st.selectbox(
        "Válaszd ki az ID-kat tartalmazó oszlopot!",
        (["Válassz!"] + decode.get_choices_list(lst))
    )

    st.markdown("---")

    if choice == "Válassz!":
        st.warning("Nem válaszottál oszlopot")
    else:
        st.success("A megadott településen nincs iparűzési adófizetésre vonatkozó kötelezettség!")
        text_contents = decode.list_creator(choice, lst)
        st.download_button('Letöltés', text_contents, file_name=dt_string)

st.markdown("---")
st.write("@author: E. Martin Maho")
