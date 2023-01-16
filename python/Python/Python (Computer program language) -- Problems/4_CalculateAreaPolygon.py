from math import tan, pi
n_sides=int(input('input number of Sides : '))
s_length = float(input('input the length of s side : '))
p_area= n_sides*(s_length**2)/(4*tan(pi/n_sides))
print('the Area of the Polygon is : ',p_area)