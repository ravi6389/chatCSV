import os
import streamlit as st
import pandas as pd

# from langchain_groq.chat_models import ChatGroq

from langchain_experimental.agents import create_pandas_dataframe_agent



from langchain_groq import ChatGroq
import ssl
context = ssl._create_unverified_context()

print("I am in chatcsv2")




llm = ChatGroq(temperature=0, groq_api_key=st.secrets['GROQ_API_KEY'], model_name="mixtral-8x7b-32768")





st.header('Analyze CSV file with Parchi - a GenAI tool for chatting with CSV')
st.subheader('Developed by Ravi Shankar Prasad - https://www.linkedin.com/in/ravi-shankar-prasad-371825101')

uploaded_file = st.file_uploader('Upload your CSV file')

if(uploaded_file):
    df = pd.read_csv(uploaded_file)

    st.write(df.head(3))

    prompt = st.text_input('Enter your prompt')

    if st.button('Generate'):
        if prompt:
            agent = create_pandas_dataframe_agent(llm = llm,df = df, allow_dangerous_code=True)
            
            with st.spinner("generating response..."):
                output = agent.invoke(prompt)
                st.write(output)


        else:
            st.warning("Please enter your prompt.")
