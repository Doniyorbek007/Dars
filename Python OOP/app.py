class Calc:
    def __init__(self, a,b) -> None:
        self.a = a
        self.b = b
        self.a = int(input("A sonni kiriting: "))
        self.b = int(input("B sonni kiriting: "))

    def sum(self):
        return self.a + self.b

    def divergence(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def residual_division(self):
        return self.a % self.b
    
    def darajaga_kutarish(self):
        return self.a ** self.b
