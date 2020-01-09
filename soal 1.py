def circle(r):					#calculate area of circle
    s=3.14*r**2
    return s
   
def rectangle(length,width):			#calculate area of rectangle
    s=length*width
    return s

def square(side):				#calculate area of square
    s=side**2
    return s
    
def triangle(base,height):			#calculate area of triangle
    s=base*height/2
    return s
    
def get_func(ls):				#vared kardane ashkal dar yek list
    print("Enter name of 4 shape:")
    for i in range(0,4):
        shape=input()
        ls.append(shape)
    return ls
      
ls=[]

print(get_func(ls))

choose=input("choose a shape from list:")	#entekhabe yek shekl baraye hesab kardan va neshan dadane masahat
if choose=='circle':
    r=int(input("Enter Radius:"))
    print("Area of circle is:",circle(r))
elif choose=='rectangle':
    length=int(input("Enter length of rectangle:"))
    width=int(input("Enter width of rectangle:"))
    print("Area of rectangle is:",rectangle(length,width))
elif choose=='triangle':
      height=int(input("Enter height of triangle:"))
      base=int(input("Enter base of triangle:"))
      print("Area of triangle is:",triangle(height,base))
elif choose=='square':
      side=int(input("Enter side of square:"))
      print("Area of square is:",square(side))
else:
    print("character you are Entered is invalid")

