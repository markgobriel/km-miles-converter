# this is where the user inputs the km value
km = float(input("enter a distance in km: "))

# converting km --> miles
conv_fac = 0.621371

# in miles
miles = km * conv_fac
print('%0.2f kilometers is equivalent to %0.2f miles' %(km,miles))