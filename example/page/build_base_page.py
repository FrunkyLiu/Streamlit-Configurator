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
            you can use **`ComponentConfig`**, **`PageConfig`**, and **`PageRenderer`** to simplify page construction.

            ### 📌 Steps to Build a Streamlit App with Configurator
            Follow these steps to build a basic Streamlit application using Streamlit Configurator:
            1. **Define UI Elements**
            
                Use **`ComponentConfig`** to create and configure Streamlit components (e.g., buttons, inputs, segmented controls).
            
            2. **Configure the Page Layout**
            
                Use **`PageConfig`** to define the structure of the page, including 
                the **`page_tag`**, **`body`**, and **`sidebar`**. The **`sidebar`** parameter works 
                similarly to **`body`**, but its components are rendered in **`st.sidebar`**.
            
            3. **Render the Page**
                
                Use **`PageRenderer`** to render the configured components into a working Streamlit app.

            ###### 📝 Example Code

            Here is an example of how to create a simple Streamlit app with a **segmented control**:

            ```python
            import streamlit as st
            from st_configurator import ComponentConfig, PageConfig, PageRenderer

            # Define a Streamlit UI element for the main content using ComponentConfig
            segmented_control = ComponentConfig(
                component=st.segmented_control,
                args=("Directions", ["Option 1", "Option 2", "Option 3"]),
                kwargs={"selection_mode": "multi"}
            )

            # Define a sidebar element using ComponentConfig
            sidebar_text = ComponentConfig(
                component=st.write,
                args=("Welcome to the sidebar!",)
            )

            # Define the page layout and structure using PageConfig
            page_config = PageConfig(
                page_tag="My Streamlit App",
                body=[segmented_control],
                sidebar=[sidebar_text]
            )

            # Render the configured page
            PageRenderer().render_page(page_config)
            ```
            #### Parameter Explanations:
            - **`component`**

                Accepts any callable object—this can be a native Streamlit element or a custom function.
            
            - **`args`** & **`kwargs `**
                
                Used to pass positional and keyword parameters to the callable.
            
            - **`page_tag`**

                A unique identifier for the page, which can help differentiate pages and scope placeholder values.
            
            - **`body`**
            
                A list of **`ComponentConfig`** instances that are rendered in order to create the main content of the page.
            
            - **`sidebar`**

                A list of **`ComponentConfig`** instances rendered within **`st.sidebar`**.
            """
        ),
    ),
)

# Define a sidebar element using ComponentConfig
sidebar_text = ComponentConfig(
    component=st.write, args=("Welcome to the sidebar!",)
)

# Define a Streamlit element using ComponentConfig
page_config = PageConfig(
    page_tag="My Streamlit App",
    body=[
        section_build,
        section_build_description_base,
        show_demo_template.update(children=[segmented_control]),
    ],
    sidebar=[sidebar_text],
)

# Render page
PageRenderer().render_page(page_config)
