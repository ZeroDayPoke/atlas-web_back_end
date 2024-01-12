#!/usr/bin/env python3
"""Logger"""
import logging
from typing import List
import re
import os
import mysql.connector
from mysql.connector import connection


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def main():
    db = get_db()
    logger = get_logger()

    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users;")
        for row in cursor:
            log_record = logging.LogRecord("user_data", logging.INFO,
                                           None, None, str(row), None, None)
            print(logger.handle(log_record))
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        cursor.close()
        db.close()


def get_db() -> connection.MySQLConnection:
    """Create and return a connection to the database."""
    db_username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')
    db_port = os.getenv('PERSONAL_DATA_DB_PORT', 3306)

    return mysql.connector.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        database=db_name,
        port=db_port
    )


def get_logger() -> logging.Logger:
    """Create and return a logger object."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns the log message obfuscated"""
    regex_pattern = '|'.join([f'(?<={field}=)[^{separator}]+'
                              for field in fields])
    return re.sub(regex_pattern, redaction, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """initializes RedactingFormatter"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filters values in incoming log records using filter_datum"""
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            original_message, self.SEPARATOR)


if __name__ == "__main__":
    main()
