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


class MyPlaceholder(Placeholder):
    SHOW_TEXT_AREA_SWITCH = PlaceholderValue()
    CLOSE_TEXT_AREA_SWITCH = PlaceholderValue()
    PERSIST_TEXT_AREA_SWITCH = PlaceholderValue()


title = title_template.update(
    args=("🎛️ Dynamic Behavior with Conditions",),
)


section_build_description = description_template.update(
    args=(
        textwrap.dedent(
            """

            This page demonstrates how to **conditionally render** Streamlit 
            components using **`PlaceholderValue`** or another 
            **`ComponentConfig`** as the condition. A component only renders 
            if its condition evaluates to `True`. You can also:
            - Use **`format_fn`** to transform the placeholder's value 
            (for instance, invert a **`True/False`**).
            - Control whether a placeholder's updated value remains 
            permanently changed by setting **`persist=True`**.

            ---
    
            ### Defining a Custom Placeholder Class
            To manage multiple placeholders in one page, it's a good practice 
            to create a custom class that extends **`Placeholder`**. For example:
            ```python
            from st_configurator.placeholder import Placeholder, PlaceholderValue

            class MyPlaceholder(Placeholder):
                SHOW_TEXT_AREA_SWITCH = PlaceholderValue()
                CLOSE_TEXT_AREA_SWITCH = PlaceholderValue()
                PERSIST_TEXT_AREA_SWITCH = PlaceholderValue()
            ```

            Each class-level attribute (e.g., **`SHOW_TEXT_AREA_SWITCH`**) becomes 
            its own **`PlaceholderValue`**, identified by a key that includes the 
            current page's tag (or **`_GLOBAL_`** if **`global_scope=True`**).

            ---

            ### Using a Placeholder as a Condition
            1. **Define a switch** component that sets a placeholder value:
            ```python
            text_area_switch = ComponentConfig(
                component=st.button,
                args=("Show Text Area",),
                result_key=MyPlaceholder.SHOW_TEXT_AREA_SWITCH,
            )
            ```
            2. **Conditionally render** another component based on that placeholder:
            
            ```python
            text_area = ComponentConfig(
                condition=MyPlaceholder.SHOW_TEXT_AREA_SWITCH,
                component=st.text_area,
                args=("Enter some text here",),
            )
            ```
            In this example, if **`MyPlaceholder.SHOW_TEXT_AREA_SWITCH`** 
            is **`True`**, the text area appears; otherwise, it's hidden.

            ---
            ### Using a ComponentConfig Directly as a Condition
            Instead of referencing a placeholder, you can pass a 
            **`ComponentConfig`** directly:
            ```python
            text_area = ComponentConfig(
                condition=text_area_switch,  # The button config itself
                component=st.text_area,
                args=("Enter some text here",),
            )
            ```
            The component's return value (e.g., the button state) is used as the condition.
            """
        ),
    ),
)


section_invert_description = description_template.update(
    args=(
        textwrap.dedent(
            """
            ### Transforming the Placeholder's Value with **`format_fn`**
            If you want to invert a placeholder value or apply another custom 
            transformation, pass a callable via **`format_fn`**:
            ```python
            text_area_invert = ComponentConfig(
                condition=MyPlaceholder.CLOSE_TEXT_AREA_SWITCH(
                    format_fn=lambda x: not bool(x)
                ),
                component=st.text_area,
                args=("Enter some text here (invert)",),
            )
            ```
            Here, the button's **`True`**/**`False`** value is flipped, so the 
            text area renders if the button is not pressed (i.e., the 
            placeholder is **`False`**).
            """
        ),
    ),
)

section_persist_description = description_template.update(
    args=(
        textwrap.dedent(
            """
            ### Persisting the Condition State
            By default, a placeholder might revert to its **initial default** on 
            each page refresh or re-run. If you set **`persist=True`**, 
            once its value changes, it remains at that updated value for all 
            subsequent checks—**ignoring** further attempts to modify it. 
            For example:
            ```python
            text_area_persist = ComponentConfig(
                condition=MyPlaceholder.PERSIST_TEXT_AREA_SWITCH(persist=True),
                component=st.text_area,
                args=("Enter some text here (persist)",),
                kwargs={
                    "placeholder": "Enter text and press `Ctrl + Enter` to trigger page refresh."
                },
            )
            ```
            In this scenario, after the placeholder's value is changed to 
            **`True`** once, it stays **`True`** unless you manually reset it 
            (such as clearing the session state).
            """
        ),
    ),
)

section_tail_description = description_template.update(
    args=(
        textwrap.dedent(
            """
            By following these steps, you can build interactive Streamlit 
            apps where certain components appear only under specific 
            conditions, optionally **inverting** the condition or **locking** a 
            placeholder's state with persistence.
            """
        ),
    ),
)

text_area_switch = ComponentConfig(
    component=st.button,
    args=("Show Text Area",),
    result_key=MyPlaceholder.SHOW_TEXT_AREA_SWITCH,
)

text_area = ComponentConfig(
    condition=MyPlaceholder.SHOW_TEXT_AREA_SWITCH,
    component=st.text_area,
    args=("Enter some text here",),
)

text_area_switch_invert = ComponentConfig(
    component=st.button,
    args=("Close Text Area",),
    result_key=MyPlaceholder.CLOSE_TEXT_AREA_SWITCH,
)

text_area_invert = ComponentConfig(
    condition=MyPlaceholder.CLOSE_TEXT_AREA_SWITCH(
        format_fn=lambda x: not bool(x)
    ),
    component=st.text_area,
    args=("Enter some text here (invert)",),
)

text_area_switch_persist = ComponentConfig(
    component=st.button,
    args=("Show Text Area Persist",),
    result_key=MyPlaceholder.PERSIST_TEXT_AREA_SWITCH,
)

text_area_persist = ComponentConfig(
    condition=MyPlaceholder.PERSIST_TEXT_AREA_SWITCH(persist=True),
    component=st.text_area,
    args=("Enter some text here (persist)",),
    kwargs={
        "placeholder": "Enter text and press `Ctrl + Enter` to trigger page refresh."
    },
)

divider = ComponentConfig(component=st.divider)

page_config = PageConfig(
    page_tag="Dynamic Behavior with Conditions",
    body=[
        title,
        section_build_description,
        show_demo_template.update(children=[text_area_switch, text_area]),
        divider,
        section_invert_description,
        show_demo_template.update(
            children=[text_area_switch_invert, text_area_invert]
        ),
        divider,
        section_persist_description,
        show_demo_template.update(
            children=[text_area_switch_persist, text_area_persist]
        ),
        divider,
        section_tail_description,
    ],
)

PageRenderer().render_page(page_config)
