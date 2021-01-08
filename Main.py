import streamlit as st


st.write("""# **Simple Converter App**
""")

Menu = st.radio(
	"What would you like to do?",
	("Denary Conversion", "Binary Conversion", "Hexadecimal Conversion")
)
st.write(""" ____ """)

if Menu == "Denary Conversion":
	User = st.slider("Please select a Denary Number", min_value=1,max_value=255,value=1)
	st.write(User, "in Binary is", bin(User)[2:],"\n",
	"\n", User, "in Hexadecimal is", hex(User)[2:]
	)

if Menu == "Binary Conversion":
	User = st.text_input("Please Enter a Byte of binary")
	try:
		Internal = int(User, 2)
		st.write(User, "in Denary is", int(User,2))
		st.write(User, "in Hexadecimal is", hex(Internal)[2:])
	except:
		st.error("Please Enter a Valid Input.")

if Menu == "Hexadecimal Conversion":
	User = st.text_input("Please input a Hexadecimal String")
	try:
		Internal = int(User, 16)
		st.write(User, "in Binary is", bin(Internal)[2:])
		st.write(User, "in Denary is", Internal)
	except:
		st.error("Please Enter a Valid Input.")

	



