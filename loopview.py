import random
z = "0"
n = 0
usname = "LUCCAS"
usprofession = "student"
usnameslice = usname[slice(3)]
usprofslice = usprofession[slice(3)]
userid = usnameslice + z + str(n+1) + usprofslice
randsymbollist = ['@', '#', '$']
randsymbol = random.choice(randsymbollist)
rand1 = random.randint(0,10)
rand2 = random.randint(0,10)
rand3 = random.randint(0,10)
rand4 = random.randint(0,10)

uspassword = usnameslice + usprofslice + randsymbol + str(rand1) + str(rand3) + str(rand2) + str(rand4)
print(uspassword)
print(userid)
