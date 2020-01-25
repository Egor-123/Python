import itertools

l = [10, 23, 45, 26]
s = ['sss', 'sasf', 'asaeff', 'sfgg', 'sfffs']

for el_l, el_s in itertools.zip_longest(l, s):
    print(el_l, el_s)