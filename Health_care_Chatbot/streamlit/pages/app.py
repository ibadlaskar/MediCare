import requests
import streamlit as st

# Initialize session state if not already initialized
if "chat_messages" not in st.session_state:
    st.session_state["chat_messages"] = []

# Define the function to display chat messages
def display_chat(chat_messages):
    # Display chat messages
    for sender, message in chat_messages:
        if sender == 'user':
            # Apply CSS styling for user response
            st.write(
                 f'<div style="display:flex; align-items:center; flex-direction:row-reverse; padding-top: 10px; padding-bottom: 10px;">'
                f'<div style="margin-right: 10px;  margin-top: 10px">'
                f'👤'  # User emoji
                f'</div>'
                f'<div style="background-color:#0f7511; padding:10px; border-radius:10px;">'
                f'{message}'
                f'</div>'
                f'</div>',
                unsafe_allow_html=True
            )
        else:
            # Apply CSS styling for bot response
            st.write(
                f'<div style="display:flex; align-items:center; padding-top: 10px; padding-bottom: 10px;">'
                f'<div style="margin-right: 10px;margin-top: 10px ">'
                f'🤖'  # Bot emoji
                f'</div>'
                f'<div style="background-color:#075E54; padding:10px; border-radius:10px;">'
                f'{message}'
                f'</div>'
                f'</div>',
                unsafe_allow_html=True
            )

# Main chatbot interface
def chat_interface(chat_messages):

    button_pressed = False

    BASE_URL ="http://127.0.0.1:8090/chat"

    user_input = st.text_input('Query')

    if st.button('Ask'):
        button_pressed = True
        st.write(
             f'<div style="display:flex; align-items:center; padding-top: 10px; padding-bottom: 10px;">'
            f'<div style="margin-right: 10px;">'
            f'🤖'  # Bot emoji
            f'</div>'
            f'<div style="background-color:#075E54; padding:10px; border-radius:10px;">'
            f'Hi There! How may I help you today?'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True
        )

        if user_input != "":
            try:
                response = requests.post(BASE_URL, json={'input': user_input})
                if response.ok:
                    bot_response = response.json()['response']
                    bot_score = float(response.json()['score'])
                    print(bot_score)
                    if bot_score > 0.72: 
                        # Add user message to chat messages list
                        chat_messages.append(('user', user_input))
                        chat_messages.append(('bot', bot_response))
                    else:
                        st.error("Please be more specific in the query!")

                    display_chat(chat_messages)
                else:
                    st.error(f"Failed to get response from the server. Status code: {response.status_code}")
            except requests.RequestException as e:
                st.error(f"HTTP request failed: {e}")

        else:
            st.error("Please enter a query!")
            display_chat(chat_messages)

    if button_pressed == False:
        st.write(
          f'<div style="display:flex; align-items:center; padding-top: 10px; padding-bottom: 10px;">'
            f'<div style="margin-right: 10px ;padding-top=10px">'
            f'🤖'  # Bot emoji
            f'</div>'
            f'<div style="background-color:#075E54; padding:10px; border-radius:10px;">'
            f'Hi There! How may I help you today?'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True
        )
    else:
        st.write("")

    st.write("")

    if st.button('Clear chat'):
        st.session_state["chat_messages"] = []

# Run the chat interface
if __name__ == '__main__':
    # Set Streamlit app title
    st.title("Your Medicare ChatBot")

    chat_interface(st.session_state["chat_messages"])
