import cx_Oracle
import pyautogui
cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle") 
try: 
    connection = cx_Oracle.connect(
                 user='',
                 password='',
                 dsn= '',
                 encoding = 'UTF-8'
                            )
    cursor = connection.cursor()
except:    
    pyautogui.alert("Error: Conexion con el servidor no establecida")

est = False

while est == False:
    
    ingreso = pyautogui.prompt(text='', title='Digite la cedula o el nombre de usuario que esta bloqueando:' , default='')
    
    try:

        query_1 = """ select oid from genusuario where usunombre ='"""+ ingreso.strip().upper() +"""' """ 
        query_conf = """commit"""
        oid1 = []
        oid2 = []
        cursor.execute(query_1)
        for row in cursor:
            oid1.append(str(row))
            
        oid_str1 = oid1[0].rsplit('(', 1)

        oid_str2 = oid_str1[1].rsplit(',', 1)


        query_2 = """ select oid from gendocume WHERE genusuario= '"""+ oid_str2[0]+"""' """

        cursor.execute(query_2)
        for row in cursor:
            oid2.append(str(row))
        print(oid2)

        oids = []
        for x in oid2:
            oid2_str1 = x.rsplit('(', 1)
            oid2_str2 = oid2_str1[1].rsplit(',', 1)
            oids.append(oid2_str2[0])


        str_queries = ""
        for v in oids:
            query_del = """ delete from gendocume where oid = '"""+ v +"""' """
            cursor.execute(query_del)

        cursor.execute(query_conf)
        pyautogui.confirm("Documentos desbloqueado", buttons=['OK'])
        break
    except: 
        if ingreso == None:
            break
        pyautogui.alert("Error: Digite correctamente el usuario o cedula")
        est = False
