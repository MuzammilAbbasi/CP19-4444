Mass = int(input("Enter the mass: "))
Velocity = int(input("Enter the velocity: "))
def KE(Mass,Velocity):
  return 1/2*Mass*Velocity**2
print("Kinetic Energy of given input is",KE(Mass,Velocity))
