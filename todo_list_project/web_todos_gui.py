import streamlit as st

from functions import get_read_todos

todos_list = get_read_todos()

st.title('My todo app')
st.subheader('This is my todolist project')
st.write('This app will increase your productivity')

for todo_item in todos_list:
    st.checkbox(todo_item)

st.text_input(label='', placeholder='Add your todo...')

# print('Hello')