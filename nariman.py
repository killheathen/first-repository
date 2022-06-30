import math
sheklha = ["mosalas=m", "dayere=d", "morabaa=m4", "mostatil=m2", "lozi=l", "chand zelee=cz", "motavazi al azlaa=maa",
            "baizy=b","zozenaghe=z","korea=k"]
print(*sheklha)
a = input("che shekli ro mikhay hesab konam?")
if a == 'm':
    b = int(input("ghaede chande?"))
    c = int(input("ertefa chande?"))
    hhj = b * c
    masahat = hhj / 2

    for i in range(3):
        m = int(input("zelee bego"))
        mohit = mohit + m
    print("mohit", mohit)
    print("masahat", masahat)
elif a == 'd':
    shoaa = int(input("shoaa chande?"))
    mohit =  (shoaa * 3.14 * 2)
    print("mohit", mohit)
    masahat = shoaa * shoaa * 3.14
    print("masahat", masahat)
elif a == 'm4':
    zelee = int(input("yek zelesho begoo"))
    masahat = zelee * zelee
    print('masahat', masahat)
    mohit = zelee * 4
    print("mohit", mohit)
elif a == 'm2':
    tool = int(input("yek tool begoo"))
    arz = int(input("yek arz begoo"))
    mohit = tool + arz * 2
    print("mohit", mohit)
    masahat = tool * arz
    print('masahat', masahat)
elif a == 'l':
    ghotr1 = int(input("ghotr koochik begoo"))
    ghotr2 = int(input("ghotr bozorg begoo"))
    ghotr3 = ghotr1 * ghotr2
    masahat = ghotr3 / 2
    print('masahat', masahat)
    zelee1 = int(input("yek zelee begoo"))
    mohit = zelee1 * 4
    print("mohit", mohit)
elif a == 'cz':
    tool1 = int(input(" yek zelee bego"))
    tedadzelee = int(input('chandzelee dare?'))
    mohit = tool1 * tedadzelee
    print("mohit", mohit)
    print("motasefane masahat be dalil moshkelat mohasebati peyda nashod ")
elif a == 'maa':
    zeleemojaver1 = int(input("zelee mojaver bego"))
    zeleemojaver2 = int(input("zelee mojaver bego"))
    mohit = (zeleemojaver1 + zeleemojaver2) * 2
    print("mohit", mohit)
    b1 = int(input("ghaede chande?"))
    c1 = int(input("ertefa chande?"))
    masahat = b1 * c1
    print('masahat', masahat)
elif a == 'b':
    shoaa1 = int(input('shoaa kochik chande ?'))
    shoaa2 = int(input('shoaa bozorg chande ?'))
    masahat = (shoaa1 * shoaa2) * 3.14
    print('masahat', masahat)
    k80=((shoaa1**2+shoaa2**2)/2)*(2*3.14)
    mohit=math.sqrt(k80)
    print(" mohit ",mohit)
elif a == 'z':
    print("masahat")
    ghaedei1 = int(input("ghaedei koochik begoo"))
    ghaedei2 = int(input("ghaedei bozorg begoo"))
    ertefa1 = int(input("ertefa chande?"))
    masahat=((ghaedei1 + ghaedei2) / 2) * ertefa1
    print('masahat', masahat)
    print("mohit")
    print("motasefane mohit be dalil moshkelat mohasebati peyda nashod ")
elif a == 'k':
    r=int(input("shoaa chande?"))
    masahat=4*3.14*r**3
    t=(round(masahat))
    print("masahat",t)
    hajm=1.33*3.14*r**3
    p=(round(hajm))
    print("hajm taghribi",p)