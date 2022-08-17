import sqlite3 as sq3
from flask import request
from flask_restful import Resource


class Articles(Resource):
    def post(self):
        data = request.get_json()
        conn = sq3.connect('data.db')
        curs = conn.cursor()

        query = "INSERT INTO articles VALUES(?, ?)"
        curs.execute(query, (data['title'], data['body']))

        conn.commit()
        conn.close()

        return {"message": "the article added successfuly...!"}

    def get(self):
        conn = sq3.connect('data.db')
        curs = conn.cursor()

        query = "SELECT * FROM articles"
        curs.execute(query)

        rows = curs.fetchall()
        conn.close()

        if rows:
            article = []
            for row in rows:
                article.append({"title": row[0], "body": row[1]})
        else:
            article = None

        return article
