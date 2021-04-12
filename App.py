import streamlit as st
import wikipedia
import spacy
import spacy_streamlit
from spacy import displacy
#from textblob import TextBlob

def entity_analyzer(wiki_name):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(wiki_name)
    #entities = [(entity.text) for entity in docx.ents]
    displacy.render(doc, style="ent")


    spacy_streamlit.visualize_ner(doc,labels = nlp.get_pipe('ner').labels)

def main():
    st.title("Named Entity Recognition")
    st.subheader("Enter Wikipedia Name:")
    wiki_name = st.text_input("")
    wiki_name = wiki_name.strip()

    try:
        if wiki_name!="":
            results = wikipedia.summary(wiki_name)
            st.subheader("Extract Entities from Text")
        if st. button("Extract NER"):
            entity_analyzer(results)


    except Exception:
        st.text("Entered Wikipedia Page does not exist\nTry with Correct Wikipedia Title")






if __name__ == "__main__":
    main()