from constituents import *

def list2parsetree(l):

    lst = []
    for c in l[1:]:
        if type(c[1]) == str:
            lst.append(Token(c[0], c[1]))
        else:
            lst.append(list2parsetree(c))
    P = Phrase(l[0], lst)
    return P

print(list2parsetree(['S', ['NP', ['DT', 'The'], ['NN', 'cat']], ['VP', ['VB', 'chases'], ['NP', ['DT' ,'the'], ['NN' ,'mouse']]], ['PUNCT' , '.']]))

    
