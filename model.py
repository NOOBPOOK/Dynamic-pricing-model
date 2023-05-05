from sys import exit

'''
This fuction below implements the Mathematical model followed by this algorithm
'''
def pricingModel(order,or_arr,count,x):
    cost = 0
    yo = 0
    menu = ["Appetizers","Bread","Rice","Main-Course","Soups","Salads","Snacks"]
    print("\n")
    #adds the priority of all food-items to variable yo variable
    for y in order:
       yo += y[2]

    #compares the value of yo var to x var, whose values are then stored in variable ty
    ty = float(x/yo)
    if ty < 2:
       ty += 0.50

    #Actaul implementation of mathematical order
    for i in order:
        co = ty*i[1]*i[2]
        print(f"The cost of {menu[i[0]-1]} per plate is {int(co)}")
        for u in i[3]:
            if u in or_arr:
                co -= co*0.1
                print(f"After getting discount as dependacy on {menu[u-1]} ,Final price is {int(co)}")
                break
        cost += int(co)
    cost = (int(cost/10)+1)*10
    print(f"\nThe cost per one plate of food is {cost} considering other expenses and rounding off\n")
    cost *= count
    print("*"*100,end="\n")
    print(f"The total price for the food event will be {cost}",end="\n")
    print("*"*100,end="\n")



print("Welcome to the pricing model\n\n")
'''
This dictionary describes the menu for the model. Menu can be extended for details later
For now only major categories of menus have been selected for model purpose
'''
menu = {
    "Appetizers":[1,60,.3,[5]],#appetizers
    "Bread":[2,50,.2,[4]],#Bread
    "Rice":[3,120,.5,[]],#Rice
    "MainC":[4,130,.5,[]],#mc
    "Soups":[5,80,.2,[1]],#soups
    "Salads":[6,50,.1,[3]],#salads
    "Snacks":[7,40,.1,[]]#snacks
}
cu = int(input("Please enter the number of guests!  "))
gh = list(map(str,input("Please enter the food items  ").split(" ")))

'''
x variable repressnts the amount a person can eat
if more types of food items are selected we can assume the people will eat a little more than normal
'''
x = 2
if len(gh)>3:
  x = 2.5
if len(gh)>5:
  x = 3.5

arr = []
or_arr = []
for i in gh:
  try:
    arr.append(menu[i])
    or_arr.append(menu[i][0])
  except:
    print("This food item doesn't exist in the menu!")
    exit(0)

pricingModel(arr,or_arr,cu,x)

  
