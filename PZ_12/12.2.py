# 2.Составить генератор (yield), который выводит из строки только буквы.
from string import ascii_letters


def generator(st):
    for i in st:
        if i in ascii_letters:
            yield i


st = "a,s,f,ew,fsa,hre,wer,gfdsa,nbcvb,23,5,1,55,4,132,1"
for el in generator(st):
    print(el, end=' ')
