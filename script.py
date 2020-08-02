train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5 / 9
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)


def get_force(mass, acceleration):
  return mass*acceleration

#Test of def get_force
train_force = get_force(22680, 10)
print("\nTrain force is " + str(train_force))

print("\nThe GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass, c = int(3*10**8)):
  return mass * c**2

#Test of def get_energy
bomb_energy = get_energy(1)
print("\nBomb energy is " + str(bomb_energy))

print("\nA 1kg bomb supplies " + str(bomb_energy) + " Joules.")

def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

#Test of def get_work
train_work = get_work(22680, 10, 100)
print("\nTrain work is "+ str(train_work))

print("\nThe GE train does " + str(train_work) +  " Joules of work over " + str(train_distance) + " meters.")