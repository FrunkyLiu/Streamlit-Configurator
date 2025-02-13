import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

import textwrap

import streamlit as st
from share_component import description_template, title_template

from st_configurator import ComponentConfig, PageConfig, PageRenderer

title = title_template.update(
    args=("Placeholder API 📝",),
)

description_config = description_template.update(
    args=(
        textwrap.dedent(
            """
            **Overview:**
            Placeholders in **Streamlit-Configurator** store and retrieve state while providing:
            - **Default values**: Easily initialize your placeholders with a default.
            - **Persistence**: Preserve your placeholder's value during page refreshes or page switches.
            - **Global scoping**: Optionally share a placeholder across all pages.
            - **Value formatting**: Apply a custom **`format_fn`** to transform the stored value on retrieval.

            By default, placeholders automatically use the current page's **`page_tag`** 
            as a key prefix. This means you can reuse the same placeholder names on different pages without conflicting values.

            ---

            ### Placeholder
            
            - ##### **Description:**
            
                The **`Placeholder`** class (using a custom metaclass) automatically 
                converts its class-level attributes into **`PlaceholderValue`** objects. 
                It also provides helper methods for updating these attributes. 
                Essentially, any attribute you define at the class level 
                becomes a **stateful placeholder**.

            - #### **Key Methods:**

              - ##### ***update_param_placeholders(obj, obj_args, obj_kwargs, result_key) -> (List[Any], Dict[str, Any])***

                ###### Parameters:

                - **`obj`**: A callable component (e.g., **`st.button`**, **`st.text_input`**).
                - **`obj_args`**: A list of positional arguments (which may include **`PlaceholderValue`** objects).
                - **`obj_kwargs`**: A dictionary of keyword arguments (which may include **`PlaceholderValue`** objects).
                - **`result_key`** (optional): A **`PlaceholderValue`** to store the return value of `obj`.
                              
                ###### Return:
                  - A tuple `(new_args, new_kwargs)` where any `PlaceholderValue` in `obj_args` or `obj_kwargs` is replaced by its current value.  
                  > If `result_key` is provided, the return value of `obj` will be stored into `result_key`.

                
                ###### Example:
                ```python
                from st_configurator.placeholder import Placeholder, PlaceholderValue

                class MyPlaceholder(Placeholder):
                    VALUE = PlaceholderValue(default=10)

                # Suppose we have a component that takes one argument.
                def dummy_component(x):
                    return x

                # Replace PlaceholderValues with their current values before calling dummy_component.
                args, kwargs = MyPlaceholder.update_param_placeholders(
                    dummy_component,
                    (MyPlaceholder.VALUE,),
                    {}
                )
                result = dummy_component(*args, **kwargs)
                print("Resolved Value:", result)  # Expected: 10
                ```

              - #### ***set_attr(name, value) -> None***

                ###### Parameters:

                  - **`name`**: The attribute name to update or create.
                  - **`value`**: If this is not already a **`PlaceholderValue`**, it will be converted into one.
                
                ###### Return:
                  - **`None`**.  Dynamically updates the placeholder on the **`Placeholder`** class.

                ###### Example:
                ```python
                from st_configurator.placeholder import Placeholder, PlaceholderValue

                class MyPlaceholder(Placeholder):
                    NUMBER = PlaceholderValue(default=10)

                # Update the NUMBER placeholder to a new value.
                MyPlaceholder.set_attr("NUMBER", 20)
                print("Updated NUMBER:", MyPlaceholder.NUMBER.get())  # Should print 20
                ```

            ---

            ### PlaceholderValue
            
            - ##### **Description:**
            
                A **`PlaceholderValue`** is a single state container with additional 
                configuration options. It stores its value in Streamlit's session 
                state under an automatically generated key (by default, **`<page_tag>_<name>`**). 
                If **`global_scope=True`**, the key becomes **`_GLOBAL_<name>`** instead, 
                making it accessible across pages.

            - #### **Key Methods:**

              - ##### ***\_\_init\_\_(self, default=None, persist=False, name=None, global_scope=False, format_fn=None)***

                ###### Parameters:

                  - **`default`**: The initial default value (default: **`None`**).
                  - **`persist`**: If **`True`**, once the placeholder value changes from its initial default, 
                      that new value becomes locked and persists for all subsequent calls. 
                      In other words, any attempt to overwrite the value again will be 
                      ignored—once changed, it stays at the updated value.
                  - **`name`**: An optional custom name. If not specified, the class attribute name is used.
                  - **`global_scope`**: If **`True`**, uses a global key prefix (**`_GLOBAL`**) so the placeholder is the same on all pages (default: **`False`**).
                  - **`format_fn`**: An optional function that transforms the stored value on retrieval.
                
              - #### ***\_\_call\_\_(self, default=None, persist=False, global_scope=False, format_fn=None) -> PlaceholderValue***

                ###### Parameters:
                  - Identical parameters to **`__init__`**. 
                  
                ###### Return:
                  - **Returns** the same **`PlaceholderValue`** instance, allowing you to 
                  update properties (like **`persist`**, **`format_fn`** etc.) after it has been defined.
    
                  
              - #### ***set(self, value, \*, key=None) -> None***
                ###### Parameters:

                  - **`value`**: The new value to store.
                  - **`key`**(optional): Override the default storage key if needed.
                  
                ###### Return:
                  - **Updates** the session state. No return value.

              - #### ***get(self, \*, key=None) -> Any***
                ###### Parameters:

                  - **`key`**(optional): If provided, overrides the default storage key.
                  
                ###### Return:
                  - **Returns** the current stored value. If format_fn is defined, it returns the transformed value.

              - #### ***set_streamlit_key(self, key) -> None***
                ###### Parameters:

                  - **`key`**: The new key to override the default.
                  
                ###### Return:
                  - **Updates** the internal reference so future calls also store or retrieve using this Streamlit session key.

            ##### Example:
            ```python
            from st_configurator.placeholder import PlaceholderValue

            # A placeholder for a counter with default=0, shared across all pages.
            counter = PlaceholderValue(default=0, global_scope=True)
            counter.set(5)
            print("Counter:", counter.get())  # Output: 5
            ```

            ---

            ### Important Notes
            1. **Key Prefixes and Page Isolation**

              By default, a placeholder's key is prefixed with the current 
              page's **`page_tag`**, making the same placeholder name reusable on 
              different pages without interference. If **`global_scope=True`**, the 
              placeholder uses a **`_GLOBAL_`** prefix, making it accessible everywhere.

            2. **Multiple Placeholder Classes**

              If you define multiple **`Placeholder`** classes with the same attribute 
              name on the **same page**, they may resolve to the same underlying 
              session key (unless one uses **`global_scope`** and the other doesn't, 
              resulting in different key prefixes).
              ```python
              class MyPlaceholder(Placeholder):
                  VALUE = PlaceholderValue()

              class MyPlaceholder2(Placeholder):
                  VALUE = PlaceholderValue()
              ```
              On a single page, **`MyPlaceholder.VALUE.get()`** and **`MyPlaceholder2.VALUE.get() `**
              will often refer to the same stored value (i.e., **`<page_tag>_VALUE)`**, 
              unless you explicitly manage different keys. It is recommended to 
              define a single **`Placeholder`** class with unique attribute names to 
              avoid confusion.

            3. **Modifying Placeholder Configurations Globally**

              Because attributes in a **`Placeholder`** class are at the class level, 
              changing any placeholder's configuration (e.g., calling **`MyPlaceholder.VALUE(persist=True)) `**
              affects all references to that placeholder attribute throughout 
              your code. Be cautious when updating placeholder settings, especially 
              if the same placeholder is used in multiple locations.
              
              Example, if you set:
              ```python
              MyPlaceholder.VALUE = PlaceholderValue(default=0)
              ```
              and later call:
              ```python
              MyPlaceholder.VALUE(global_scope=True)
              ```
              the previous default value (**`0`**) will be overridden (resulting in 
              the default becoming **`None`** if not explicitly set again). Be 
              cautious when updating placeholder settings, as they affect 
              **all references** to that attribute globally.

              A correct way to update the global scope and keep default value would be:
              ```python
              MyPlaceholder.VALUE(default=0, global_scope=True)
              ```
            """
        ),
        True,
    ),
)

page_config = PageConfig(
    page_tag="Main Page",
    body=[title, description_config],
)

PageRenderer().render_page(page_config)