def threeLinesArea(m1, b1, m2, b2, m3, b3):
    xOne = lineIntersection(m1,b1,m2,b2)
    xTwo = lineIntersection(m2,b2,m3,b3)
    xThree = lineIntersection(m3,b3, m1, b1)
    yOne = findY(m1,b1, xOne)
    yTwo = findY(m2,b2, xTwo)
    yThree = findY(m3,b3, xThree)
    dis1 = distance(xOne, yOne, xTwo, yTwo)
    dis2 = distance(xTwo, yTwo, xThree, yThree)
    dis3 = distance(xThree, yThree, xOne, yOne)
    areaTri = triangleArea(dis1,dis2,dis3)
    return areaTri


def lineIntersection(m1, b1, m2, b2):
    intersectionX = (b2 - b1) / (m1-m2)
    return intersectionX

def distance(x1, y1, x2, y2):
    dis = ((x2 - x1)**2 + (y2 - y1)**2)** 0.5
    return dis

def triangleArea(a, b, c):
    s = (a+b+c)/2
    ar = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return ar

def findY(m,b, x):
    y = m * x + b
    return y

def testThreeLinesArea():
    import math
    print("Testing threeLinesArea()...", end="")

    # y=3x-5 and y=x+5 intersect at (5,10)
    assert(math.isclose(lineIntersection(3, -5, 1, 5), 5))
    # y=10x and y=-4x+35 intersect at (2.5,25)
    assert(math.isclose(lineIntersection(10, 0, -4, 35), 2.5))

    assert(math.isclose(distance(0, 0, 1, 1), 2**0.5))
    assert(math.isclose(distance(3, 3, -3, -3), 6*2**0.5))
    assert(math.isclose(distance(20, 20, 23, 24), 5))

    assert(math.isclose(triangleArea(3, 4, 5), 6))
    assert(math.isclose(triangleArea(2**0.5, 1, 1), 0.5))
    assert(math.isclose(triangleArea(2**0.5, 2**0.5, 2), 1))

    assert(threeLinesArea(1, 2, 3, 4, 5, 6) < 0.0001) # == 0
    assert(math.isclose(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(math.isclose(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666))
    assert(math.isclose(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(math.isclose(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))

    print("... done!")
testThreeLinesArea()