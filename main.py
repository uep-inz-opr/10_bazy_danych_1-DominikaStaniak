import pymysql
import csv

connection = pymysql.connect(host = "ego.kie.ue.poznan.pl", port = 8080, user="inz_opr", passwd="inz_opr", database="inzynieria_oprogramowania")
cursor = connection.cursor()


with connection.cursor() as cursor:
    sql = "SELECT sum(duration) from polaczenia"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    print(result)



if __name__ == '__main__':
    pass
