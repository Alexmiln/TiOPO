import sys

ORDINARY_TRIANGLE = 'обычный'
ISOSCELES_TRIANGLE = 'равнобедренный'
EQUILATERAL_TRIANGLE = 'равносторонний'
NOT_A_TRIANGLE = 'не треугольник'
UNDEFINED_ERROR = 'неизвестная ошибка'

def checkArgsCount():
    if len(sys.argv) != 4:
        raise RuntimeError


def getTriangleType(side1: float, side2: float, side3: float) -> str:
    if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
        return NOT_A_TRIANGLE

    if (side1 == side2) and (side1 == side3) and (side2 == side3):
        return EQUILATERAL_TRIANGLE

    if (side1 == side2) or (side1 == side3) or (side2 == side3):
        return ISOSCELES_TRIANGLE

    return ORDINARY_TRIANGLE


try:
    checkArgsCount()

    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])

    print(getTriangleType(a, b, c))

except ValueError:
    print(UNDEFINED_ERROR)
    exit()
except RuntimeError:
    print(UNDEFINED_ERROR)
    exit()
