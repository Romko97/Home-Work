# Simple: Find The Distance Between Two Points
# Given two ordered pairs calculate the distance
#  between them. Round to two decimal places.
#  This should be easy to do in 0(1) timing.


def distance(x1, y1, x2, y2):
    """This fanction are finding the distance betvin two points"""
    print(round(((((x1-x2)**2)+((y1-y2)**2))**0.5), 2))


"""distance(1, 1, 0, 0)"""
