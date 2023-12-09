class computer:
    name = "pc"
    generation = 0

    class hard:
        name = "hard"
        capacity = 0
        speed = 0

    class ram :
        name = "ram"
        capacity = 1
        size = 16


r1 =computer.ram()
print(r1.name)

#other war to print the class hard

r2 = computer()
print(r2.name)
print(r2.ram.name)
print(r2.hard)
