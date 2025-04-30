# LGSW_mysql_crud_test

### sqlite3 라이브러리 설치 및 classicmodels 쿼리 추가
```shell
    pip install mysql-to-sqlite3
    mysql2sqlite -f classicmodels.sqlite -d classicmodels -u root -p
```

### streamlit 대시보드 개발
-- sqlite3와 연결 (Connect to server)
    -> classicmodels.sqite path 지정

### 대시보드 디자인 시작
- 고객 정보 입력
```python
    search_name = st.text_input("고객 이름을 입력하세요:")
``` 
- 강제 소문자 변환 & 띄어쓰기 제거 후 search
```sql
    -- search 성공 시
    WHERE LOWER(customerName) LIKE LOWER('%{search_name.strip()}%') LIMIT 10;
    -- search 실패 시
    SELECT * FROM customers LIMIT 10;
```

### 배포 deploy, streamlit
--

## Tech Stack

![python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)
![sqlite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=joseonyeong)](https://github.com/anuraghazra/github-readme-stats)
--

## Communication
📌 아래 뱃지를 클릭하면 노션 페이지로 이동합니다!

![discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)
<a href="https://rebel-sponge-f81.notion.site/MySQL-Python_DB-table-sqlite3-streamlit-1e595b3f859c80edb774c5d8ca52b62c" target="_blank">
  <img src="https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white" alt="Notion Badge">
</a>