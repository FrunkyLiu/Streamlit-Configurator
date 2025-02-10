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
    NAME = PlaceholderValue(default="")
    AGE = PlaceholderValue(default=18)
    GENDER = PlaceholderValue(default="Others")
    GENDER_INDEX = PlaceholderValue(default=None)


title_config = title_template.update(
    args=("💾 Unified Input and Output with Placeholders",),
)

description_config = description_template.update(
    args=(
        textwrap.dedent(
            """
            In this example, placeholders serve a dual purpose—they not only capture and store 
            the resulting output but also provide default input values to components. 
            This unified approach overcomes common issues with state persistence when using component keys, 
            ensuring that user inputs remain intact even when switching pages.
            ***
            #### Example: Unified Input and Output with Placeholders
            ```python
            import streamlit as st
            from st_configurator import ComponentConfig, PageConfig, PageRenderer
            from st_configurator.placeholder import Placeholder, PlaceholderValue

            # Define placeholders with default values.
            class MyPlaceholder(Placeholder):
                NAME = PlaceholderValue()
                AGE = PlaceholderValue(default=18)
                GENDER = PlaceholderValue(default="Others")
                GENDER_INDEX = PlaceholderValue(default=None)

            gender_options = ["Male", "Female", "Others"]

            def str2index(value):
                if value:
                    return gender_options.index(value)
                return None

            # Configure a text input component.
            # The placeholder provides both the initial value and records user input.
            name_input_config = ComponentConfig(
                component=st.text_input,
                args=("What is your name?",),
                kwargs={
                    "value": MyPlaceholder.NAME(default=""),
                    "placeholder": "Enter your name here...",
                },
                result_key=MyPlaceholder.NAME,
            )

            # Configure a slider component for AGE.
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

            # Configure a selectbox component for gender selection.
            gender_selectbox_config = ComponentConfig(
                component=st.selectbox,
                args=("What is your gender?", gender_options),
                kwargs={"placeholder": "Select your gender", "index": MyPlaceholder.GENDER_INDEX},
                result_key=MyPlaceholder.GENDER,
            )

            # Convert the selected gender into an index.
            gender_converter_config = ComponentConfig(
                component=str2index,
                args=(MyPlaceholder.GENDER,),
                result_key=MyPlaceholder.GENDER_INDEX,
            )

            # Define the page configuration with all the components.
            page_config = PageConfig(
                page_tag="User Information",
                body=[
                    name_input_config,
                    age_slider_config,
                    gender_selectbox_config,
                    gender_converter_config,
                ],
            )

            PageRenderer().render_page(page_config)
            ```
            #### Demo:
            Try configuring this page: Set your values using the inputs provided, 
            switch to another page via your sidebar, and then return. 
            You'll see that the values you entered remain intact—only the components 
            on this page use this advanced placeholder mechanism, ensuring that your user data is preserved.
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
            ### How It Works
            - **Dual Role of Placeholders:**

                In the above example, the same placeholder (e.g., `MyPlaceholder.NAME`) is 
                used to provide the initial value for a component and to capture the user's 
                input. This eliminates the need to manage separate keys for state and ensures 
                that values persist even when the page is reloaded or navigated away from.

            - Avoiding State Loss:

                Typically, Streamlit components use keys (e.g., `key="name"`) to store 
                values in `st.session_state`. However, when switching pages via a sidebar, 
                these values may reset to their defaults. With placeholders, the internal 
                mechanism preserves state reliably across page changes.

            - Handling Timing Issues:

                Manual state management can lead to timing problems (e.g., a slider 
                reverting to an old value due to page refreshes before the new value is saved). 
                By integrating default values and result recording within the placeholder, 
                these issues are avoided.
            
            ##### Timing issue example:
            ```python
            if 'my_age' not in st.session_state:
                st.session_state['my_age'] = 18
            st.slider("How old are you?", min_value=0, max_value=100, value=st.session_state['my_age'], key="age")
            st.session_state['my_age'] = st.session_state.get('age', 18)
            ```
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
            - Unified Input/Output:
            
                A single placeholder instance manages both the initial value and the user-provided updates, streamlining your code.

            - Enhanced State Persistence:
            
                Values remain consistent even when users navigate away and return, improving the user experience.

            - Reduced Manual State Management:

                The placeholder mechanism abstracts away the complexities of managing st.session_state manually, reducing potential bugs.


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
