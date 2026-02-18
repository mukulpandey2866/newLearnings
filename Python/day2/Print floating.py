# printing floating point values with different formats

print('Division = %f'%(10/3)) # this will print "Division = 3.333333" with the default floating-point format, which includes six decimal places.
print('Division = %.2f'%(10/3)) # this will print "Division = 3.33" with two decimal places.
print('Division = %.3f'%(10/3)) # this will print "Division = 3.333" with three decimal places.
print('Division = %.4f'%(10/3)) # this will print "Division = 3.3333" with four decimal places.
print('Division = {:.4f}'.format(10/3)) # this will print "Division = 3.3333" with four decimal places using format method.

flt = 3.1415926535897932384626433832795
print(f'Pi = {flt:.2f}') # this will print "Pi = 3.14" with two decimal places using f-string formatting.
print(f'Pi = {flt:.4f}') # this will print "Pi = 3.1416" with four decimal places using f-string formatting.

print('Pi = %.2f'%(flt)) # this will print "Pi = 3.14" with two decimal places.
print('Pi = %.4f'%(flt)) # this will print "Pi = 3.1416" with four decimal places.
print()