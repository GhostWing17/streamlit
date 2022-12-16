import streamlit as st
import pandas as pd


def main() : 
    df = pd.read_csv('streamlit_data/iris.csv')
    if st.button('데이터프레임 보기') :
        st.dataframe(df)
        
        name='Mike'
        if st.button('대문자로') :
            st.text(name.upper())
            
# 슬라이더
age = st.slider('나이', 1, 100)
st.text('당신이 선택한 나이는 ' +str(age)+ '입니다.')

st.slider('데이터', 1 , 100, step=5)
st.slider('데이터', 1, 200, value=75)
st.slider('데이터', 0.0, 1.0, step=0.1)

with st.expander('hello') :
    st.text('안녕하세요.')
    

if __name__ == '__main__' :
    main()
    