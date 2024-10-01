# Importing the necessary modules from the Streamlit and LangChain packages

    
'''
References:
 https://discuss.streamlit.io/t/update-text-area/38084/6
'''
import streamlit as st
from langchain.llms import OpenAI
import openai 
from langchain_community import llms
# Setting the title of the Streamlit application
st.title('Product Ingredients Analyzer')

# Creating a sidebar input widget for the OpenAI API key, input type is password for security
openai_api_key = 'sk-36zXGcu_tJqTPzrKRi6G2UXF5FUPjeDaltTjBc6-ajT3BlbkFJBdr4EughftGeArWidxKP5Sdss3cTmC84uXJm2d_4kA'
openai.api_key=openai_api_key
#st.sidebar.text_input('OpenAI API Key', type='password')

# Defining a function to generate a response using the OpenAI model
def generate_response(input_text):
    # Initializing the OpenAI model with a specified temperature and API key
    llm = OpenAI(temperature=0.0, openai_api_key=openai_api_key)
    # Displaying the generated response as an informational message in the Streamlit app
   
    st.info(llm(prompt))


    
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
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0 # this is the degree of randomness of the model's output
             
        )
        #return response.choices[0].message["content"]
        st.info(response.choices[0].message["content"])
        



    # Displaying a warning if the entered API key does not start with 'sk-'
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    # If the form is submitted and the API key is valid, generate a response
    if submitted and openai_api_key.startswith('sk-'):
        #generate_response(prompt)
        #print(get_completion(prompt, model="gpt-3.5-turbo"))
        get_completion(prompt, model="gpt-3.5-turbo")
    if click_clear:
    
        a=1 
    
    if click_product_ingredients:
    
        a=1
    
