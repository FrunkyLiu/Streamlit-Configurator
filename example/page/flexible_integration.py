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
            Streamlit-Configurator offers a powerful declarative framework using 
            placeholders and component configurations. However, building everything 
            exclusively with `st_configurator` can sometimes feel verbose and 
            counterintuitive compared to native Streamlit usage. In contrast, 
            you can integrate custom functions for a more familiar coding style 
            while still enjoying robust state management.

            
            Below are two examples that demonstrate these approaches for building a simple echo chatbot.
            ***
            #### Example 1: Full Declarative Approach Using `st_configurator`
            In this approach, every component is built using st_configurator constructs 
            and placeholders. This method ensures robust state persistence but 
            may feel more complex for simple use cases.
            ```python
            import streamlit as st
            from st_configurator import ComponentConfig, PageConfig, PageRenderer
            from st_configurator.placeholder import Placeholder, PlaceholderValue

            # Define placeholders with optional default values.
            class MyPlaceholder(Placeholder):
                # Placeholder for capturing chat input.
                CHAT_INPUT = PlaceholderValue()
                # Placeholder for storing the echo response.
                ECHO_RESPONSE = PlaceholderValue()
                # Placeholder for accumulating chat history.
                HISTORY_MESSAGES = PlaceholderValue()

            # Function to add a new message to the chat history.
            def keep_messages_history(role: str, content: str, history_messages):
                message = {"role": role, "content": content}
                history_messages.append(message)
                return history_messages

            # Function to display the chat history.
            def display_messages(messages):
                for message in messages:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])

            # Function to generate an echo response based on user input.
            def echo_response(prompt: str):
                response = f"Echo: {prompt}"
                return response

            # ComponentConfig to save the user's message into the history.
            save_user_message = ComponentConfig(
                condition=MyPlaceholder.CHAT_INPUT,
                component=keep_messages_history,
                args=("user", MyPlaceholder.CHAT_INPUT, MyPlaceholder.HISTORY_MESSAGES(default=[])),
                result_key=MyPlaceholder.HISTORY_MESSAGES,
            )

            # ComponentConfig to save the assistant's (echo) message into the history.
            save_assistant_message = ComponentConfig(
                condition=MyPlaceholder.CHAT_INPUT,
                component=keep_messages_history,
                args=("assistant", MyPlaceholder.ECHO_RESPONSE,
                result_key=MyPlaceholder.HISTORY_MESSAGES,
            )

            # ComponentConfig to display all messages from the history.
            display_messages_config = ComponentConfig(
                component=display_messages,
                args=(MyPlaceholder.HISTORY_MESSAGES,),
            )

            # ComponentConfig for the chat input field.
            chat_input_config = ComponentConfig(
                component=st.chat_input,
                args=("What is up?",),
                result_key=MyPlaceholder.CHAT_INPUT,
            )

            # ComponentConfig to generate an echo response from the user's input.
            get_echo_response_config = ComponentConfig(
                condition=MyPlaceholder.CHAT_INPUT,
                component=echo_response,
                args=(MyPlaceholder.CHAT_INPUT,),
                result_key=MyPlaceholder.ECHO_RESPONSE,
            )

            # Combine components into a container panel that displays the chat history and handles responses.
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

            # Define the overall chat layout: message panel and input field.
            chat_layout = [
                message_panel,
                chat_input_config,
            ]

            # Configure the page using the chat layout.
            page = PageConfig(
                page_tag="Chatbot",
                sidebar=[],
                body=[show_demo_template.update(children=chat_layout)],
            )

            # Render the page.
            PageRenderer().render_page(page)
            ```
            ##### Takeaway for Example 1:
            Using st_configurator exclusively—with placeholders handling both 
            initial values and output capture—ensures robust state management 
            across page switches. However, for simple applications like a 
            chatbot, this method can become overly complex.

            ***

            #### Example 2: Custom Function Integration for Native Compatibility
            In this alternative approach, a custom function encapsulates the 
            chatbot logic. This allows you to write code in a style closer to 
            native Streamlit while still leveraging placeholders for state management.
            ```python
            import streamlit as st
            from st_configurator import ComponentConfig, PageConfig, PageRenderer
            from st_configurator.placeholder import Placeholder, PlaceholderValue

            # Define placeholders with defaults.
            class MyPlaceholder(Placeholder):
                # Placeholder for capturing chat input.
                CHAT_INPUT = PlaceholderValue()
                # Placeholder for storing chat history; default is an empty list.
                HISTORY_MESSAGES = PlaceholderValue(default=[])

            # Custom function to handle chatbot behavior.
            def echo_chatbot(chat_input, history_messages):
                with st.container(height=450):
                    if chat_input:
                        # Append the user's message.
                        history_messages.append({"role": "user", "content": chat_input})
                        # Append the assistant's echo response.
                        history_messages.append({"role": "assistant", "content": "Echo: " + chat_input})
                        # Display each message in the history.
                        for message in history_messages:
                            with st.chat_message(message["role"]):
                                st.markdown(message["content"])
                # Return the updated history.
                return history_messages

            # ComponentConfig for the chat input field.
            chat_input_config = ComponentConfig(
                component=st.chat_input,
                args=("What is up?",),  # Prompt text.
                result_key=MyPlaceholder.CHAT_INPUT,  # Store input in placeholder.
            )

            # ComponentConfig that calls the custom chatbot function.
            chatbot_config = ComponentConfig(
                component=echo_chatbot,
                args=(MyPlaceholder.CHAT_INPUT, MyPlaceholder.HISTORY_MESSAGES),
                result_key=MyPlaceholder.HISTORY_MESSAGES,  # Update chat history.
            )

            # Configure the page layout using the custom function approach.
            page = PageConfig(
                page_tag="Chatbot",
                sidebar=[],  # No sidebar.
                body=[show_demo_template.update(children=[chatbot_config, chat_input_config])],
            )

            # Render the page.
            PageRenderer().render_page(page)
            ```
            ##### Takeaway for Example 2:
            By encapsulating the chatbot logic in a custom function, you maintain 
            a coding style closer to native Streamlit usage. This approach simplifies 
            development while still benefiting from st_configurator's robust 
            state management through placeholders.
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
            ### Key Benefits of These Approaches

            - **Flexibility:**

                The full declarative approach offers a complete, modular configuration 
                but can be verbose. The custom function approach provides compatibility 
                with traditional coding patterns without sacrificing state management benefits.

            - **Choose What Fits:**
            
                Depending on your project’s complexity and your preference for 
                declarative versus imperative styles, you can opt for a fully 
                configurator-based solution or integrate custom functions for 
                a more intuitive development experience.
            """
        ),
    ),
)


page_config = PageConfig(
    page_tag="Flexible Integration & Compatibility",
    body=[
        title,
        description_config,
        show_demo_template.update(children=[chatbot_config, chat_input_config]),
        second_description_config
    ],
)

PageRenderer().render_page(page_config)