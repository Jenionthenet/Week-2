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
        self.total_time_min = None
        self.start_time_min = None
        self.end_time = None
        self.total_cost_per_hour = 30.0
        self.total_cost = 0.00
        
   
    def display_min_played(self):
        self.total_time = self.end_time - self.start_time
        self.total_time_min = round(self.total_time.total_seconds()/60) 
        if self.total_time_min < 60:
            print(f"Total time checked out: {self.total_time_min} minutes")
        else:
            hours = math.floor(self.total_time_min/60)
            minutes = ((self.total_time_min/60) - hours) * 60
            print(f"Total time checked out: {hours} hours and {minutes} minutes")

    def checking_in(self):
        self.is_vacant = True
        self.end_time = datetime.now()
        self.end_time_min = datetime.now().minute
        self.total_time = self.end_time - self.start_time
        self.total_time_min = self.total_time.total_seconds() / 60
        self.total_cost = (self.total_cost_per_hour/60) * self.total_time_min
        #self.display_min_played()
        #elf.total_time_min = self.end_time_min - self.start_time_min 
        #if self.total_time_min < 60:
            #print(f"Total time checked out: {self.total_time_min} minutes")
        #else:
            #hours = math.floor(self.total_time_min/60)
            #minutes = ((self.total_time_min/60) - hours) * 60
            #print(f"Total time checked out: {hours} hours and {minutes} minutes")
        
        
         
      

    def checking_out(self):
        self.is_vacant = False
        self.start_time = datetime.now()
        self.start_time_min = datetime.now().minute 
       
        
    
