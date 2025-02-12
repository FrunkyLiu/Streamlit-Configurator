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
    args=("🔧 Building a Basic Streamlit Page with Streamlit Configurator",),
)

section_build_description_base = description_template.update(
    args=(
        textwrap.dedent(
            """
            **Streamlit Configurator** provides a declarative way to build and 
            manage Streamlit UI elements. Rather than manually writing 
            Streamlit calls in a traditional procedural approach, you use:
            - **`ComponentConfig`** to define individual UI elements (e.g., buttons, inputs, segmented controls).
            - **`PageConfig`** to organize those components into a page structure (body and sidebar).
            - **`PageRenderer`** to render the page as a functional Streamlit app.

            ---

            ### 📌 Steps to Build a Streamlit App with Configurator
            1. **Define UI Elements**  
                
                Create **`ComponentConfig`** instances for each Streamlit 
                component you need—this could be a native Streamlit 
                function (like **`st.button`**) or a custom function 
                (like **`st.segmented_control`** if it's provided by your codebase).

            2. **Configure the Page Layout**  
                
                Use **`PageConfig`** to specify:
                - **`page_tag`**: A unique identifier for the page.
                - **`body`**: The main UI elements (a list of **`ComponentConfig`** instances).
                - **`sidebar`**: Optional components rendered in the Streamlit sidebar.

            3. **Render the Page**  
                
                Invoke `PageRenderer().render_page(...)` with your `PageConfig`. 
                This automatically processes conditions, nested layouts, 
                and placeholders before displaying everything in Streamlit.

            ---    
            
            ### 📝 Example Code

            Below is a minimal example demonstrating how to define a 
            **segmented control** in the body and a simple text in the sidebar:

            ```python
            import streamlit as st
            from st_configurator import ComponentConfig, PageConfig, PageRenderer

            # This is assumed to be a custom or extended Streamlit function
            # that displays a segmented control. Adapt it as needed.
            segmented_control_config = ComponentConfig(
                component=st.segmented_control,        # or your custom function
                args=("Directions", ["Option 1", "Option 2", "Option 3"]),
                kwargs={"selection_mode": "multi"}
            )

            # Define a sidebar element using ComponentConfig
            sidebar_text_config = ComponentConfig(
                component=st.write,
                args=("Welcome to the sidebar!",)
            )

            # Define the page layout
            page_config = PageConfig(
                page_tag="My Streamlit App",
                body=[segmented_control_config],    # Main content
                sidebar=[sidebar_text_config]       # Sidebar content
            )

            # Render the configured page
            PageRenderer().render_page(page_config)
            ```
            #### Parameter Highlights:
            - **`component`**

                Any callable object (e.g., **`st.button`**, **`st.text_input`**
                , or a custom function).
            
            - **`args`** & **`kwargs `**
                
                Positional and keyword arguments passed to the component.
            
            - **`page_tag`**

                A unique label identifying this page 
                (used for scoping placeholders if you use them).
            
            - **`body`**
            
                A list of **`ComponentConfig`** objects that make up the main page content.
            
            - **`sidebar`**

                A list of **`ComponentConfig`** objects for the Streamlit sidebar.

            This approach scales seamlessly as your application grows, 
            allowing you to maintain a clean, declarative structure for your Streamlit app.
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
