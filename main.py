import spacy
import requests 
import pandas as pd 
from spacy import displacy
from bs4 import BeautifulSoup



nlp = spacy.load("en_core_web_sm")
pd.set_option("display.max_rows", 200)

content = "Hello my name is chetanya jolly. I am a 4th year student in manipal university jaipur. I am currently pursing a bachealors in Computer science and engineering with a major in Artificial Intelligence and Machine Learning.gi"

doc = nlp(content)
for ent in doc.ents:
    print(f"Entity: {ent.text}")
    print(f"Start Character: {ent.start_char}")
    print(f"End Character: {ent.end_char}")
    print(f"Label: {ent.label}\n")

displacy.render(doc, style="ent")

entities = [(ent.text, ent.label_, ent.lemma_) for ent in doc.ents]
df = pd.DataFrame(entities, columns=['text', 'type', 'lemma'])
print(df)