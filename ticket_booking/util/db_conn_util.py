import mysql.connector as sql

class DBConnUtil:
    def getconn(self):
        try:
            conn = sql.connect(host='localhost', database='ticket_booking_system', user='root', password='karthikeyan@26')
            if conn.is_connected():
                print("Database is connected.")
                return conn
        except Exception as e:
            print("Error:", e)
            return None

    def open(self):
        return self.getconn()
