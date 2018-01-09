import spacy
import sys

usage = "--Error--\nUsage: python " + sys.argv[0] + " sm | md | lg\n--Error--"
if len(sys.argv) != 2:
    print usage
    sys.exit(1)

model = sys.argv[1]
print "using model: " + model
nlp = spacy.load('en_core_web_' + model)
# Determine semantic similarities
doc1 = nlp(u'help me with devops')
doc2 = nlp(u'i need help with devops')
print "similarity: " + str(doc1.similarity(doc2))
