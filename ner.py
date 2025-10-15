import spacy
import requests 
import pandas as pd 
from spacy import displacy
from bs4 import BeautifulSoup

nlp = spacy.load("en_core_web_sm")
pd.set_option("display.max_rows", 200)

def NER(content):
    doc = nlp(content)
    displacy.render(doc, style="ent")
    entities = [(ent.text, ent.label_, ent.lemma_) for ent in doc.ents]
    df = pd.DataFrame(entities, columns=['text', 'type', 'lemma'])
    return df