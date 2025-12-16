import streamlit as st
import spacy
import spacy.cli

spacy.cli.download("en_core_web_sm")
nlp = spacy.load("en_core_web_sm")

st.title("Grammar Analysis of English News")

text = st.text_area("Paste an English news article here:")

if st.button("Analyze"):
    doc = nlp(text)

    st.subheader("Part of Speech Analysis")
    for token in doc:
        if not token.is_punct:
            st.write(token.text, "-", token.pos_)

    st.subheader("Passive Sentences")
    for sent in doc.sents:
        for token in sent:
            if token.dep_ == "auxpass":
                st.write(sent.text)
                break
