import mysql.connector
from modules import *
import os
from dotenv import load_dotenv
load_dotenv()

password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST", "127.0.0.1")
db_name = os.getenv("DB_NAME")
user = os.getenv("DB_USER")



def get_cnx():
    return mysql.connector.connect(password=password, host=host, database=db_name, user=user)


class DataInteractor:
    
    def __init__(self):
        self.cnx = get_cnx()

    def list_to_dict(items: list):
        return 
    
    def get_all(self):
        try:
            cursor = self.cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM contacts")
            rows = cursor.fetchall()
            self.cnx.commit()
            cursor.close()
            return rows
        except mysql.connector.Error as e:
            raise e
        
    def add_contact(self, contact: Contact):
        try:
            cursor = self.cnx.cursor()
            cursor.execute("INSERT INTO contacts (first_name, last_name,phone_number) VALUES (%s, %s, %s)",
            (contact['first_name'], contact['last_name'], contact['phone_number']))
            self.cnx.commit()
            new_id = cursor.lastrowid
            cursor.close()
            return{
                "message": "Contact created successfully",
                "id": new_id
            }
        except mysql.connector.Error as e:
            raise e 
    
    def update_contact(self, id: int, contact):
        try:
            cursor = self.cnx.cursor()
            query = f'"UPDATE contacts SET"'
            for k , v in contact.items():
                if v != None:
                    query = f"UPDATE contacts SET {k}=%s WHERE id=%s"
                    cursor.execute(query, (v, id,))
            if cursor.rowcount == 0:
                self.cnx.rollback()
                return {"message": "id not found"}
            self.cnx.commit()
            return {"message": "Contact update successfully"}
        except mysql.connector.Error as e:
            raise e
        finally:
            cursor.close()
        
        
    def del_contact(self, id: int):
        try:
            cursor = self.cnx.cursor()
            cursor.execute("DELETE FROM contacts WHERE id=%s",(id,))
            if cursor.rowcount == 0:
                self.cnx.rollback()
                return {"message": "id not found"}
            self.cnx.commit()
            cursor.close()
            return {"message": "Contact delete successfully"}
        except mysql.connector.Error as e:
            raise e
        finally:
            cursor.close()

