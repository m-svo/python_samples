print("importing pyodbc")
import pyodbc
print("pyodbc imported")
cnxn = pyodbc.connect("Driver=FreeTDS;"
                      "Server=;"
                      "PORT=;"
                      "Database=;"
                      "UID=;PWD=;"
                      "TDS_Version=8.0;"
                      "ClientCharset=UTF8;")
print("sql connected")
cursor = cnxn.cursor()
print("cursor set")
guid=input("Please input guid: ")
if guid:
    cursor.execute("SELECT top 1 guid, adate, data_xml FROM gds_request WHERE gds_request.guid=? order by adate desc", [guid])
else:
    cursor.execute("SELECT top 1 guid, adate, data_xml FROM gds_request order by adate desc")
print("sql executed")

result = cursor.fetchall()

for row in result:
    print(row)

cursor.close()
print("cursor closed")
del cursor
print("cursor deleted")
cnxn.close()
print("connection closed")
if not guid:
    result_list=list(str(result[0]).split(','))
    guid=result_list[0].translate(dict.fromkeys(map(ord, '(\''), None))
with open('%s.log' % guid, 'w') as f:
    for item in result:
        f.write("%s\n" % item)
print("result written to file")
print("guid is: %s" % guid)
