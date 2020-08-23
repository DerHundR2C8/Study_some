import fractions
if __name__ == '__main__':
    int1 = 2
    fraction1 = fractions.Fraction(1, 3)
    print(int1 * fraction1)
    print(fractions.Fraction(6, 4))
    try:
        print(fractions.Fraction(0, 0))
    except:
        pass
