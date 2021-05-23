"""
Template - Compute the area of a triangle (using Heron's formula),
    given its side lengths.
"""

###################################################
# Triangle area (Heron's) formula
# Student should enter function on the next lines.
# Hint:  Use point_distance as a helper function.


def point_dis(x_0, y_0, x_1, y_1):
    x_dis = x_0-x_1
    y_dis = y_0-y_1
    return (((x_dis)**2+(y_dis)**2)**0.5)


def triangle_area(x_0, y_0, x_1, y_1, x_2, y_2):
    len1 = point_dis(x_0, y_0, x_1, y_1)
    len2 = point_dis(x_0, y_0, x_2, y_2)
    len3 = point_dis(x_2, y_2, x_1, y_1)
    s = (len1+len2+len3)/2
    return ((s*(s-len1)*(s-len2)*(s-len3))**0.5)

###################################################
# Tests
# Student should not change this code.


def test(x_0, y_0, x_1, y_1, x_2, y_2):
    """Tests the triangle_area function."""

    print("A triangle with vertices (" + str(x_0) + "," + str(y_0) + "),")
    print("(" + str(x_1) + "," + str(y_1) + "), and")
    print("(" + str(x_2) + "," + str(y_2) + ") has an area of")
    print(str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")


x_0, y_0, x_1, y_1, x_2, y_2 = 0, 0, 3, 4, 1, 1
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" +
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) +
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2))
      + ".")

x_0, y_0, x_1, y_1, x_2, y_2 = -2, 4, 1, 6, 2, 1
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" +
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) +
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2))
      + ".")

x_0, y_0, x_1, y_1, x_2, y_2 = 10, 0, 0, 0, 0, 10
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" +
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) +
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2))
      + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.
# A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.
# A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.
