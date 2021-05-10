import psycopg2
import psycopg2.errorcodes
import csv

database = input('Введіть назву БД: ')
user = input("Введіть ім'я користувача: ")
password = input("Введіть пароль: ")
host = input("Введіть хост: ")
port = input("Введіть порт: ")
print("--------------------------\n")

#підключення до бази даних
con = psycopg2.connect(
   database=database, user=user, password=password, host=host, port=port)

cur = con.cursor()

def result_func():
    print("Запит оброблюється...")
    select_query = '''
SELECT Region.RegName AS "Область", Human.Year AS "Рік", max(Hist.histBall100) AS "Максимальний бал"
FROM Hist JOIN Human ON
    Hist.OUTID = Human.OUTID 
JOIN Region ON Human.reg_id = Region.reg_id
WHERE Hist.histTestStatus = 'Зараховано' 
GROUP BY Region.RegName, Human.Year;
'''

    cur.execute(select_query)

    with open('result_2.csv', 'w', encoding="utf-8") as new_csv_file:
        csv_writer = csv.writer(new_csv_file)
        csv_writer.writerow(['Область', 'Рік', 'Найкращий бал з Історії України'])
        for row in cur:
            csv_writer.writerow(row)
            
result_func()
    
print("--------------------------\n")
print("Результат запиту записаний у 'result_2.csv' ")


cur.close()
con.close()


