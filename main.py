from utils import add, subtract
from logger import log_operation

def run():
    a, b = 10, 5

    result1 = add(a, b)
    log_operation("add", a, b, result1)

    result2 = subtract(a, b)
    log_operation("subtract", a, b, result2)

if __name__ == "__main__":
    run()