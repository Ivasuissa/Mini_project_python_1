from Classes import file_handler
from Classes import log


FileHandler = file_handler.FileHandler



class User:
    def __init__(self):
        self.name_list = []
        self.users = FileHandler()
        self.log = log.Logger()

    def user_auth(self, name, password):
        self.users.load_from_csv("/Users/evasuissa/Desktop/ITC2/Python/day1-alone/Mini_project_python_1/csv_files/user.csv")
        try:
            for item in self.users.data_info:
                self.name_list.append(item[1])

        except Exception as error:
            print(error)

        try:
            if name in self.name_list:
                print("yes we found " + name)
                name_index = self.name_list.index(name)
                self.log.add_to_log("We found the same name")
            else:
                print("no name in list")

        except Exception as error:
            print(error)


        try:
            if str(password) == self.users.data_info[name_index][3]:
                print("password is correct")
                self.log.add_to_log("The password is the same")
            else:
                print("password is wrong")

        except Exception as error:
            print(error)


user = User()
role = user.user_auth("amir", "12345678")

