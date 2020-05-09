from os import path
import pandas as pd

def create_LocalDatabaseServiceRoutines():
    return LocalDatabaseServiceRoutines()

class LocalDatabaseServiceRoutines(object):
    def __init__(self):
        self.name = 'Cron Jobs'
        self.index = {}
        self.userdata = path.join(path.dirname(__file__), '../static/Data/users.csv')

    def ReadCSVUsersDB(self):
        df = pd.read_csv(self.userdata)
        return df

    def WriteCSVToFile_users(self, df):
        df.to_csv(self.userdata, index=False)

    def IsUserExist(self, username):
        df = self.ReadCSVUsersDB()
        df = df.set_index('username')
        return (username in df.index.values)

    def IsLoginGood(self, username, password):
        df = self.ReadCSVUsersDB()
        df=df.reset_index()
        selection = [username]
        df = df[pd.DataFrame(df.username.tolist()).isin(selection).any(1)]

        df = df.set_index('password')
        return (password in df.index.values)
     
    def AddNewUser(self, User):
        df = self.ReadCSVUsersDB()
        dfNew = pd.DataFrame([[User.firstname.data, User.lastname.data, User.username.data, User.password.data]], columns=['firstname', 'lastname', 'username', 'password'])
        dfComplete = df.append(dfNew, ignore_index=True)
        self.WriteCSVToFile_users(dfComplete)
