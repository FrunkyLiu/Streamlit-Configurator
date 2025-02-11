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
            Placeholders in Streamlit-Configurator store and retrieve state while 
            providing features like default values, persistence, global scoping, and value formatting. 
            They also automatically use the current page's page_tag as a key prefix, 
            ensuring that the same placeholder names can be used across different pages without value conflicts.

            ***
            ### Placeholder
            
            - ##### **Description:**
            
                The `Placeholder` class (with its metaclass) automatically converts 
                class attributes into `PlaceholderValue` objects and provides utility methods for updating them.

            - #### **Key Methods:**

              - ##### ***update_param_placeholders(cls, obj, obj_args, obj_kwargs, result_key) -> Tuple[List[Any], Dict[str, Any]]***

                ###### Parameters:

                  - **`obj`**: The callable component whose parameters are being processed.
                  - **`obj_args`**: A list of positional arguments (may include ***`PlaceholderValue`*** objects).
                  - **`obj_kwargs`**: A dictionary of keyword arguments (may include ***`PlaceholderValue`*** objects).
                  - **`result_key`**: Optional; a ***`PlaceholderValue`*** to capture the component's output. 
                
                ###### Return:
                  - A tuple `(new_args, new_kwargs)` with all `PlaceholderValue` objects replaced by their actual values.
                
                ###### Example:
                ```python
                from st_configurator.placeholder import Placeholder, PlaceholderValue

                class MyPlaceholder(Placeholder):
                    VALUE = PlaceholderValue(default=10)

                # Suppose we have a component that accepts one argument.
                def dummy_component(x):
                    return x

                # Before calling dummy_component, update parameters:
                args, kwargs = MyPlaceholder.update_param_placeholders(dummy_component, (MyPlaceholder.VALUE,), {})
                print(args)  # This will print the resolved value, e.g. [10]
                ```

              - #### ***set_attr(cls, name, value) -> None***

                ###### Parameters:

                  - **`name`**: The attribute name to set.
                  - **`value`**: The value to assign (if not a PlaceholderValue, it is converted). 
                
                ###### Return:
                  - **`None`**. Dynamically updates the placeholder attribute.

                ###### Example:
                ```python
                from st_configurator.placeholder import Placeholder, PlaceholderValue

                class MyPlaceholder(Placeholder):
                    NUMBER = PlaceholderValue(default=10)

                # Update VALUE using set_attr.
                MyPlaceholder.set_attr("VALUE", 20)
                print("Updated VALUE:", MyPlaceholder.VALUE.get())  # Should print 20
                ```

            ***
            ### PlaceholderValue
            
            - ##### **Description:**
            
                Represents a single state-holding object with additional configuration settings.

            - #### **Key Methods:**

              - ##### ***\_\_init\_\_(self, default=None, persist=False, name=None, global_scope=False, format_fn: Optional[Callable] = None)***

                ###### Parameters:

                  - **`default`**: The initial default value (default: None).
                  - **`persist`**: A boolean indicating if the value should persist across page switches (default: False).
                  - **`name`**: Optional custom name. 
                  
                    A unique key is generated by combining the current page's 
                    ***`page_tag`*** with this ***`name`***. If not provided, the attribute 
                    name (e.g., ***`VALUE`*** in ***`class MyPlaceholder(Placeholder): 
                    VALUE = PlaceholderValue()`***) is used automatically.

                  - **`global_scope`**: If True, the placeholder is accessible across all pages (default: False).
                  - **`format_fn`**: Optional function to format the value when retrieved. 
                
              - #### ***\_\_call\_\_(self, default=None, persist=False, global_scope=False, format_fn: Optional[Callable] = None) -> PlaceholderValue***

                ###### Parameters:
                  - Same as \_\_init\_\_. 
                  
                ###### Return:
                  - Returns the same `PlaceholderValue` instance after updating its settings.
    
                  
              - #### ***set(self, value, \*, key=None) -> None***
                ###### Parameters:

                  - **`value`**: The new value to store.
                  - **`key`**:  Optional key to override the default storage key
                  
                ###### Return:
                  - **`None`**. Updates the value in session state.

              - #### ***get(self, \*, key=None) -> Any***
                ###### Parameters:

                  - **`key`**:  Optional key to override the default storage key
                  
                ###### Return:
                  - The current value (formatted if format_fn is provided).

              - #### ***set_streamlit_key(self, key) -> None***
                ###### Parameters:

                  - **`key`**:  The key to override the default storage key.
                  
                ###### Return:
                  - **`None`**.

            #### Example:
            ```python
            from st_configurator.placeholder import PlaceholderValue

            # Create a placeholder for a counter with a default of 0.
            counter = PlaceholderValue(default=0, global_scope=True)
            counter.set(5)
            print("Counter:", counter.get())  # Output: 5
            ```
            ***
            """
        ),
        True,
    ),
)

note_config = ComponentConfig(
    component=st.info,
    args=(
        textwrap.dedent(
            """
            ##### Note:
            Placeholders use the current page's ***`page_tag`*** as a key prefix. 
            This allows the same placeholder name to be reused across 
            different pages without interfering with each other. 
            However, if you define multiple Placeholder classes with the same 
            attribute name (e.g., ***`MyPlaceholder.VALUE`*** and ***`MyPlaceholder2.VALUE`***)
            , they will resolve to the same underlying value on the same page 
            (i.e. ***`MyPlaceholder.VALUE.get() == MyPlaceholder2.VALUE.get()`***). 
            Therefore, it is recommended to consolidate your placeholders into 
            a single class to avoid confusion.
            """
        ),
    ),
)

note_class_config = ComponentConfig(
    component=st.info,
    args=(
        textwrap.dedent(
            """
            ##### Note:
            Because the attributes in a ***`Placeholder`*** class are defined at the 
            class level, any call to update a placeholder—using the ***`__call__`***
            method—applies globally. That is, if you set:
            ```python
            MyPlaceholder.VALUE = PlaceholderValue(default=0)
            ```
            and later call:
            ```python
            MyPlaceholder.VALUE(global_scope=True)
            ```
            the previous default value (***`0`***) will be overridden (resulting in 
            the default becoming ***`None`*** if not explicitly set again). Be 
            cautious when updating placeholder settings, as they affect 
            all references to that attribute globally.
            """
        ),
    ),
)


page_config = PageConfig(
    page_tag="Main Page",
    body=[title, description_config, note_config, note_class_config],
)

PageRenderer().render_page(page_config)
