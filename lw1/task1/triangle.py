import sys
import math

ORDINARY_TRIANGLE = 'обычный'
ISOSCELES_TRIANGLE = 'равнобедренный'
EQUILATERAL_TRIANGLE = 'равносторонний'
NOT_A_TRIANGLE = 'не треугольник'
UNDEFINED_ERROR = 'неизвестная ошибка'

def checkArgsCount():
    if len(sys.argv) != 4:
        raise RuntimeError


def getTriangleType(side1: float, side2: float, side3: float) -> str:
    def isValidLinesValue() -> bool:
        MAX_VALID_LINE_VALUE = 2147483647
        MIN_VALID_LINE_VALUE = 0.000001

        return (side1 >= MIN_VALID_LINE_VALUE) and (side1 <= MAX_VALID_LINE_VALUE) \
               and (side2 >= MIN_VALID_LINE_VALUE) and (side2 <= MAX_VALID_LINE_VALUE) \
               and (side3 >= MIN_VALID_LINE_VALUE) and (side3 <= MAX_VALID_LINE_VALUE)

    def isTriangle() -> bool:
        return side1 + side2 > side3 and side3 + side2 > side1 and side1 + side3 > side2

    if not isValidLinesValue() or not isTriangle():
        return NOT_A_TRIANGLE

    if math.isclose(side1, side2, rel_tol=1e-14, abs_tol=0.0) and \
            math.isclose(side3, side2, rel_tol=1e-14, abs_tol=0.0):
        return EQUILATERAL_TRIANGLE

    if math.isclose(side1, side2, rel_tol=1e-14, abs_tol=0.0) or math.isclose(side3, side2, rel_tol=1e-14, abs_tol=0.0)\
            or math.isclose(side1, side3, rel_tol=1e-14, abs_tol=0.0):
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
