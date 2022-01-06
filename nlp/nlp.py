def extractCity(txt):
    import spacy
    
    nlp = spacy.load("fr_core_news_sm")

    doc = nlp(txt)

    for i in doc.ents:
        print(i.text, i.start_char, i.end_char, i.label_)


extractCity("Je veux aller de Paris a Besançon en passant par Lyon Elon Musk")


