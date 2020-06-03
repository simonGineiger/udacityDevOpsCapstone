from sqlalchemy import create_engine
import pandas as pd
import boto3
import utils

ssm_client = boto3.client("ssm", region_name="eu-central-1")
connection_string_parameter = ssm_client.get_parameter(Name="bankoji_postgres_connection_string", WithDecryption=True)
connection_string = connection_string_parameter["Parameter"]["Value"]
engine = create_engine(connection_string, echo=False)


def get_latest(pairings, timeframe_in_minutes, stats=False):
    results = dict()
    timeframe = utils.build_timeframe(timeframe_end=utils.get_last_passed_minute_utc(), duration_in_minutes=timeframe_in_minutes)
    earliest, latest = (timeframe[0], timeframe[-1])
    for pairing in pairings:
        query = "SELECT * FROM {} WHERE start_time BETWEEN '{}' AND '{}'".format(pairing.lower(), earliest, latest)
        data = pd.read_sql(query, engine)
        if stats:
            results[pairing] = data.describe().to_json()
        else:
            results[pairing] = data.to_json()
    return results


def get_damaged(pairings, mend_only=False):
    results = dict()
    for pairing in pairings:
        if mend_only:
            query = "SELECT * FROM {} WHERE mend = True ".format(pairing.lower())
        else:
            query = "SELECT * FROM {} WHERE mend = True OR review = True " \
                    "OR checked = False OR sane = False".format(pairing.lower())
        result = pd.read_sql(query, engine)
        results[pairing] = result.to_json()
    return results


########################################################################################


#
# def initialize_database():
#     create_smrfcohlcv_table_statement = "CREATE TABLE {} (" \
#                                         "start_time TIMESTAMP PRIMARY KEY," \
#                                         "sane BOOL," \
#                                         "mend BOOL," \
#                                         "review BOOL," \
#                                         "filled BOOL," \
#                                         "checked BOOL," \
#                                         "open NUMERIC," \
#                                         "high NUMERIC," \
#                                         "low NUMERIC," \
#                                         "close NUMERIC," \
#                                         "volume NUMERIC" \
#                                         ")"
#     for pairing in pairings:
#         engine.execute(create_smrfcohlcv_table_statement.format(pairing.lower()))
#
#
# def drop_all_tables():
#     drop_string = "DROP TABLE {}"
#     for pairing in pairings:
#         engine.execute(drop_string.format(pairing.lower()))


##########################################################################################################





