# coding=windows-1251

print("importing pyodbc")
import pyodbc
print("pyodbc imported")
cnxn = pyodbc.connect("Driver={SQL Server Native Client 10.0};"
                      "Server=;"
                      "Database=;"
                      "UID=;PWD=")
print("sql connected")
cursor = cnxn.cursor()
print("cursor set")
cursor.execute("SELECT top 1 convert(varchar,[table].[inc]) + ' some_text ' + [table].[name] + ' ' + convert(varchar,[table].[date],104) as cheque_text, [person].[email] FROM table LEFT JOIN [person] on [person].[inc]=[table].[person] WHERE [table].[inc]=1000")
print("sql executed")

row = cursor.fetchone()
result_text = str(row)
print(row)
print(result_text)
result_array = result_text.split(",")
cheque_body = result_array[0]
email_result = result_array[1]
cheque_body = cheque_body.replace("(","")
cheque_body = cheque_body.replace("'","")
email_result = email_result.replace(")","")
email_result = email_result.replace("'","")
email_result = email_result.replace(" ","")
print(cheque_body)
print(email_result)

cursor.close()
print("cursor closed")
del cursor
print("cursor deleted")
cnxn.close()
print("connection closed")
