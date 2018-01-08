import spacy
nlp = spacy.load('en')
# Determine semantic similarities
doc1 = nlp(u'help me with devops')
doc2 = nlp(u'i need help with devops')
print doc1.similarity(doc2)
