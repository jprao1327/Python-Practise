import sys
class Car:
    discount=100
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def print_bill(self):
        print(self.price-Car.discount)
def main():
    name=sys.stdin.readline().rstrip()
    price=int(sys.stdin.readline().rstrip())
    car=Car(name,price)
    car.print_bill()

if __name__=="__main__":
    main()