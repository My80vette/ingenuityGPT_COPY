import streamlit as st

st.title('Mars Ingenuity SME')

chatTab, chatHistoryTab = st.tabs(["Chat", "Chat History"])

# main view with text-message style display of current model conversation.
with chatTab:
    messageCol, sendCol = st.columns([6, 1])
    with messageCol:
        st.text_area('', key='message')
    with sendCol:
        st.button('Send', key='send')
    if st.session_state.get('send'):
        st.write(st.session_state['message'])
            
        

# view of previous, possibly continuable chats (stretch goal)
with chatHistoryTab:
    st.write('This is the chat history view.')

    # if st.session_state.get('clear'):
    #     st.session_state['name'] = ''
    # if st.session_state.get('streamlit'):
    #     st.session_state['name'] = 'Streamlit'

    # st.text_input('Name', key='name')

    # st.button('Clear name', key='clear')
    # st.button('Streamlit!', key='streamlit')

