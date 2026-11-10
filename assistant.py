
print("================================")
print("       ECE AI ASSISTANT")
print("================================")

print("1. Calculate Voltage")
print("2. Calculate Current")
print("3. Calculate Resistance")
print("4. Exit")

choice = input("\nEnter your choice: ")

if choice == "1":
    current = float(input("Enter current in amperes: "))
    resistance = float(input("Enter resistance in ohms: "))
    voltage = current * resistance
    print("Voltage =", voltage, "V")

elif choice == "2":
    voltage = float(input("Enter voltage in volts: "))
    resistance = float(input("Enter resistance in ohms: "))

    if resistance == 0:
        print("Resistance cannot be zero.")
    else:
        current = voltage / resistance
        print("Current =", current, "A")

elif choice == "3":
    voltage = float(input("Enter voltage in volts: "))
    current = float(input("Enter current in amperes: "))

    if current == 0:
        print("Current cannot be zero.")
    else:
        resistance = voltage / current
        print("Resistance =", resistance, "ohms")

elif choice == "4":
    print("Goodbye!")

else:
    print("Invalid choice. Try again.")
