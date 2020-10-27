# PROBLEM 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.'
#
# Find the sum of all the multiples of 3 or 5 below 1000.

counter = 1

end = 1000
divident_eins = 3
divident_zwei = 5
sum = 0

while counter < end:
    if counter % divident_eins == 0:
        sum += counter

    elif counter % divident_zwei ==0:
        sum += counter
    #print("counter ist %r" % (counter))
    #print("Die Summe ist %r" % (sum))
    counter += 1

print("Die Summe ist %r" % (sum))

# -----DONE-----
