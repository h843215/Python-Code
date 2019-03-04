from turtle import *
left(90)
h = 80
w = 10
for i in range (8):
    for i in range (2):
        
        forward(h)
        right(90)
        forward(w)
        right(90)

    h = h-10    
    w = w+10

done()
