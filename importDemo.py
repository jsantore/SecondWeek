import math

def main():
    radius = 6
    circum = math.pi * radius *2
    result = math.pow(circum, 3)
    print(f"circumference is {circum} and then when cubed is {result}")
    demo = "the quick brown fox jumped over the tired student before arriving at the ."
    how_many = demo.count("the")  # how_many has the value 3 now
    print(f"'the'  showed up {how_many} times")
    capital_version = demo.upper()
    print(capital_version)
    

main()
