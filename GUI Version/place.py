from placecollection import PlaceCollection as pc #import placecollections classes as name pc that contains lot of function needed like read data,save ,etc.

class Place (pc):

    def __init__(self):
        #This method is automatically initialized when Place class is called.
        self.data=[] #this variable in Place that used for contain the data read from the csv files.
        self.new_place = [] #this variable in in Place that is used for contain correct user input that passed from main and give it to place collection that will be add later.
        pc.read(self) #calling method in place collections for containing the data from csv files.

    def mark_place(self,xy):
        #This method is used for marking place when the button of place is pressed.
        x=int(xy) - 1 #this variable is used to concate str to int and since list start from 0 so the value is minus by 1
        if self.sorted_data[x][3] != "v": #check the conditions of the selected data is visited or not if its not it will be changed to visited.
            self.sorted_data[x][3] = "v"#changed the value of unvisited to visited.
            if self.priority_place(x):#check if the place is important or not if its True it will give different print in status bar.
                self.root.ids.status.text = "You visited {0} in {1} . Great Travelling!".format(self.sorted_data[x][0], self.sorted_data[x][1]) #if its important or True will print this
            else:
                self.root.ids.status.text = "You Visited {0} in {1} .".format(self.sorted_data[x][0], self.sorted_data[x][1])#if its important or False will print this
        else: #check the conditions of the selected data is visited or not if its not it will be changed to visited.
            self.sorted_data[x][3] = "n"#changed the value of unvisited to visited.
            if self.priority_place(x):#check if the place is important or not if its True it will give different print in status bar.
                self.root.ids.status.text = "You Need to visit {0} in {1} . Get Going!".format(self.sorted_data[x][0],
                                                                                  self.sorted_data[x][1])#if its important or True will print this
            else:
                self.root.ids.status.text = "You Need to visit {0} in {1} .".format(self.sorted_data[x][0],
                                                                                              self.sorted_data[x][1])#if its important or False will print this
        self.sorted(self.root.ids.spinners.text)#after the place is marked it will call the sorted function to sort again after the data list is modified.
    def priority_place(self,x):
        #This method is used for checking if the priority is important or not.
        if int(self.sorted_data[x][2]) <= 2 : #if the conditions are met it will returning True
            return True
        else:# if its false it will return False value that will give different input.
            return False

    def __str__(self):
        # method for test place
        for x in self.data: #loop for loop the data
            return "{},{},{},{}".format(x[3],x[0],x[1],x[2])