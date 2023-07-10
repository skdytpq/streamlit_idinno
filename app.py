


import streamlit as st

# 버거 메뉴 + footer 수정
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden; }
            footer {visibility: hidden;}
            footer:after {visibility: visible; content:"footer!";}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# CSS styling to position the image in the top left corner
st.markdown(
    """
    <style>
    .image-container {
        position: absolute;
        top: 0;
        left: 0;
        padding: 10px;
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

# Add the image with the CSS class
st.markdown('<div class="image-container"><img src="https://ethno-mining.com/resources/iknowyou/image/code/K01.png"></div>', unsafe_allow_html=True)
