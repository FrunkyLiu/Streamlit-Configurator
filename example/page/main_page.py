import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

import textwrap

import streamlit as st
from share_component import description_template, title_template

from st_configurator import ComponentConfig, PageConfig, PageRenderer

title = title_template.update(
    args=("📃 Streamlit Configurator",),
)

st_congifurator_info = description_template.update(
    args=(
        textwrap.dedent(
            """
            Streamlit Configurator provides a structured approach to building modular 
            and reusable Streamlit components. By defining a template once, you can 
            effortlessly replicate the same layout across multiple pages—reducing 
            redundant code, ensuring consistent behavior, and enhancing maintainability.

            
            **Key Benefits:**

            
             - **Reusable Components🔄**:
            
                Each instance of `ComponentConfig` can be reused throughout 
                your application, making it easy to maintain a consistent 
                layout and behavior across different pages.

             - **Flexible Parameter Passing & Robust State Management🔗**:

                The built-in Placeholder mechanism allows you to pass parameters 
                seamlessly between components while maintaining stable 
                state—even across page switches. This means you can share data 
                (such as user inputs or computed values) across various parts 
                of your configuration without worrying about inconsistencies 
                or loss of state.

             - **Compatibility & Resilience Against Updates 🛡️**:

                By leveraging the Placeholder mechanism, Streamlit Configurator 
                minimizes the risk of errors arising from changes in Streamlit's 
                update process. It also integrates harmoniously with native 
                Streamlit coding patterns, ensuring that your application 
                consistently reads and manages values correctly as underlying 
                components evolve.
            
            Overall, Streamlit Configurator streamlines the development process, 
            enhances code reusability, and provides a robust, flexible 
            foundation for building consistent, interactive, and modular 
            Streamlit applications.

            """
        ),
    ),
)

page_config = PageConfig(
    page_tag="Main Page",
    body=[title, st_congifurator_info],
)

PageRenderer().render_page(page_config)
