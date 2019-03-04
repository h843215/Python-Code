from constituents import Phrase, Token

TheT = Token('DT', 'The')
catT = Token('NN', 'cat')
chasesT = Token('VB', 'chases')
theT = Token('DT', 'the')
mouseT = Token('NN', 'mouse')
PUNCTT = Token('PUNCT', '.')

np_cat = Phrase('NP', [TheT, catT])
np_mouse = Phrase('NP', [theT, mouseT])
vp_chases = Phrase('VP', [chasesT, np_mouse])
sent = Phrase('S', [np_cat, vp_chases, PUNCTT])

#print(sent)
