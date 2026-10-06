import sqlite3

# Whitelisted columns
VALID_COLUMNS = {
    "student": ["id", "name", "spi"],
    "course": ["id", "name"],
    "registration": ["student_id", "course_id"]
}

def validate_column(col):
    table, field = col.split(".")
    return table in VALID_COLUMNS and field in VALID_COLUMNS[table]

def build_query(columns, where, order, limit):
    # Validate columns
    for col in columns:
        if not validate_column(col):
            raise ValueError(f"Invalid column: {col}")

    if not (1 <= limit <= 1000):
        raise ValueError("Limit must be between 1 and 1000")

    # Build SQL
    sql = f"SELECT {', '.join(columns)} FROM Student s JOIN CourseRegistration r ON s.id=r.student_id JOIN Course c ON r.course_id=c.id"
    params = []
    if where:
        sql += " WHERE " + where
    if order:
        sql += " ORDER BY " + order
    sql += f" LIMIT {limit}"
    return sql, params


# ---------------- SAMPLE INPUT ----------------
columns = ["student.name", "course.name"]
where = "course.id='CS201'"
order = "student.spi DESC"
limit = 3

sql, params = build_query(columns, where, order, limit)
print("SQL_OK")
print(sql)
