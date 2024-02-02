from pathlib import Path
import streamlit as st
from streamlit_chatbox import *
from loguru import logger


currentTab = "chatTab"
logname = "log.txt"


# different views selectable from sidebar
with st.sidebar:
    st.title("AI SME")
    st.button("Chat", key="chatTab")
    st.button("Chat History", key="chatHistoryTab")
    st.button("Options", key="optionsTab")
    # variable logging for debug purposes
    # st.write(st.session_state)
    # st.write(currentTab)


# basic logging code (need more in depth, duplicate logging issues, etc.)

# logger.add(logname)
# logger.debug("This is a debug message")
# st.write("Does the log file work? Last 10 lines")
# lines = "\n".join(Path(logname).read_text().splitlines()[-10:])
# st.code(lines)


def displayView():
    # contents of each view
    if currentTab == "chatTab":
        # simple chat box structure
        chat_box = ChatBox()
        chat_box.init_session()
        chat_box.output_messages()
        if query := st.chat_input("input your question here"):
            chat_box.user_say(query)
            chat_box.ai_say("you said: " + query)
    elif currentTab == "chatHistoryTab":
        st.write("This is the Chat History View")
    elif currentTab == "optionsTab":
        # tempurature slider (non functional)
        # (other options may be placed here)
        temperature = st.slider("Response Temperature", 0, 100, 50)


# view switching logic
if st.session_state.get("chatTab"):
    currentTab = "chatTab"
    displayView()
elif st.session_state.get("chatHistoryTab"):
    currentTab = "chatHistoryTab"
    displayView()
elif st.session_state.get("optionsTab"):
    currentTab = "optionsTab"
    displayView()
else:
    currentTab = "chatTab"
    displayView()
