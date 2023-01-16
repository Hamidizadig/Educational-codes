class User:
    UsreName = 'abcd'
    Password = '1234'

    def isCorrect(self, userName, password):
        return self.UserName == userName and self.Password == password
userName = input('Enter user name : ')
password = input('Enter password : ')
user1 = User()
if user1.isCorrect(userName, password) == True:
    print('Correct')
else:
    print('Not Correct')