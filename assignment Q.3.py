import mysql.connector
import csv

def student_course_analytics(db_config, student_csv, reg_csv, course_id, spi_threshold):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Create tables if not exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Student (
            id INT PRIMARY KEY,
            name VARCHAR(100),
            spi FLOAT
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS CourseRegistration (
            student_id INT,
            course_id VARCHAR(20),
            FOREIGN KEY (student_id) REFERENCES Student(id)
        )
        """)

        # Insert students
        with open(student_csv, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                cursor.execute("INSERT IGNORE INTO Student VALUES (%s,%s,%s)", (int(row[0]), row[1], float(row[2])))

        # Insert registrations
        with open(reg_csv, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                cursor.execute("INSERT IGNORE INTO CourseRegistration VALUES (%s,%s)", (int(row[0]), row[1]))

        conn.commit()

        # Query students with SPI > threshold for given course
        query = """
        SELECT s.id, s.name, s.spi, c.course_id
        FROM Student s
        JOIN CourseRegistration c ON s.id = c.student_id
        WHERE c.course_id = %s AND s.spi > %s
        ORDER BY s.spi DESC, s.id ASC
        """
        cursor.execute(query, (course_id, spi_threshold))
        results = cursor.fetchall()

        for r in results:
            print(r[0], r[1], r[2], r[3])

    except mysql.connector.Error as e:
        print("Database error:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


# ---------------- SAMPLE INPUT ----------------
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "college"
}

# student.csv
# 101,Riya,9.2
# 102,Karan,7.8
# 103,Meera,8.5

# registration.csv
# 101,PY201
# 102,PY201
# 103,PY201

student_course_analytics(db_config, "student.csv", "registration.csv", "PY201", 8.0)
