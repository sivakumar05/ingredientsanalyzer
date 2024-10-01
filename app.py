# Importing the necessary modules from the Streamlit and LangChain packages

    
'''
References:
 https://discuss.streamlit.io/t/update-text-area/38084/6
'''

import streamlit as st
import os 
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

from openai import OpenAI
import configparser

config = configparser.RawConfigParser()
config.read('config.ini')
    
details_dict = dict(config.items('My Section'))
print(details_dict)
KVUri = f"https://openai-ia.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

retrieved_secret = client.get_secret('openai')


# Setting the title of the Streamlit application
st.title('Product Ingredients Analyzer')

# Creating a sidebar input widget for the OpenAI API key, input type is password for security


#st.sidebar.text_input('OpenAI API Key', type='password')


client = OpenAI(
    api_key=retrieved_secret.value
    )

    
# Creating a form in the Streamlit app for user input
with st.form('my_form'):
    # Adding a text area for user input with a default prompt
    text = st.text_area('Enter Product Ingredients:', '',key='input')
    
    prompt = f"""
    Identify the top 2 ingredients that are beneficial and top 2 ingredients that are concern for health
    along with reasons. 
    Also, highlight for which age groups and the people suffering with various diseases these 
    top2 beneficial ingredients, top 2 concenring ingredients  
    are using upto 50 words from the input_text delimited 
    by triple backticks    
   
    ```{text}```
    """
    # Adding a submit button for the form
    submitted = st.form_submit_button('Submit')
    
    # Adding a Clear results button for the form to erase the results 
    click_clear = st.form_submit_button('Clear Results')
    
    def on_clear_clicked():
        st.session_state.input = ''

    # Adding a Clear Product Ingredoents button for the form to erase the ingredients entered  
    click_product_ingredients = st.form_submit_button('Clear Product Ingredients',on_click=on_clear_clicked)
     
    
    
    def get_completion(prompt, model="gpt-4"):
        messages = [{"role": "user", "content": prompt}]
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0 # this is the degree of randomness of the model's output
             
        )
        
        st.info(response.choices[0].message.content)
        



    # Displaying a warning if the entered API key does not start with 'sk-'
    # If the form is submitted and the API key is valid, generate a response
    if submitted :
        get_completion(prompt, model="gpt-4")
    if click_clear:
    
        pass 
    
    if click_product_ingredients:
    
        pass
    
