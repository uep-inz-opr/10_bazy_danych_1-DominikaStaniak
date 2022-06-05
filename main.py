import pymysql
import csv



class ReportGenerator:
  def __init__(self, host, port, user, passwd, database):
    self.connection = pymysql.connect(host = "ego.kie.ue.poznan.pl", 
                                      port = 8080,
                                      user="inz_opr", 
                                      passwd="inz_opr", 
                                      database="inzynieria_oprogramowania")

  def generate_report(self):
    cursor = self.connection.cursor()
    cursor.execute(f"Select sum(duration) from polaczenia")
    result = cursor.fetchall()
    print(result)
    pass


if __name__ == '__main__':
    pass
