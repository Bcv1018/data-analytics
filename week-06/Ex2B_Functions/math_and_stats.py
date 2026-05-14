import random
import math
import statistics

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi
area_up = math.ceil(pi * (radius ** 2))
area_down = math.floor(pi * (radius ** 2))

# Experimenting with a subset of integers 1-100:

# Sum of 75 sample values from 1 to 100
sum_vals_sample = sum(vals_sample)
#print(f'The sum of 75 sample values is {sum_vals_sample}')

# Avg of 75 sample values
avg_vals_sample = statistics.mean(vals_sample)
#print(f'The average of 75 samples is {avg_vals_sample}')

# Median of 75 sample values
median_vals_sample = statistics.median(vals_sample)
# print(f'The median of 75 samples is {median_vals_sample}')

## _Experimenting with a superset of 200 values, integers 1-100:

# Average of 200 values
avg_200_vals = statistics.mean(vals_choices)
# print(f'The average of 200 values is {avg_200_vals}')

# Median of 200 values
median_200_vals = statistics.median(vals_choices)
# print(f'The median of 200 values is {median_200_vals}')

# Mode of 200 values
mode_200_vals = statistics.mode(vals_choices)
# print(f'The mode of 200 values is {mode_200_vals}')

# Standard deviation of 200 values
stdev_200_vals = statistics.stdev(vals_choices)
# print(f'The standard deviation of 200 values is {stdev_200_vals:.2f}')

# Variance of 200 values
vari_200_vals = statistics.variance(vals_choices)
# print(f'The variance of 200 values is {vari_200_vals:.2f}')


## Modeling a random circle:
circleup = (f'Radius = {radius}, Area = {area_up}') # rounds up to the nearest integer
circledown = (f'Radius = {radius}, Area = {area_down}') # rounds down to the nearest integer

print(f'''
_Experimenting with a subset of integers 1-100:
Sum of 75 sample values from 1 to 100: {sum_vals_sample}
Average of 75 sample values: {avg_vals_sample:.2f}
Median of 75 sample values: {median_vals_sample} \n
_Experimenting with a superset of 200 values, integers 1-100:
Average of 200 values: {avg_200_vals}
Median of 200 values: {median_200_vals}
Mode of 200 values: {mode_200_vals}
Standard deviation of 200 values: {stdev_200_vals:.2f}
Variance of 200 values: {vari_200_vals:.2f} \n
_Modeling a random circle:
Radius = {radius}, area = {area_up} (rounded up to the nearest integer)
Radius = {radius}, area = {area_down} (rounded down to the nearest integer)
 ''')

