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

title = title_template.update(
    args=("🔄 Flexible Integration & Compatibility",),
)

description_config = description_template.update(
    args=(
        textwrap.dedent(
            """
            ### Overview
            While **Streamlit Configurator** provides a powerful declarative 
            framework, it can sometimes feel overly verbose—especially for 
            straightforward apps or prototypes. To balance **robust state 
            management** with a more **native Streamlit** coding style, you 
            can integrate **custom functions** alongside placeholders. This 
            duality lets you choose between a **fully declarative** or 
            **hybrid** approach, depending on the complexity of your project.

            ---

            ### Example 1: Full Declarative Approach
            A purely declarative method means defining every component with `ComponentConfig` and using `PlaceholderValue` for all state:
            ```python
            import streamlit as st
            from st_configurator import ComponentConfig, PageConfig, PageRenderer
            from st_configurator.placeholder import Placeholder, PlaceholderValue

            # 1. Declare placeholders for each piece of state.
            class MyPlaceholder(Placeholder):
                CHAT_INPUT = PlaceholderValue()
                ECHO_RESPONSE = PlaceholderValue()
                HISTORY_MESSAGES = PlaceholderValue(default=[])

            # 2. Define helper functions.
            def keep_messages_history(role: str, content: str, history_messages):
                history_messages.append({"role": role, "content": content})
                return history_messages

            def display_messages(messages):
                for message in messages:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])

            def echo_response(prompt: str):
                return f"Echo: {prompt}"

            # 3. Build each step of the chatbot logic as a ComponentConfig.
            save_user_message = ComponentConfig(
                condition=MyPlaceholder.CHAT_INPUT,
                component=keep_messages_history,
                args=("user", MyPlaceholder.CHAT_INPUT, MyPlaceholder.HISTORY_MESSAGES),
                result_key=MyPlaceholder.HISTORY_MESSAGES,
            )

            save_assistant_message = ComponentConfig(
                condition=MyPlaceholder.CHAT_INPUT,
                component=keep_messages_history,
                args=("assistant", MyPlaceholder.ECHO_RESPONSE, MyPlaceholder.HISTORY_MESSAGES),
                result_key=MyPlaceholder.HISTORY_MESSAGES,
            )

            display_messages_config = ComponentConfig(
                component=display_messages,
                args=(MyPlaceholder.HISTORY_MESSAGES,),
            )

            chat_input_config = ComponentConfig(
                component=st.chat_input,
                args=("What is up?",),
                result_key=MyPlaceholder.CHAT_INPUT,
            )

            get_echo_response_config = ComponentConfig(
                condition=MyPlaceholder.CHAT_INPUT,
                component=echo_response,
                args=(MyPlaceholder.CHAT_INPUT,),
                result_key=MyPlaceholder.ECHO_RESPONSE,
            )

            # 4. Group configurations into a container and render.
            message_panel = ComponentConfig(
                component=st.container,
                kwargs={"height": 450},
                children=[
                    save_user_message,
                    save_assistant_message,
                    display_messages_config,
                    get_echo_response_config,
                ],
            )

            page = PageConfig(
                page_tag="Chatbot",
                body=[message_panel, chat_input_config],
            )

            PageRenderer().render_page(page)
            ```
            ##### Why Choose Declarative?
            - Complete control over every component's input and output through placeholders.
            - Seamless state sharing across pages thanks to the underlying placeholder system.
            
            ---

            ### Example 2: Custom Function Integration
            Here, you encapsulate the chatbot logic in a custom function, 
            while still leveraging placeholders for persistent state:
            ```python
            import streamlit as st
            from st_configurator import ComponentConfig, PageConfig, PageRenderer
            from st_configurator.placeholder import Placeholder, PlaceholderValue

            # 1. Placeholders manage just the critical parts (chat input and chat history).
            class MyPlaceholder(Placeholder):
                CHAT_INPUT = PlaceholderValue()
                HISTORY_MESSAGES = PlaceholderValue(default=[])

            def echo_chatbot(chat_input, history_messages):
                with st.container(height=450):
                    if chat_input:
                        history_messages.append({"role": "user", "content": chat_input})
                        history_messages.append({"role": "assistant", "content": "Echo: " + chat_input})
                        for message in history_messages:
                            with st.chat_message(message["role"]):
                                st.markdown(message["content"])
                return history_messages

            # 2. Configure the components:
            chat_input_config = ComponentConfig(
                component=st.chat_input,
                args=("What is up?",),
                result_key=MyPlaceholder.CHAT_INPUT,
            )

            chatbot_config = ComponentConfig(
                component=echo_chatbot,
                args=(MyPlaceholder.CHAT_INPUT, MyPlaceholder.HISTORY_MESSAGES),
                result_key=MyPlaceholder.HISTORY_MESSAGES,
            )

            # 3. Define the page layout.
            page = PageConfig(
                page_tag="Chatbot",
                body=[chatbot_config, chat_input_config],
            )

            PageRenderer().render_page(page)
            ```
            ##### Why Choose a Custom Function?
            - Code reads closer to **native Streamlit**.
            - Still benefits from **placeholder-based** persistence, preventing data loss when switching pages.
            - Lets you selectively apply **`st_configurator`** features 
            without overcomplicating simpler code sections.
            """
        ),
    )
)


class MyPlaceholder(Placeholder):
    CHAT_INPUT = PlaceholderValue()
    HISTORY_MESSAGES = PlaceholderValue(default=[])


def echo_chatbot(chat_input, history_messages):
    with st.container(height=450):
        if chat_input:
            history_messages.append({"role": "user", "content": chat_input})
            history_messages.append(
                {"role": "assistant", "content": "Echo: " + chat_input}
            )
            for message in history_messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

    return history_messages


chat_input_config = ComponentConfig(
    component=st.chat_input,
    args=("What is up?",),
    result_key=MyPlaceholder.CHAT_INPUT,
)

chatbot_config = ComponentConfig(
    component=echo_chatbot,
    args=(
        MyPlaceholder.CHAT_INPUT,
        MyPlaceholder.HISTORY_MESSAGES,
    ),
    result_key=MyPlaceholder.HISTORY_MESSAGES,
)


second_description_config = description_template.update(
    args=(
        textwrap.dedent(
            """
            ***
            ### Key Benefits

            - **Flexibility:**

                You can combine declarative and imperative patterns as needed.

            - **Maintainability:**
            
                Custom functions can keep your code more concise or more 
                familiar if you're used to traditional Streamlit.
        
            - **State Persistence:**

                Regardless of your chosen style, placeholders ensure 
                consistent data across page navigation.
                
            Ultimately, you can adopt the style that best aligns with your 
            **project size**, team skill set, and development preferences 
            without sacrificing the advantages of st_configurator's 
            placeholder-based state management.
            """
        ),
    ),
)


page_config = PageConfig(
    page_tag="Flexible Integration & Compatibility",
    body=[
        title,
        description_config,
        show_demo_template.update(
            children=[chatbot_config, chat_input_config]
        ),
        second_description_config,
    ],
)

PageRenderer().render_page(page_config)
