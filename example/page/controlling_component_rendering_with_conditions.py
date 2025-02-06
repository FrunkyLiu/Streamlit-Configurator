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
    args=("🎛️Dynamic Behavior with Conditions",),
)


section_build_description = description_template.update(
    args=(
        textwrap.dedent(
            """
            This page demonstrates how to control component rendering using conditions. 
            With conditions, a component is executed only when a specified condition evaluates to True. 
            You can either use a placeholder or a component config directly as the condition. 
            In addition, you can invert the logic or make the condition state persist across page refreshes.

            ### Using a Placeholder as a Condition
            First, create a switch component that sets a placeholder value:
            ```python
            text_area_switch = ComponentConfig(
                component=st.button,
                args=("Show Text Area",),
                result_key=MyPlaceholder.TEXT_AREA_SWITCH,
            )
            ```
            Then, define a text area component that only renders when the condition is met:
            ```python
            text_area = ComponentConfig(
                condition=MyPlaceholder.TEXT_AREA_SWITCH,
                component=st.text_area,
                args=("Enter some text here",),
            )
            ```
            Note: Here, the value of `MyPlaceholder.TEXT_AREA_SWITCH` is converted to a boolean. Only if it evaluates to `True` will the text area be rendered.

            ### Using a Component Config Directly as a Condition
            You can also pass the component configuration (instead of a placeholder) as the condition:
            ```python
            text_area = ComponentConfig(
                condition=text_area_switch,
                component=st.text_area,
                args=("Enter some text here",),
            )
            ```
            This approach bypasses the need to use a placeholder for condition checking.

            """
        ),
    ),
)


section_invert_description = description_template.update(
    args=(
        textwrap.dedent(
            """
            ### Inverting the Condition
            If you need the reverse logic (i.e. render the component when the condition is NOT met), you can invert the condition as follows:
            ```python
            text_area = ComponentConfig(
                condition=MyPlaceholder.TEXT_AREA_SWITCH(invert=True),
                component=st.text_area,
                args=("Enter some text here",),
            )
            ```
            """
        ),
    ),
)

section_persist_description = description_template.update(
    args=(
        textwrap.dedent(
            """
            ### Persisting the Condition State
            By default, the state of a placeholder (e.g., from a button click) might reset on page refresh.
            If you want the condition to remain True after the initial click, set the persist flag to True:
            ```python
            text_area = ComponentConfig(
                condition=MyPlaceholder.TEXT_AREA_SWITCH(persist=True),
                component=st.text_area,
                args=("Enter some text here",),
            )
            ```
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
    condition=MyPlaceholder.CLOSE_TEXT_AREA_SWITCH(invert=True),
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
    ],
)

PageRenderer().render_page(page_config)
