# 2.Составить генератор (yield), который выводит из строки только буквы.


def generator(st):
    for i in st:
        if i.isalpha():
            yield i

st = "a,s,f,ew,fsa,hre,wer,gfdsa,nbcvb,23,5,1,55,4,132,1"
for el in generator(st):
    print(el, end=' ')
