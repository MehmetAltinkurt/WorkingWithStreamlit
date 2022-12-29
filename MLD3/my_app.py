
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


#title text
st.title("This is a title")
st.text("this is a text")

#
st.markdown("streamlit is **_really_ cool** : +1")

st.markdown("# Markdown")
st.markdown("## Markdown")
st.markdown("### Markdown")
st.markdown("#### Markdown")

#header/subheader

st.header("This is a header")
st.subheader("Subheader")

#success info error

st.success("this is a success message")
st.info("this is a info message")
st.error("this is a error message")
st.warning("this is a warning message")

st.exception("NameError('name tree is not defined')")

#help
st.help(range)

#write
st.write("Hello c12 Cohort")

st.write(range(10))

#image
img=Image.open("images.jpeg")
st.image(img,caption="C12")

st.video("https://www.youtube.com/watch?v=uHKfrz65KSU")

st.checkbox("up and down")
if st.checkbox("hide and seek"):
    st.write("hide")
else:
    st.write("seek")

clr=st.radio("select a color",("blue","red","yellow"))
st.write("favori rengin: ",clr)

if st.button("click me"):
    st.success("prediction complated")


st.selectbox("Your color", ["Blue", "Red", "Green"])




occupation=st.selectbox("Your Occupation", ["Programmer", "DataScientist", "Doctor"])
st.write("You selected this option :", occupation)


# multi select
multi_select = st.multiselect("Select multiple numbers",[1,2,3,4,5])
st.write("You selected this option :", multi_select)

# slider
option1 = st.slider("Select a number", min_value=5, max_value=70, value=30, step=5)
option2 = st.slider("Select a number", min_value=10, max_value=80, step=5)
option3 = st.slider("Select a number", 10)

result = option1 * option2
st.write("The result is:", result)



# text input
name = st.text_input("Enter your name", placeholder="Your name here")
if st.button("Submit"):
   st.write("Hello", name.title())


# code

st.code("import pandas as pd")
st.code("import pandas as pd\nimport numpy as np")


with st.echo():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({"a":[1,2,3], "b":[4,5,6]})
    df



# date input

import datetime
today = st.date_input("Today is", datetime.datetime.now())

date = st.date_input("Enter the date")

# time input

hour = st.time_input(str(pd.Timestamp.now()))
st.write("Hour is", hour)

time = st.time_input("Time is")

# sidebar

st.sidebar.title("sidebar title")

st.sidebar.header("Sidebar header")
a=st.sidebar.slider("input",0,5,2,1)
x=st.sidebar.slider("input2")


st.write("sidebar input products")
st.success(a*x)