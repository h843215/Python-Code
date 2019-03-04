from conlltoken import ConLLToken
class ConLLUTokenBuilder(object):
    def buildToken(self, line):
        line = line.split()
        token = ConLLToken(line[1], line[2], line[3], line[5])
        return token

class ConLL09TokenBuilder(object):
    def buildToken(self, line):
        line = line.split()
        token = ConLLToken(line[1], line[2], line[4], line[6])
        return token 



class SplitTokenBuilder(object):
    def buildToken(self, line):
        line = line.split('&')
        token = ConLLToken(line[0], line[1], line[2], line[3])
        return token


# checking ConLLUTokenBuilder
builder = ConLLUTokenBuilder ()
line = "1 The the DET _ Definite=Def|PronType=Art _ _ _ _"
tok = builder.buildToken(line)
print("From ConLLU:", str(tok ))
# checking SplitTokenBuilder
builder = SplitTokenBuilder ()
line = "courts&court&NOUN&Number=Plur"
tok = builder.buildToken(line)
print("From Split:", str(tok ))        
