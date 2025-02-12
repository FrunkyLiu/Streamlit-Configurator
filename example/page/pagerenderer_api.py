import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

import textwrap

import streamlit as st
from share_component import description_template, title_template

from st_configurator import ComponentConfig, PageConfig, PageRenderer

title = title_template.update(
    args=("PageRenderer API 🚀",),
)

description_config = description_template.update(
    args=(
        textwrap.dedent(
            """
            **Overview:**
            The **`PageRenderer`** class is responsible for processing **component configurations** 
            and rendering them in **Streamlit**. It automatically:
            - Resolves **Placeholders** before rendering.
            - **Evaluates conditions** to determine whether a component should be displayed.
            - Handles **nested layouts**, allowing for complex UI structures.

            ---

            ### PageRenderer

            - #### **Key Methods:**

              - ##### ***render_layout(self, configs: Sequence[ComponentConfig | None]) -> None***
                Renders a sequence of **component configurations**. It:
                - Iterates through the **`configs`** list.
                - Checks each component’s **condition** (if specified).
                - Processes **nested components** within layouts like columns or containers.

                
                ###### Parameters:

                - **`configs`**: A sequence (list) of **`ComponentConfig`** objects or **`None`**.

                ###### Return:
                - **`None`**. The layout is displayed in **Streamlit**.

                ###### Example:
                ```python
                from st_configurator import PageRenderer

                # Assume we have a list of component configurations.
                renderer = PageRenderer()
                renderer.render_layout(layout_configs)
                ```
                
              - ##### ***render_page(self, configs: PageConfig) -> None***
                Renders an entire **page** based on the provided **`PageConfig`**. It:

                - Updates the **current page tag** in **`Placeholder`**.
                - Renders the **sidebar** first (if any).
                - Then renders the main **body** components.


                ###### Parameters:

                - **`configs`**: A **`PageConfig`** object containing **`page_tag`**, 
                **`body`**, and **`sidebar`**.

                ###### Return:
                - **`None`**. The full page layout is rendered in **`Streamlit`**.
                
                ##### Example:
                ```python
                from st_configurator import PageRenderer

                # Assume page_config is already defined.
                renderer = PageRenderer()
                renderer.render_page(page_config)
                ```
            """
        ),
        True,
    ),
)


page_config = PageConfig(
    page_tag="Main Page",
    body=[title, description_config],
)

PageRenderer().render_page(page_config)