import textwrap

import streamlit as st

from st_configurator import LayoutConfig, PageConfig, PageRenderer

show_demo_template = LayoutConfig(
    component=st.expander,
    args=("Show Demo",),
    children=[],
)

title = LayoutConfig(
    component=st.title,
    args=("Streamlit Configurator",),
)

st_congifurator_description = LayoutConfig(
    component=st.markdown,
    args=(
        textwrap.dedent(
            """
            The Streamlit Configurator provides a structured approach to building modular and reusable Streamlit components. 
            By defining a template once, you can effortlessly replicate the same layout across multiple pages.
            This reduces redundant code, enhances maintainability, and ensures a consistent user experience throughout your application.
            """
        ),
    ),
)

section_build = LayoutConfig(
    component=st.header,
    args=("How to Use?",),
    kwargs={"divider": True},
)

section_build_description = LayoutConfig(
    component=st.markdown,
    args=(
        textwrap.dedent(
            """
            To build a Streamlit application using the Streamlit Configurator, follow these steps:
            > Step 1. Define a Streamlit element using LayoutConfig.
            """
        ),
    ),
)

# Define a Streamlit element using LayoutConfig
segmented_control = LayoutConfig(
    component=st.segmented_control,
    args=(
        "Directions",
        ["Option 1", "Option 2", "Option 3"],
    ),
    kwargs={"selection_mode": "multi"},
)

code_eample = LayoutConfig(
    component=st.code,
    args=(
        textwrap.dedent(
            """
            from st_configurator import LayoutConfig, PageConfig, PageRenderer

            # Define the streamlit element using LayoutConfig
            segmented_control = LayoutConfig(
                component=st.segmented_control,
                args=("Directions", ["Option 1", "Option 2", "Option 3"],),
                kwargs={"selection_mode": "multi"}
            )

            # Define page using configuration
            page_config = PageConfig(
                title="My Streamlit App",
                body=[segmented_control]
            )

            # Render page
            PageRenderer().render_page(page_config)
            """
        ),
    ),
)

# Define the page configuration
page_config = PageConfig(
    page_tag="My Streamlit App",
    body=[
        title,
        st_congifurator_description,
        section_build,
        section_build_description,
        code_eample,
        show_demo_template.update(children=[segmented_control]),
    ],
)

# Render page
PageRenderer().render_page(page_config)
