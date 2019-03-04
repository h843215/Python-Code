class ConLLToken(object):
    def __init__(self, word, lemma, pos, morph):
        self.word = word
        self.lemma = lemma
        self.pos = pos
        self.morph = morph
        
    def is_capitalized(self):
        return self.word.istitle()

    def is_punctuation(self):
        return self.pos == 'PUNCT'
            

    def is_inflected(self):
        self.word = self.word.lower()
        self.lemma = self.lemma.lower()
        if self.lemma == self.word:
            return False
        else:
            return True

    def get_number(self):
        if 'Number' not in self.morph:
            return None
        else:
            if 'Number' in self.morph:
                value = self.morph.split('|')
                value1 = value[1].split('=')
                return value1[1]

    def __str__(self):
        fields = [self.word, self.lemma, self.pos, self.morph]
        return ','.join(fields)
        

#tok = ConLLToken("comes", "come", "VERB","Mood=Ind|Number=Sing|Person=3")
#print("Token=", str(tok ))
#print("Capitalized?", tok.is_capitalized ())
#print("Punctuation?", tok.is_punctuation ())
#print("Inflected?", tok.is_inflected ())
#print("Number=", tok.get_number ())
        
