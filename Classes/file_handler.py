import csv


class FileHandler:

    def __init__(self):
        self.data_info = []

    def load_from_csv(self,file_name):

        try:
            with open(file_name, newline='') as csvfile:
                data =  csv.reader(csvfile, delimiter=',')
                line_count = 0
                try:
                    for row in data:
                        if line_count == 0:
                            line_count += 1
                        else:
                            self.data_info.append(row)
                except Exception as error:
                    print("There is an error with forloop:")
                    print(error)
        except Exception as error:
            print("There is an error with open file:")
            print(error)

        print(self.data_info)
        return self.data_info


file = FileHandler()
file.load_from_csv("/Users/evasuissa/Desktop/ITC2/Python/day1-alone/Mini_project_python_1/csv_files/user.csv")

