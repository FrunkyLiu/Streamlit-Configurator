# Streamlit Configurator

A **declarative** and **modular** approach to building Streamlit applications. **Streamlit Configurator** allows you to define UI components and layouts in a structured, reusable manner—eliminating repetitive Streamlit calls, improving maintainability, and enabling robust state management.

## Contents
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Basic Usage](#basic-usage)
- [Advanced Usage](#advanced-usage)
- [License](#license)
- [Contact & Contributing](#contact--contributing)


## Features
- **Declarative Layouts**: Use `ComponentConfig` and `PageConfig` to define pages in a more **descriptive** style—no need to manually chain together multiple Streamlit calls.
- **Robust State Management**: Utilize **placeholders** (`PlaceholderValue`) to seamlessly store and retrieve data across page refreshes or navigations.
- **Reusable Configurations**: Once you define a component or layout, you can reuse it across different pages, ensuring consistency and reducing code duplication.
- **Integration & Compatibility**: Works **alongside** native Streamlit calls. You can still write custom functions or direct Streamlit code where it makes sense.
- **Scalable Architecture**: As your app grows, define new placeholders or restructure layouts without rewriting large sections of code.


## Installation

### From PyPI (Upcoming / Planned)
We’re preparing to publish **Streamlit Configurator** on PyPI. Once available, you can simply install it with:
```bash
pip install st-configurator
```
(Stay tuned for the official release.)

### From Source (Current)
1. Clone or download this repository.
2. Navigate to the project’s root directory.
3. Install using pip:
    ```bash
    pip install .
    ```
4. Make sure Streamlit is installed:
    ```bash
    pip install streamlit
    ```

## Quick Start
Below is a minimal example showing how to set up a page with **Streamlit Configurator**.
    
```python
import streamlit as st
from st_configurator import ComponentConfig, PageConfig, PageRenderer
from st_configurator.placeholder import Placeholder, PlaceholderValue

# 1. Define a custom placeholder class to hold your state
class MyPlaceholder(Placeholder):
    NAME = PlaceholderValue(default="Guest")

# 2. Create a Streamlit component config (e.g., a text input)
name_input_config = ComponentConfig(
    component=st.text_input,
    args=("What's your name?",),
    kwargs={"value": MyPlaceholder.NAME},
    result_key=MyPlaceholder.NAME
)

# 3. Define a page config that includes this component
page_config = PageConfig(
    page_tag="HomePage",
    body=[name_input_config]
)

# 4. Render the page
PageRenderer().render_page(page_config)
```

1. Run your script with:
    ```bash
    streamlit run your_script.py
    ```
2. Interact with the text input, navigate to other pages (if any), and come back. Notice the placeholder value persists.

## Basic Usage

1. **Define Placeholders:** Inherit from **`Placeholder`** and declare **`PlaceholderValues`** for any data you need to persist.
2. **Create Components:** Use **`ComponentConfig`** to wrap any Streamlit callable (e.g., **`st.button`**, **`st.text_input`**). Pass placeholders or default values as **`args`** or **`kwargs`**, and capture outputs by assigning **`result_key`**.
3. **Assemble Pages:** Group components in a PageConfig. You can place some components in body and others in sidebar.
4. **Render:** Call **`PageRenderer().render_page(my_page_config)`** to display your page.

## Advanced Usage
- **Conditional Rendering:** Add a **`condition`** to any **`ComponentConfig`** to selectively display or hide it based on a placeholder’s boolean value (or the returned value of another component).
- **Nested Layouts:** Use **`children`** in a **`ComponentConfig`** for layout containers like **`st.columns`** or **`st.tabs`**.
- **Persistence:** If you need a placeholder to remain **locked** once it changes, set **`persist=True`**. The new value overrides the default permanently, ignoring subsequent resets.
- **Global Scope:** Set **`global_scope=True`** for placeholders that are shared across **all** pages.

## License
This project is licensed under the terms of the [LICENSE](LICENSE) file.

## Contact & Contributing
- Email: x77497856@gmail.com
- GitHub: https://github.com/FrunkyLiu/Streamlit-Configurator

Contributions, bug reports, and feature requests are welcome! Feel free to open an issue or submit a pull request. If you find this project useful, please consider giving a star ⭐ on GitHub to support its continued development.
