shopping_lists = []

   
class ShoppingList:
    def __init__(self, title, address):
        self.title = title
        self.address = address
        self.items = []
        
        
class Items:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity 
    

while True:

    print("")
    print("1 to Add a store to your shopping list")
    print("2 to Add items to your shopping list")
    print("3 to View your shopping lists")
    print("4 to delete a store from your shopping list")
    print("5 to delete items from your shopping list")
    print("6 to Quit")
    print("")
    try:
        option = int(input("Enter your option: "))
    
    
        if option == 1:
            store_name = input("Enter store name: ")
            store_address = input("Enter store address: ")
            store = ShoppingList(store_name, store_address)
            shopping_lists.append(store)

        elif option == 2:
        
            for index in range(0, len(shopping_lists)):
                store = shopping_lists[index]
                print(f"{index + 1} - {store.title}")
                
            store_index = int(input("Enter the store number: "))
            item_name = input("Enter the name of the item: ")
            price = float(input("Enter the price: "))
            quantity = int(input("Enter the quantity: "))
            item = Items(item_name, price, quantity)
            
            shopping_lists[store_index -1].items.append(item)
        
        

        elif option == 3:
            
            for index in range(0, len(shopping_lists)):
                store = shopping_lists[index]
                print(f"{index + 1} {store.title}")
                
                for index in range(0, len(store.items)):
                    title = store.items[index].title
                    quantity = store.items[index].quantity 
                    print(f" - {title} ({quantity})")
        
        elif option == 4:
            for index in range(0, len(shopping_lists)):
                store = shopping_lists[index]
                print(f"{index + 1} - {store.title}")
                
            delete_store = int(input("Enter the store number that you wish to delete: "))
            del shopping_lists[delete_store - 1]

        elif option == 5:
            
            for index in range(0, len(shopping_lists)):
                store = shopping_lists[index]
                print(f"{index + 1} {store.title}")
                
                for index in range(0, len(store.items)):
                    title = store.items[index].title
                    quantity = store.items[index].quantity 
                    print(f"   {index +1} - {title} ({quantity})")
                    
            delete_item_store = int(input("Enter the store number that you wish to delete an item from: "))
            store = shopping_lists[delete_item_store - 1]
            for index in range(0, len(store.items)):
                print(f"{index + 1} {store.items[index].title}")

            delete_item = int(input("Enter the number of the item that you wish to delete: "))
            del store.items[delete_item - 1]

        
        elif option == 6:
            break

    except ValueError:
        print("Invalid input. Please enter a number, not a letter: ")