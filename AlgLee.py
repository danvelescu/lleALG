import numpy

i = int(input("give i"))
j = int(input("give j"))

labirintZla = numpy.arange(i * j).reshape(i, j)


def changeAllMatrix(nr):
    m = 0
    n = 0
    while n < i:
        m = 0
        while m < j:
            labirintZla[n][m] = nr
            m += 1
        n += 1


def addStartPointAndEndPoint():
    startpoint = [int(input("start x: ")), int(input("start y: "))]
    endpont = [int(input("end x: ")), int(input("end y: "))]

    labirintZla[startpoint[0]][startpoint[1]] = -2
    labirintZla[endpont[0]][endpont[1]] = -3


def setRandomObstacle():
    number_of_obstacle = int(input("set number of obstacle"))
    for x in range(number_of_obstacle):
        labirintZla[numpy.random.randint(0, i)][numpy.random.randint(0, j)] = -1


def rt(k):
    m = 0
    n = 0
    while n < i:
        m = 0
        while m < j:




            m += 1
        n += 1



changeAllMatrix(0)
addStartPointAndEndPoint()
setRandomObstacle()
print(labirintZla)
