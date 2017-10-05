# elena thornton
# 10/5/17
# octagon flower
# this program draws a hexagon flower. It takes user input to do so.

import turtle


def get_a_number():
    """
    this function get the length of a side.
    :return: number

    """
    y = input("what is the length of a side of the hexagon:", )
    number = float(y)
    return number


def draw_an_hexagon(users_center_color, size):

    """
    this function draws the center hexagon,for the flower.
    :param users_center_color: the color that the user wants for the center.
    :param size: the length of a hexagon side
    :return: none

    """

    turtle.begin_fill()
    turtle.fillcolor(users_center_color)
    for x in range(6):
        turtle.forward(size)
        turtle.left(60)
    turtle.end_fill()


def draw_a_petal(times, size, users_color):
    """

    this function draws petals for the flower.
    :param times: this says how many time the petal will be drawn.
    :param size: this keep the sizes of the center hexagon and the petals the same.
    :param users_color: this is the color for the petals
    :return:none.

    """
    for x in range(times):
        turtle.right(size)
        draw_an_hexagon(users_color)


def main():
    size = get_a_number()

    users_center_color = input("what is the center color of the flower?:", )

    draw_an_hexagon(users_center_color, size)

    users_color = input("what is the petal color:", )

    draw_a_petal(2, 120, users_color)

    turtle.forward(size)
    turtle.left(60)

    draw_a_petal(1, 120, users_color)

    turtle.forward(size)
    turtle.left(60)

    draw_a_petal(1, 120, users_color)

    turtle.forward(size)
    turtle.left(60)

    draw_a_petal(1, 120, users_color)

    turtle.forward(size)
    turtle.left(60)

    draw_a_petal(1, 120, users_color)

main()

turtle.exitonclick()
