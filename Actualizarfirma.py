import cx_Oracle
import pyautogui
cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle") 

connection = cx_Oracle.connect(
             user='empresa20',
             password='admin20',
             dsn= '100.65.33.115/gzd',
             encoding = 'UTF-8'
                        )
    
cursor = connection.cursor() 

est = False

while est == False:
    
    cedula = pyautogui.prompt(text='', title='Digite la cedula del medico' , default='')

    try:

        query_med = """---ACTUALIZAR FIRMA---
        update genmedico set gmefirma=(select gmefotoima from genmedico where gmecodigo='"""+ cedula+"""')
        where gmecodigo='"""+ cedula+"""' """ 

        cursor.execute(query_med)

        query_conf = """commit"""

        cursor.execute(query_conf) 
        pyautogui.confirm("Firma actualizada", buttons=['OK'])

    except: 
        if cedula == None:
            break
        pyautogui.alert("Error: Digite correctamente la cedula")
        est = False
