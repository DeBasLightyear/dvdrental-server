from typing import Any, List
import psycopg2
from flask import Flask, jsonify, request

from config import postgres_connection_variables
app = Flask(__name__)


def _execute_query(sql: str) -> List[List[Any]]:
    # get a connection
    conn_vars = postgres_connection_variables()
    conn = psycopg2.connect(
        dbname=conn_vars.name,
        user=conn_vars.user,
        password=conn_vars.password,
        host=conn_vars.host,
        port=conn_vars.port
    )

    # execute the query
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            column_names = [d[0] for d in cursor.description]
            result = cursor.fetchall()

    conn.close()
    return [column_names, *result]


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/dvdrental/', methods=['POST'])
def execute_query_on_database():
    """
    POST to this endpoint with a sql field or a JSON object with sql field, that contains your query.
    """

    # not sure which method will come in handy, so I'll support both for now
    sql = (request.values.get('sql', None) or
           request.get_json().get('sql', None))

    if sql is None:
        return 'Error: Provide a query to fetch data and test your SQL skills.', 400

    result = _execute_query(sql)

    return jsonify(result), 200
