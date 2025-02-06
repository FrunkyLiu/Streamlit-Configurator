import streamlit as st

from st_configurator import ComponentConfig

segmented_control = ComponentConfig(
    component=st.segmented_control,
    args=(
        "Options",
        ["Option 1", "Option 2", "Option 3"],
    ),
    kwargs={"selection_mode": "multi"},
)

show_demo_template = ComponentConfig(
    component=st.expander,
    args=("Show Demo",),
    children=[],
)

description_template = ComponentConfig(component=st.markdown)

title_template = ComponentConfig(
    component=st.header,
    kwargs={"divider": True},
)