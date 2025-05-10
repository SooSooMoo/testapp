# app.py
import streamlit as st
import openai

st.title("エージェントAIチャット")

api_key = st.text_input("OpenAI APIキーを入力してください（外部に保存されません）", type="password")

if api_key:
    openai.api_key = api_key
    user_input = st.text_input("あなたのメッセージを入力してください")

    if st.button("送信") and user_input:
        with st.spinner("考え中..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": user_input}]
                )
                st.markdown("**AIの返答:**")
                st.write(response["choices"][0]["message"]["content"])
            except Exception as e:
                st.error(f"エラー: {e}")
