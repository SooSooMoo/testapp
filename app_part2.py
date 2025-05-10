# app.py（修正版）
import streamlit as st
from openai import OpenAI

st.title("エージェントAIチャット")

api_key = st.text_input("OpenAI APIキーを入力してください（外部に保存されません）", type="password")

if api_key:
    client = OpenAI(api_key=api_key)

    user_input = st.text_input("あなたのメッセージを入力してください")

    if st.button("送信") and user_input:
        with st.spinner("考え中..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": user_input}]
                )
                st.markdown("**AIの返答:**")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"エラー: {e}")
