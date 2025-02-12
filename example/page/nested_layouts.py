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
    args=("📦 Containers & Nested Components with Children",),
)


section_build_description = description_template.update(
    args=(
        textwrap.dedent(
            """
            **Streamlit Configurator** supports **nested children** primarily 
            for **`st.columns`** and **`st.tabs`** (or other similar 
            container-like Streamlit functions). You can place multiple 
            **ComponentConfig** items within these containers by specifying 
            them as nested lists in the **`children`** attribute. Additionally, 
            you can insert **`None`** to intentionally leave a **column or tab** 
            empty.  

            > **Note**: While other elements (like **`st.container`**) might 
            also work with children in some contexts, the **automated nesting** 
            and **`None`** placeholders are primarily designed for 
            **`st.columns`** and **`st.tabs`**.  

            ---

            ### Multi-Row Layout with Nested Lists (Columns)
            When using **`st.columns`**, you can nest lists to create 
            multi-row layouts. Each **inner list** represents a row, and each 
            element in that list corresponds to **one column**.
            ```python
            import streamlit as st
            from st_configurator import ComponentConfig

            # Example components
            area_1 = ComponentConfig(component=st.code, args=("Area 1", None))
            area_2 = ComponentConfig(component=st.code, args=("Area 2", None))
            area_3 = ComponentConfig(component=st.code, args=("Area 3", None))
            area_4 = ComponentConfig(component=st.code, args=("Area 4", None))
            area_5 = ComponentConfig(component=st.code, args=("Area 5", None))
            area_6 = ComponentConfig(component=st.code, args=("Area 6", None))

            # Use st.columns as the container
            multi_row_layout = ComponentConfig(
                component=st.columns,
                args=(3,),  # 3 columns
                kwargs={"vertical_alignment": "center"},
                children=[
                    [area_1, area_2, area_3],  # First row
                    [area_4, area_5, area_6],  # Second row
                ],
            )
            ```
            With this structure, Streamlit Configurator handles creating the 
            columns and arranging components into rows.
            """
        ),
    ),
)


areas = [
    ComponentConfig(component=st.code, args=(f"Area {i}", None))
    for i in range(1, 7)
]

# Create a multi-row layout using nested lists.
# Here, we use st.columns as an example of a container that supports children.
multi_row_layout = ComponentConfig(
    component=st.columns,
    args=(3,),  # 3 columns per row
    kwargs={"vertical_alignment": "center"},
    children=[
        # First row
        [*areas[:3]],
        # Second row
        [*areas[3:]],
    ],
)

section_none_description = description_template.update(
    args=(
        textwrap.dedent(
            """
            ### Skipping a Column (**`None`**)
            To leave a column empty in either **`st.columns`** or **`st.tabs`**
            , insert **`None`** into the **`children`** list at the desired 
            position:
            
            ```python
            layout_with_gap = ComponentConfig(
                component=st.columns,
                args=(3,),
                kwargs={"vertical_alignment": "center"},
                children=[
                    [area_1, None, area_3],
                ],
            )
            ```
            Here, the **middle** column is intentionally left blank. This same 
            logic also applies if you are creating tabs: you could specify 
            **`None`** to skip a particular tab slot (though typically you’d 
            just omit that tab entirely).
            """
        ),
    ),
)

multi_row_layout_with_gap = ComponentConfig(
    component=st.columns,
    args=(3,),  # 3 columns per row
    kwargs={"vertical_alignment": "center"},
    children=[
        areas[0],
        None,
        areas[2],
    ],
)

section_none_warning_description = ComponentConfig(
    component=st.info,
    args=(
        """
        ##### Note
        When you insert a `None` value in the `children` list (to leave a column empty), 
        the actual layout adjustment depends on the `vertical_alignment` setting of the container. For example:

        - **vertical_alignment="top"**:

            Components in the same row may shift upward to fill the gap created by None. That is, the empty space might be effectively "filled" by aligning the content in adjacent cells toward the top.

        - **vertical_alignment="bottom"**:

            The empty column remains empty, and no upward shift occurs—the components retain their original positions.

        - **vertical_alignment="center"**:

            Components are centered vertically relative to the row, preserving the gap as a balanced empty space.

        Be sure to choose the appropriate vertical_alignment value for your layout design, as it directly influences how gaps (created by None) affect the overall appearance of your multi-column arrangement.
        
        
        Example:

        ```python
        # Layout with an intentionally empty middle column in the first row
        layout_with_gap = ComponentConfig(
            component=st.columns,
            args=(3,),
            kwargs={"vertical_alignment": "center"},
            children=[
                [area_1, None, area_3],
                [area_4, area_5, area_6],
            ],
        )
        ```
        """,
    ),
)

warning_layout_example_config = ComponentConfig(
    component=st.columns,
    args=(3,),  # 3 columns per row
    kwargs={"vertical_alignment": "center"},
    children=[
        [areas[0], None, areas[2]],
        [*areas[3:]],
    ],
)

section_dialog_description = description_template.update(
    args=(
        textwrap.dedent(
            """
            ### Using Children with Decorator (e.g. @st.dialog)
            If you employ a container-like decorator (e.g., **`@st.dialog`**) 
            that naturally supports children, you can declare those children 
            in the same way:

            Example:
            ```python
            dialog_config = ComponentConfig(
                condition=ComponentConfig(
                    component=st.button,
                    args=("Show Dialog",),
                    kwargs={"type": "primary", "use_container_width": True},
                ),
                component=st.dialog,
                args=("Dialog Title",),
                children=[
                    ComponentConfig(
                        component=st.write,
                        args=("This is the content of the dialog.",),
                    )
                ],
            )
            ```
            """
        ),
    ),
)


dialog_config = ComponentConfig(
    condition=ComponentConfig(
        component=st.button,
        args=("Show Dialog",),
        kwargs={"type": "primary", "use_container_width": True},
    ),
    component=st.dialog,
    args=("Dialog Title",),
    children=[
        ComponentConfig(
            component=st.write,
            args=("This is the content of the dialog.",),
        )
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
        section_none_warning_description,
        show_demo_template.update(children=[warning_layout_example_config]),
        divider,
        section_dialog_description,
        show_demo_template.update(children=[dialog_config]),
    ],
)

PageRenderer().render_page(page_config)
