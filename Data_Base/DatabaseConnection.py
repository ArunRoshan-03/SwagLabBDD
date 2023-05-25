import pymysql


class DatabaseConnection:

    def __init__(self, cursor):
        self.cursor = cursor

    def insert_data(self, product_names, product_prices, table_name):
        try:
            create_table_query = f"""
                    CREATE TABLE IF NOT EXISTS {table_name} (
                          id INT AUTO_INCREMENT PRIMARY KEY,
                          product_name VARCHAR(50),
                          product_price DECIMAL(10, 2)
                    )
                """
            self.cursor.execute(create_table_query)
            print("Table created successfully")

            insert_query = f"INSERT INTO {table_name} (product_name, product_price) VALUES (%s, %s)"

            for name, price in zip(product_names, product_prices):
                select_query = f"SELECT * FROM {table_name} WHERE product_name = %s AND product_price = %s"
                self.cursor.execute(select_query, (name, price))
                existing_data = self.cursor.fetchone()

                if existing_data:
                    print("Data already exists:", existing_data)
                else:
                    try:
                        self.cursor.execute(insert_query, (name, price))
                        self.cursor.connection.commit()
                        print(f"Data inserted successfully: {name}, {price}")
                    except pymysql.Error as e:
                        print("Error occurred while inserting data:", e)

            print("All data inserted successfully")
        except pymysql.Error as e:
            print("Error occurred while connecting to MySQL:", e)

    def retrieve_data(self, table_name):
        try:
            select_query = f"SELECT * FROM {table_name}"
            self.cursor.execute(select_query)
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
        except pymysql.Error as e:
            print("Error occurred while connecting to MySQL:", e)
