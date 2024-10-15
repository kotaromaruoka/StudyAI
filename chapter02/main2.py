# Github: https://github.com/naotaka1128/llm_app_codes/chapter02/main.py
import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pathlib import Path

###### dotenv を利用しない場合は消してください ######
try:
    from dotenv import load_dotenv
    env_path = Path('..') / '.env'
    load_dotenv(dotenv_path=env_path)
except ImportError:
    import warnings
    warnings.warn("dotenv not found. Please make sure to set your environment variables manually.",
ImportWarning)
################################################

def main():
    st.set_page_config(
        page_title="Title: My Great ChatGPT",
        page_icon="✒️"
    )
    st.header("My Great ChatGPT 🤗")

    if "message_history" not in st.session_state:
        st.session_state.message_history = [
            ("system", "You are a helpful assistant.") #<-AIのキャラクター設定
        ]
    
    if user_input := st.chat_input("聞きたいことを入力してね？"):
        # 何か入力されればここが実行される
        with st.spinner("ChatGPT is typing..."):
            
            #何か入力されてSubmitボタンが押されたら実行される
            print('test')
            llm = ChatOpenAI(temperature=0)
            prompt = ChatPromptTemplate.from_messages([
                *st.session_state.message_history,
                ("user","{input}")
            ])
            output_parser = StrOutputParser()
            chain = prompt | llm | output_parser
            response = chain.invoke({"input": user_input})

        st.session_state.message_history.append(("user",user_input))
        st.session_state.message_history.append(("ai",response))
    for role,message in st.session_state.get("message_history",[]):
        st.chat_message(role).markdown(message)
        
    
if __name__ == '__main__':
    main()
    

