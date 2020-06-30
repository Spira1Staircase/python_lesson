from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(100)
    left(90)
    forword(100)
    left(90)
    forword(100)
    left(90)
    forword(100)
    left(90)
    if abs(pos()) < 1:
        break
end_fill()
done()
