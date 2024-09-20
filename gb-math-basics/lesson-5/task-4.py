import itertools

for p in itertools.product("012",repeat=5):
    print(''.join(p))