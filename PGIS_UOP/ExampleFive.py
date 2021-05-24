def pigsAndChickens(heads, legs):


    for pig_head in range(1, heads):
        if pig_head * 4 + (heads - pig_head) * 2 == legs:
            print('Pig count ', pig_head, 'chicken count ', (heads - pig_head))

pigsAndChickens(20, 56)


def countAnimal(heads, legs):


    pigs = 0
    while pigs <= heads:
        chicken = heads - pigs
        if (pigs * 4) + (chicken * 2) == legs:
            print('Pigs ', pigs)
            print('chicken ', chicken)
            return None
        else:
            pigs = pigs + 1

countAnimal(20, 56)


def countChickenPigsSpiders(heads, legs):


    pigs = 0
    while pigs <= heads:
        rem = heads - pigs
        chicken = 0
        while chicken <= rem:
            spider = rem - chicken
            if (pigs * 4) + (chicken * 2) + (spider * 8) == legs:
                print('Pigs ', pigs)
                print('chicken ', chicken)
                print('Spider', spider)
                return None
            else:
                chicken = chicken + 1
        pigs = pigs + 1

print('There is no valid answer')

countChickenPigsSpiders(20, 56)
