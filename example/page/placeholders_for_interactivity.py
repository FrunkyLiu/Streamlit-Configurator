import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

import textwrap

import streamlit as st
from share_component import (
    description_template,
    segmented_control,
    show_demo_template,
    title_template,
)

from st_configurator import ComponentConfig, PageConfig, PageRenderer
from st_configurator.placeholder import Placeholder, PlaceholderValue


class MyPlaceholder(Placeholder):
    SC_RESULT = PlaceholderValue()


title = title_template.update(
    args=("🧩 Using Placeholders for Interactive Components",),
)


section_build_description_placeholder = description_template.update(
    args=(
        textwrap.dedent(
            """
            When you need interactive behavior between components, 
            you can use Placeholders to capture and share component outputs across your application.

            1. **Create a Placeholder**


            First, import the necessary classes and define your own placeholder class:
            ```python
            from st_configurator.placeholder import Placeholder, PlaceholderValue

            class MyPlaceholder(Placeholder):
                SC_RESULT = PlaceholderValue()
            ```
            2. **Configure the Component to Use the Placeholder**


            Modify the component configuration so that its output is stored in the placeholder. You can either specify the placeholder when creating the component:
            ```python
            segmented_control = ComponentConfig(
                component=st.segmented_control,
                args=(
                    "Options",
                    ["Option 1", "Option 2", "Option 3"],
                ),
                kwargs={"selection_mode": "multi"},
                result_key=MyPlaceholder.SC_RESULT,
            )
            ```
            Or, if you already have an existing configuration, update it using the update method:
            ```python
            segmented_control.update(result_key=MyPlaceholder.SC_RESULT)
            ```
            In either case, the component's return value will be recorded in MyPlaceholder.SC_RESULT so that it can be accessed by other functions or components.
            
            
            3. **Utilize the Placeholder's Value**


            Next, you can use the value stored in `MyPlaceholder.SC_RESULT` to drive further logic in your application. 
            It can be passed as an argument or keyword argument to other components.
            For example, you can pass the placeholder value to a component that processes the data:
            ```python
            display_segmented_control = ComponentConfig(
                component=lambda x: st.write(f"Selected Options: {' '.join(x)}"),
                args=(MyPlaceholder.SC_RESULT,),
            )
            ```
            In this example, the value captured by MyPlaceholder.SC_RESULT is passed into a lambda function that writes the selected options.
            This flexibility allows you to seamlessly integrate interactive behaviors across your application.


            4. **Finalize the Page Configuration**


            Finally, include both components in your page configuration so they work together:
            ```python
            page_config = PageConfig(
                page_tag="My Streamlit App",
                body=[segmented_control, display_segmented_control]
            )
            ```
            """
        ),
    ),
)

section_additional_information = description_template.update(
    args=(
        textwrap.dedent(
            """
            ##### 📌 Note: Using `global_scope` for Placeholders Across Pages

            By default, Placeholders retrieve values based on the current page, 
            ensuring that each page maintains its own separate state.
            However, if you need a Placeholder to be accessible across all pages, 
            you can enable the `global_scope` option.

            ###### Option 1: Define a Global Placeholder
            Modify the Placeholder definition to enable `global_scope`:
            ```python
            class MyPlaceholder(Placeholder):
                SC_RESULT = PlaceholderValue(global_scope=True)
            ```
            ###### Option 2: Enable `global_scope` When Assigning the `result_key`
            Alternatively, when using the Placeholder in a component, specify `global_scope=True`:
            ```python
            segmented_control = ComponentConfig(
                component=st.segmented_control,
                args=(
                    "Options",
                    ["Option 1", "Option 2", "Option 3"],
                ),
                kwargs={"selection_mode": "multi"},
                result_key=MyPlaceholder.SC_RESULT(global_scope=True),
            )
            ```
            With `global_scope=True`, the placeholder value will be shared across all pages, preventing parameter separation between different pages.
            This is useful when you want to maintain a global state in a multi-page application.
            """
        ),
    ),
)

segmented_control_with_placeholder = segmented_control.update(
    result_key=MyPlaceholder.SC_RESULT
)

display_segmented_control = ComponentConfig(
    component=lambda x: st.write(f"Selected Options: {' '.join(x)}"),
    args=(MyPlaceholder.SC_RESULT,),
)

divider = ComponentConfig(component=st.divider)

# Define the page configuration
page_config = PageConfig(
    page_tag="My Streamlit App",
    body=[
        title,
        section_build_description_placeholder,
        show_demo_template.update(
            children=[
                segmented_control_with_placeholder,
                display_segmented_control,
            ]
        ),
        divider,
        section_additional_information,
    ],
)

# Render page
PageRenderer().render_page(page_config)
