from app import Calc 

if __name__ == '__main__':
    my_calc = Calc(0,0)
    print(f"A + B = {my_calc.sum()}")
    print(f"A - B = {my_calc.divergence()}")
    print(f"A * B = {my_calc.multiplication()}")
    print(f"A / B = {my_calc.division()}")
    print(f"A % B = {my_calc.residual_division()}")
    print(f"A ** B = {my_calc.darajaga_kutarish()}")
    print(f"A ** (1 / B) = {my_calc.ildiz_olish()}")
