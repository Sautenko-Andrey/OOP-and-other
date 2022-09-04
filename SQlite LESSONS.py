import sqlite3 as sq


def main1():
    with sq.connect('saper.db') as my_connect:
        my_cursor=my_connect.cursor()

        my_cursor.execute("""DROP TABLE IF EXISTS users""")

        my_cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            sex INTEGER DEFAULT 1,
            old INTEGER,
            score INTEGER
            )""")

    #ограничитель NOT NULL вверху используется,чтобы поле таблиы никогда не было пустым
    #ограничитель DEFAULT 1 записывает по умолчанию знаечение 1,если мы не передаем никаких данных

    #my_cursor.execute(""" DROP TABLE users""") # это нужно для удаления таблицы

#main1()

def main2():
    with sq.connect('saper.db') as my_connect:
        my_cursor=my_connect.cursor()

        my_cursor.execute('SELECT * FROM users WHERE score<1000 AND sex=1 ORDER BY score LIMIT 4')
        for result3 in my_cursor:
            print(result3)


        # result1=my_cursor.fetchone()
        # result2=my_cursor.fetchmany(2)
        # print(result1)
        # print(result2)
        # print('---------')

#main2()


def main3():
    with sq.connect('team.db') as con:
        cur=con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS players (
        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        team TEXT NOT NULL,
        runk FLOAT NOT NULL,
        height INTEGER NOT NULL,
        age INTEGER NOT NULL)''')

#main3()

def main4():
    with sq.connect('team.db') as con:
        cur=con.cursor()

    cur.execute('''SELECT * FROM players WHERE age<40 ORDER BY runk ''')
    for player in cur:
        print(player)


#main4()

def main5():
    with sq.connect('saper.db') as con:
        cur=con.cursor()

    cur.execute(''' CREATE TABLE IF NOT EXISTS games (
        user_id INTEGER,
        score INTEGER,
        time INTEGER)''')

#main5()

def main6():
    with sq.connect('volley.db') as coonect:
        cursor=coonect.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS teams(
        team TEXT NOT NULL,
        city TEXT NOT NULL,
        points FLOAT NOT NULL)''')

#main6()
def main7():
    with sq.connect('volley.db') as connect:
        cursor=connect.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS registration_pay (
        team TEXT NOT NULL,
        money FLOAT DEFAULT 0)''')

#main7()

def main8():
    with sq.connect('bowling.db') as conect:
        cursor=conect.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS games (
        user_id INTEGER NOT NULL,
        points INTEGER DEFAULT 0,
        time INTEGER NOT NULL)''')

#main8()

def main9():
    with sq.connect('bowling.db') as connect:
        cursor=connect.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS players(
        row_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL)''')

#main9()

def main10():
    with sq.connect('donbusscup2022.db') as connect:
        cursor=connect.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS teams(
        runk INTEGER PRIMARY KEY AUTOINCREMENT,
        team_name TEXT NOT NULL,
        draw TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS reg_pay(
        name TEXT NOT NULL,
        paid FLOAT DEFAULT 0)''')

#main10()

def main11():
    with sq.connect('donbusscup2022.db') as connect:
        cursor=connect.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS tab1(
        value INTEGER DEFAULT 0,
        type TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS tab2(
        score INTEGER DEFAULT 0,
        type TEXT NOT NULL)''')

#main11()

def main12():
    with sq.connect('school.db') as connect:
        cursor=connect.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS math(
        lesson  INTEGER NOT NULL,
        hours FLOAT NOT NULL)''')

    cursor.execute("""CREATE TABLE IF NOT EXISTS phisycs(
        lesson INTEGER NOT NULL,
        hours FLOAT NOT NULL)""")

#main12()

def main13():
    with sq.connect('persons.db') as connect:
        func=connect.cursor()

    func.execute("""CREATE TABLE IF NOT EXISTS info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone text NOT NULL)""")

    func.execute("""CREATE TABLE IF NOT EXISTS adress(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        home_adress TEXT NOT NULL)""")


#main13()

def main14():
    with sq.connect('students.db') as connect:
        my_funk=connect.cursor()

    my_funk.execute("""CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        sex INTEGER,
        old INTEGER)""")

    my_funk.execute("""CREATE TABLE IF NOT EXISTS marks(
        id INTEGER NOT NULL,
        subject TEXT NOT NULL,
        mark INTEGER NOT NULL)""")

    my_funk.execute("""CREATE TABLE IF NOT EXISTS female(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        sex INTEGER,
        old INTEGER)""")

#main14()

def main15():
    with sq.connect('alcoholics.db') as alcoholics:
        execute_func=alcoholics.cursor()

    execute_func.execute("""CREATE TABLE IF NOT EXISTS party(
            id INTEGER NOT NULL,
            alcohol TEXT NOT NULL,
            amount INTEGER NOT NULL)""")

    execute_func.execute("""CREATE TABLE IF NOT EXISTS info(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            weight INTEGER,
            old INTEGER)""")


#main15()


def main16():
    with sq.connect('friendscars.db') as con:
        cur=con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS cars (
                car_id INTEGER PRIMARY KEY AUTOINCREMENT,
                model TEXT,
                price INTEGER
    )""")

    cur.execute("INSERT INTO cars(car_id,model,price) VALUES(6,'Audi',50000)")

#main16()

def main17():
    cars=[
        ('DAEWOO',3000),
        ('Renault',16000),
        ('Skoda',25000),
        ('Citroen',13000),
        ('Opel',1500)
    ]

    cars2=[
        ('Mazda',80000),
        ('Dacia',35000),
        ('MAN',43000)
    ]

    with sq.connect('carshop.db') as my_connect:
        my_cursor=my_connect.cursor()

        my_cursor.execute("""DROP TABLE IF EXISTS cars""")

        my_cursor.execute("""CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT NOT NULL,
            price INTEGER
            )""")

        my_cursor.execute("INSERT INTO cars(car_id,model,price) VALUES(1,'Audi',50000)")
        my_cursor.execute("INSERT INTO cars(car_id,model,price) VALUES(2,'BMW',75000)")
        my_cursor.execute("INSERT INTO cars(car_id,model,price) VALUES(3,'Lexus',100000)")
        my_cursor.execute("INSERT INTO cars(car_id,model,price) VALUES(4,'Ferrari',150000)")
        my_cursor.execute("INSERT INTO cars(car_id,model,price) VALUES(5,'Nissan',4000)")


        for car in cars:
            my_cursor.execute("INSERT INTO cars VALUES(null,?,?)",car)

        my_cursor.executemany("INSERT INTO cars VALUES(null,?,?)",cars2)

        my_cursor.execute("UPDATE cars SET price= :Price WHERE model LIKE 'Renault'",{'Price':0})

        my_cursor.executescript("""DELETE FROM cars WHERE model LIKE 'Renault';
                                UPDATE cars SET price=price+1000
        """)
#main17()

def main18():
    connect=None
    old=[
        ('Жигули 5',300),
        ('Волга',450),
        ('Москвич 415',250)
    ]

    try:
        connect=sq.connect('carshop.db')
        cursor=connect.cursor()

        cursor.executescript("""CREATE TABLE IF NOT EXISTS old_car (
                car_id INTEGER PRIMARY KEY AUTOINCREMENT,
                model TEXT,
                price INTEGER
            );
            BEGIN;
            CREATE TABLE IF NOT EXISTS customer (name TEXT,tr_in INTEGER,buy INTEGER);
            INSERT INTO old_car VALUES (NULL,'ZEPER',100);
            INSERT INTO old_car VALUES (NULL,'Velo',400);
            INSERT INTO old_car VALUES (NULL,'Samokat',200);
            UPDATE old_car SET price=price+1000;
            INSERT INTO old_car VALUES (NULL,'Zaporojec',50)
        """)

        last_row_id=cursor.lastrowid
        buy_car_id=2
        cursor.execute("INSERT INTO customer('Юрий',?,?)",(last_row_id,buy_car_id))


        connect.commit()

    except sq.Error as e:
        if connect: connect.rollback()
        print('Ошибка выполнения запроса!')
    finally:
        if connect:connect.close()

#main18()

def main19():
    with sq.connect('sportshop.db') as my_connect:
        my_cursor=my_connect.cursor()

        my_cursor.execute("""DROP TABLE IF EXISTS shop""")

        my_cursor.executescript("""CREATE TABLE IF NOT EXISTS shop(
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            article INTEGER,
            qr_code INTEGER,
            price INTEGER
            );
            CREATE TABLE IF NOT EXISTS customer(name TEXT,tr_in INTEGER);
        """)

        my_cursor.execute("INSERT INTO shop(item_id,name,article,qr_code,price) VALUES(1,'shoes',123,25,1000)")
        last_row_id=my_cursor.lastrowid
        my_cursor.execute("INSERT INTO customer (name,tr_in) VALUES('Юрий',?)",(last_row_id))

#main19()

def main20():
    players=[
        ('Саутенко',192),
        ('Чаусов',197),
        ('Дыкань',190),
        ('Терещук',202),
        ('Веселов',188)
    ]

    with sq.connect('gigant.db') as my_connect:
        my_connect.row_factory=sq.Row
        my_cursor=my_connect.cursor()


        my_cursor.executescript("""CREATE TABLE IF NOT EXISTS our_players (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            height INTEGER
        )""")

        #my_cursor.executemany("INSERT INTO our_players VALUES(NULL,?,?)",players)
        my_cursor.execute("SELECT name,height FROM our_players")

        # rows=my_cursor.fetchmany(3)
        # print(rows)
        # rows=my_cursor.fetchone()
        # print(rows)
        # rows=my_cursor.fetchall()
        # print(rows)
        for row in my_cursor:
            print(row['name'],row['height'])

#main20()



# def readAva(number):
#     try:
#         with open(f"avas/{number}.png","rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
# with sq.connect('gigant2.db') as my_connect:
#     my_cursor=my_connect.cursor()
#
#     my_cursor.execute("""DROP TABLE IF EXISTS users""")
#
#     my_cursor.executescript("""CREATE TABLE IF NOT EXISTS users (
#         name TEXT,
#         ava BLOB,
#         runk INTEGER
#     )""")
#
# img=readAva(1)
# if img:
#     binary=sq.Binary(img)
#     my_cursor.execute("INSERT INTO users(name,ava,runk) VALUES('Саутенко',?,75)",(binary,))

def main21():
    with sq.connect('cars.db') as connect:
        my_cursor=connect.cursor()

    # for sql in connect.iterdump():      чтобы просто прочитать
    #     print(sql)


    # with open("sql_damp.sql","w") as f:     для записи БД( чтобы был файл на компе,для возможного восстановления)
    #     for sql in connect.iterdump():
    #         f.write(sql)

    # with open("sql_damp.sql","r") as f:      для восстановления БД
    #     sql=f.read()
    #     my_cursor.executescript(sql)


#main21()












