"""
Replace the contents of this module docstring with your own details
Name: Richard Setiawan
Date started:29 July 2019
GitHub URL: https://github.com/JCUS-CP1404/jcus-cp1404-assg1-01richardrs
"""

import csv

NAME_FILE = "places.csv"

class a1():

    def read_files(self):
        # Read and store files inside the CSV files
        csv_data = []
        with open(NAME_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                csv_data.append(list(row))
        file.close()
        return csv_data

    def check_total_place(self,user_input, data):
        # Function to check availability of list places number
        sorted_data = sorted(data, key=lambda row: (row[3], int(row[2])))
        count_place = 0
        for a in sorted_data:
            count_place += 1
        if int(user_input) > count_place:
            return False
        else:
            return True

    def check_place_mark(self,user_input, data):
        # Function to check if the place is already visited or not
        sorted_data = sorted(data, key=lambda row: (row[3], int(row[2])))
        count_place = 0
        for row in sorted_data:
            count_place += 1
            if count_place == int(user_input):
                if row[3] == "v":
                    return False
                else:
                    return True

    def check_num(self,user_input):
        # Function to check is there any number in input
        data = list(user_input)
        counter = 0
        for i in data:
            x = i.isdigit()
            if x:
                counter += 1
            else:
                counter = counter
        if counter > 0:
            return False
        else:
            return True

    def check_symbol(self,user_input):
        # Function to check symbol in user input
        data = list(user_input)
        counter = 0
        for i in data:
            SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
            if i in SPECIAL_CHARACTERS:
                counter += 1
            else:
                counter = counter
        if counter > 0:
            return False
        else:
            return True

    def visit_place(self,data):
        # Function to count visited places
        count_visit = 0
        count = 0
        for row in data:
            count += 1
            if row[3] == "n":
                count_visit += 1
        return count_visit, count

    def list_data(self,visited, data):
        # Function to list the data from CSV files that already make in list
        counting = 0
        sorted_data = sorted(data, key=lambda row: (row[3], int(row[2])))
        for a in sorted_data:
            if a[3] == "n":
                print("*{0:>2}.{1:<10} in {2:<12} priority {3:>5}".format(counting + 1, a[0], a[1], a[2]))
            else:
                print(" {0:>2}.{1:<10} in {2:<12} priority {3:>5}".format(counting + 1, a[0], a[1], a[2]))
            counting += 1
        if visited == 0:
            print("{0} places. No places left to visit. Why not add a new place?".format(counting))
        else:
            print("{0} places. You still want to visit {1} places.".format(counting, visited))

    def add_data(self,data):
        # Function to add data or places to the list of the CSV files
        new_places = []
        while True:
            place_name = str(input("Name: ")).capitalize()
            if place_name == "":
                print("Input can not be blank")
            elif not self.check_num(place_name):
                print("Please input correct name")
            elif not self.check_symbol(place_name):
                print("Please input correct name")
            else:
                break

        while True:
            country_name = str(input("Country: ")).capitalize()
            if country_name == "":
                print("Input can not be blank")
            elif not self.check_num(country_name):
                print("Please input correct name")
            elif not self.check_symbol(country_name):
                print("Please input correct name")
            else:
                break

        while True:
            try:
                priority_num = int(input("Priority: "))
                if priority_num <= 0:
                    print("Number must be >0")
                else:
                    break
            except ValueError:
                print("Invalid input; enter a valid number")
        mark_visited = "n"
        print("{0} in {1} (priority {2}) added to Travel Tracker".format(place_name, country_name, priority_num))
        new_places.append(place_name)
        new_places.append(country_name)
        new_places.append(priority_num)
        new_places.append(mark_visited)
        data.append(new_places)

    def mark_data(self,visited, data):
        # Function to mark visited place
        self.list_data(visited, data)
        counter = 0
        sorted_data = sorted(data, key=lambda row: (row[3], int(row[2])))
        print("Enter the number of a place to mark as visited")

        while True:
            try:
                user_input = int(input(">>> "))
                if user_input <= 0:
                    print("Number must be > 0")
                    continue
                elif not self.check_total_place(user_input, data):
                    print("Invalid place number")
                    continue
                elif self.check_place_mark(user_input, data) == False:
                    print("That Place is already visited")
                break
            except ValueError:
                print("Invalid Input; Enter a valid number")

        for row in sorted_data:
            counter = counter + 1
            if counter == int(user_input):
                if row[3] != "v":
                    print("{} in {} visited!".format(row[0], row[1]))
                    row[3] = "v"

    def write_data(self,NAME_FILE, data):
        # Function to sort the data at last
        sorted_data = sorted(data, key=lambda row: (row[3], int(row[2])))
        with open(NAME_FILE, mode='w', newline="") as files:
            writer = csv.writer(files)
            for row in sorted_data:
                writer.writerow(row)

    def menu(self):
        # Function to show menu and ask user_choice
        print("Menu: ")
        print("L - List places")
        print("A - Add new place")
        print("M - Mark a place as visited")
        print("Q - Quit")
        user_choice = input(">>> ").upper()
        return user_choice

    def get_option(self,csv_data, NAME_FILE):
        # Function to check and direct user_choice
        option = self.menu()
        while option != "Q":
            visited = self.visit_place(csv_data)
            if option == "L":
                self.list_data(visited[0], csv_data)
                option = self.menu()
            elif option == "A":
                self.add_data(csv_data)
                option = self.menu()
            elif option == "M":
                if visited[0] > 0:
                    self.mark_data(visited[0], csv_data)
                    option = self.menu()
                else:
                    print("No unvisited place")
                    option = self.menu()
            else:
                print("Invalid menu Choice")
                option = self.menu()
        self.write_data(NAME_FILE, csv_data)

    def main(self):
        data = self.read_files()
        print("Travel Tracker 1.0 - by Richard Setiawan")
        print("{0} places loaded from {1}".format(self.visit_place(data)[1], NAME_FILE))
        self.get_option(data, NAME_FILE)
        print("{0} places saved to {1}".format(self.visit_place(data)[1], NAME_FILE))
        print("Have a nice day :)")

if __name__ == '__main__':
    a1.main()

