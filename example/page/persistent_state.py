import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

import textwrap

import streamlit as st
from share_component import description_template, title_template

from st_configurator import ComponentConfig, PageConfig, PageRenderer
from st_configurator.placeholder import Placeholder, PlaceholderValue


class MyPlaceholder(Placeholder):
    NAME = PlaceholderValue()
    AGE = PlaceholderValue()
    GENDER = PlaceholderValue(default="Others")
    GENDER_INDEX = PlaceholderValue(default=None)


title_config = title_template.update(
    args=("💾 Unified Input and Output with Placeholders",),
)

description_config = description_template.update(
    args=(
        textwrap.dedent(
            """
            ### Overview 
            In many Streamlit apps, **component keys** (**`key="something"`**) 
            are used to preserve input values across re-runs. However, when 
            you **switch pages** within a Streamlit app, these keys often reset
            , causing inputs to revert to their **default** states. By using 
            **placeholders**—in which each placeholder handles both the 
            **initial value** and the **updated user input**—you can maintain 
            values more reliably, even when navigating between pages.

            ---

            ### Dual Role of Placeholders
            Placeholders (`PlaceholderValue`) serve a **twofold purpose**:
            1. **Initial Value**: When passed as **`value`** to a component like 
            **`st.text_input`** or **`st.slider`**, the placeholder provides the 
            component's starting value.
            2. **Result Capture**: By assigning the placeholder as 
            **`result_key`**, any user updates are stored back into that same 
            placeholder—overriding the initial default.

            This approach neatly **avoids** the need for separate keys and 
            manual synchronization with **`st.session_state`**.

            ---

            ### Example Usage
            Below is a simplified illustration of how placeholders can unify input and output:

            ```python
            import streamlit as st
            from st_configurator import ComponentConfig, PageConfig, PageRenderer
            from st_configurator.placeholder import Placeholder, PlaceholderValue

            # 1. Define placeholders with defaults.
            class MyPlaceholder(Placeholder):
                NAME = PlaceholderValue(default="")
                AGE = PlaceholderValue(default=18)
                GENDER = PlaceholderValue(default="Others")
                GENDER_INDEX = PlaceholderValue(default=None)

            gender_options = ["Male", "Female", "Others"]

            def str2index(value):
                if value:
                    return gender_options.index(value)
                return None

            # 2. Configure components to both read & write from the same placeholder.
            name_input_config = ComponentConfig(
                component=st.text_input,
                args=("What is your name?",),
                kwargs={
                    "value": MyPlaceholder.NAME,
                    "placeholder": "Enter your name here...",
                },
                result_key=MyPlaceholder.NAME,
            )

            age_slider_config = ComponentConfig(
                component=st.slider,
                args=("How old are you?",),
                kwargs={
                    "min_value": 0,
                    "max_value": 100,
                    "value": MyPlaceholder.AGE,
                },
                result_key=MyPlaceholder.AGE,
            )

            gender_selectbox_config = ComponentConfig(
                component=st.selectbox,
                args=("What is your gender?", gender_options),
                kwargs={"placeholder": "Select your gender", "index": MyPlaceholder.GENDER_INDEX},
                result_key=MyPlaceholder.GENDER,
            )

            gender_converter_config = ComponentConfig(
                component=str2index,
                args=(MyPlaceholder.GENDER,),
                result_key=MyPlaceholder.GENDER_INDEX,
            )

            # 3. Assemble the page.
            page_config = PageConfig(
                page_tag="Unified Input and Output with Placeholders",
                body=[
                    name_input_config,
                    age_slider_config,
                    gender_selectbox_config,
                    gender_converter_config,
                ],
            )

            PageRenderer().render_page(page_config)
            ```
            In this setup:

            - **`MyPlaceholder.NAME`** is provided as both the default value 
            (**`kwargs["value"]`**) and the destination for user input 
            (**`result_key`**).
            - The same logic applies to **`AGE`**, **`GENDER`**, and 
            **`GENDER_INDEX`**.
            
            As a result, you can **navigate away** from the page and return 
            later to find the user's inputs still populated—no extra session 
            state handling is needed.
            """
        ),
    ),
)

gender_options = ["Male", "Female", "Others"]


def str2index(value):
    if value:
        return gender_options.index(value)
    return None


name_input_config = ComponentConfig(
    component=st.text_input,
    args=("What is your name?",),
    kwargs={
        "value": MyPlaceholder.NAME(default=""),
        "placeholder": "Enter your name here...",
    },
    result_key=MyPlaceholder.NAME,
)

age_slider_config = ComponentConfig(
    component=st.slider,
    args=("How old are you?",),
    kwargs={
        "min_value": 0,
        "max_value": 100,
        "value": MyPlaceholder.AGE(default=18),
    },
    result_key=MyPlaceholder.AGE,
)

gender_selectbox_config = ComponentConfig(
    component=st.selectbox,
    args=(
        "What is your gender?",
        gender_options,
    ),
    kwargs={
        "placeholder": "Select your gender",
        "index": MyPlaceholder.GENDER_INDEX,
    },
    result_key=MyPlaceholder.GENDER,
)

gender_converter_config = ComponentConfig(
    component=str2index,
    args=(MyPlaceholder.GENDER,),
    result_key=MyPlaceholder.GENDER_INDEX,
)

advanced_demo_panel = ComponentConfig(
    component=st.container,
    kwargs={"border": True},
    children=[
        name_input_config,
        age_slider_config,
        gender_selectbox_config,
        gender_converter_config,
    ],
)

divider = ComponentConfig(component=st.divider)

secoond_description_config = description_template.update(
    args=(
        textwrap.dedent(
            """
            ### Avoiding Timing Issues
            A common pitfall when manually managing **`st.session_state`** is 
            timing. If the user interacts with a slider or text input, then 
            rapidly triggers a page refresh, the new value might not be 
            captured before the old value is restored. Here's a minimal 
            example of where timing problems can occur:

            ```python
            if 'my_age' not in st.session_state:
                st.session_state['my_age'] = 18
            st.slider("How old are you?", 0, 100, value=st.session_state['my_age'], key="age")
            st.session_state['my_age'] = st.session_state.get('age', 18)
            ```
            If the user changes the slider value **twice in quick** succession, 
            Streamlit could re-run and revert to an earlier state. By using 
            placeholders for both **default input** and **updated output**, you avoid 
            these conflicts because the placeholder is consistently 
            responsible for storing—and retrieving—the latest value.
            ##### Timing issue demo:
            Please drag the slider at least twice.
            """
        ),
    ),
)


def timing_issue_demo():
    if "my_age" not in st.session_state:
        st.session_state["my_age"] = 18
    st.slider(
        "How old are you?", 0, 100, value=st.session_state["my_age"], key="age"
    )
    st.session_state["my_age"] = st.session_state.get("age", 18)


timing_issue_demo_config = ComponentConfig(
    component=st.container,
    kwargs={"border": True},
    children=[ComponentConfig(component=timing_issue_demo)],
)

third_description_config = description_template.update(
    args=(
        textwrap.dedent(
            """
            ### Benefits
            - **Unified Input/Output:**
            
                A single placeholder instance handles both the initial value 
                and any user updates, reducing complexity.

            - **Enhanced State Persistence:**
            
                User inputs are preserved across page switches—no separate key 
                management required.

            - **Cleaner Code:**

                Automatic synchronization via placeholders eliminates extra 
                session-state checks and minimizes potential timing bugs.


            """
        ),
    ),
)


page_config = PageConfig(
    page_tag="Unified Input and Output with Placeholders",
    body=[
        title_config,
        description_config,
        advanced_demo_panel,
        divider,
        secoond_description_config,
        timing_issue_demo_config,
        divider,
        third_description_config,
    ],
)

PageRenderer().render_page(page_config)
