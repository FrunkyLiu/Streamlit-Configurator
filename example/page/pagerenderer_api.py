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
            The `PageRenderer` class processes the component configurations and renders them in Streamlit. 
            It resolves placeholders, checks conditions, and handles nested components.

            ***
            ### PageRenderer

            - #### **Key Methods:**

              - ##### ***render_layout(self, configs: Sequence[ComponentConfig | None]) -> None***

                ###### Parameters:

                - **`configs`**:  A sequence of component configurations (or None).

                ###### Return:
                - **`None`**. Renders the layout defined by the configurations.
                
              - ##### ***render_page(self, configs: PageConfig) -> None***

                ###### Parameters:

                - **`configs`**:  The complete page configuration.

                ###### Return:
                - **`None`**. Renders the entire page, including sidebar and body.
                
            #### Example:
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
