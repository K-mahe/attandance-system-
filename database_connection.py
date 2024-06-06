import mysql.connector
import datetime
from get_faces_from_camera_tkinter import Face_Register

def update_registered_faces_count(count):
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Siddu@187",
        database="mysql"
    )
    cursor = conn.cursor()
    
    # Update the count of registered faces in the database
    date_today = datetime.datetime.now().strftime('%Y-%m-%d')
    cursor.execute("INSERT INTO attendance_info (date, registered_faces) VALUES (%s, %s) ON DUPLICATE KEY UPDATE registered_faces = %s",
                   (date_today, count, count))
    
    # Commit changes
    conn.commit()

    # Close the connection
    conn.close()

def count_attendance():
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Siddu@187",
        database="mysql"
    )
    cursor = conn.cursor()
    
    # Count the total number of presentees
    cursor.execute("SELECT COUNT(DISTINCT name) FROM attendance WHERE date = %s ", (datetime.datetime.now().strftime('%Y-%m-%d'),))
    presentees_count = cursor.fetchone()[0]

    # Count the total number of students
    cursor.execute("SELECT COUNT(DISTINCT name) FROM attendance")
    total_students_count = cursor.fetchone()[0]

    # Calculate the total number of absentees
    absentees_count = total_students_count - presentees_count

    # Close the connection
    conn.close()

    return presentees_count, absentees_count

def main():
    # Initialize your Face_Register class instance
    Face_Register_con = Face_Register()

    # Update the count of registered faces in the database
    registered_faces_count = Face_Register_con.count_registered_faces()
    update_registered_faces_count(registered_faces_count)

    # Count attendance
    presentees, absentees = count_attendance()
    print("Total Presentees:", presentees)
    print("Total Absentees:", absentees)

if __name__ == '__main__':
    main()
