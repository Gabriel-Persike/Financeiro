
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="financeiro"

)


def POST_ENTRADA(data):

    def ValidateParams(data):
        print(not data["descricao"])
        if not data["descricao"]:
            return "Descrição Invalida"

        return True

    validate = ValidateParams(data)
    if validate != True:
        return validate
 
    mycursor = mydb.cursor()

    sql = "INSERT INTO ENTRADAS (DESCRICAO, VALOR, DATA) values (%s, %s, %s)"
    val = [data["descricao"], data["valor"], data["data"]]
    print(val)

    mycursor.execute(sql, val)

    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return True


def GET_ENTRADAS():
    sql = "SELECT ID, DESCRICAO, VALOR, DATA FROM ENTRADAS"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()


    retorno = []
    for entrada in myresult:
        ID = entrada[0]
        DESCRICAO = entrada[1]
        VALOR = entrada[2]
        DATA = entrada[3]

        print(entrada)
        obj = dict(descricao = DESCRICAO)
        retorno.append(obj)

    return retorno
    

