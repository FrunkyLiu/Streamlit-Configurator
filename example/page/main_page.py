import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

import textwrap

import streamlit as st
from share_component import description_template, title_template

from st_configurator import ComponentConfig, PageConfig, PageRenderer

title = title_template.update(
    args=(":page_with_curl: Streamlit Configurator",),
)

st_congifurator_info = description_template.update(
    args=(
        textwrap.dedent(
            """
            Streamlit Configurator provides a structured approach to building modular and reusable Streamlit components. By defining a template once, you can effortlessly replicate the same layout across multiple pages, reducing redundant code and enhancing maintainability.

            
            **Key Benefits:**

            
             - **Reusable Components🔄**:
            > Each instance of `ComponentConfig` can be reused throughout your application, making it easy to maintain a consistent layout and behavior across different pages.

             - **Flexible Parameter Passing🔗**:
            > The built-in Placeholder mechanism allows you to pass parameters seamlessly between components. This means you can share data (such as user inputs or computed values) across different parts of your configuration without worrying about data inconsistencies.

             - **Robust Against Streamlit Updates🕹️**:
            > By leveraging the Placeholder mechanism, Streamlit Configurator minimizes the risk of errors that may arise from changes in Streamlit’s update process. This helps ensure that your application reads and manages values correctly, even as underlying components evolve.

            Overall, Streamlit Configurator streamlines the development process, enhances code reusability, and provides a robust foundation for building consistent, interactive, and modular Streamlit applications.


            """
        ),
    ),
)

page_config = PageConfig(
    page_tag="Main Page",
    body=[title, st_congifurator_info],
)

PageRenderer().render_page(page_config)