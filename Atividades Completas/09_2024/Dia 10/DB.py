import mysql.connector
dataBase = mysql.connector.connect(
                     host = "10.28.2.39",
                     user = "suporte",
                     password = "suporte",
                     database = "registros")  
 
savequery = "select * from registros.login"
 
cursor = dataBase.cursor()
try:
    cursor.execute(savequery)
    myresult = cursor.fetchall()
   
    for x in myresult:
        print(x)
        print("Query Excecuted successfully")
 
except:
    dataBase.rollback()
    print("Error occured")
 
cursorObject = dataBase.cursor()  
dataBase.close()