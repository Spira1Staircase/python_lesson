from turtle import*
t1 = Turtle()
t2 = Turtle()
t1.color('red')
t2.color('blue')
for i in range(180):
    t1.forward(5)
    t2.forward(3)
    t1.left(2)
    t2.left(2)
done()