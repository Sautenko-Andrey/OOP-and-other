def main():
    x,y=100,100
    width,heith=200,200

    draw_house(x,y,width,heith)

def draw_house(x,y,width,heigth):
    """
    Нарисовать домик ширины width и высоты height от опорной точки (x,y),
    которая находится в середине нижней точки фундамента.
    :param x: координата х середины домика
    :param y: координата y низа фундамента
    :param width: полная ширина домика (фундамент и вылеты крыши включены)
    :param heith: полная высота домика
    :return: ничего не надо возвращать
    """
    print('типа рисую домик....',x,y,width,heigth)

    foundation_height=0.05*heigth
    walls_height=0.5*heigth
    walls_width=0.9*width
    roof_height=heigth-foundation_height-walls_height

    draw_foundation(x,y,width,foundation_height)
    draw_house_walls(x,y-foundation_height,walls_height,walls_width)
    draw_house_roof(x,y-foundation_height-walls_height,width,roof_height)

def draw_foundation(x,y,width,height):
    pass
    print('типа рисую основание....',x, y, width, height)
"""
    Нарисовать основание ширины width и высоты height от опорной точки (x,y),
    которая находится в середине нижней точки фундамента.
    :param x: координата х середины фундамента
    :param y: координата y низа фундамента
    :param width: полная ширина фундамента
    :param heith: полная высота фундамента
    :return: ничего не надо возвращать
    """

def draw_house_walls(x,y,width,height):
    print('типа рисую стены....', x, y, width, height)
    pass


def draw_house_roof(x,y,width,height):
    print('типа рисую крышу....', x, y, width, height)
    pass


main()