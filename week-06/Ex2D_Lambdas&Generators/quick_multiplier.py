doubler = lambda n: n * 2

print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

tripler = lambda n: n * 3
print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

def multipler(multi):
    return lambda n: n * multi

quadrupler = multipler(4)
quintupler = multipler(5)
sextupler = multipler(6)
septupler = multipler(7)
octupler = multipler(8)
nonupler = multipler(9) 
decupler = multipler(10)

print(quadrupler(5))
print(quintupler(8))
print(sextupler(7))
print(septupler(6))
print(octupler(2))
print(nonupler(3))
print(decupler(5))