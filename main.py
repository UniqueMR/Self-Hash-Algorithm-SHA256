from sha import sha256

sha = sha256()

res1 = sha.operation(message='abc')
res2 = sha.operation(message='')
res3 = sha.operation(message='abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq')
res4 = sha.operation(message='abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmnoijklmnopjklmnopqklmnopqrlmnopqrsmnopqrstnopqrstu')

print('res1: ' + res1)
print('res2: ' + res2)
print('res3: ' + res3)
print('res4: ' + res4)


print('finished')