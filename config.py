from os import environ as env

DB_DETAILS = {
    "dev": {
        "SOURCE_DB": {
            "DB_TYPE": "mysql",
            "DB_HOST": "localhost",
            "DB_NAME": "s_retail_db",
            "DB_USER": env.get("SOURCE_DB_USER", None),
            "DB_PASS": env.get("SOURCE_DB_KEY", None)
        },
        "TARGET_DB": {
            "DB_TYPE": "postgres",
            "DB_HOST": "localhost",
            "DB_NAME": "t_retail_db",
            "DB_USER": env.get("TARGET_DB_USER", None),
            "DB_PASS": env.get("TARGET_DB_KEY", None)
        }
    }
}

if __name__ == "__main__":
    print(DB_DETAILS)