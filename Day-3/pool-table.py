from datetime import datetime
from time import strftime
from pool_table_class import PoolTable

pool_tables_arr = []


def display_pool_tables():
    for table in pool_tables_arr:
        print(f"\nPool table {table.table_no}--is vacant: {table.is_vacant}")
        
        if table.is_vacant == False:
            checkout_time = table.start_time.strftime("%b %d %Y %H:%M:%S")
            print(f"Checkout Time {checkout_time}")
            
               

def display_available_tables():
    for table in pool_tables_arr:
        if table.is_vacant == True:
            print(f"\n Pool table {table.table_no}")

def display_checked_out_tables():
    for table in pool_tables_arr:
        if table.is_vacant == False:
            print(f"\n Pool table {table.table_no}")


for index in range(1, 13):
    table = PoolTable(index)
    pool_tables_arr.append(table)


while True:
 
    print("")
    print("1 to Check out a pool table")
    print("2 to Check in a pool table")
    print("3 to Display all tables")
    print("4 to Quit")
    print("")

    option = int(input("Enter your option: "))

    if option == 1:
        
        display_available_tables()
                 
        check_out_no = int(input("\n Enter the pool table number you wish to check out: ")) 
        if pool_tables_arr[check_out_no - 1].is_vacant == False:
            print(f"\n**Pool table {check_out_no} is curently occupied**")
        
        ch_out_choice = pool_tables_arr[check_out_no - 1]
        ch_out_choice.checking_out()

    if option == 2:

        display_checked_out_tables()

        check_in_no = int(input("\nEnter the pool table number you wish to check in: "))
        if pool_tables_arr[check_in_no - 1].is_vacant == True:
            print(f"\n**Pool table {check_in_no} is curently available**")
        ch_in_choice = pool_tables_arr[check_in_no - 1]
        ch_in_choice.checking_in()

        

    if option == 3: 

        display_pool_tables()

      
    if option == 4:
        break