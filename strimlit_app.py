import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text( '🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text( '🥑🍞avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas --> move it to top of the screen

#import file to variable My Fruit List
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Choose the Fruit Name Column as the Index
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include . #fruit provide in the picker list names of fruits.
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

#Create a repatable block of code called FUNCTION

def get_fruityvice_data(this_fruit_choice):
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      # write your own comment -what does the next line do? - normalize json file
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      return (fruityvice_normalized) 

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
  else:
      back_from_function = get_fruityvice_data(fruit_choice)
      # write your own comment - what does this do? output screen as a table
      streamlit.dataframe (back_from_function)
      
except URLError as e:
  Streamlit.error()
      
#don`t run anything past here while we troubleshoot
streamlit.stop()

#import snowflake.connector --> move it to the top of screen
streamlit.header("The fuit load list contains:")
#Snowflake related functions
def get_fruit_load_list():
      with my_cnx.cursor() as my_cur:
      my_cur.execute("select * from fruit_load_list")
      return my_cur.fetchall()

#add a button to load the fruit
if strimlit.button ('Get Fruit Load List)
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      my_data_rows = get_fruit_load_list()
      streamlit.dataframe(my_data_rows)

streamlit.header("The fuit load list contains:")


add_my_fruit = streamlit.text_input('What fruit would you like to add','jackfruit')
streamlit.write('The user entered ', add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
