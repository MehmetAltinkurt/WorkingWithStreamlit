print("Hello VSC")

import streamlit as st

st.title('First Streamlit')
st.header('This is a Header')

st.subheader('This is a SubHeader')

st.text('Normal Text')

st.markdown("### Markdown")


st.success("Successful")

st.info("informatiion")

st.warning("warning")

st.error("error")

st.exception("exception")
st.help(st)

st.write('Hello Streamlit')

st.image("https://lms.clarusway.com/pluginfile.php/1/core_admin/logocompact/300x300/1668173907/clarusway_LOGO_tek_png.png")

st.video("https://www.youtube.com/watch?v=Dptu5K9Fx90")




if st.checkbox("show/hide"):
    st.text("show hide widget")

status=st.radio("radio:",("active","pasive"))
st.write(status)

occupation=st.selectbox("selectbox",["student","programmer","entrepreneur"])

st.write(occupation)

ms=st.multiselect("multiselect",("aaa","bbb","ccc","ddd"))

sayi=st.slider("sayi")
st.write(sayi)


if st.button("click"):
    st.write("you clicked the button")

name=st.text_input("enter your name")
st.write("your name is:",name)

st.text_area("text area")


st.write("echo:")
with st.echo():
    #this is a comment
    import numpy as np


st.text("st.progress(70)")
st.progress(70)


import time
with st.spinner('Wait for it...'):
     time.sleep(5)
st.success('Done!')


st.balloons()

st.sidebar.header("About")
st.sidebar.text("text")



@st.cache
def func():
    return range(100)
st.write(func())





















