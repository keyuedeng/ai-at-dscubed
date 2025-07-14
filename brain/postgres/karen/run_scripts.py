import psycopg2



def get_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

def run_ddl():
    with open("DDL/create_table.sql", "r") as f:
        ddl_script = f.read()

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(ddl_script)
    conn.commit()
    cur.close()
    conn.close()
    print("DDL script executed: table created")

def run_dml():
    with open("DML/insert_data.sql", "r") as f:
        dml_script = f.read()

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(dml_script)
    conn.commit()
    cur.close()
    conn.close()
    print("DML script executed: data inserted")

def view_table(table_name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name};")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def run_downstream_ddl():
    with open("DDL/create_downstream_table.sql", "r") as f:
        ddl_script = f.read()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(ddl_script)
    conn.commit()
    cur.close()
    conn.close()
    print("Downstream DDL script executed: summary table created")


def run_downstream_dml():
    with open("DML/insert_downstream_table.sql", "r") as f:
        dml_script = f.read()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(dml_script)
    conn.commit()
    cur.close()
    conn.close()
    print("Downstream DML script executed: summary data inserted")


if __name__ == "__main__":
    run_ddl()
    run_dml()
    run_downstream_ddl()
    run_downstream_dml()
    view_table("project_two.employee")
    view_table("project_two.department_salary")


