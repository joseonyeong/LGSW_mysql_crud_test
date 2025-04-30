import streamlit as st
import sqlite3
import pandas as pd

# SQLite 데이터베이스 연결
conn = sqlite3.connect('classicmodels.sqlite')
cursor = conn.cursor()

# Streamlit 앱 타이틀
st.title("Classic Models 데이터베이스")

# MySQL 데이터베이스에서 데이터를 읽어오는 쿼리 예시
query = "SELECT * FROM customers LIMIT 10;"  # 예시: customers 테이블에서 상위 10개 레코드 조회

# 데이터베이스에서 데이터를 pandas DataFrame으로 가져오기
df = pd.read_sql(query, conn)

# Streamlit으로 데이터 표시
st.write("고객 정보 (상위 10개):")
st.dataframe(df)

# 검색 기능 추가 예시 (고객 이름을 기준으로 검색)
search_name = st.text_input("고객 이름을 입력하세요:")

if search_name.strip():
    query_search = f"""
        SELECT * FROM customers 
        WHERE LOWER(customerName) LIKE LOWER('%{search_name.strip()}%')
        LIMIT 10;
    """
else:
    query_search = "SELECT * FROM customers LIMIT 10;"

df_search = pd.read_sql(query_search, conn)
st.dataframe(df_search)



# 연결 종료
conn.close()
