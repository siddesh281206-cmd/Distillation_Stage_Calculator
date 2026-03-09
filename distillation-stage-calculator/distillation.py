import math

def calculate_stages(xD, xB, alpha):
    """
    Estimate number of theoretical stages in a distillation column
    """
    if xD <= xB:
        print("Distillate composition must be greater than bottom composition.")
        return None

    N = math.log(xD / xB) / math.log(alpha)
    return N


def main():
    print("Distillation Column Stage Calculator")

    xD = float(input("Enter distillate composition (xD): "))
    xB = float(input("Enter bottom composition (xB): "))
    alpha = float(input("Enter relative volatility (alpha): "))

    stages = calculate_stages(xD, xB, alpha)

    if stages:
        print("Estimated theoretical stages:", round(stages, 2))


if __name__ == "__main__":
    main()