def maxi():
    list1 = str1.split()
    d1 = {}
    d1["апельсин"] = []
    d1["яблоко"] = []
    for w in list1[1:6]:
        d1["апельсин"].append(int(w))
    for w in list1[7:]:
        d1["яблоко"].append(int(w))
    s1 = d1["яблоко"]
    s2 = d1["апельсин"]
    print(max(s1))
    print(max(s2))
    print(set(s1) | set(s2))

str1 = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
maxi()
