import csv #import csv library in order to be able to read csv files.

NAME_FILE = "places.csv" #Constant value for showing filename.

class PlaceCollection():

    def read(self):
        #This method is used for adding list of the data from csv files readed.
        with open(NAME_FILE, mode='r') as file:# open functions for open files but only in read mode.
             reader = csv.reader(file)#use csv functions imported above to be able to read the file.
             for row in reader: #This loops is to read the data in csv data based on each line.
                 self.data.append(list(row)) #the data each line from csv file will be added in data variable.
        file.close()#even with function is closing the files , i make more close function to make sure the files close.
    def sort(self,sort_by):
        #This method is used for sorting the data that already read based on choice that user choose.
        #each choice is already set in dictionary in main files, for example : sort by visited function means sort by value 3.
        if sort_by == 0:
            #sort by city name
            self.sorted_data = sorted(self.data,reverse=False, key=lambda row: (row[0], int(row[2]))) #This variable is for containing sorted data based on choice
        elif sort_by == 1:
            #sort by Country
            self.sorted_data = sorted(self.data, reverse=False, key=lambda row: (row[1], int(row[2]))) #This variable is for containing sorted data based on choice
        elif sort_by == 2:
            #Sort by Priority
            self.sorted_data = sorted(self.data, reverse=False, key=lambda row: (int(row[2]))) #This variable is for containing sorted data based on choice
        elif sort_by == 3:
            #sort by Visited place
            self.sorted_data = sorted(self.data, reverse=False, key=lambda row: (row[3], int(row[2]))) #This variable is for containing sorted data based on choice
        elif sort_by == 4:
            #sort by unvisited place
            self.sorted_data = sorted(self.data, reverse=True, key=lambda row: (row[3], int(row[2]))) #This variable is for containing sorted data based on choice[ This one is the same with number 3 with special occasion to reverse the value]
    def add(self):
        #This method is used for adding the place to the data based on user input that already through many error check.
        self.new_place.append("n") #this append function is to add fixed value for new added place will be unvisited.
        self.data.append(self.new_place) #after all files have been checked and true it will be append or add in main data list.

    def save(self):
        #This method is used for saving the data list that have been modified in the end that used in on_stop applications.
        with open(NAME_FILE, mode='w', newline="") as files: #have the same function for opening files but in write mode.
            writer = csv.writer(files) #use csv functions imported above to be able to read the file.
            for row in self.sorted_data: #loop for read each line of the data list and add them one by one that already sorted.
                writer.writerow(row) #write the list of data in the files.
        files.close()#even with function is closing the files , i make more close function to make sure the files close.
    def visit_place(self):
        # Function to count unvisited places and keep tracking of unvisited place
        count_visit = 0 #variable to make 0 value at start and will be added if the loop data show visit.
        for row in self.data: #loop for reading the data in side the data list.
            if row[3] == "n": #conditions in data that get from data list for checking if its unvisited
                count_visit += 1 #if the conditions are met the variable count_visit is added by 1
        return count_visit #after the loops end it can return the unvisited place.
    def check_number(self,user_input):
        #This method is used for check if there is number in the user input.
        data = list(user_input) # the data get from the user input will be put in list.
        counter = 0 #this variable is used for count how many number
        for i in data: #loops for check if its a digit or not.
            x = i.isdigit() #with this function it will check if its digit or not
            if x: #if its results true it will add the value of count 1
                counter += 1
            else: #else it will keep the value of the counter
                counter = counter
        if counter > 0: # if counter is more than 0 or there is number in the user input it will results False
            return False
        else: #else if there is no number it will return True and pass the values.
            return True
    def check_symbol(self,user_input):
        #This method is used for check if there is symbol in the user input.
        data = list(user_input) # the data get from the user input will be put in list.
        counter = 0 #this variable is used for count how many symbols
        for i in data:#loops for check if its include symbol or not.
            SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
            if i in SPECIAL_CHARACTERS: #with this loop it will check every data if its include the symbol or not , if so it will add counter with 1.
                counter += 1
            else:#else it will keep the value of the counter
                counter = counter
        if counter > 0:  # if counter is more than 0 or there is symbol in the user input it will results False
            return False
        else: #else if there is no number it will return True and pass the values.
            return True
    def priority_check(self, user_input):
        #This method is used for check priority check input by the users.
        try:
            if int(user_input) <= 0: #first its try check the user_input if its valid which means positive numbers.
                self.root.ids.status.text = "Priority us be > 0" #if it is it will return text in status bar in applications.
            elif user_input == "":#first its try check the user_input if its valid which its not empty.
                self.root.ids.status.text = "All fields must be completed"#if it is it will return text in status bar in applications.
            else:
                return int(user_input) #if all conditions are met and no error it will returning user input.
        except ValueError: #With this except it will check and prevent error of the program if user not inputting integer data types
            if user_input == "":#first its try check the user_input if its valid which its not empty.
                self.root.ids.status.text = "All fields must be completed"#if it is it will return text in status bar in applications.
            else:# if users put wrong number mixed with text it will show this.
                self.root.ids.status.text = "Please enter a valid number"#if it is it will return text in status bar in applications.
    def error_check(self, checking):
        #This method is used for check user input in city and country inputed by the users.
        if checking == "":#first its try check the user_input if its valid which its not empty.
            self.root.ids.status.text = "All field must be completed"#if it is it will return text in status bar in applications.
        elif not self.check_number(checking):# This will call the method for check if the value consist number or not. if its true then will ask for input correct name.
            self.root.ids.status.text = "Please input correct name"#if it is it will return text in status bar in applications.
        elif not self.check_symbol(checking):# This will call the method for check if the value consist number or not. if its true then will ask for input correct name.
            self.root.ids.status.text = "Please input correct name"#if it is it will return text in status bar in applications.
        else:
            return checking.capitalize() #returning value after every error check have been fulfilled and to make sure sort in correct way all user input will be capitalized.


