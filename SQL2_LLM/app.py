#import packages 
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI

#load environment file 
load_dotenv()

#function to create SQL query and Text
def sqldb_txt(query):
    db = SQLDatabase.from_uri("sqlite:///Chinook.db")
    chain = create_sql_query_chain(ChatOpenAI(temperature=0), db)
    response = chain.invoke({"question":query})
    return response , db.run(response) 

#creating streamlit app
st.title("Query on Database")

#query entered 
query = st.text_area("Query your Data to Generate Graph", height=200)

#Perform transformation on button click
st.text("Note: After entering the query click Submit button.")
if st.button("Submit"):
    if query is not None:
        sql_query,result = sqldb_txt(query)
        st.write("SQL_query:")
        st.write(sql_query)
        st.write("Result:")
        st.write(result)
    else:
        st.warning("Enter query before submitting..")
    