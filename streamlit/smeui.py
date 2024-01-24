import streamlit as st

st.title('Mars Engenuity Subject Matter Expert')

chatTab, chatHistoryTab = st.tabs(["Chat", "Chat History"])

# main view with text-message style display of current model conversation.
with chatTab:
    # temp code from copied example

    st.write('This is the chat view.')
    # st.header("A cat")
    # t.image("", width=200)

# view of previous, possibly continuable chats (stretch goal)
with chatHistoryTab:
    # temp code from copied example
    
    st.write('This is the chat history view.')
    # st.header("A dog")
    # st.image("", width=200)

# playing with button functionality (learning as I go, this is the first commit)

# st.button("Reset", type="primary")
# if st.button('Say hello'):
#     st.write('Why hello there')
# else:
#     st.write('Goodbye')