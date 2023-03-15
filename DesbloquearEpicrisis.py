import cx_Oracle
import pyautogui
cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle") 

connection = cx_Oracle.connect(
             user='',
             password='',
             dsn= '',
             encoding = 'UTF-8'
                        )
    
cursor = connection.cursor() 

est = False

while est == False:

    ingreso = pyautogui.prompt(text='', title='Digite el ingreso del paciente' , default='')
    
    try:
        query_1 = """ SELECT OID FROM ADNINGRESO WHERE AINCONSEC='"""+ ingreso+"""' """ 
        query_conf = """commit"""
    
        oid1 = []
        oid2 = []
        cursor.execute(query_1)
        for row in cursor:
            oid1.append(str(row))
        print(oid1[0])
    
        oid_str1 = oid1[0].rsplit('(', 1)
        print(oid_str1)
        oid_str2 = oid_str1[1].rsplit(',', 1)
        print(oid_str2[0]) 
    
        query_2 = """ SELECT OID FROM HCNEPICRI WHERE ADNINGRESO= '"""+ oid_str2[0]+"""' """
    
        cursor.execute(query_2)
        for row in cursor:
            oid2.append(str(row))
        print(oid2[0])
    
        oid2_str1 = oid2[0].rsplit('(', 1)
        print(oid_str1)
        oid2_str2 = oid2_str1[1].rsplit(',', 1)
        print(oid2_str2[0]) 
    
        query_3 = """ UPDATE HCNEPICRI SET HCEESTDOC=0 WHERE OID= '"""+ oid2_str2[0]+"""'  """ 
        cursor.execute(query_3)
        cursor.execute(query_conf)
        pyautogui.confirm("Epicrisis desbloqueada", buttons=['OK'])
    except: 
            if ingreso == None:
                break
            pyautogui.alert("Error: Digite correctamente el ingreso")
            est = False

print("listo")

