def SuperFloatPow(num, num2, num3) :
    """(number, number, number) -> float

    Takes three numbers inculding float and the first number is taken to the
    second numbers power then divided by the third and the answer is the remainder

    >>>SuperFloatPow(4.5, 6.4, 8.9)

    7.344729065655461

    """
    return((num**num2)% num3)
