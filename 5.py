mass = int(input('Enter Mass : '))        
velocity = int(input('Enter Velocity : '))
def kinetic_energy(a,b):
    KE = (1/2)*((a)*(b**2))
    print(KE)

kinetic_energy(mass,velocity)
