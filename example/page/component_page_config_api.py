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
            These data classes let you **declaratively** define your UI components and page layout in **Streamlit-Configurator**.

            ***
            ### ComponentConfig
            
            - ##### **Description:**

                Represents a single UI component's configuration, including:
                - Which Streamlit or custom function to call (**`component`**)
                - Any positional (**`args`**) or keyword (**`kwargs`**) parameters it needs
                - A conditional rule (**`condition`**) to decide if the component is rendered
                - Nested child components (**`children`**)
                - An optional placeholder (**`result_key`**) to store the component's output
            
            - #### **Attributes:**
                - **`component: Callable`** 

                    The Streamlit component (e.g., `st.button`, `st.text_input`) or a custom callable.
                - **`args: Tuple[Union[PlaceholderValue, Any], ...]`**  

                    Positional arguments passed to the component.
                - **`kwargs: Dict[str, Union[PlaceholderValue, Any]]`**  
                    Keyword arguments passed to the component. Merged with existing `kwargs` if updated.
                - **`children: Optional[Sequence[Union[ComponentConfig, Sequence[Optional[ComponentConfig]], None]]]`**  
                    A list (or nested lists) of other `ComponentConfig` instances. Allows for complex, nested layouts.
                - **`condition: Optional[Union[PlaceholderValue, ComponentConfig]]`**  
                    A condition controlling whether the component is rendered:
                  - If it's a `PlaceholderValue`, its boolean interpretation determines rendering.
                  - If it's another `ComponentConfig`, the returned value from that config is interpreted as a boolean.
                - **`result_key: Optional[PlaceholderValue]`**  
                    A placeholder to store the component's return value (if the component produces one).

            - #### **Key Methods:**

              - ##### ***update(self, args=None, kwargs=None, children=None, condition=None, result_key=None) -> ComponentConfig***

                ###### Parameters:

                  - **`args`**: A new tuple to replace the current `args`.
                  - **`kwargs`**: A dictionary merged into the current `kwargs`, overwriting any conflicting keys.
                  - **`children`**: A new list (or nested lists) to replace the current `children`.
                  - **`condition`**: A new condition to replace the current one.
                  - **`result_key`**: A new placeholder for capturing the component's return value.

                ###### Return:
                  - A **new** **`ComponentConfig`** instance with the specified updates.
                
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
            updated_name_input_config = name_input_config.update(
                kwargs={"placeholder": "Your full name"}
            )
            ```
            
            ---

            ### PageConfig
            
            - ##### **Description:**
            
                **`PageConfig`** defines the overall page structure with a **unique page tag**, 
                a list of **body** components, and an optional list of **sidebar** components.

            - #### **Attributes:**

                - **`page_tag: str`** 

                    A unique identifier for the page (also used as a prefix for placeholders if not in global scope).
                - **`body: List[ComponentConfig]`** 

                    A list of **`ComponentConfig`** objects representing the main body content.
                - **`sidebar: Optional[List[ComponentConfig]]`** 
                
                    A list of **`ComponentConfig`** objects for the page's sidebar. This field is optional.
    
            #### Example:
            ```python
            from st_configurator import PageConfig

            # Using the previously defined configs.
            page_config = PageConfig(
                page_tag="HomePage",
                body=[name_input_config],             # Main content
                sidebar=[updated_name_input_config]   # Sidebar content
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