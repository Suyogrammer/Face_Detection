import mysql.connector

print('Start')
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nepal123!"
    )

    if conn.is_connected():
        print("Connection successfully established to MYSQL server")

except mysql.connector.Error as err:
    print("ERROR ", err)

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("🔌 Connection closed")
