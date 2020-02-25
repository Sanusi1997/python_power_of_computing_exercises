def energy(mass, c = 1.86 * (10 ** 5)):
    energy = mass * (c ** 2)
    return print("Energy for the mass input is {:<6.2f} Kgm/s".format(energy))

energy(55)


