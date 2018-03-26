import cx_Oracle
import getpass
import sys

#con = cx_Oracle.connect('tangen/' + sys.argv[1] + '@stgebs')
instance = input('instance [prdebsnew,stgebs,tstebs,dv1ebs,etc.]:')
username = input('username:')
pswd = getpass.getpass('password:')
con = cx_Oracle.connect(username + '/' + pswd + '@' + instance)
cur = con.cursor()
cur.execute('SELECT count(*) FROM apps.fnd_user f, (SELECT fu.user_name, COUNT(frl.responsibility_name) as all_resp_count FROM APPs.fnd_user fu, APPS.fnd_user_resp_groups_direct furg, APPS.fnd_responsibility_vl frl WHERE fu.user_id = furg.user_id and furg.responsibility_id = frl.responsibility_id and furg.responsibility_application_id = frl.application_id and furg.end_date is NULL group by fu.user_name MINUS SELECT fu.user_name, COUNT(case when frl.responsibility_name like \'%iProc%\'then frl.responsibility_name end) as iProc_resp_count FROM apps.fnd_user fu, APPS.fnd_user_resp_groups_direct furg, APPS.fnd_responsibility_vl frl WHERE fu.user_id = furg.user_id and furg.responsibility_id = frl.responsibility_id and furg.responsibility_application_id = frl.application_id and furg.end_date is NULL group by fu.user_name) u WHERE f.user_name = u.user_name AND (end_date > sysdate or end_date is null) AND created_by not in (1,2,-1,0)')
print(cur.fetchall())
cur.close()
con.close()


