import streamlit as st
import time

# App description
st.markdown('''
# Countdown Timer

- Source Code: https://github.com/steven-ngo/Countdown-Timer
- Language: `Python`
- Libraries: `streamlit`
''')
st.write('---')

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
          18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
          35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
          52, 53, 54, 55, 56, 57, 58, 59]

col1, col2, col3 = st.columns(3)

hour = col1.selectbox(
   "Hour:",
   numbers,
   index=0,
)

min = col2.selectbox(
   "Minute:",
   numbers,
   index=0,
)

sec = col3.selectbox(
   "Second:",
   numbers,
   index=0,
)

timeInSecond = (hour*3600) + (min*60) + sec

if st.button("Start"):
    with st.empty():
        for timeRemain in range(timeInSecond, 0, -1):
            seconds = timeRemain % 60
            minutes = int(timeRemain/60) %60
            hours = int(timeRemain/3600)
        
            displayTime = '<h2>' + f'⏳ {hours:02}:{minutes:02}:{seconds:02}' + '</h2>'
            
            st.write(displayTime, unsafe_allow_html=True)
            
            time.sleep(1)
        
        st.write("<h2>✅ Time Over!</h2>",unsafe_allow_html=True)
