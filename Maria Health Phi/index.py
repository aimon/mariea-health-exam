x = 11
first = 1
second = 0
if x % 3 and x % 5:
    for i in range(0, x):
        nxt = first + second
        first = second
        second = nxt
        print(nxt)
elif x % 3 == 0 and x % 5 == 0:
    print('Maria Health')
else:
    if x % 3 == 0:
      print('Maria')

    if x % 5 == 0:
      print('Health')
