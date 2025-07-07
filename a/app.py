import streamlit as st
import requests
import time
from datetime import datetime

API_URL = "http://localhost:8000/messages"
SEND_URL = "http://localhost:8000/send"

st.set_page_config(page_title="🗨️ Chat Space", layout="wide")
st.title("🗨️ Chat Space")

# Prompt for username
if "username" not in st.session_state:
    st.session_state.username = ""
    st.session_state.started = False

if not st.session_state.started:
    st.subheader("Enter your username to start chatting:")
    username_input = st.text_input("Username")
    if st.button("Start Chat"):
        if username_input.strip():
            st.session_state.username = username_input.strip()
            st.session_state.started = True
        else:
            st.warning("Username cannot be empty.")

if st.session_state.started:
    st.success(f"Welcome, {st.session_state.username}!")

    chat_container = st.empty()

    def fetch_messages():
        try:
            response = requests.get(API_URL)
            response.raise_for_status()
            messages_data = response.json()

            for msg in messages_data:
                timestamp_str = msg.get("timestamp", "")
                if timestamp_str:
                    try:
                        msg['timestamp'] = datetime.fromisoformat(timestamp_str)
                    except ValueError:
                        try:
                            msg['timestamp'] = datetime.strptime(timestamp_str.split('.')[0], "%Y-%m-%dT%H:%M:%S")
                        except ValueError:
                            msg['timestamp'] = datetime.min
                else:
                    msg['timestamp'] = datetime.min

            st.session_state.chat_messages = sorted(messages_data, key=lambda x: x.get('timestamp', datetime.min))
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the chat server. Make sure the FastAPI backend is running.")
            st.session_state.chat_messages = []
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching messages: {e}")
            st.session_state.chat_messages = []
        except Exception as e:
            st.error(f"An unexpected error occurred during message fetch: {e}")
            st.session_state.chat_messages = []

    def render_messages():
        messages = st.session_state.chat_messages
        with chat_container.container():
            for msg in messages:
                username = msg.get("username", "Unknown")
                message_text = msg.get("text", "")  # ✅ FIXED
                timestamp = msg.get("timestamp", "")

                if isinstance(timestamp, datetime):
                    display_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    display_time = "Time Unknown"

                if username == st.session_state.username:
                    st.markdown(
                        f"<div style='text-align: right; background-color: #e0f7fa; padding: 8px; border-radius: 10px; margin-bottom: 5px; margin-left: 20%;'>"
                        f"<b>You</b> ({display_time}): {message_text}"
                        f"</div>",
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"<div style='text-align: left; background-color: #f0f0f0; padding: 8px; border-radius: 10px; margin-bottom: 5px; margin-right: 20%;'>"
                        f"<b>{username}</b> ({display_time}): {message_text}"
                        f"</div>",
                        unsafe_allow_html=True
                    )

    fetch_messages()
    render_messages()
    time.sleep(2)

    message = st.text_input("Type your message:", key="message_input_area")
    if st.button("Send"):
        if message.strip():
            payload = {
                "username": st.session_state.username,
                "text": message.strip()  # ✅ FIXED
            }
            try:
                res = requests.post(SEND_URL, json=payload)
                if res.status_code == 200:
                    st.session_state.message_input_area = ""  # Clear input
                    st.rerun()
                else:
                    st.error(f"Message send failed. Server response: {res.status_code}")
            except requests.exceptions.RequestException as e:
                st.error(f"Failed to send message: {e}")
        else:
            st.warning("Message cannot be empty.")

    if st.button("Refresh Chat"):
        st.rerun()
