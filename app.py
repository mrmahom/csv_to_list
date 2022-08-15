import streamlit as st
import decode

# --------------------------------------

st.set_page_config(page_title="ID lista vesszővel")

st.title("ID lista vesszővel")

uploaded_file = st.file_uploader("Töltsd fel a csv fájlt!")

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
        st.download_button('Letöltés', text_contents)

st.markdown("---")
st.write("@author: E. Martin Maho")