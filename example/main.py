import streamlit as st

st.set_page_config(page_title="Streamlit Configurator!!!")

page = st.navigation(
    {
        "Streamlit Configurator": [
            st.Page("page/main_page.py", title="Introduction"),
        ],
        "Base Tutorial": [
            st.Page("page/build_base_page.py", title="Build Base Page"),
        ]
    },
)

page.run()