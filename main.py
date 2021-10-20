#Programmer: Michael Gell
#Date: 10/20/21
#Class: CS-151-04
#Lab 05

#using a function to calculate room sizes using function size_room. Used 1 to count for error (Similar to how we used -1 in class).
def size_rooms(count):
    count+=1
    if count == 1:
        try:
            length=float(input("please input the length of the 1st room").lower().replace(" ",""))
            width = float(input("please input the width of the 1st room").lower().replace(" ", ""))
        except:
            print("there was an error inputing your room, this room will be skipped")
            return [0,0]
    else:
        try:
            length = float(input("please input the length of the next room").lower().replace(" ", ""))
            width = float(input("please input the width of the next room").lower().replace(" ", ""))
        except:
            print("there was an error inputing your room, this room will be skipped")
            return [0,0]
    return[length,width]
#using a function to find what kind of flooring
def flooring(i):
    type=input("please input the type of flooring you would like for this room ").lower()
    type=type.replace(" ","")
    print(type)
    if type!="carpet" and type!="tile" and type!="hardwood":
        print("you did not input a correct flooring type, this room will not be calculated")
        return "missing"
    else:
        return type
#calculating room cost by multiplying length,width, and type of flooring
def roomcost(l,w,t):
    if t=="missing" or l==0:
        print("the cost of this room could not be calculated due to an improper flooring type or improper dimensions")
        return 0
    else:
        if t=="carpet":
            cost = round(l*w*3.99,2)
            print("the cost for this room was")
            print(cost)
        elif t=="hardwood":
            cost = round(l*w*1.39,2)
            print("the cost for this room was")
            print(cost)
        elif t=="tile":
            cost = round(l*w*4.99,2)
            print("the cost for this room was")
            print(cost)
        return cost



flooring_types=[[""],[""],[""],[""],[""]]
rooms=[[0,0],[0,0],[0,0],[0,0],[0,0]]
#calling other functions in main to find total cost. starting cost at 0. Using range button to print sequences
def main():
    total_cost = 0
    for i in range(len(rooms)):
        rooms[i]=size_rooms(i)
        flooring_types[i] = flooring(i)
    for i in range(len(rooms)):
        total_cost=total_cost + float(roomcost(rooms[i][0],rooms[i][1],flooring_types[i]))
    print("the total cost is ")
    print(total_cost)

main()

