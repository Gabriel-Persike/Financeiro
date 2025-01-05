
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="financeiro"

)


def POST_ENTRADA(data):
    # if not data.descricao:
    #     return False
    mycursor = mydb.cursor()

    sql = "INSERT INTO ENTRADAS (DESCRICAO, VALOR, DATA) values (%s, %s, %s)"
    val = [data["descricao"], data["valor"], data["data"]]
    print(val)

    mycursor.execute(sql, val)

    mydb.commit()
    print(mycursor.rowcount, "record inserted.")




