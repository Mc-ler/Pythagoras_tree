import turtle as t
from math import asin, pi

k = 24
small_leg = 3*k
big_leg = 4*k
right_leg = 5*k
s = 8
sin = big_leg / right_leg
cos = small_leg / right_leg

alpha = asin(sin) * 180 / pi
beta = 90 - alpha
print(alpha)
t.setup(width=1000, height=1000)
t.pensize(2)
t.speed(0)
t.penup()
t.goto(0 - right_leg / 2, -400)
t.pendown()
t.forward(right_leg)
t.left(90)


def draw_root(a_1, level):
    print('draw_root')
    t.forward(a_1)
    t.left(90)
    t.forward(a_1)

    if level:
        draw_triangle(a_1 * cos, a_1 * sin, a_1, level - 1)
    else:
        t.left(90)
        t.forward(a_1)
    
def draw_uplevel_square(a_2, level):
    print('draw_uplevel_square')
    t.forward(a_2)
    t.left(90)
    t.forward(a_2)
    if level:
        draw_triangle(a_2 * cos, a_2 * sin, a_2, level - 1)
    else:
        t.left(90)
        t.forward(a_2)

def draw_triangle(a_3, b_3, c_3, level):
    print('draw_triangle:{} {} {}'.format(a_3, b_3, c_3))
    t.right(180 - alpha)
    t.forward(a_3)
    t.right(90)
    t.forward(b_3)
    t.left(90)
    draw_uplevel_square(b_3, level)
    t.right(90)
    draw_root(a_3, level)
    t.right(alpha)
    t.forward(c_3)
    
    
draw_root(right_leg, s)
t.mainloop()