import json

class User:
    def __init__(self):
        self.login = None
        self.password = None
        self.server = None

    @staticmethod
    def save_credentials(login, password, server):
        login_data = {
            'login': login,
            'password': password,
            'server': server
        }
        with open('credentials.json', 'w') as file:
            json.dump(login_data, file, indent=4)
        
    @staticmethod
    def check_for_credentials():
        try:
            with open('credentials.json') as file:
                data = json.load(file)
            return data
        except:
            print("there's no saved credentials")
            return None