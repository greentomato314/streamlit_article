import streamlit as st
import collections
import datetime
import os

st.title('記事投稿')
tabs = st.tabs(['編集',"プレビュー"])

def flag1_true():
    st.session_state['flag1'] = True

def flag2_true():
    st.session_state['flag2'] = True
    st.session_state['flag1'] = False

if not ('flag1' in  st.session_state):st.session_state['flag1'] = False
if not ('flag2' in  st.session_state):st.session_state['flag2'] = False

if st.session_state["edit_ind"] >= 0:
    fname = st.session_state["fls"][st.session_state["edit_ind"]]
    info = fname.split('\\')[-1].split('_')
    st.session_state['title'] = info[0]
    st.session_state['name'] = info[1]
    st.session_state['password'] = info[2]
    with open(fname,'r') as f:
        a = f.read()
    st.session_state['text'] = a

if not ('title' in st.session_state):st.session_state['title'] = ''
if not ('text' in st.session_state):st.session_state['text'] = ''
if not ('name' in st.session_state):st.session_state['name'] = ''
if not ('password' in st.session_state):st.session_state['password'] = ''

with tabs[0]:
    st.session_state['title'] = st.text_input('タイトル',value=st.session_state['title']) 
    st.session_state['text'] = st.text_area('記事本文',value=st.session_state['text'])
    st.button('保存',on_click=flag1_true)
    if st.session_state['flag1']:
        cols = st.columns(2)
        with cols[0]:
            st.session_state['name'] = st.text_input('投稿者(更新者)名',value=st.session_state['name'])
        with cols[1]:
            st.session_state['password'] = st.text_input('パスワード',value=st.session_state['password'])
        st.write('＊_(アンダーバー)は使わないでください。')
        st.button('確定',on_click=flag2_true)
    if st.session_state['flag2']:
        if st.session_state["edit_ind"] >= 0:
            fname = st.session_state["fls"][st.session_state["edit_ind"]]
            os.remove(fname)
        dt_now = datetime.datetime.now()
        filename = st.session_state['title']+'_'+st.session_state['name']+'_'+st.session_state['password']+\
                   '_'+str(dt_now).split()[0]+'_'+str(dt_now).split()[1].split('.')[0].replace(':', '-')+'.txt'
        st.session_state['flag2'] = False
        with open(st.session_state['path']+filename, 'x') as f:
            f.write(st.session_state['text'])
        st.write('投稿されました')

with tabs[1]:
    st.write(st.session_state['text'],unsafe_allow_html=True)

