
import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

button = st.button('시작')


if button:
    st.write('편하게 참여해주세요:smiling_face_with_3_hearts:')
agree = st.checkbox('반갑습니다')

if agree:
    st.write('저도 반갑습니다')
animal = st.radio(
    '여러분은 어떤 동물을 좋아하시나요',
    ('고양이','토끼', '강아지'))
if animal =='고양이':
    st.write(':black_cat:')
if animal == '토끼':
    st.write(':rabbit2:')
if animal == '강아지':
    st.write(':dog2:')

options = st.multiselect(
    '여행 갔을 때 어떤 숙소에서 묵는 것을 좋아하시나요?',
    ['캠핑', '글램핑', '호텔', '펜션', '차박', '풀빌라'])

start_time = st.slider(
    "올해 안에 길게 여행을 떠날 수 있다면 언제 가고 싶나요?",
    min_value=dt(2024, 6, 22), 
    max_value=dt(2024, 12, 31),
    value=dt(2024, 6, 22),
    step=datetime.timedelta(days=1),
    format="MM/DD/YY")
st.write("선택한 날짜", start_time)

title = st.text_input(
    label='현재 가장 먹고 싶은 음식은 무엇인가요?', 
    placeholder='음식을 입력해 주세요'
)
st.write(f'당신이 선택한 음식: :green[{title}]')