import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function To get response from LLAma 2 model

def getLLamaresponse(ingredients,cook_time,difficulty):

    ### LLama2 model
    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':512,
                              'temperature':0.01})
    
    ## Prompt Template
    ## Lists 3 recipes and talks them through. 
    ## Should change so it lists 3 recipes, their calories/macros, how long to cook and difficulty level.

    template="""
        Give me 1 recipe to make with the following ingredients {ingredients}. 
        I want to cook for {cook_time} minutes or less.
        The difficulty level of cooking should be {difficulty}.
            """
    
    prompt=PromptTemplate(input_variables=["ingredients","cook_time",'difficulty'],
                          template=template)
    
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(difficulty=difficulty,ingredients=ingredients,cook_time=cook_time))
    print(response)
    return response



st.set_page_config(page_title="Generate Recipe",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Recipes 🤖")

ingredients=st.text_input("What ingredients do you have at home?")

## creating to more columns for additonal 2 fields

col1,col2=st.columns([5,5])

with col1:
    cook_time=st.text_input('How much time do you want to cook for?')
with col2:
    difficulty=st.selectbox('What type of food do you want to cook?',
                            ('Beginner','Intermediate','Advanced'),index=0)
    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(ingredients,cook_time,difficulty))