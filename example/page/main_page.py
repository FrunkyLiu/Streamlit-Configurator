import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

import textwrap

import streamlit as st
from share_component import description_template, title_template

from st_configurator import ComponentConfig, PageConfig, PageRenderer

title = title_template.update(
    args=("✨ Streamlit Configurator",),
)

st_congifurator_info = description_template.update(
    args=(
        textwrap.dedent(
            """
            ### Overview
            **Streamlit Configurator** provides a structured, declarative 
            approach to building and reusing Streamlit components. By defining 
            layout and behavior once, you can consistently apply the same 
            patterns across multiple pages—minimizing repetitive code and 
            reducing maintenance overhead.

            ---

            ### Key Benefits

            - **Reusable Components 🔄**  
                
                Define a `ComponentConfig` once and leverage it 
                everywhere—ensuring consistent layout, logic, and styling 
                throughout your Streamlit app.

            - **Flexible Parameter Passing & Robust State Management 🔗**  
                
                Built-in **placeholders** allow for seamless sharing of 
                parameters across components, preserving their values even 
                when switching pages. This ensures stability and consistency, 
                without relying on fragile, key-based state references.

            - **Compatibility & Resilience 🛡️**  
                
                The placeholder mechanism coexists smoothly with standard 
                Streamlit usage. It safeguards against unexpected re-runs or 
                version updates by maintaining a reliable reference to state, 
                preventing data loss and streamlining user interactions.

            By combining declarative layouts, dynamic placeholders, and straightforward integrations, **Streamlit Configurator** lays the foundation for building **interactive, modular, and maintainable** Streamlit applications.

            ---

            ### Contact & GitHub
            - **📭 Email**: [x77497856@gmail.com](mailto:x77497856@gmail.com)  
            - **👍 GitHub**: [https://github.com/FrunkyLiu/Streamlit-Configurator](https://github.com/FrunkyLiu/Streamlit-Configurator)
            """
        ),
    ),
)

page_config = PageConfig(
    page_tag="Main Page",
    body=[title, st_congifurator_info],
)

PageRenderer().render_page(page_config)
