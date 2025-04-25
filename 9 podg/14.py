d = {'a': 1, 'b': 2, 'h': 5, 'c': 6}
s = sorted(d)
print(s)
ц = sorted(d.items(), key=lambda x: x[1])
print(ц)