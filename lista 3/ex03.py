cityA = 80000
cityB = 200000

x = 0
while cityA <= cityB:
  cityA = cityA +  3 / 100 * cityA
  cityB = cityB +  1.5 / 100 * cityB
  x= x + 1

print(f'Em {x} anos')
