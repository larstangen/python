import sys
import cx_Oracle
import getpass
import pandas as pd


instance = input('instance [prd,stg,tst,dv1,etc.]:')
#print(instance)
username = input('username:')
#print(username)
#password = input('password:')
pswd = getpass.getpass('password:')
#print(pswd)
constring = '\'' + username + '/' + pswd + "@" + 'instance' + '\''
#con = cx_Oracle.connect(constring)
print(constring)

#if __name__ == "__main__":
#   print(sys.argv[1])

csv = pd.read_csv('inputs.csv')
print(csv[:])
