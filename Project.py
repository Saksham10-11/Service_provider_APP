# Importing the required modules and packages
import pandas as pd   # <-- To create DataFrames
import webbrowser as web   # <-- To redirect to the given Link


'''************* The below functions are only for the program to run internally**************'''


# Encrypts the input string (Currently there is just the basic encryption)

def encrypt(string):
    encrypted_string = ""
    key = 23
    for i in (string):
        char = chr(ord(i)+key)
        encrypted_string += char
    return encrypted_string


# Extracts the data from the csv file to encrypt it one by one

def Extract_encrypt_Admins(data):
    shape = data.shape
    Column_list = ['PhoneNum', 'FirstName', 'LastName', 'Password']
    for i in range(shape[0]):
        for j in Column_list:
            if j == "PhoneNum":
                string = data.at[i, j]
                string = str(string)
                str1 = encrypt(string)
                data.at[i, j] = str1
            else:
                string = data.at[i, j]
                str1 = encrypt(string)
                data.at[i, j] = str1


#  Extracts the data from the csv file to encrypt it one by one

def Extract_encrypt_Users(data):
    shape = data.shape
    Column_list = ['PhoneNum', 'FirstName', 'LastName', "E-mail", 'Password']
    for i in range(shape[0]):
        for j in Column_list:
            if j == "PhoneNum":
                string = data.at[i, j]
                string = str(string)
                str1 = encrypt(string)
                data.at[i, j] = str1
            else:
                string = data.at[i, j]
                str1 = encrypt(string)
                data.at[i, j] = str1


# Extracts the data from the csv file to encrypt it one by one

def Extract_encrypt_Workers(data):
    shape = data.shape
    Column_list = ['PhoneNum', 'Type', 'FirstName', 'LastName',
                   "E-mail", 'Landmark', 'Distance', 'WebLink']
    for i in range(shape[0]):
        for j in Column_list:
            if j == "PhoneNum":
                string = data.at[i, j]
                string = str(string)
                str1 = encrypt(string)
                data.at[i, j] = str1
            else:
                string = data.at[i, j]
                str1 = encrypt(string)
                data.at[i, j] = str1


# Decrypts the input string

def decrypt(string):
    encrypted_string = ""
    key = 23
    for i in (string):
        char = chr(ord(i)-key)
        encrypted_string += char
    return encrypted_string


# Extract the data one by one from the dataframe to dcrypt it

def Extract_decrypt_Admins(data):
    shape = data.shape
    Column_list = ['PhoneNum', 'FirstName', 'LastName', 'Password']
    for i in range(shape[0]):
        for j in Column_list:
            if j == "PhoneNum":
                string = data.at[i, j]
                str1 = decrypt(string)
                str1 = int(str1)
                data.at[i, j] = str1
            else:
                string = data.at[i, j]
                str1 = decrypt(string)
                data.at[i, j] = str1


# Extract the data one by one from the dataframe to dcrypt it

def Extract_decrypt_Users(data):
    shape = data.shape
    Column_list = ['PhoneNum', 'FirstName', 'LastName', 'E-mail', 'Password']
    for i in range(shape[0]):
        for j in Column_list:
            if j == "PhoneNum":
                string = data.at[i, j]
                str1 = decrypt(string)
                str1 = int(str1)
                data.at[i, j] = str1
            else:
                string = data.at[i, j]
                str1 = decrypt(string)
                data.at[i, j] = str1


# Extract the data one by one from the dataframe to dcrypt it

def Extract_decrypt_Workers(data):
    shape = data.shape
    Column_list = ['PhoneNum', 'Type', 'FirstName', 'LastName',
                   "E-mail", 'Landmark', 'Distance', 'WebLink']
    for i in range(shape[0]):
        for j in Column_list:
            if j == "PhoneNum":
                string = data.at[i, j]
                str1 = decrypt(string)
                str1 = int(str1)
                data.at[i, j] = str1
            else:
                string = data.at[i, j]
                str1 = decrypt(string)
                data.at[i, j] = str1


# Redirects to the link privided

def getDirections(Weblink):
    Browser_path = "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"
    web.register('google-chrome', None,
                 web.BackgroundBrowser(Browser_path))
    browser = web.get('google-chrome')
    browser.open_new_tab(Weblink)


# Generates the OTP

def GenerateOTP():
    from random import randint

    OTP = ''
    for i in range(4):
        digit = randint(0, 9)
        OTP += str(digit)
    return OTP


# Displays the detailed info of the worker which user has asked for

def DisplayDetailedInfo(idx):
    # Extracting the stored worker data
    WorkerData = pd.read_csv("Workers.csv")

    # The row from which the data is to be extracted
    row = int(idx)

    # Extracting the data of the required data
    FirstName = WorkerData.loc[row, 'FirstName']
    LastName = WorkerData.loc[row, 'LastName']
    Profession = WorkerData.loc[row, 'Type']
    Contact = WorkerData.loc[row, 'PhoneNum']
    Email = WorkerData.loc[row, 'E-mail']
    Ladmark = WorkerData.loc[row, 'Landmark']
    Distance = WorkerData.loc[row, 'Distance']
    Weblink = WorkerData.loc[row, 'WebLink']

    # Creating a list of Required data of workers
    List_WorkerData = []
    List_WorkerData.append(decrypt(FirstName))
    List_WorkerData.append(decrypt(LastName))
    List_WorkerData.append(decrypt(Profession))
    List_WorkerData.append(decrypt(Contact))
    List_WorkerData.append(decrypt(Email))
    List_WorkerData.append(decrypt(Ladmark))
    List_WorkerData.append(decrypt(Distance))
    List_WorkerData.append(decrypt(Weblink))

    return List_WorkerData

# Returns the list of available workers


def DisplayAvailabeWorkers(reqLandmark, reqType):
    Landmark_indexes = []
    WorkerType_indexes = []
    WorkerData = pd.read_csv("Workers.csv")
    Extract_decrypt_Workers(WorkerData)
    shape = WorkerData.shape

    # Returns the list in which the Landmark matches the user input
    for i in range(shape[0]):
        if WorkerData.loc[i, "Landmark"] == reqLandmark:
            Landmark_indexes.append(i)
        else:
            pass

    # Returns the list in which the WorkerType matches the user input
    for i in range(shape[0]):
        if WorkerData.loc[i, 'Type'] == reqType:
            WorkerType_indexes.append(i)
        else:
            pass

     # Returns intersection of the two list
    set1 = set(WorkerType_indexes)
    set2 = set(Landmark_indexes)
    Required_indexes = list(set1.intersection(set2))

    AvailableWorkers = []
    Distance_list = []
    Name_list = []
    for i in Required_indexes:
        FirstName = WorkerData.loc[i, 'FirstName']
        LastName = WorkerData.loc[i, 'LastName']
        FullName = FirstName+' '+LastName
        Distance = WorkerData.loc[i, 'Distance']
        AvailableWorkers.append(f'{FullName}   ---- {Distance}')
        Distance_list.append(Distance)
        Name_list.append(FirstName)

    return AvailableWorkers, Required_indexes, Name_list, Distance_list


# This function checks if the phone number entered is valid and returns True or False

def CheckPhoneNumber(Phone_num):
    if len(Phone_num) == 10:
        for i in Phone_num:
            if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return True
            else:
                return False
    else:
        return False


# This function checks if the email entered is valid or not

def CheckEmail(email):
    import string
    alpha_list=string.ascii_lowercase
    str1 = email
    check1=True
    check2=True
    if str1.endswith('.com'):
        str1 = str1.replace(".com", '')
        for i in str1.lower():
            if i not in alpha_list and i not in ['@', '.']:
                check1=False
        if '@' in str1:
            check2=True
    if check2==True and check1==True:
        return True
    else :
        return False


# This function checks weather the

def CheckName(FirstName, LastName):
    for i in FirstName.lower():
        if i >= 'a' and i <= 'z':
            first = True
        else:
            first = False
            break
    for i in LastName.lower():
        if i >= 'a' and i <= 'z':
            last = True
        else:
            last = False
            break
    if last == True and first == True:
        return True
    else:
        return False


# This checks if the profession entered by the worker is valid or not

def CheckType(Type):
    L = ['Electrician', 'Laundry', 'Mechanic', 'Plumber']
    if Type in L:
        return True
    else:
        return False


# This checks if the landmark entered is supported or not

def CheckLandmark(Landmark):
    L = ['VIITMainGate']
    if Landmark in L:
        return True
    else:
        return False


# This function checks weather the phone number is in DataBase or not

def CheckNumInDatabase(Phone_num):
    Phone_num = encrypt(Phone_num)
    AdminData = pd.read_csv('Admins.csv')
    WorkerData = pd.read_csv('Workers.csv')
    UserData = pd.read_csv('Users.csv')
    typ = None
    a = AdminData.shape
    n1 = a[0]
    w = WorkerData.shape
    n2 = w[0]
    u = UserData.shape
    n3 = u[0]
    for i in range(n1):
        if Phone_num == AdminData['PhoneNum'][i]:
            typ = "Admin"
    for i in range(n2):
        if Phone_num == WorkerData['PhoneNum'][i]:
            typ = "Worker"
    for i in range(n3):
        if Phone_num == UserData['PhoneNum'][i]:
            typ = "User"
    return typ


# Returns the index in the form of tuple

def getIndexFromDataFrame(DataFrame, element):
    listOfPos = []
    # Below code Returns a boolean DataFrame
    result = DataFrame.isin([element])
    # Below code returns any random column
    series = result.any()
    # Below code gives list of the column index in the series
    columnNames = list(series[series == True].index)
    for col in columnNames:
        # Below code gives list of the row index
        rows = list(result[col][result[col] == True].index)
        for row in rows:
            listOfPos.append((row, col))
    return listOfPos


# If already registered then Extracts the data of that person

def ExtractName(Phone_num, Type):
    Phone_num = encrypt(Phone_num)
    if Type == "Admin":
        AdminData = pd.read_csv('Admins.csv')
        L = getIndexFromDataFrame(AdminData, Phone_num)
        Row = L[0][0]
        Name_raw = AdminData.loc[Row, 'FirstName']
        Name=decrypt(Name_raw)
    elif Type == "Worker":
        WorkerData = pd.read_csv('Workers.csv')
        L = getIndexFromDataFrame(WorkerData, Phone_num)
        Row = L[0][0]
        Name_raw = WorkerData.loc[Row, 'FirstName']
        Name=decrypt(Name_raw)
    elif Type == "User":
        UserData = pd.read_csv('Users.csv')
        L = getIndexFromDataFrame(UserData, Phone_num)
        Row = L[0][0]
        Name_raw = UserData.loc[Row, 'FirstName']
        Name=decrypt(Name_raw)
    else:
        print('Sorry , An unexpected error has been occured !!')
        exit()
    return Name


# Extracts the stored password of user from the dataframe

def ExtractUserPass(Phone_num):
    Phone_num = encrypt(Phone_num)
    UserData = pd.read_csv('Users.csv')
    L = getIndexFromDataFrame(UserData, Phone_num)
    Row = L[0][0]
    Password = UserData.loc[Row, 'Password']
    Password=decrypt(Password)
    return Password


# Changes the password of the user

def ChangeUserPass(Phone_num, Pass):
    Phone_num = encrypt(Phone_num)
    UserData = pd.read_csv("Users.csv")
    L = getIndexFromDataFrame(UserData, Phone_num)
    Row = L[0][0]
    Pass=decrypt(Pass)
    UserData.at[Row, 'Password'] = Pass


# Creates a user accont if filled correctly

def CreateUserAccount(Phone_num, FirstName, LastName, Email, Password):
    UserData = pd.read_csv("Users.csv")
    dict1 = {'PhoneNum': [Phone_num], 'FirstName': [FirstName], 'LastName': [LastName],
             'E-mail': [Email], 'Password': [Password]}
    UserDataNew = pd.DataFrame(dict1)
    UserDataNew_Encrypted=Extract_encrypt_Users(UserDataNew)
    UserDataUpdated = pd.concat([UserData, UserDataNew_Encrypted], ignore_index=True)
    UserDataUpdated.to_csv('Users.csv', index=False)


# Creates a worker account if filled correctly

def CreateWorkerAccount(Phone_num, Type, FirstName, LastName, Email, Landmark, Distance, Weblink):
    WorkerData = pd.read_csv("Workers.csv")
    dict1 = {'PhoneNum': [Phone_num], 'Type': [Type], 'FirstName': [FirstName], 'LastName': [LastName],
             'E-mail': [Email], 'Landmark': [Landmark], 'Distance': [Distance], 'Weblink': [Weblink]}
    WorkerDataNew = pd.DataFrame(dict1)
    WorkerDataNew_Encrypted=Extract_encrypt_Workers(WorkerDataNew)
    WorkerDataUpdated = pd.concat(
        [WorkerData, WorkerDataNew_Encrypted], ignore_index=True)
    WorkerDataUpdated.to_csv("Workers.csv", index=False)
