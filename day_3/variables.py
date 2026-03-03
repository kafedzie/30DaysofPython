x = int(30)
y = float(1.80)
z = complex(1+2j)

base = float(input('Enter base: '))
height = float(input('Enter height: '))

area_of_triangle = float(0.5 * base * height)

print('Area of triangle: ', area_of_triangle)

a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))

perimeter = a + b + c
print('Perimeter of triangle: ', perimeter)

g = float(input('Enter length: '))
h = float(input('Enter width: '))

area_of_rectangle = g + h
print('Area of rectangle: ', area_of_triangle)

perimeter_of_rectangle = 2 * (g + h)
print('Perimeter of rectangle: ', perimeter_of_rectangle)

radius = input('Enter radius: ')
area_of_circle = 3.14 * radius ** 2
print('Area of circle: ', area_of_circle)

circumference = 2 * 3.14 * radius
print('Circumference of circle: ', circumference)


