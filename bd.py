import sqlite3
import os
db_path='D://python_db'
db_file='dbinvest.db'
full_path=os.path.join(db_path,db_file)
id=1
con=sqlite3.connect(full_path)
cur=con.cursor()
cur.execute('DROP TABLE IF EXISTS Login')
cur.execute('DROP TABLE IF EXISTS Profile')
cur.execute('DROP TABLE IF EXISTS Profile_history')
cur.execute('DROP TABLE IF EXISTS Profile_investing')
cur.execute('DROP TABLE IF EXISTS Live_complexes')

cur.execute('DROP TABLE IF EXISTS All_offers')
cur.execute('DROP TABLE IF EXISTS flats')
cur.execute('DROP TABLE IF EXISTS park')
cur.execute('DROP TABLE IF EXISTS comm')
cur.execute('DROP TABLE IF EXISTS zagorod')
cur.execute('DROP TABLE IF EXISTS prices_changes')
cur.execute('CREATE TABLE Login(id_profile INTEGER PRIMARY KEY, email varchar(40), mobilenumber INTEGER NOT NULL,'
            'pass INTEGER NOT NULL, FOREIGN KEY (email) REFERENCES Profile (email), UNIQUE(mobilenumber), UNIQUE(email), '
            'FOREIGN KEY (id_profile) REFERENCES Profile(id))')
cur.execute('CREATE TABLE Profile(id INTEGER PRIMARY KEY, email varchar(40) NOT NULL, surname varchar(30) NOT NULL,'
            ' name varchar(30) NOT NULL, mobilenumber INTEGER NOT NULL, registration_date varchar(12) NOT NULL, UNIQUE (mobilenumber), UNIQUE (email))')
cur.execute('CREATE TABLE Live_complexes(id_complex INTEGER PRIMARY KEY, adress varchar(40) NOT NULL, when_sdacha varchar(30),'
            ' liter varchar(5) NOT NULL, developer varchar(40) NOT NULL, name_complex varchar(20) NOT NULL)')
cur.execute('CREATE TABLE All_offers(id INTEGER PRIMARY KEY, offer_type INTEGER NOT NULL, type_id INTEGER NOT NULL)')
cur.execute('CREATE TABLE flats(id INTEGER PRIMARY KEY, kolvo_rooms INTEGER,'
            ' offer_type INTEGER NOT NULL, complex_id INTEGER NOT NULL, square_min REAL, square_max REAL,'
            ' FOREIGN KEY (complex_id) REFERENCES Live_complexes (id_complex))')
cur.execute('CREATE TABLE park(id INTEGER PRIMARY KEY, complex_id INTEGER NOT NULL, '
            'offer_type INTEGER NOT NULL, square REAL, flour INTEGER, '
            'FOREIGN KEY (complex_id) REFERENCES Live_complexes(id_complex))')
cur.execute('CREATE TABLE comm(id INTEGER PRIMARY KEY, complex_id INTEGER NOT NULL,'
            ' offer_type INTEGER NOT NULL, square_min REAL, square_max REAL, flour INTEGER, '
            'FOREIGN KEY (complex_id) REFERENCES Live_complexes(id_complex))')
cur.execute('CREATE TABLE zagorod(id INTEGER PRIMARY KEY, flours INTEGER,'
            'offer_type INTEGER NOT NULL, square_house REAL, square_place REAL, adress varchar(40)) ')
cur.execute('CREATE TABLE Profile_history(id_profile INTEGER, id_offer INTEGER, last_view_date varchar(12) NOT NULL,'
            'FOREIGN KEY (id_profile) REFERENCES Profile(id), FOREIGN KEY (id_offer) REFERENCES All_offers(id), PRIMARY KEY (id_profile, id_offer))')
cur.execute('CREATE TABLE Profile_investing(id_profile INTEGER, id_offer INTEGER, investing_sum INTEGER, item_number INTEGER,'
            ' investing_date varchar2(12) NOT NULL, FOREIGN KEY (id_profile) REFERENCES Profile(id),FOREIGN KEY (id_offer) REFERENCES All_offers(id),'
            ' PRIMARY KEY(id_profile, id_offer, investing_date))')
cur.execute('CREATE TABLE prices_changes(id INTEGER NOT NULL, offer_type INTEGER NOT NULL, price INTEGER NOT NULL, update_date varchar(20) NOT NULL, PRIMARY KEY (id, offer_type, update_date))')

con.commit()
cur.execute('INSERT INTO Profile(id, email, surname, name, mobilenumber, registration_date) VALUES ( 1, "vvados@mail.ru", "Dudnik", "Valerii", 9881783234, "15.02.2023 14:34:51")')
cur.execute('INSERT INTO Login(id_profile, email, mobilenumber, pass) VALUES (1, "vvados@mail.ru", 9881783234, 1234)')
cur.execute('INSERT INTO live_complexes(id_complex, adress, when_sdacha, liter, developer, name_complex) VALUES (1, "ул. Гаранжая, 75", "2 квартал 23 года", "5", "ООО Застрой", "ЖК ОЛИМП ПЛАЗА ФЛЕКС")')
cur.execute('INSERT INTO flats(id, kolvo_rooms, offer_type, complex_id, square_min, square_max) VALUES ( 1, 2, 1, 1, 57.1 , 57.5)')
cur.execute('INSERT INTO prices_changes(id, offer_type, price, update_date) VALUES (1, 1, 61000, "10.02.2023 14:34:51")')
cur.execute('INSERT INTO comm(id, complex_id, offer_type, square_min, square_max, flour) VALUES (1, 1, 2, null, null, 1)')
cur.execute('INSERT INTO prices_changes(id, offer_type, price, update_date) VALUES (1, 2, 120000, "12.02.2023 16:21:23")')
cur.execute('INSERT INTO zagorod(id, flours, offer_type, square_house, square_place, adress ) VALUES ( 1, 2, 3, 250.5, 12,"СНТ Аэропорт, ул. Солнечненская, 175")')
cur.execute('INSERT INTO prices_changes(id, offer_type, price, update_date) VALUES (1, 3, 10000000, "16.02.2023 19:00:49")')
cur.execute('INSERT INTO park(id, complex_id, offer_type, square, flour) VALUES ( 1, 1, 4, null, -1)')
cur.execute('INSERT INTO prices_changes(id, offer_type, price, update_date) VALUES (1, 4, 500000, "17.02.2023 11:11:11")')

cur.execute('INSERT INTO All_offers(id, offer_type, type_id) VALUES (1, 1, 1)')
cur.execute('INSERT INTO All_offers(id, offer_type, type_id) VALUES (2, 2, 1)')
cur.execute('INSERT INTO All_offers(id, offer_type, type_id) VALUES (3, 3, 1)')
cur.execute('INSERT INTO All_offers(id, offer_type, type_id) VALUES (4, 4, 1)')
cur.execute('INSERT INTO Profile_investing(id_profile, id_offer, investing_sum, item_number, investing_date) VALUES (1, 1, 10485900, 3, "17.02.2023 14:20:30")')
cur.execute('INSERT INTO Profile_history(id_profile, id_offer, last_view_date) VALUES (1, 3,  "16.02.2023 00:35:10")')
cur.execute('INSERT INTO prices_changes(id, offer_type, price, update_date) VALUES (1, 1, 62000, "15.02.2023 15:36:12")')
cur.execute('SELECT * from Profile')
print(cur.fetchall())
cur.execute('SELECT * from Login')
print(cur.fetchall())
cur.execute('SELECT * from Profile_history')
print(cur.fetchall())
cur.execute('SELECT * from Profile_investing')
print(cur.fetchall())
cur.execute('SELECT * from Live_complexes')
print(cur.fetchall())
cur.execute('SELECT * from All_offers')
print(cur.fetchall())
cur.execute('SELECT * from flats')
print(cur.fetchall())
cur.execute('SELECT * from park')
print(cur.fetchall())
cur.execute('SELECT * from comm')
print(cur.fetchall())
cur.execute('SELECT * from zagorod')
print(cur.fetchall())
cur.execute('SELECT * from prices_changes')
print(cur.fetchall())
con.commit()
