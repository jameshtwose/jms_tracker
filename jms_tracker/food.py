import pandas as pd
import numpy as np
import os
import psycopg2

from dotenv import load_dotenv
from jmspack.internal_utils import (postgresql_data_extraction,
                                    postgresql_table_names_list,
                                   create_postgresql_table_based_on_df,
                                    add_data_to_postgresql_table,
                                   delete_postgresql_table)

from flask import Blueprint, render_template, redirect, url_for, request, flash

load_dotenv("../.env")

table_name = "foodcodes"

try:
    conn = psycopg2.connect(
        host=os.getenv("postgresql_host"),
        database="tracker",
        user="tracker",
        password=os.getenv("postgresql_password"),
    )
    df = pd.read_sql_query(f"SELECT * from {table_name}", conn)

    _ = conn.commit()
    _ = conn.close()

except psycopg2.Error as e:
    print(e)

food_examples = {
    "food":[
    {
    "name": "apple",
    "barcode": 132124123,
    },
    {
        "name": "banana",
        "barcode": 258746,
    },
    {
        "name": "minty",
        "barcode": 87197401,
    },
    ]
}


food_example =     {
    "name": "apple",
    "barcode": 132124123,
    }

food = Blueprint("food", __name__)

@food.route('/foodCodes', methods=['GET'])
def food_get():
    return df.to_json(orient="records")


