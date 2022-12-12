import streamlit as st

def main() : 
    st.title('웹 대시보드')
    
    # 비주얼 스튜디오 터미널에 표시해주고 싶을때 print 사용
    print('웹 대시보드')
    
    st.text('웹 대시보드 개발하기')
    
    st.header('이 영역은 헤더 영역')
    st.subheader('이 영역은 서브 헤더 영역')
    
    # 초록색으로 메시지 표시
    st.success('성공했을때 메시지를 보여줄때 사용')
    
    #노란색으로 메시지 표시
    st.warning('경보 메세지를 보여주고 싶을때')
    
    
    #파란색 메시지를 표시
    st.info('정보성 메세지를 보여주고 싶을때')
    
    # 빨간색으로 메시지 표시
    st.error('문제가 발생했을 경우에 보여주고 싶을때')
    
    
    # 파이썬의 함수들의 설명을 보여주고 싶을때
    st.help( sum )
    st.help( len )


if __name__ == '__main__' :
    main()