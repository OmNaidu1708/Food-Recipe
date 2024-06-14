import streamlit as st
from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')

def generate_recipe(ingredients):
    prompt = f"Recipe using the following ingredients: {', '.join(ingredients)}.\n\n"
    
    output = generator(prompt, max_length=200, num_return_sequences=1)
    recipe = output[0]['generated_text']

    return recipe

def main():
    st.title('Recipe Generator')
    ingredients = st.text_input('Enter ingredients separated by commas (e.g., chicken, broccoli, rice):')

    if st.button('Generate Recipe'):
        if ingredients:
            ingredients_list = [ing.strip() for ing in ingredients.split(',')]
            recipe = generate_recipe(ingredients_list)
            st.subheader('Generated Recipe:')
            st.write(recipe)
        else:
            st.warning('Please enter some ingredients.')

if __name__ == '__main__':
    main()
