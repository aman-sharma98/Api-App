import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                    user="aman",
                    passwd="aman@1998",
                    db="audios")
    
    c = conn.cursor()

    return c, conn