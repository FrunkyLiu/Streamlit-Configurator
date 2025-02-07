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
    args=("📦Containers & Nested Components with Children",),
)


section_build_description = description_template.update(
    args=(
        textwrap.dedent(
            """
            Streamlit Configurator allows you to nest components using the children attribute. 
            This mechanism isn’t limited to a single container type—it works with any container-like 
            element (such as columns, containers, dialogs, etc.) and enables you to build complex, 
            multi-row and multi-column layouts in a declarative fashion. Additionally, 
            you can use `None` to intentionally leave a space empty.
            > Note: While the examples below use `st.columns` to illustrate the children mechanism, 
            the same approach applies to other container elements like `st.container` or custom dialogs.

            
            ### Multi-Row Layout with Nested Lists
            Use nested lists within the children attribute to create layouts spanning multiple rows. 
            Each inner list represents a row, and each element in that list represents a column (or child component) within that row.

            ```python
            import streamlit as st
            from st_configurator import ComponentConfig

            # Define components for the layout
            name_input = ComponentConfig(
                component=st.text_input,
                kwargs={"label": "Enter your name"},
            )

            submit_button = ComponentConfig(
                component=st.button,
                kwargs={"label": "Submit", "use_container_width": True},
            )

            terms_checkbox = ComponentConfig(
                component=st.checkbox,
                kwargs={"label": "Accept Terms"},
            )

            comments_textarea = ComponentConfig(
                component=st.text_area,
                kwargs={"label": "Additional Comments"},
            )

            option_radio = ComponentConfig(
                component=st.radio,
                args=("Choose an option", ["Option A", "Option B", "Option C"]),
            )

            age_slider = ComponentConfig(
                component=st.slider,
                args=("Set your age", 18, 100),
            )

            # Create a multi-row layout using nested lists.
            # Here, we use st.columns as an example of a container that supports children.
            multi_row_layout = ComponentConfig(
                component=st.columns,
                args=(3,),  # 3 columns per row
                kwargs={"vertical_alignment": "center", "border": True},
                children=[
                    # First row
                    [name_input, submit_button, terms_checkbox],
                    # Second row
                    [comments_textarea, option_radio, age_slider],
                ],
            )
            ```
            """
        ),
    ),
)


# Define components for the layout
name_input = ComponentConfig(
    component=st.text_input,
    kwargs={"label": "Enter your name"},
)

submit_button = ComponentConfig(
    component=st.button,
    kwargs={"label": "Submit", "use_container_width": True},
)

terms_checkbox = ComponentConfig(
    component=st.checkbox,
    kwargs={"label": "Accept Terms"},
)

comments_textarea = ComponentConfig(
    component=st.text_area,
    kwargs={"label": "Additional Comments"},
)

option_radio = ComponentConfig(
    component=st.radio,
    args=("Choose an option", ["Option A", "Option B", "Option C"]),
)

age_slider = ComponentConfig(
    component=st.slider,
    args=("Set your age", 18, 100),
)

# Create a multi-row layout using nested lists.
# Here, we use st.columns as an example of a container that supports children.
multi_row_layout = ComponentConfig(
    component=st.columns,
    args=(3,),  # 3 columns per row
    kwargs={"vertical_alignment": "top", "border": True},
    children=[
        # First row
        [name_input, submit_button, terms_checkbox],
        # Second row
        [comments_textarea, option_radio, age_slider],
    ],
)

section_none_description = description_template.update(
    args=(
        textwrap.dedent(
            """
            ### Skipping a Column
            If you need to leave a space empty in your layout, simply insert `None` at that position in the children list. 
            

            Example:
            ```python
            # Layout with an intentionally empty middle column in the first row
            layout_with_gap = ComponentConfig(
                component=st.columns,
                args=(3,),
                kwargs={"vertical_alignment": "center"},
                children=[
                    [name_input, None, terms_checkbox],
                ],
            )
            ```
            In this example, the first row’s middle column is empty. 
            Streamlit's `st.columns` will automatically adjust the layout by shifting the components accordingly.

            """
        ),
    ),
)

multi_row_layout_with_gap = ComponentConfig(
    component=st.columns,
    args=(3,),  # 3 columns per row
    kwargs={"vertical_alignment": "center"},
    children=[
        name_input.update(kwargs={"key": "name_input"}),
        None,
        terms_checkbox.update(kwargs={"key": "terms_checkbox"}),
    ],
)

# Warning: When using `st.columns`, a `None` value will cause Streamlit to automatically shift subsequent components upward within that row.
divider = ComponentConfig(component=st.divider)

page_config = PageConfig(
    page_tag="Dynamic Behavior with Conditions",
    body=[
        title,
        section_build_description,
        show_demo_template.update(children=[multi_row_layout]),
        divider,
        section_none_description,
        show_demo_template.update(children=[multi_row_layout_with_gap]),
    ],
)

PageRenderer().render_page(page_config)