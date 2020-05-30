# bounce.py
#
# Exercise 1.5

height = 100 # meters
bounce_percentage = 3/5 # after each bounce
max_bounce = 10 # iterations
it = 1

while it <= max_bounce:
    height = height * bounce_percentage
    print(it, round(height, 4)) 
    it = it + 1

