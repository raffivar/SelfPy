def powered_by(num1, num2):
    """
    calculates the value of num1 powered by num2
    :param num1: base number
    :type num1: int
    :param num2: the number that the base number will be powered by
    :type num2: int
    :return: num1 powered by num2
    :rtype int
    """
    return num1 ** num2


def main():
    help(powered_by)
    #OR
    print(powered_by.__doc__)


if __name__ == "__main__":
    main()
