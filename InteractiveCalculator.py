# Interactive calc model with python operations using class exceptions modules


class Calculator(Exception):
    def _init_(self):
        self.a=0
        self.b=0
    def input_numbers(self):
        try:
            self.a =float(input("Enter 1st number:"))
            self.b =float(input("Enter 2nd number:"))
        except ValueError as e:
            print("Invalid input...please enter numbers")
            self.input_numbers()
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        if self.b==0:
            raise ZeroDivisionError
        return self.a/self.b
    def modulo(self):
        return self.a%self.b
    def expo(self):
        return self.a**self.b
    def floor_division(self):
        return self.a/self.b
    
def display_menu():
    print("-- Calculator Menu ---")
    l = ["Addition","Subraction","Product","Division","Modulo","Power","Floor Division","Exit"]
    for i in range(len(l)):
        print(f"{i+1} {l[i]}")

def main():
    calc = Calculator()
    while True:
        display_menu()
        choice = input("select an operation(1-8):")
        if choice =="8":
            print("Exit")
            break
        calc.input_numbers()
        try:
            if choice =="1":
                print("Result:",calc.add())
            elif choice =="2":
                print("Result:",calc.sub())
            elif choice == "3":
                print("Result",calc.mul())
            elif choice=="4":
                print("Result",calc.div())
            elif choice=="5":
                print("Result",calc.modulo())
            elif choice =="6":
                print("Result",calc.expo())
            elif choice=="7":
                print("Result",calc.floor_division())
            else:
                print("Invalid choice,select from 1-8 ")
        except ZeroDivisionError as e:
            print("Error:",e)
        except Exception as e:
            print("Unexpected error:",e)

main()
