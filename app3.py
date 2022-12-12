# 판다스의 데이터프레임을, 웹화면으로 보여주는 방법

import streamlit as st
import pandas as pd


def main() :

  st.title('아이리스 꽃 데이터')
  df = pd.read_csv('streamlit_data/iris.csv')
  
  st.dataframe(df)
  
  
  #데이터프레임 값 불러오는 방법
  species = df['species'].unique()
  st.text('아이리스 꽃은' + species + '으로 되어있다.')
  
  

if __name__ == '__main__' :
    main()