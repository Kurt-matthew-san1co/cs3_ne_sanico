def calculate_fuel(cargo_weight):
    cargo = ""
    cargo_weight = 0
    while cargo != "launch":
        total_fuel = (cargo_weight + 50000) * 3
        cargo = str(input("Cargo: "))
        if cargo == "launch":
            print (f"Your total fuel consumption is {total_fuel} gallons.")
            break
        if cargo == "satellite":
            cargo_weight += 1000
        elif cargo == "rover":
            cargo_weight += 2500
        elif cargo == "supplies":
            cargo_weight += 500 
        elif cargo != "satellite" or cargo != "rover" or cargo != "supplies":
            print ("That item is not approved for the mission. ")
        if cargo_weight > 10000:
            print ("MAX WEIGHT REACHED")
            break

calculate_fuel(1)