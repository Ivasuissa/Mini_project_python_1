from Mini_project_python_1.Classes.file_handler import load_from_csv

file_name = "/Users/evasuissa/Desktop/ITC2/Python/day1-alone/Mini_project_python_1/csv_files/user.csv"

def user_auth(name, password):

    name_list = []

    data_info = load_from_csv(file_name)

    try:
        for item in data_info:
            name_list.append(item[1])

    except Exception as error:
        print(error)

    try:
        if name in name_list:
            print("yes we found " + name)
        else:
            print("no")



    except Exception as error:
        print(error)


user_auth("amir", "123456")
