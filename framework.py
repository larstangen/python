import sys
import cx_Oracle
import getpass

#if __name__ == "__main__":
#   print(sys.argv[1])

username = input('username:')
print(username)
#password = input('password:')
pswd = getpass.getpass('password:')
print(pswd)
