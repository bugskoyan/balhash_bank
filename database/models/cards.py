# Python
import datetime

# Local
from database.core import Connection
from database.models.accounts import Accounts


class Cards:
    """Object from db. Cards."""

    id:int
    number:str
    account_id:Accounts
    cvv:int
    date_end:datetime
    is_active:bool
    pin:str

    @staticmethod
    def create(
        conn: Connection,
        number:str,
        account_id:Accounts,
        cvv:int,
        date_end:datetime,
        is_active:bool,
        pin:str
    ):
        with conn.cursor() as cur:
            cur.execute(f"""
                INSERT INTO cards(
                    number,
                    account_id,
                    cvv,
                    date_end,
                    is_active,
                    pin
                )
                VALUES (
                    '{number}',
                    '{account_id}',
                    '{cvv}',
                    '{date_end}',
                    '{is_active}',
                    '{pin}'
                )
                """
            )


    @staticmethod
    def filter(conn: Connection,**kwargs: dict[str,any]) -> 'Cards':

        condition: list[str] = []
        for i in kwargs:
            if isinstance(kwargs[i], str):
                condition.append(f"{i}='{kwargs[i]}'")
            else:
                condition.append(f'{i}={kwargs[i]}')

        
        with conn.cursor() as cur:
            cur.execute(f"""
                SELECT * FROM cards
                WHERE {' AND '.join(condition)}
            """)
            return cur.fetchall()
        
    

    @staticmethod
    def all(conn: Connection) -> 'Cards':
        with conn.cursor() as cur:
            cur.execute(f"""
                SELECT * FROM cards
            """)
            return cur.fetchall()