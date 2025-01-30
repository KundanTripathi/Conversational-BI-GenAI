#import packages 
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_openai import OpenAI

#load environment file 
load_dotenv()

#function to create SQL query and Text
def sqldb_txt(query):
    db = SQLDatabase.from_uri("sqlite:///Chinook.db")
    llm = OpenAI(temperature=0, verbose=True)
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
    return db_chain.run(query)

#creating streamlit app
st.title("Query on Database")

#query entered 
query = st.text_area("Query your Data to Generate Graph", height=200)

#Perform transformation on button click
st.text("Note: After entering the query click Submit button.")
if st.button("Submit"):
    if query is not None:
        result = sqldb_txt(query)
        st.write("Result:")
        st.write(result)
    else:
        st.warning("Enter query before submitting..")
    