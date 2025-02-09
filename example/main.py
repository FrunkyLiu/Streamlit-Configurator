import streamlit as st

st.set_page_config(page_title="Streamlit Configurator")

page = st.navigation(
    {
        "Streamlit Configurator": [
            st.Page("page/main_page.py", title="Introduction"),
        ],
        "Base Tutorial": [
            st.Page("page/build_base_page.py", title="Build Base Page"),
            st.Page(
                "page/placeholders_for_interactivity.py",
                title="Placeholders for Interactivity",
            ),
            st.Page(
                "page/controlling_component_rendering_with_conditions.py",
                title="Controlling Component Rendering with Conditions",
            ),
            st.Page(
                "page/nested_layouts.py",
                title="Nested Layouts",
            ),
        ],
    },
)

page.run()
