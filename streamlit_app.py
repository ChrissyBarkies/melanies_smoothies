# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(f":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write("Choose the fruits you want in your custom Smoothie!")

name_on_order = st.text_input('Name on Smoothie')
st.write('The name on your Smoothie will be:', name_on_order)

session = st.connection("snowflake").session()

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
ingredients_list = st.multiselect('Choose up to 5 ingredients:', my_dataframe)

ingredients_string = ''
if ingredients_list:
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

my_insert_stmt = """
    INSERT INTO smoothies.public.orders (name_on_order, ingredients)
    VALUES ('""" + name_on_order + """', '""" + ingredients_string + """')
"""

time_to_insert = st.button('Submit Order')
if time_to_insert:
    session.sql(my_insert_stmt).collect()
    st.success('Your Smoothie is ordered, ' + name_on_order + '!', icon="✅")
import requests
smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
st.text(smoothiefroot_response)
#st.text(smoothiefroot_response.json)
sf_df = st.dataframe(data = smoothiefroot_response.json(), use_container_width= True)
