import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

import textwrap

import streamlit as st
from share_component import description_template, title_template

from st_configurator import ComponentConfig, PageConfig, PageRenderer

title = title_template.update(
    args=("Component & Page Config API 🔧",),
)

description_config = description_template.update(
    args=(
        textwrap.dedent(
            """
            **Overview:**
            These data classes allow you to declaratively define your UI components and overall page layout.

            ***
            ### ComponentConfig
            
            - ##### **Description:**
            
                Describes a single UI component's configuration, including the 
                component callable, arguments, nested children, condition for 
                rendering, and output storage.
            
            - #### **Attributes:**

                - **`component: Callable`** — The Streamlit component or custom function.
                - **`args: Tuple[Union[PlaceholderValue, Any], ...]`** — Positional arguments for the component.
                - **`kwargs: Dict[str, Union[PlaceholderValue, Any]]`** — Keyword arguments for the component.
                - **`children: Optional[...]`** — Nested component configurations (supports flat or nested lists).
                - **`condition: Optional[Union[PlaceholderValue, ComponentConfig]]`** — A condition controlling rendering.
                - **`result_key: Optional[PlaceholderValue]`** — A placeholder for capturing the component's

            - #### **Key Methods:**

              - ##### ***update(self, args=None, kwargs=None, children=None, condition=None, result_key=None) -> ComponentConfig***

                ###### Parameters:

                - **`args`**: Optional tuple to replace current positional arguments.
                - **`kwargs`**: Optional dictionary to ***merge*** with or replace current keyword arguments.
                - **`children`**: Optional list to replace current children configurations.
                - **`condition`**: Optional replacement for the current condition.
                - **`result_key`**: Optional new result placeholder.

                ###### Return:
                  - A new ComponentConfig instance with the updated parameters.
                
            #### Example:
            ```python
            from st_configurator import ComponentConfig
            import streamlit as st

            # Define a simple text input configuration.
            name_input_config = ComponentConfig(
                component=st.text_input,
                args=("What is your name?",),
                kwargs={"placeholder": "Enter your name"},
            )

            # Update the configuration to modify the placeholder text.
            updated_name_input_config = name_input_config.update(kwargs={"placeholder": "Your full name"})
            ```
            ***

            ### PageConfig
            
            - ##### **Description:**
            
                Defines the overall page layout with a unique page tag, main body components, and an optional sidebar.

            - #### **Attributes:**

                - **`page_tag: str`** — A unique identifier for the page.
                - **`body: List[ComponentConfig]`** — A list of configurations for the main content.
                - **`sidebar: Optional[List[ComponentConfig]]`** — A list of configurations for the sidebar (optional).
    
            #### Example:
            ```python
            from st_configurator import PageConfig

            # Create a simple page configuration.
            page_config = PageConfig(
                page_tag="HomePage",
                body=[name_input_config],   # Main content components
                sidebar=[updated_name_input_config] # Sidebar components
            )
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
