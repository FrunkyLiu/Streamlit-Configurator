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
            **Streamlit Configurator** provides a **declarative** way to define and manage UI elements in Streamlit.  
            Instead of manually structuring Streamlit components using **imperative code**, you can use:
            
            - **`ComponentConfig`** to define UI elements.
            - **`PageConfig`** to structure the layout.
            - **`PageRenderer`** to render the page efficiently.

            This approach enhances **modularity, maintainability, and reusability** in Streamlit applications.
            
            ---
            
            1. **Define UI Elements**  
            Use **`ComponentConfig`** to create and configure Streamlit components such as buttons, inputs, and segmented controls.

            2. **Configure the Page Layout**  
            Use **`PageConfig`** to define the page structure, including:
                - **`page_tag`**: A unique identifier for the page.
                - **`body`**: The main page content (list of `ComponentConfig` instances).
                - **`sidebar`**: Components rendered inside `st.sidebar`.

            3. **Render the Page**  
            Use **`PageRenderer`** to render the page based on the defined configurations.
            
            ---

            ### 📝 Example: Creating a Simple Streamlit Page  

            The following example demonstrates how to **build a page** using a 
            **segmented control** inside the main content area and a **sidebar message**.

            ```python
            import streamlit as st
            from st_configurator import ComponentConfig, PageConfig, PageRenderer

            # Define a Streamlit UI element for the main content using ComponentConfig
            segmented_control = ComponentConfig(
                component=st.segmented_control,
                args=("Options", ["Option 1", "Option 2", "Option 3"]),
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

            ---

            #### 🔍 Explanation of Parameters
            - **`component`**

                Accepts any callable object (e.g., a native Streamlit element like **`st.button`** or a custom function).
            
            - **`args`** & **`kwargs `**
                
                Used to pass positional and keyword arguments to the component.
            
            - **`page_tag`**

                A unique identifier for the page, which helps manage scoped 
                placeholder values and avoids key conflicts.
            
            - **`body`**
            
                A list of **`ComponentConfig`** instances defining the main content of the page.
        
            - **`sidebar`**

                A list of **`ComponentConfig`** instances rendered inside **`st.sidebar`**.
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
