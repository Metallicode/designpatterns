import sqlite3
import datetime

class MessageLogger:
    def __init__(self):
        self._connect_to_db()     
        self._create_table()
        
    def _connect_to_db(self):
        self._conn = sqlite3.connect('log.db')

    def _create_table(self):
        c = self._conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS logs (date TEXT, msg TEXT)")
        self._conn.commit()

    def LogMessage(self, msg):
        timeStamp = str(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        c = self._conn.cursor()
        c.execute(f"INSERT INTO logs VALUES (?,?)", (timeStamp, f"{msg[0]} {msg[1]}"))
        self._conn.commit()

    def __del__(self):
        print("close db connection...")
        self._conn.close()




if __name__ == "__main__":    
    ml = MessageLogger()
    ml.LogMessage("this is test")


