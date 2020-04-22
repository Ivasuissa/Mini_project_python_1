from Classes.file_handler import load_from_csv

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
            print(name_list.index(name))
            name_index = name_list.index(name)
        else:
            print("no name in list")

    except Exception as error:
        print(error)


    try:
        if str(password) == data_info[name_index][3]:

            print("password is correct")
        else:
            print("password is wrong")

    except Exception as error:
        print(error)


user_auth("amir", "12345678")
