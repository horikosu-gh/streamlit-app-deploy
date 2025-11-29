import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("OpenAI チャットテスト")

message = st.text_input("メッセージを入力してください")

if st.button("送信"):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=message
    )
    st.write("### 回答")
    st.write(response.output_text)
