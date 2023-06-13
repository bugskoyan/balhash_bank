# Python
import datetime

# Local
from database.core import Connection


class User:
    """Object from db. User."""

    id:int
    first_name: str
    last_name: str
    date_of_birth: datetime.datetime
    iin: str
    phone_number: str

    @staticmethod
    def create(
        conn: Connection,
        first_name: str,
        last_name: str,
        date_of_birth: datetime,
        iin: str,
        phone_number: str
    ):
        with conn.cursor() as cur:
            cur.execute(f"""
                INSERT INTO users(
                    first_name,
                    last_name,
                    date_of_birth,
                    iin,
                    phone_number
                )
                VALUES (
                    '{first_name}',
                    '{last_name}',
                    '{date_of_birth}',
                    '{iin}',
                    '{phone_number}'
                )
                """
            )

    @staticmethod
    def get(conn: Connection,**kwargs: dict[str,any]) -> 'User':
        """SELECT * FROM users WHERE id=1 AND user='as'"""

        condition: list[str] = []
        for i in kwargs:
            if isinstance(kwargs[i], str):
                condition.append(f"{i}='{kwargs[i]}'")
            else:
                condition.append(f'{i}={kwargs[i]}')

        
        with conn.cursor() as cur:
            cur.execute(f"""
                SELECT * FROM users
                WHERE {' AND '.join(condition)}
                LIMIT 1
            """)
            return cur.fetchone()
        

    @staticmethod
    def filter(conn: Connection,**kwargs: dict[str,any]) -> 'User':

        condition: list[str] = []
        for i in kwargs:
            if isinstance(kwargs[i], str):
                condition.append(f"{i}='{kwargs[i]}'")
            else:
                condition.append(f'{i}={kwargs[i]}')

        
        with conn.cursor() as cur:
            cur.execute(f"""
                SELECT * FROM users
                WHERE {' AND '.join(condition)}
            """)
            return cur.fetchall()
        

    @staticmethod
    def all(conn: Connection) -> 'User':
        with conn.cursor() as cur:
            cur.execute(f"""
                SELECT * FROM users
            """)
            return cur.fetchall()
        

    @staticmethod
    def join(conn: Connection) ->'User':
        with conn.cursor() as cur:
            cur.execute(f"""
                SELECT users.first_name, users.last_name, cards.number, cards.date_end, accounts.balance FROM accounts
                INNER JOIN users ON users.id = accounts.owner_id
                INNER JOIN cards ON cards.account_id = accounts.id

            """)
            return cur.fetchall()
        

 

