import csv
from Classes import log



class FileHandler:

    def __init__(self):
        self.data_info = []
        self.log = log.Logger()

    def load_from_csv(self,file_name):

        try:
            with open(file_name, newline='') as csv_file:
                cvs_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                try:
                    for row in cvs_reader:
                        self.data_info.append(row)
                        line_count += 1
                    self.log.add_to_log("The cvs_file has been loaded ")
                except Exception as error:
                    print("There is an error with forloop:" + str(error))
        except Exception as error:
            print("There is an error with open file:" + str(error))
            self.log.add_to_log("We wasn't able to open the file")

        print(self.data_info)
        return self.data_info

    def append_to_csv(self, file_name, data):
        id_list =[]
        print(self.data_info)
        try:
            with open(file_name, newline='') as csv_file:
                cvs_reader = csv.reader(csv_file, delimiter=',')
                for row in cvs_reader:
                    length_row = len(row) #need to find a better way to get the len(row) without a for loop
                    id_list.append(row[0])
            print(id_list)
        except Exception as error:
            print("There is an error with open file:")
            print(error)
        try:
            if length_row == len(data):
                print("length is ok")
                if data[0] not in id_list:
                    print("id is ok")
                    with open(file_name, mode='a', newline ='') as csv_file:
                        data_writer = csv.writer(csv_file, delimiter=',')
                        data_writer.writerow(data)
                        self.log.add_to_log("New user added successfully")
                        return self.data_info
                else:
                    print("the id exist already")
            else:
                print("not enough informations, you have " + str(len(data)) + " values and should have " + str(length_row))
        except Exception as error:
            print("There is an error to append")
            print(error)


file = FileHandler()

file.append_to_csv("/Users/evasuissa/Desktop/ITC2/Python/day1-alone/Mini_project_python_1/csv_files/user.csv", ['29', 'Albert', 'Suissa', '12345678', 'consultantr', '10000', 'consultant'])
file.load_from_csv("/Users/evasuissa/Desktop/ITC2/Python/day1-alone/Mini_project_python_1/csv_files/user.csv")
