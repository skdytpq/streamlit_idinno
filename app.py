import streamlit as st
import pandas as pd
import time
# 커스텀 CSS를 사용하여 이미지를 대체할 요소에 추가
st.markdown(
    """
    <style>
    #root > div:nth-child(1) > div.withScreencast > div > div > header {
        background-image: url('https://ethno-mining.com/resources/iknowyou/image/code/K01.png');
        background-size: 150px;
        background-position: left;
        background-repeat: no-repeat;
        padding: 20px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > header > div.css-14xtw13.e13qjvis0 > div:nth-child(1) {
        display: none;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > header > div.css-14xtw13.e13qjvis0 > div:nth-child(2) {
        display: none;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > header > div.css-14xtw13.e13qjvis0 > div:nth-child(3) {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# 커스텀 CSS를 사용하여 이미지를 툴바에 추가
st.markdown(
    """
    <style>
    .toolbar {
        display: flex;
        align-items: center;
        padding: 10px;
    }
    
    .toolbar-image {
        margin-right: 10px;
    }
    
    .header-container {
        display: flex;
        align-items: center;
        padding: 20px;
        background-color: #f0f0f0;
    }
    
    .header-title {
        font-size: 24px;
        margin-left: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 헤더 컨테이너 생성
header_container = st.container()
with header_container:
    # 헤더 이미지 및 제목
    st.markdown(
        """
        <div class="header-container">
            <img class="toolbar-image" src="https://ethno-mining.com/resources/iknowyou/image/code/K01.png">
            <h1 class="header-title">아이노유 서비스 크롤링 프로그램입니다.</h1>
        </div>
        """,
        unsafe_allow_html=True
    )


option = st.selectbox('데이터 크롤링 타입 선택', ('아이노유 페르소나', '병원 페르소나', '패션 데이터 페르소나'))
values = st.slider('크롤링 데이터 규모', 0.0, 100000.0, (5000.0, 100000.0))

st.write('Values:', values)
st.write('You selected:', option)

csv_file = st.file_uploader('크롤링 데이터 URL csv를 업로드 해주세요', type=['csv'])
time.sleep(3)
file = pd.read_csv(csv_file)
file_url = file['url']

hide_streamlit_style = """
<style>
#MainMenu { visibility: hidden; }
footer {
    visibility: hidden;
    background-image: url('https://ethno-mining.com/resources/iknowyou/image/code/K01.png');
    background-size: cover;
    background-position: center;
    padding: 20px;
}
footer:after { visibility: visible; content: "Iknowyou"; }
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
