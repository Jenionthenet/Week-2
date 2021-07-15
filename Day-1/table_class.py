class Table:
    def _init_(self):
        self.height = 0.0
        self.shape = ""
        self.width = 0.0
        self.material = ""
        self.color = ""
        self.function = ""

# height and width are in feet
table = Table()
table.height = 1 
table.shape = "oval"
table.width = 2 
table.material = "glass"
table.color = "black"
table.function = "coffee"

table_2 = Table()
table_2.height = 2.5 
table_2.shape = "rectangle"
table_2.width = 3
table_2.material = "plywood"
table_2.color = "red"
table_2.function = "dining"

table_3 = Table()
table_3.height = 2.42
table_3.shape = "kidney"
table_3.width = 4.17
table_3.material = "ebony"
table_3.color = "black"
table_3.function = "desk"
