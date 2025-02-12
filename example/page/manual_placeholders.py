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
            ### Overview
            In certain cases, you may need to **create or update placeholders 
            on the fly**, rather than pre-defining all of them in a class. 
            This approach provides extra **flexibility**, allowing you to 
            dynamically manage placeholder states. Below are three methods for 
            adding a new placeholder value, as well as guidelines for updating 
            and retrieving values.

            ---

            ### Adding New Placeholder Values
            Suppose you already have a class like:
            ```python
            class MyPlaceholder(Placeholder):
                CHAT_INPUT = PlaceholderValue()
                HISTORY_MESSAGES = PlaceholderValue()
            ```
            If you want to add a new placeholder (e.g., for a numeric value), 
            you have three main options:

            1. **Recommended:** Assign a **`PlaceholderValue`** directly with 
            
                the desired parameters:
                ```python
                MyPlaceholder.NUMBER = PlaceholderValue(default=0)
                # Optionally specify extra parameters in one step:
                # MyPlaceholder.NUMBER = PlaceholderValue(default=0, persist=True, global_scope=True)
                ```
            
            2. **Direct Assignment:**

                ```python
                MyPlaceholder.NUMBER = 0
                ```
                Even when assigning a raw value like **`0`**, Streamlit Configurator 
                automatically converts it into a **`PlaceholderValue`**. Thus you 
                still benefit from methods like **`.get()`** and **`.set()`**.
            
            3. **Using `set_attr`:**

                ```python
                MyPlaceholder.set_attr("NUMBER", 0)
                ```
                This helper method also ensures that the assigned value becomes a 
                **`PlaceholderValue`**.

            The first method is preferred because it allows you to define all 
            placeholder properties (like **`persist`** or **`global_scope`**) 
            in a single, clear statement.
            
            ---
            
            ### Updating and Retrieving Placeholder Values
            Once a placeholder exists on your class:

            - **Update** its value:

                ```python
                MyPlaceholder.NUMBER.set(2)
                ```
            
            - **Retrieve** its value:

                ```python
                current_value = MyPlaceholder.NUMBER.get()
                ```
            
            This read/write mechanism ensures consistency and state 
            persistence, even if the user navigates away or refreshes the page.

            ---

            ### Why Use Manual Placeholder Setup?
            1. **Dynamic Configuration**
                
                You can add or modify placeholders at runtime, which can be 
                crucial for apps that generate new state requirements based on 
                user interactions or external data.

            2. **Enhanced Parameterization**
            
                Passing parameters like **`persist=True`** or 
                **`global_scope=True`** in a single assignment keeps 
                configuration organized. This also helps ensure that state 
                remains intact when switching pages, a common shortcoming of 
                Streamlit’s default key-based system.

            3. **Improved Compatibility**
            
                By manually manipulating placeholders (e.g., assigning a raw 
                value that is auto-converted or using **`set_attr`**), you can 
                seamlessly blend native Streamlit coding patterns with 
                **Streamlit Configurator’s declarative** approach. This hybrid 
                strategy is especially useful when keys alone risk losing 
                state due to page transitions or complex refresh triggers.

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
