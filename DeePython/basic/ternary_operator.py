foo = True
bar = 'a' if foo else 'b'

print(bar)  # a

foo = False
bar = 'a' if foo else 'b'

print(bar)  # b
