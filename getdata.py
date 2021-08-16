import configparser

import cx_Oracle
from config import Config


class GetData:
    def __init__(self):
        self.config = Config()

    def conn_driver(self):

        config_data = self.config.config_dsn()

        for data in range(len(config_data)):
            cx_Oracle.init_oracle_client(
                lib_dir=rf"{config_data[0]}")
            break

    def db_conn(self):
        config_data = self.config.config_dsn()
        dsn = cx_Oracle.makedsn(config_data[1], config_data[2], service_name=config_data[3])
        config_connection = self.config.config_connect()
        for i in range(len(config_connection)):
            connection = cx_Oracle.connect(config_connection[0], config_connection[1], dsn, encoding="UTF-8")
        cursor = connection.cursor()
        return cursor


    def get_data_from_db(self):
        cursor = self.db_conn()
        query = self.config.query()
        cursor.execute(query)
        result_set = cursor.fetchall()
        print(' ',result_set)
        return result_set




