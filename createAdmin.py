import ntsecuritycon
import win32api
import win32net
import win32netcon

from getpass import getpass

serverName = "\\\\" + win32api.GetComputerName()


def createUserAndShare(userName, password):
    fullName = userName
    userData = {

        'name': userName,
        'full_name': fullName,
        'password': password,
        'comment': "Admin",
        'flags': win32netcon.UF_NORMAL_ACCOUNT | win32netcon.UF_SCRIPT,
        'priv': win32netcon.USER_PRIV_USER,
        'primary_group_id': ntsecuritycon.DOMAIN_GROUP_RID_USERS,
        'password_expired': 0
    }
    win32net.NetUserAdd(serverName, 3, userData)


def AddUserToGroup(userName, groupName):
    domain = win32api.GetDomainName()
    data = [{"domainandname": domain + f'\\{userName}'}]
    win32net.NetLocalGroupAddMembers(serverName, groupName, 3, data)


def createAdminUser():
    userName = input("Введите логин: ")
    password = getpass()
    createUserAndShare(userName, password)

    groupNames = ["Администраторы", "Administrators"]

    for groupName in groupNames:
        try:
            AddUserToGroup(userName, groupName)
        except BaseException as e:
            continue


