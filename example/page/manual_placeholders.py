import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

import textwrap

import streamlit as st
from share_component import (
    description_template,
    show_demo_template,
    title_template,
)

from st_configurator import ComponentConfig, PageConfig, PageRenderer
from st_configurator.placeholder import Placeholder, PlaceholderValue

title = title_template.update(
    args=("🛠️ Manual Placeholder Setup",),
)

description_config = description_template.update(
    args=(
        textwrap.dedent(
            """
            Sometimes, you may need to add or update placeholders manually—without 
            pre-defining all of them within your class. This flexibility allows 
            you to dynamically configure and update placeholders as needed. 
            Below are three methods to add a new placeholder value, along with 
            how to update and retrieve the value.
            ***
            ### Adding New Placeholder Values
            Consider the following base definition:
            ```python
            class MyPlaceholder(Placeholder):
                CHAT_INPUT = PlaceholderValue()
                HISTORY_MESSAGES = PlaceholderValue()
            ```
            Now, suppose you need to add a new placeholder for a numeric value. 
            You can do this in three ways:
            1. **Recommended:**

                Create and assign a new placeholder with all parameters in one step.
                ```python
                MyPlaceholder.NUMBER = PlaceholderValue(default=0)
                # You can also include extra parameters:
                # MyPlaceholder.NUMBER = PlaceholderValue(default=0, persist=True, global_scope=True)
                ```

            2. **Direct Assignment:**

                Simply assign a new value.

                ```python
                MyPlaceholder.NUMBER = 0
                ```
                Even when you directly assign a raw value like `0`, it is automatically 
                converted into a `PlaceholderValue` object. This ensures that the 
                new value still supports all the associated methods (such as `.set()` and `.get()`) 
                and remains fully compatible with the st_configurator system.

            3. **Using set_attr:**

                Use the `set_attr` method to assign a new placeholder value.
                ```python
                MyPlaceholder.set_attr("NUMBER", 0)
                ```

            The **recommended method** is the first one—`MyPlaceholder.NUMBER = 
            PlaceholderValue(default=0)`—since it allows you to specify additional 
            parameters (like `persist` and `global_scope`) in a single call.
            ***
            ### Updating and Retrieving Placeholder Values
            Once a placeholder is set up, you can update its value and retrieve it when needed:
            - **Update the Value:**
            ```python
            MyPlaceholder.NUMBER.set(2)
            ```
            - **Retrieve the Value:**
            ```python
            current_value = MyPlaceholder.NUMBER.get()
            ```
            ***
            ### Why Use Manual Placeholder Setup?
            Flexibility & Control:

            - **Dynamic Configuration:**

                Manually setting placeholders gives you the freedom to add or 
                modify placeholders on the fly, which can be especially useful 
                in dynamic applications where new state variables might be 
                needed at runtime.

            - **Enhanced Parameterization:**

                By using the recommended method—creating a placeholder with a call like
                `MyPlaceholder.NUMBER = PlaceholderValue(default=0, persist=True, global_scope=True)`
                —you can bundle additional settings (such as persistence or global scope) 
                with the default value. This makes your state management more robust, 
                ensuring that even if Streamlit's built-in key-based mechanism fails 
                to retain state across page switches, your placeholder will still 
                hold the correct value.
            
            - **Improved Compatibility:**

                Manual manipulation of placeholders (for example, assigning a raw 
                value directly or using helper methods like `set_attr`) lets you 
                bridge the gap between native Streamlit coding and the declarative 
                configuration approach of Streamlit-Configurator. This 
                compatibility is crucial when the straightforward key-based 
                approach might lead to lost or outdated state, especially 
                during page transitions.
            """
        ),
    )
)

page_config = PageConfig(
    page_tag="Flexible Integration & Compatibility",
    body=[
        title,
        description_config,
    ],
)

PageRenderer().render_page(page_config)
