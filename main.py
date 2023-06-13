#Python
from decouple import config 
import datetime

#local
from database.core import Connection
from database.models.users import User
from database.models.cards import Cards
from database.models.accounts import Accounts


my_connection: Connection = Connection(
    host=config('DB_HOST', str),
    port=config('DB_PORT', int),
    user=config('DB_USER', str),
    password=config('DB_PASSWORD', str),
    dbname=config('DB_NAME', str)
)

if __name__ == '__main__':
    my_connection.create_tables()
    # User.create(
    #     conn=my_connection.conn,
    #     first_name='Bob',
    #     last_name= 'Hui',
    #     date_of_birth=datetime.datetime(
    #         year=1999,
    #         month=12,
    #         day=25
    #     ),
    #     iin='980515123453',
    #     phone_number='7009000903'
    # )
    # Accounts.create(
    #     conn=my_connection.conn,
    #     number='38457934702987098407',
    #     owner_id=12,
    #     balance=1500,
    #     type='soop'
    # )
    # Cards.create(
    #     conn=my_connection.conn,
    #     number='4400546834549899',
    #     account_id=1,
    #     cvv='987',
    #     date_end=datetime.datetime(
    #         year=2025,
    #         month=11,
    #         day=20
    #     ),
    #     is_active=True,
    #     pin='1234'
    # )
   
   
    # print(User.all(conn=my_connection.conn))
    
    # print(User.filter(conn=my_connection.conn, last_name='Bob'))

    print(User.join(conn=my_connection.conn))
 