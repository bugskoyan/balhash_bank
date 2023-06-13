

# Local
from database.core import Connection
from database.models.users import User


class Accounts:
    """Object from db. Account."""

    id:int
    number:str
    owner_id:User
    balance:int
    type:str
    
    @staticmethod
    def create(
        conn: Connection,
        number:str,
        owner_id:User,
        balance:int,
        type:str
    ):
        with conn.cursor() as cur:
            cur.execute(f"""
                INSERT INTO accounts(
                    number,
                    owner_id,
                    balance,
                    type
                )
                VALUES (
                    '{number}',
                    '{owner_id}',
                    '{balance}',
                    '{type}'
                )
                """
            )

    

    @staticmethod
    def filter(conn: Connection,**kwargs: dict[str,any]) -> 'Accounts':

        condition: list[str] = []
        for i in kwargs:
            if isinstance(kwargs[i], str):
                condition.append(f"{i}='{kwargs[i]}'")
            else:
                condition.append(f'{i}={kwargs[i]}')

        
        with conn.cursor() as cur:
            cur.execute(f"""
                SELECT * FROM accounts
                WHERE {' AND '.join(condition)}
            """)
            return cur.fetchall()
        

    @staticmethod
    def all(conn: Connection) -> 'Accounts':
        with conn.cursor() as cur:
            cur.execute(f"""
                SELECT * FROM accounts
            """)
            return cur.fetchall()