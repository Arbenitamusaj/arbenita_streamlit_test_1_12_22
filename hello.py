import streamlit as st

text = st.text_input("Type a text:")
lst1=[]
lst2=[]

def convert_list(text):
    lst1=text.split()
    return lst1

convert=convert_list(text)

if st.button('Return list'):
    st.write(convert)

def convert_upper(convert):
    for i in convert:
        upper_i=i.upper()
        lst2.append(upper_i)
    return lst2
convert2=convert_upper(convert)
if st.button('Upper'):
    st.write(convert2)

def count(convert):
   
    return len(convert)

x=count(convert)
if st.button('count'):
    st.write(x)




   