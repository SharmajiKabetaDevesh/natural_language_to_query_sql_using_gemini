from dotenv import load_dotenv
load_dotenv()
import os
import sqlite3
import streamlit as st
import google.generativeai as genai

google_api_key=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=google_api_key)

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content([prompt[0],question])
    response =response.text
    response = response.replace("```sql", "").replace("```", "").strip()
    return response


## function to retrieve query from the sql databse
def read_db(sql,db):
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    cursor.execute(sql)
    rows=cursor.fetchall()
    conn.commit()
    conn.close()
    return rows


prompt=[

   """
  You are an expert in converting English questions to SQL query!
  The SQL database has the name STUDENT and has the following columns-NAME,CLASS,SECTION and MARKS\n\n
  For Example,\nExample 1- How many entries of records are present?
  The sql command will be something like this SELECT COUNT(*) FROM student;
  \n Example 2 -Tell me all the students studying in Data Science class?,
  the SQL command will be something like this SELECT * FROM STUDENT where CLASS="DATA Science"
  also the sql code should not have --- in the begining or end and sql word should be in capital
"""
]



st.set_page_config(page_title="Using Gemini to query a SQL Database")
st.header("Using Gemini to query a SQL Database")

questions=st.text_input("What do you want from the Database: ",key="input")

submit =st.button("Press to get desired data")


if submit:
    response=get_gemini_response(question=questions,prompt=prompt)
    st.write(response)
    
    data=read_db(response,"student.db")
    print(data)
    st.subheader("Output: ")
    for row in data:
       st.subheader(f"{row}")
    