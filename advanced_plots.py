import csv
import plotter
import re

def plot_grades(filename, firstname, lastname):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        first_name_pattern = firstname + ", [A-Za-z]*"
        last_name_pattern = ", " + lastname
        for record in csv_reader:
            if re.findall(first_name_pattern,record[0]) and re.findall(last_name_pattern, record[0]):
                plotter.init(record[0], "Grade Item", "Score")
                plotter.new_series("Series 1")
                for index in range(len(record)):
                    if index > 2:
                        plotter.add_data_point(float(record[index]))
                plotter.plot()
        else:
            print("Could not find any matched result, aborting")

def get_average(filename, column):
    with open(filename) as file:
        csv_reader =csv.reader(file)
        next(csv_reader)
        total_score = 0
        counter = 0
        for record in csv_reader:
            counter += 1
            try:
                total_score += float(record[column])
            except:
                print("Not able to convert", record[column], " to a float value...skipping")
                continue
        print("Average of a given column is: ", (total_score/counter))
        

plot_grades("data/full_grades_010.csv", "Tsiatsos", "Shamella")
get_average("data/full_grades_010.csv", 4)