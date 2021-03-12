class Customer:
    def __init__(self): #Class constructor
        self.name = ""
    def set_type(self):
        while True:
            try:
                self.type = int(input("Would you like to Enter as a Loyal Customer(1) or Bargain Hunter(2)?"))
                if self.type == 1:
                    return Loyal_Customer()
                elif self.type == 2:
                    return Bargain_Hunter()

            except ValueError:
                print("Invalid input")
    def __str__(self):  #Class print instance
        result = "Welcome {}, choose from the options below\n".format(self.name)
        return result

class Loyal_Customer(Customer): #Sub class of customer
    def __init__(self): #Class constructor
        super().__init__()
        self.name = str(input("Enter customer name"))
    def Loyal(self):    #Returns true if loyal
        return True
    def history_list(self,bought_items= None):  #Default product history to none
        print("Here's your purchase history",self.name,"\n",(bought_items))
    def get_products(self):
        self.products = {"Bracelet": "35", "Necklace": "30", "Ring": "25", "Bag": "45", "Shoes": "40", "Hat": "20",
                           "Watch": "30"}
        return self.products
    def __str__(self):  #Class print instance
        result = super().__str__() + "We appreciate your loyalty.\n"
        return result

class  Bargain_Hunter(Customer):
    def __init__(self): #Class constructor
        super().__init__()
        self.name = str(input("Enter customer name"))
    def Loyal(self):    #Returns true if loyal
        return False
    def history_list(self):
        print("Unable to view history as you're not a loyal customer")
    def get_products(self): #Returns product list
        self.products = {"Necklace": "30", "Ring": "25", "Bag": "45", "Shoes": "40", "Hat": "20"}
        return self.products
    def __str__(self):  #Class print instance
        result = super().__str__() + "You have reduced access to products\n"
        return result

class Shopping_Cart:
    def __init__(self): #Class constructor
        self.__itemdict= {}
        self.__counter = 0
    def __add__(self, other):   #Addition overload instance
        self.__counter+= 1  #Basket counter
        self.__itemdict[self.__counter]=[other] #Value
    def __sub__(self, other):   #Subtract overload instance
        for key, value in self.__itemdict.items():
                if other in value:
                    del self.__itemdict[key]
                    return  #Breaks instance
        print("No such item")   #Error check if not in dicitonary
    def __str__(self):  #Class print instance
        result=""
        for key,value in self.__itemdict.items():
            result +="{}. {}\n".format(key,value)
        return result
    def get_items(self):    #returns the dictionary privately
        return self.__itemdict.items()

class Address:  #Class to print and set address information
    def __init__(self): #Class constructor
        self.__line1 = ""
        self.__line2 = ""
        self.__postcode = ""
    def set_address(self):  #Instance to set variables in constructor
        try:
            self.__line1 = str(input("      Address line 1: "))
            self.__line2 = str(input("      Address line 2: "))
            self.__postcode = str(input("      Postcode: "))
        except ValueError:
            print("Input error")
    def __str__(self):
        result = ('Address line1:{:>10s}\nAddress line2:{:>10s}\nPostcode:{:>10s}\n'.format(self.__line1,self.__line2,self.__postcode))
        return result
class Payment:  #Class to print and set payment information
    def __init__(self): #Class constructor
        self.__Card_No = ""
        self.__Card_Exp = ""
        self.__Card_CVC = ""
    def set_Payment(self):  #Instance to set variables in constructor
        while True:
            try:
                self.__Card_No = int(input("      Card No.: "))
                self.__Card_Exp = str(input("      Card expiry: "))
                self.__Card_CVC = int(input("      Card CVC: "))
                break
            except ValueError:
                print("Input error")
                pass
    def __str__(self):
        result = ('Card No.:{:>10d}\nCard expiry:{:>10s}\nCard CVC:{:>10d}\n'.format(self.__Card_No,self.__Card_Exp,self.__Card_CVC))
        return result
def main():
    """The function called by the program that operates the program requirements"""
    existing_customer = 0   #Ensure customer exists
    emptycart=1 #Cart is empty at start
    my_shopping_cart = Shopping_Cart()  #Creates the basket class
    bought_items = None #Blank purchase history
    menuu=0
    while True: #Menu always runs
        menu()
        if existing_customer == 1 and my_customer_type.Loyal() is True: #Checks if loyal customer
            print("6. Purchase History")
            if menuu==6:
                my_customer_type.history_list(bought_items) #Calls class instance to print history
        try:
            menuu=int(input())
        except ValueError:
            print("Try again")
            break   #Must start over if fail the menu
        if (menuu!=1 and existing_customer==0): #Error check customer exists
            print("Create customer first")
        elif(menuu==1): #Creates customer
            existing_customer=1
            my_customer = Customer()    #Creates customer class
            my_customer_type=my_customer.set_type()
            product_list=my_customer_type.get_products()
            print(my_customer_type.__str__())  #Prints customer class print instance
        elif(menuu==2): #List products
            List_products(product_list)
        elif(menuu==3): #Change cart
            emptycart=Change_cart(my_shopping_cart,product_list)    #Calls change cart function that returns emptcart
        elif(menuu==4): #Shows cart
            Show_cart(my_shopping_cart)
        elif (menuu == 5 and emptycart == 1):   #Checks cart is not empty
            print("Add a product to cart first")
        elif (menuu == 5 and emptycart == 0):   #Go to checkout
            bought_items = checkout(my_shopping_cart, product_list)
        else:   #Menu error value check
            print("Invalid option")

def menu():
    """Prints the menu for the program"""
    print("1. Create a customer\n"
          "2. List products\n"
          "3. Add/remove a product from the shopping cart\n"
          "4. See current shopping cart\n"
          "5. Checkout")

def List_products(product_list):
    """Prints available products for customer"""
    for k,v in product_list.items():
        print(k,"   €"+v)

def Change_cart(my_shopping_cart,product_list):
    """Takes the shopping cart created and the general list of products"""
    while True:
        retry=0
        while True:
            try:
                add_remove = int(input("1 to add and 2 to remove"))
                break   #Breaks current while
            except ValueError:  #Check value error
                print("Invalid input")
                pass #Tries again
        if add_remove == 1:
            add_item=str(input("Enter item name to add to cart\n"))
            if add_item.title() in product_list:    #Propers the input string and cheks product dictionary
                my_shopping_cart+=(add_item.title())       #Overload my_shopping_cart class
                empty_cart = 0  #Cart not empty
            else:
                print("Item not in product list\nPress 1 to try adding again or anything else to return.")
                try:
                    retry=int(input())
                except ValueError:
                    print("Invalid input")
                    empty_cart = 1
                    break #Breaks current while, goes to return at the end
                empty_cart = 1  #Cart still empty
            if retry != 1:
                break
        elif add_remove == 2:
            remove_item = str(input("Enter item name to remove from cart\n"))
            my_shopping_cart-=(remove_item.title()) #Goes to sub instance in cart class to remove proper of input
            empty_cart = 0
            break
    return empty_cart   #back to main

def Show_cart(my_shopping_cart):
    """Prints the contents of the item cart"""
    print(my_shopping_cart) #Goes to str instance in cart class

def checkout(my_shopping_cart,product_list):
    """Checkout with subtotal, billing and delivery info. Again the cart and general product list is passed"""
    total=0
    your_address = Address()    #Creates address class
    your_payment = Payment()    #Creates payment class
    for k,v in my_shopping_cart.get_items():
        total=total+int(product_list[str(v[0]).translate(string.punctuation)])  #Index product list with dictionary value abd add to total as integer
        print(k,".      "+str(v[0]).translate(string.punctuation),"     €"+product_list[str(v[0]).translate(string.punctuation)])   #Prints cart info
    print("Subtotal =",total)
    print("Enter delivery info:")
    your_address.set_address()  #Goes to set address instance
    print("Enter payment info:")
    your_payment.set_Payment()  #Goes to set payment instance
    print("Would you like a review of your information?")
    if str(input("Y/N"))== "Y": #Print review
        print(your_address,your_payment,"Items:\n",my_shopping_cart,"Subtotal =",total)
    print("Confirming payment...")
    print("Shipment will arrive @...")
    bought_items=(my_shopping_cart.get_items())
    return bought_items

def test():
    menu()
    products = {"Bracelet": "35", "Necklace": "30", "Ring": "25", "Bag": "45", "Shoes": "40", "Hat": "20",
                "Watch": "30"}
    my_shopping_cart=Shopping_Cart()
    List_products(products)
    Change_cart(my_shopping_cart,products)
    Show_cart(my_shopping_cart)
    checkout(my_shopping_cart,products)

#MAIN CODE
import string   #For string punctuation and title methods
main()  #Call main function

#test()