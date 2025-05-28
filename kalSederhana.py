class Calculator:
    def __init__(self, x = None):
        if x is None:  
            self.x = int(input("Masukkan angka: "))  
        else:
            self.x = x  
       
    
    def __add__(self, other):
       if isinstance(other, Calculator):
           return Calculator(self.x + other.x)
       
    def __sub__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.x - other.x)
           
    def __mul__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.x * other.x)
        
    def __truediv__(self, other):
        if isinstance(other, Calculator):
            if other.x == 0:
                return "Tidak bisa dibagi dengan nol!!!"
            return Calculator(self.x / other.x)
        
    def __pow__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.x ** other.x)
    
    def __str__(self):
        return f"hasil {self.x}"

def main():
    print("Operasi yang tersedia: +, -, *, /, **")
    operator = input("Masukkan operator: ")

    num1 = Calculator()
    num2 = Calculator()

    match operator:
        case "+":
            hasil = num1 + num2
        case "-":
            hasil = num1 - num2
        case "*":
            hasil = num1 * num2
        case "/":
            hasil = num1 / num2
        case "**":
            hasil = num1 ** num2
        case _:
            hasil =  "tidak valid!!"

    print(hasil)

main()