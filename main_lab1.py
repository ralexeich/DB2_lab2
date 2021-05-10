import psycopg2
import psycopg2.errorcodes
import csv
import datetime
import itertools

#Здійснюємо з'єднання з БД
con = psycopg2.connect(
   database="lab1", user='postgres', password='123456789', host='127.0.0.1', port= '5432')

cur = con.cursor()

#Видаляємо таблицю в разі її існування
cur.execute("DROP TABLE IF EXISTS DIFFERENCE;")

#Створюємо табличку
cur.execute('''
CREATE TABLE  DIFFERENCE(
	OUTID	TEXT	NOT NULL	PRIMARY KEY, 
	Birth	INTEGER		NOT NULL,	
	SEXTYPENAME	TEXT	NOT NULL,	
	REGNAME	TEXT	NOT NULL,	
	AREANAME	TEXT	NOT NULL,	
	TERNAME	TEXT	NOT NULL,	
	REGTYPENAME	TEXT	NOT NULL,	
	TerTypeName	TEXT	NOT NULL,	
	ClassProfileNAME	TEXT,	
	ClassLangName	TEXT,	
	EONAME	TEXT,	
	EOTYPENAME	TEXT,	
	EORegName	TEXT,	
	EOAreaName	TEXT,	
	EOTerName	TEXT,	
	EOParent	TEXT,	
	UkrTest	TEXT,	
	UkrTestStatus	TEXT,	
	UkrBall100	VARCHAR,	
	UkrBall12	VARCHAR,	
	UkrBall	VARCHAR,	
	UkrAdaptScale	FLOAT,	
	UkrPTName	TEXT,	
	UkrPTRegName	TEXT,	
	UkrPTAreaName	TEXT,	
	UkrPTTerName	TEXT,	
	histTest	TEXT,	
	HistLang	TEXT,	
	histTestStatus	TEXT,	
	histBall100	VARCHAR,	
	histBall12	VARCHAR,	
	histBall	VARCHAR,	
	histPTName	TEXT,	
	histPTRegName	TEXT,	
	histPTAreaName	TEXT,	
	histPTTerName	TEXT,	
	mathTest	TEXT,	
	mathLang	TEXT,	
	mathTestStatus	TEXT,	
	mathBall100	VARCHAR,	
	mathBall12	VARCHAR,	
	mathBall	VARCHAR,	
	mathPTName	TEXT,	
	mathPTRegName	TEXT,	
	mathPTAreaName	TEXT,	
	mathPTTerName	TEXT,	
	physTest	TEXT,	
	physLang	TEXT,	
	physTestStatus	TEXT,	
	physBall100	VARCHAR,	
	physBall12	VARCHAR,	
	physBall	VARCHAR,	
	physPTName	TEXT,	
	physPTRegName	TEXT,	
	physPTAreaName	TEXT,	
	physPTTerName	TEXT,	
	chemTest	TEXT,	
	chemLang	TEXT,	
	chemTestStatus	TEXT,	
	chemBall100	VARCHAR,	
	chemBall12	VARCHAR,	
	chemBall	VARCHAR,	
	chemPTName	TEXT,	
	chemPTRegName	TEXT,	
	chemPTAreaName	TEXT,	
	chemPTTerName	TEXT,	
	bioTest	TEXT,	
	bioLang	TEXT,	
	bioTestStatus	TEXT,	
	bioBall100	VARCHAR,	
	bioBall12	VARCHAR,	
	bioBall	VARCHAR,	
	bioPTName	TEXT,	
	bioPTRegName	TEXT,	
	bioPTAreaName	TEXT,	
	bioPTTerName	TEXT,	
	geoTest	TEXT,	
	geoLang	TEXT,	
	geoTestStatus	TEXT,	
	geoBall100	VARCHAR,	
	geoBall12	VARCHAR,	
	geoBall	VARCHAR,	
	geoPTName	TEXT,	
	geoPTRegName	TEXT,	
	geoPTAreaName	TEXT,	
	geoPTTerName	TEXT,	
	engTest	TEXT,	
	engTestStatus	TEXT,	
	engBall100	VARCHAR,	
	engBall12	VARCHAR,	
	engDPALevel	TEXT,	
	engBall	VARCHAR,	
	engPTName	TEXT,	
	engPTRegName	TEXT,	
	engPTAreaName	TEXT,	
	engPTTerName	TEXT,	
	fraTest	TEXT,	
	fraTestStatus	TEXT,	
	fraBall100	VARCHAR,	
	fraBall12	VARCHAR,	
	fraDPALevel	TEXT,	
	fraBall	VARCHAR,	
	fraPTName	TEXT,	
	fraPTRegName	TEXT,	
	fraPTAreaName	TEXT,	
	fraPTTerName	TEXT,	
	deuTest	TEXT,	
	deuTestStatus	TEXT,	
	deuBall100	VARCHAR,	
	deuBall12	VARCHAR,	
	deuDPALevel	TEXT,	
	deuBall	VARCHAR,	
	deuPTName	TEXT,	
	deuPTRegName	TEXT,	
	deuPTAreaName	TEXT,	
	deuPTTerName	TEXT,	
	spaTest	TEXT,	
	spaTestStatus	TEXT,	
	spaBall100	VARCHAR,	
	spaBall12	VARCHAR,	
	spaDPALevel	TEXT,	
	spaBall	VARCHAR,	
	spaPTName	TEXT,	
	spaPTRegName	TEXT,	
	spaPTAreaName	TEXT,	
	spaPTTerName	TEXT,
	Year    INTEGER     NOT NULL
);''')

print("\nTable created successfully\n")

print("--------------------------\n")

#Функція, що заповнить створену таблицю з csv-файлу
def insert_func(csv_data, year, conn, cursor, logs_f):
    
    start_time = datetime.datetime.now() 
    logs_f.write(str(start_time) + " - час, коли почалось відкриття " + csv_data + '\n')
    
    with open(csv_data, "r", encoding="cp1251") as csv_file:

        columns = ["OUTID", "Birth", "SEXTYPENAME", "REGNAME", "AREANAME", "TERNAME", "REGTYPENAME", "TerTypeName",
                   "ClassProfileNAME", "ClassLangName", "EONAME", "EOTYPENAME", "EORegName", "EOAreaName", "EOTerName",
                   "EOParent", "UkrTest", "UkrTestStatus", "UkrBall100", "UkrBall12", "UkrBall", "UkrAdaptScale",
                   "UkrPTName", "UkrPTRegName", "UkrPTAreaName", "UkrPTTerName", "histTest", "HistLang",
                   "histTestStatus", "histBall100", "histBall12", "histBall", "histPTName", "histPTRegName",
                   "histPTAreaName", "histPTTerName", "mathTest", "mathLang", "mathTestStatus", "mathBall100",
                   "mathBall12", "mathBall", "mathPTName", "mathPTRegName", "mathPTAreaName", "mathPTTerName",
                   "physTest", "physLang", "physTestStatus", "physBall100", "physBall12", "physBall",
                   "physPTName", "physPTRegName", "physPTAreaName", "physPTTerName", "chemTest", "chemLang",
                   "chemTestStatus", "chemBall100", "chemBall12", "chemBall", "chemPTName", "chemPTRegName",
                   "chemPTAreaName", "chemPTTerName", "bioTest", "bioLang", "bioTestStatus", "bioBall100", "bioBall12",
                   "bioBall", "bioPTName", "bioPTRegName", "bioPTAreaName", "bioPTTerName", "geoTest	", "geoLang",
                   "geoTestStatus", "geoBall100", "geoBall12", "geoBall", "geoPTName", "geoPTRegName", "geoPTAreaName",
                   "geoPTTerName", "engTest", "engTestStatus", "engBall100", "engBall12", "engDPALevel", "engBall",
                   "engPTName", "engPTRegName", "engPTAreaName", "engPTTerName", "fraTest", "fraTestStatus",
                   "fraBall100", "fraBall12", "fraDPALevel", "fraBall", "fraPTName", "fraPTRegName", "fraPTAreaName",
                   "fraPTTerName", "deuTest", "deuTestStatus", "deuBall100", "deuBall12", "deuDPALevel", "deuBall",
                   "deuPTName", "deuPTRegName", "deuPTAreaName", "deuPTTerName", "spaTest", "spaTestStatus",
                   "spaBall100",
                   "spaBall12", "spaDPALevel", "spaBall", "spaPTName", "spaPTRegName", "spaPTAreaName", "spaPTTerName"]

#Читаємо дані з csv та опрацьовуємо запит
        print( csv_data + " - на опрацюванні...\n" )
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        batches_inserted = 0
        batch_size = 100
        inserted_all = False

#Поки не вставимо всі рядки
        while not inserted_all:
            try:
                insert_query = '''INSERT INTO DIFFERENCE (year, ''' + ', '.join(columns) + ') VALUES '
                count = 0
                for row in csv_reader:
                    count += 1
                    for key in row:
                        if row[key] == 'null':
                            pass
#Текстові значення беремо в одинарні лапки
                        elif key.lower() != 'birth' and 'ball' not in key.lower():
                            row[key] = "'" + row[key].replace("'", "''") + "'"
                        elif 'ball100' in key.lower():
                            row[key] = row[key].replace(',', '.')
                    insert_query += '\n\t(' + str(year) + ', ' + ','.join(row.values()) + '),'

                    if count == batch_size:
                        count = 0
                        insert_query = insert_query.rstrip(',') + ';'
                        cursor.execute(insert_query)
                        conn.commit()
                        batches_inserted += 1
                        insert_query = '''INSERT INTO DIFFERENCE (year, ''' + ', '.join(columns) + ') VALUES '
#Якщо рядків більше немає - коммітимо транзакцію і закінчуємо
                if count != 0:
                    insert_query = insert_query.rstrip(',') + ';'
                    cursor.execute(insert_query)
                    conn.commit()
                inserted_all = True
                
#Перевірки на випадок падіння БД
                
            except psycopg2.OperationalError:
                if psycopg2.OperationalError.pgcode == psycopg2.errorcodes.ADMIN_SHUTDOWN:
                    print("Немає з'єднання...")
                    connection_restored = False
                    while not connection_restored:
                        #Поновлення зєднання
                        try:
                            connection = psycopg2.connect(host="localhost",
                                                          database="lab1",
                                                          user="postgres",
                                                          password="123456789",
                                                          port="5432")
                            cursor = connection.cursor()
                            connection_restored = True
                        except psycopg2.OperationalError:
                            pass
                    print("З'єднання відновлено!")
                        

    end_time = datetime.datetime.now()
        
    logs_f.write(str(end_time) + " - час, коли файл був повністю оброблений\n")
    logs_f.write('Витрачено часу: ' + str(end_time - start_time) + '\n\n')

    return con, cursor

#Створення файлу в якому буде записані часові вимірювання
logs_file = open('log_of_time.txt', 'w')
#Завантаження даних з csv із вимірюванням часу
con, cur = insert_func("Odata2019File.csv", 2019, con, cur, logs_file)
con, cur = insert_func("Odata2020File.csv", 2020, con, cur, logs_file)  
logs_file.close()

#print("--------------------------\n")
#print("Обидва файла опрацьовані та занесені до csv\n")



#Функція, що виконує запит до БД та формує результат у 'result.csv'
def result_func(result_f, con, cur):
    query = '''
SELECT REGNAME AS "Область", Year AS "Рік", max(histBall100) AS "Максимальний бал"
FROM DIFFERENCE
WHERE histTestStatus = 'Зараховано'
GROUP BY REGNAME, Year;
'''
    cur.execute(query)
    print("Запит сформовано")
    with open(result_f, 'w', newline='', encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        # Зберігаємо заголовки
        csv_writer.writerow(['Область', 'Рік', 'Найкращий бал з Історії України'])
        # Збергіаємо результати запиту
        for row in cur:
            csv_writer.writerow(row)
    return con, cur

print("--------------------------\n")

con, cur = result_func('result_1.csv', con, cur)

print("Результат запиту записаний у 'result_1.csv' ")

con.commit()
con.close()
