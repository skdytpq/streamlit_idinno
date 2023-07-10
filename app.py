import streamlit as st

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

# 툴바에 이미지 추가
st.markdown(
    """
    <div class="toolbar">
        <img class="toolbar-image" src="https://ethno-mining.com/resources/iknowyou/image/code/K01.png">
        <span>툴바에 추가된 이미지입니다.</span>
    </div>
    """,
    unsafe_allow_html=True
)

csv_file = st.file_uploader('크롤링 데이터 URL csv를 업로드 해주세요', type=['csv'])

# CSS 클래스와 함께 이미지 추가
st.markdown('<div class="image-container"><img src="https://ethno-mining.com/resources/iknowyou/image/code/K01.png"></div>', unsafe_allow_html=True)
