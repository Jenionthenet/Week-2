from datetime import datetime
from datetime import date 
from time import strftime
import math

class PoolTable:
    def __init__(self, table_no): 
        self.table_no = table_no
        self.is_vacant = True
        self.start_time = None
        self.end_time = None
        self.total_time = None
        self.start_time_min = None
        self.end_time = None
        
    def save_to_file(self):
        #with open("pool_tables.txt", "w") as file:
            #file.write(str(self.number))
            #convert date to string
            #file.write(#date changed to string)
        date = str(date.today())
        ext = "txt"
        file_name = date + ext
        with open(file_name, "a") as  file:
            file.write(str(self.table_no))
            file.write(self.start_time)
            file.write(self.end_time)
            file.write(self.total_time)
            
    def checking_in(self):
        self.is_vacant = True
        self.end_time = datetime.now()
        self.end_time_min = datetime.now().minute
        #self.save_to_file()
        self.total_time_min = self.end_time_min - self.start_time_min 
        if self.total_time_min < 60:
            print(f"Total time checked out: {self.total_time_min} minutes")
        else:
            hours = math.floor(self.total_time_min/60)
            minutes = ((self.total_time_min/60) - hours) * 60
            print(f"Total time checked out: {hours} hours and {minutes} minutes")
        
        save_to_file()
        #while True:
        

    def checking_out(self):
        self.is_vacant = False
        self.start_time = datetime.now()
        self.start_time_min = datetime.now().minute 
        #self.save_to_file()
        
    
