from os import environ as env

DB_DETAILS = {
    "dev": {
        "SOURCE_DB": {
            "DB_TYPE": "mysql",
            "DB_HOST": "localhost",
            "DB_NAME": "s_retail_db",
            "DB_USER": env["SOURCE_DB_USER"],
            "DB_PASS": env["SOURCE_DB_KEY"]
        },
        "TARGET_DB": {
            "DB_TYPE": "postgres",
            "DB_HOST": "localhost",
            "DB_NAME": "t_retail_db",
            "DB_USER": env["TARGET_DB_USER"],
            "DB_PASS": env["TARGET_DB_KEY"]
        }
    }
}

if __name__ == "__main__":
    print(DB_DETAILS)