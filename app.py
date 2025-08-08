import streamlit as st
from todo.utils import load_tasks, save_tasks
from todo.constants import DATA_FILE, TITLE

# load tasks
tasks = load_tasks(DATA_FILE)

# title
st.title(TITLE)

# 추가
new_task = st.text_input("할 일을 입력하세요")
if st.button("추가") :
    tasks.append(new_task)
    save_tasks(DATA_FILE, tasks)
    st.rerun()

# 목록 & 삭제
st.subheader("현재 목록")
for idx, task in enumerate(tasks):
    col1, col2 = st.columns([0.85, 0.15])
    col1.write(f"- {task}")
    if col2.button("삭제", key=f"del_{idx}"):
        tasks.pop(idx)
        save_tasks(DATA_FILE, tasks)
        st.rerun()
