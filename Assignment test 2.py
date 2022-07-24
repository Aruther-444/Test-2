reply_lists1= "Yes", "yes", "y", "Y", "YES"
reply_lists2= "No", "no", "n", "N", "NO"

start= input("Do you wish to start your shopping? Yes No: ")

while start in reply_lists1:
    import math
    height = eval(input("Enter The Height Of The Wall In Meter: "))
    width = eval(input("Enter The Width Of The  Wall In Meter: "))
    num_of_wall = int(input("Enter The Number Of Wall: "))
    area = height * width * num_of_wall
    
    print("The Total Area is", format(area, ',.2f') + " meter square")
    print("")
    while True:
        print("Please Choose a Type Of Tile Stated Below")
        print("1. Small Black Granite= 001 \n2. Medium Sunset Yellow= 002 \n3. Large Oak Wood Effect= 003 \n4. Extra-large White Marble= 004")
        tiles = input("Enter the Code Type of the Tile: ")
        print("")
        
        price_of_t1, price_of_t2, price_of_t3, price_of_t4 = 85.50, 55.00, 286.00, 290.00
        t1, t2, t3, t4, = 1, 1, 1, 1    # square meter covered by each box of tile
        num_box1, num_box2, num_box3, num_box4 = math.ceil(area/t1), math.ceil(area/t2), math.ceil(area/t3), math.ceil(area/t4)
        
        code_list1= "001", "1", "01" #Creates possible customer's answers
        code_list2= "002", "2", "02" #Creates possible customer's answers
        code_list3= "003", "3", "03" #Creates possible customer's answers
        code_list4= "004", "4", "04" #Creates possible customer's answers

        if tiles in code_list1:
            print("The Total Price for Small Black Granite is RM" + str(format(price_of_t1 * num_box1, ",.2f")))
            print("Number Of Boxes Needed Are", num_box1)
        elif tiles in code_list2:
            print("The Total Price for Medium Sunset Yellow is RM" + str(format(price_of_t2 * num_box2, ",.2f")))
            print("Number Of Boxes Needed Are", num_box2)
        elif tiles in code_list3:
            print("The Total Price for Large Oak Wood Effect is RM" + str(format(price_of_t3 * num_box3, ",.2f")))
            print("Number Of Boxes Needed Are", num_box3)
        elif tiles in code_list4:
            print("The Total Price for Extra-large White Marble is RM" + str(format(price_of_t4 * num_box4, ",.2f")))
            print("Number Of Boxes Needed Are", num_box4)
        else:
            print("Error code invalid, Please Type the tiles' code!")

else:
    print("Do you wish to continue? Yes No")

    
