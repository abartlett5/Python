def main():
    print("Let's find the kinetic energy of a moving object!" )
    mass_kg = input('Enter the mass of the object in kilograms: ')
    while type(mass_kg) is not int():
        try:
            mass_kg = int(input('Enter something: '))
        except ValueError:
            print("That's not an integer!")
            continue
        else:
            break        
    velocity_ms = input('Enter the velocity of the object in m/s: ')
    while type(velocity_ms) is not int():
        try:
            velocity_ms = int(input('Enter something: '))
        except ValueError:
            print("That's not an integer!")
            continue
        else:
            break   
    kinetic_energy = 0.5 * mass_kg * (velocity_ms) ** 2    
    print('The kinetic energy of the object is', round(kinetic_energy, 2), "joules.")


    
if __name__ == "__main__":
    main()

