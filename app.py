import streamlit as st
st.markdown('<style type="text/css">body { margin: 0; padding: 0; }</style>', unsafe_allow_html=True)
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

st.title('아이노유 서비스 크롤링 프로그램입니다.')
option = st.selectbox('데이터 크롤링 타입 선택',
                    ('아이노유 페르소나', '병원 페르소나', '패션 데이터 페르소나'))
values = st.slider('크롤링 데이터 규모', 0.0, 100000.0, (5000.0,100000.0))

st.write('Values:', values)

st.write('You selected:', option)

csv_file = st.file_uploader('크롤링 데이터 URL csv 를 업로드 해주세요', type=['csv'])