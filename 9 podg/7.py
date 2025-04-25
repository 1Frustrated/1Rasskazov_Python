s1 = 'груши 45 991 63 100 12 морква 13 47 26 0 16'
def ww():
    l1 = s1.split()
    d1 = {}
    d1["груши"] = []
    d1['морква'] = []
    for w in l1[1:6]:
        d1['груши'].append(int(w))
    for w in l1[7:]:
        d1['морква'].append(int(w))
    p1 = d1["груши"]
    p2 = d1['морква']
    print(min(p1))
    print(min(p2))

ww()