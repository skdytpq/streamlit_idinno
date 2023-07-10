import streamlit as st

# 커스텀 CSS를 사용하여 이미지를 대체할 요소에 추가
st.markdown(
    """
    <style>
    #root > div:nth-child(1) > div.withScreencast > div > div > header {
        background-image: url('https://ethno-mining.com/resources/iknowyou/image/code/K01.png');
        background-size: 200px;
        background-position: left;
        background-repeat: no-repeat;
        padding: 10px;
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


st.title('아이노유 서비스 크롤링 프로그램입니다.')

option = st.selectbox('데이터 크롤링 타입 선택', ('아이노유 페르소나', '병원 페르소나', '패션 데이터 페르소나'))
values = st.slider('크롤링 데이터 규모', 0.0, 100000.0, (5000.0, 100000.0))

st.write('Values:', values)
st.write('You selected:', option)

csv_file = st.file_uploader('크롤링 데이터 URL csv를 업로드 해주세요', type=['csv'])
