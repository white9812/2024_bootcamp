# Assignment(loop)

while True:
    menu = input("1) Fahraenheit ->Celsius 2) Celsius -> Fahrenheit 3)Quit program : ")
    if menu == "1":
        fahrenheit = float(input("Input Fahreheit : "))
        print(f"fahrenheit: {fahrenheit}F,Celsius: {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C")
    elif menu == "2":
        celsius = float(input("Input celsius : "))
        print(f": celsius{celsius}c,Fahreheit: {(celsius * (9.0 / 5.0) + 32):.4f}F")
    elif menu=="3" :
        print("Terminate Program")
        break