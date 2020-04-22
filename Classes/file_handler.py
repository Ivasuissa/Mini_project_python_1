import csv

data_info = []

def load_from_csv(file_name):

    try:
        with open(file_name, newline='') as csvfile:
            data =  csv.reader(csvfile, delimiter=',')
            try:
                for row in data:
                    data_info.append(row)
            except Exception as error:
                print("There is an error with forloop:")
                print(error)
    except Exception as error:
        print("There is an error with open file:")
        print(error)
    return data_info




#load_from_csv("/Users/evasuissa/Desktop/ITC2/Python/day1-alone/csv_files/user.csv")

#print(data_info)