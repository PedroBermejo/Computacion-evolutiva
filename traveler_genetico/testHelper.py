from helper import helper 

# Test 'inversionReproduction'
print("Testing inversionReproduction")
parent = list(range(1, 21))
print(parent)
child = helper.inversionReproduction(parent.copy())
print(child)

# Test 'flipReproduction'
print("Testing flipReproduction")
parent = list(range(1, 21))
print(parent)
child = helper.flipReproduction(parent.copy())
print(child)

# Test 'getTotalDistance'
print("Testing getTotalDistance")
chrom = [20, 2, 3, 19, 16, 12, 17, 18, 6, 9, 1, 15, 7, 13, 4, 5, 14, 10, 11, 8]
distance = helper.getTotalDistance(chrom)
print(chrom)
print(distance)

# Test 'getTotalDistance' proposed in class
print("Testing getTotalDistance proposed in class")
chrom = [29, 21, 1, 8, 12, 22, 13, 4, 27, 24, 15, 2, 26, 19, 
    11, 16, 23, 7, 9, 6, 28, 20, 17, 18, 5, 14, 25, 30, 3, 10]
distance = helper.getTotalDistance(chrom)
print(chrom)
print("distance:", distance)
helper.grahpSingleChrom(chrom, distance)
