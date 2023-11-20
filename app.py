import streamlit as st

# Configuration de la page
st.set_page_config(layout="wide")

    # Lecture du template HTML
with open('template.html', 'r') as file:
    html_template = file.read()

    # Création des colonnes pour l'entrée et l'affichage
left_column, right_column = st.columns(2)

with left_column:
    st.header("Entrez vos données")
    title = st.text_input("Titre", "Titre du Journal")
    date = st.text_input("Date", "01/01/2023")
    text = st.text_area("Texte et Anecdotes")
    image_url = st.text_input("URL de l'Image")
    update_button = st.button("Mettre à jour")

with right_column:
    st.header("Aperçu du Journal")
    if update_button:
        updated_html = html_template.format(title=title, date=date, text=text, image_url=image_url)
        st.components.v1.html(updated_html, height=800)
