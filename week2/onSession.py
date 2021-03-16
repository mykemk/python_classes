#camelCase
#snake_case

def to_celsius(farenheit):
    '''
    Ths function takes ......
    '''
    temperature = (farenheit-32) * (5/9)
    return temperature

print("The temperature is, ",to_celsius(100),"degrees celsius")

#default values
# def run(distance=5):
#     name = input("Who is the runner ?")
#     print(f"{name} has run {distance} Km today")
    

# run(distance=10)

#arbitrary arguments
def greet(args):
    for visitor in args:
        print(f"Welcome {visitor}")
        

greet(["Ken", "Kelvin","Sheline","Murgor"])

#Lambda functions/anonymous

prices = [12,23,34,5,67,78]
double = lambda price: price * 2
change_name = lambda name: "AZL"+name
print(change_name("Kennedy"))

#.map() --Higher Order functions
doubled = map(double,prices)
# print(doubled)

print(double(14))