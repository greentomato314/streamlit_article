import streamlit as st
import collections
import datetime
import glob

st.title('記事')
st.session_state['path'] = "doc\\"
tabs = st.tabs(['一覧','内容'])
st.session_state["fls"] = glob.glob(st.session_state['path']+'*')

def show_f():
    st.session_state["showf"] = [False]*(len(st.session_state["fls"]))
    for i in range(len(st.session_state["showf"])):
        st.session_state["showf"][i] = st.session_state[i]
    st.session_state["editf"] = False
def edit_f():
    st.session_state["editf"] = True

if not("showf" in st.session_state):st.session_state["showf"] = [False]*(len(st.session_state["fls"]))
if not("editf" in st.session_state):st.session_state["editf"] = False
if not("edit_ind" in st.session_state):st.session_state["edit_ind"] = -1

with tabs[0]:
    for i,fname in enumerate(st.session_state["fls"]):
        name = fname.split('\\')[-1].split('_')
        tit = name[0]
        na = name[1]
        date = name[3]
        st.write('<font size="6">{}. {} </font>'.format(i+1,tit),unsafe_allow_html=True)
        cols = st.columns(2)
        with cols[0]:
            st.write('<font size="3">投稿者:{}  更新日:{}</font>'.format(na,date),unsafe_allow_html=True)
        with cols[1]:
            st.button('表示',key=i,on_click=show_f)
        with open(fname,'r') as f:
            a = f.read()
        st.text(a[:50])

with tabs[1]:
    if True in st.session_state["showf"]:
        st.button('編集',on_click=edit_f)
        ind = st.session_state["showf"].index(True)
        f = st.session_state["fls"][ind]
        if st.session_state["editf"]:
            pw = f.split('\\')[-1].split('_')[2]
            inputpw = st.text_input('password')
            if pw == inputpw:
                st.write('パスワードOK. postページにて編集可')
                st.session_state["edit_ind"] = ind
            else:
                st.write('パスワードが違います。')
                st.session_state["edit_ind"] = -1
        with open(f,'r') as f:
            a = f.read()
        st.write(a,unsafe_allow_html=True)
