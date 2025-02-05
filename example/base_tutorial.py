import textwrap

import streamlit as st

from st_configurator import LayoutConfig, PageConfig, PageRenderer

# from st_configurator.placeholder import Placeholder, PlaceholderValue

show_demo_template = LayoutConfig(
    component=st.expander,
    args=("Show Demo",),
    children=[],
)

title = LayoutConfig(
    component=st.title,
    args=("Streamlit Configurator",),
)

section_build = LayoutConfig(
    component=st.header,
    args=("How to Use?",),
    kwargs={"divider": True},
)

st_congifurator_description = LayoutConfig(
    component=st.markdown,
    args=(
        textwrap.dedent(
            """
            The Streamlit Configurator provides a structured approach for building modular and reusable Streamlit components. 
            By defining a template once, you can effortlessly replicate the same layout across multiple pages.
            This reduces repetitive code, promotes maintainability, and ensures consistent behavior throughout your application.
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
        code_eample,
        show_demo_template.update(children=[segmented_control]),
    ],
)

# Render page
PageRenderer().render_page(page_config)
