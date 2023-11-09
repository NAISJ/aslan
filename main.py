#THIS IS NEW VERSION TO CONNECT TO POSTGRESQL
import psycopg2

conn= psycopg2.connect(host = 'localhost'
                       database = 'postgress'
                       username = 'postgress'
                       password = '1')
cur = conn.cursor()
cur.execute('SELECT superhero_name FROM superhero.superhero LIMIT 5;')
usernames = [r[0] for i in cur.fetchall()]
Found= False
while not Found:
   username = input('Введите ваш логин:')
   if username in usernames:
      print('Вы есть в списке')
      Found=True
      else:
         print('Вас нет в списке')

conn.commit()
cur.close()
conn.close()
                  