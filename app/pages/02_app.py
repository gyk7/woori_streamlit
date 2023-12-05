import streamlit as st
import pandas as pd  # st은 입력과 출력만 담당할 뿐 실제 로직은 나머지 파이썬 코드로 구현됩니다.

data = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)


# 입력
st.title('1. 입력버튼들')

button_result = st.button('Hit me')
if button_result == True :
    st.write(button_result)
    st.data_editor(data)
# 버튼을 누르면 데이터프레임이 등장하도록 로직을 만들어주세요


check_result = st.checkbox('Check me out')
if check_result == True :
    st.data_editor(data)

st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,2, 3])
food_list = ['고추바사삭', '처갓집슈프림', '고추마요']
img_list = ['https://i.imgur.com/TqV2uYB.jpg', 'https://i.imgur.com/YAeN8V0.jpg', 'https://i.imgur.com/iefMfFs.jpg']

search =st.text_input('Enter some text')
# st.write(search)
for food_ in food_list :
    if search in food_ :
        img_index = food_list.index(food_)

if search != '' :
        st.image(img_list[img_index])

st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.download_button(
    label="Download data as CSV",
    data='안녕하세요',
    file_name='app_df.csv',
    mime='text/csv'
)
st.camera_input("一二三,茄子!")
st.color_picker('Pick a color')

# 출력
st.title('2. 출력메서드들')
st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
# st.image('https://i.imgur.com/TqV2uYB.jpg')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')



# https://i.imgur.com/TqV2uYB.jpg
# https://i.imgur.com/YAeN8V0.jpg
# https://i.imgur.com/iefMfFs.jpg