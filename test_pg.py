import psycopg
import time

# Connection Config
# NOTE: While you have an Ingress, standard Kubernetes Ingress is for HTTP traffic.
# PostgreSQL uses TCP. To connect to the DB from outside K8s (like this script),
# you typically use 'kubectl port-forward' or a NodePort/LoadBalancer.
# Example port-forward: kubectl port-forward svc/postgres-db 5432:5432 -n exercises
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "mdb"
DB_USER = "admin"
DB_PASS = "postgres"

def connect_and_query():
    print(f"Connecting to {DB_NAME} at {DB_HOST}:{DB_PORT} as {DB_USER}...")
    try:
        # 1. Connect to the database
        # automocommit=True lets us execute commands without manually calling conn.commit() for every transaction,
        # but for transactions (like money transfer) you often want default behavior (autocommit=False).
        with psycopg.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        ) as conn:
            print("Connected successfully!")

            # 2. Open a cursor to perform database operations
            # The cursor is used to execute queries and fetch results
            with conn.cursor() as cur:

                # 3. Execute a Command (Create Table)
                print("Creating table 'usage_test'...")
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS usage_test (
                        id serial PRIMARY KEY,
                        info text,
                        created_at timestamp DEFAULT current_timestamp
                    )
                """)

                # 4. Insert Data
                # Use strict placeholders (%s) for security (prevents SQL injection)
                print("Inserting data...")
                cur.execute(
                    "INSERT INTO usage_test (info) VALUES (%s)",
                    ("Hello from psycopg!",)
                )

                # 5. Commit changes
                # (Required if autocommit is False, which is default)
                conn.commit()
                print("Data committed.")

                # 6. Query Data
                print("Querying data...")
                cur.execute("SELECT * FROM usage_test ORDER BY id DESC LIMIT 1")

                # 7. Fetch Result
                # fetchone() returns a single tuple, fetchall() returns a list of tuples
                row = cur.fetchone()
                print(f"Retrieved row: {row}")

    except Exception as e:
        print(f"Error: {e}")
        print("Tip: Ensure you have port-forwarded the service if running locally:")
        print("kubectl port-forward svc/postgres-db 5432:5432 -n exercises")

if __name__ == "__main__":
    connect_and_query()
