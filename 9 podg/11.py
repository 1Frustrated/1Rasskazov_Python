d1 = {'овощ': 'морковь', 'напиток': 'вода'}
print(d1)


def ww():
    if d1.get('фрукт') == 'груша':
        del d1['фрукт']
        print(d1)
    else:
        print("none")


ww()