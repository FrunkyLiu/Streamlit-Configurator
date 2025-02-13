import streamlit as st
try:
    import st_configurator
except ImportError:
    import sys
    sys.path.append("../")

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
        "Advanced Tutorial": [
            st.Page(
                "page/persistent_state.py",
                title="Persistent State",
            ),
            st.Page(
                "page/flexible_integration.py",
                title="Flexible Integration",
            ),
            st.Page(
                "page/manual_placeholders.py",
                title="Manual Placeholders",
            ),
        ],
        "API Reference": [
            st.Page(
                "page/placeholder_api.py",
                title="Placeholder API",
            ),
            st.Page(
                "page/component_page_config_api.py",
                title="Component and Page Config API",
            ),
            st.Page(
                "page/pagerenderer_api.py",
                title="PageRenderer API",
            ),
        ]
    },  
)

page.run()
