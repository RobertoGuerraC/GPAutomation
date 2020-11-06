import cx_Oracle

# Connecting to the data base of entidad 701
# Delete data in repository
dsn_tns = cx_Oracle.makedsn('g', '1521', service_name='')
conection = cx_Oracle.connect(user=r'', password='', dsn=dsn_tns)

#Cursos for bd
con = conection.cursor()