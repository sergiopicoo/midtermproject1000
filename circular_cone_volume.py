from math import pi

def get_radius_from_user():
 while True:
    try:
        radius=float(input("what is the radius?"))
        break
    except Exception as e:
        print("e")
    
    return radius

def get_height_from_user():
    height=float(input("what is the height?"))
    return height

def calculate_circular_cone_volume(radius, height):
    volume=pi*radius**2*height/3
    return volume
    
def generate_report(radius,height,volume):
    print("A right circular cone of radius=*",radius,"and height=",height,"has volume of", volume)
    
def main():
    radius=get_radius_from_user()
    height=get_height_from_user()
    volume=calculate_circular_cone_volume(radius,height)
    generate_report(radius,height,volume)
    


main()

