import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

import textwrap

import streamlit as st
from share_component import (
    description_template,
    segmented_control,
    show_demo_template,
    title_template,
)

from st_configurator import ComponentConfig, PageConfig, PageRenderer

section_build = title_template.update(
    args=("🔧Building a Basic Streamlit Page with Streamlit Configurator",),
)

section_build_description_base = description_template.update(
    args=(
        textwrap.dedent(
            """
            Streamlit Configurator is a powerful tool that allows you to define and manage Streamlit UI elements in a declarative way. 
            Instead of manually structuring Streamlit components,
            you can use **ComponentConfig**, **PageConfig**, and **PageRenderer** to simplify page construction.

            ### 📌 Steps to Build a Streamlit App with Configurator
            Follow these steps to build a basic Streamlit application using Streamlit Configurator:
            1. **Define UI Elements**
            > Use `ComponentConfig` to create and configure Streamlit components (e.g., buttons, inputs, segmented controls).
            2. **Configure the Page Layout**
            > Use `PageConfig` to define the structure of the page, including the page_tag and layout.
            3. **Render the Page**
            > Use `PageRenderer` to render the configured components into a working Streamlit app.

            ###### 📝 Example Code

            Here is an example of how to create a simple Streamlit app with a **segmented control**:

            ```python
            import streamlit as st
            from st_configurator import ComponentConfig, PageConfig, PageRenderer

            # Define a Streamlit UI element using ComponentConfig
            segmented_control = ComponentConfig(
                component=st.segmented_control,
                args=("Directions", ["Option 1", "Option 2", "Option 3"]),
                kwargs={"selection_mode": "multi"}
            )

            # Define the page layout and structure using PageConfig
            page_config = PageConfig(
                page_tag="My Streamlit App",
                body=[segmented_control]
            )

            # Render the configured page
            PageRenderer().render_page(page_config)
            ```
            - The component parameter accepts any callable object—this can be a Streamlit element or a custom function.
            - args and kwargs are used to pass parameters to the callable.
            - page_tag helps to identify or differentiate the page.
            - body is a list of ComponentConfig instances that are rendered in order to create the Streamlit elements on the page.

            
            More information, please refer to the [README.md]()
            """
        ),
    ),
)

# Define a Streamlit element using ComponentConfig
page_config = PageConfig(
    page_tag="My Streamlit App",
    body=[
        section_build,
        section_build_description_base,
        show_demo_template.update(children=[segmented_control]),
    ],
)

# Render page
PageRenderer().render_page(page_config)