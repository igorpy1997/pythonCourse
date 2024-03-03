from flask import Flask, request, render_template, redirect
from random import randint
import sqlite3

from models.user import User
app = Flask(__name__, static_url_path='/static')

@app.route("/delete_item/<key>")
def delete_item(key):
    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql_add_item = f"""
        DELETE FROM user
        WHERE id = {key}
        """
        cur.execute(sql_add_item)
        conn.commit()
        return redirect("/show_base_elements")
    finally:
        conn.close()

@app.route("/write_to_db/<state>", methods = ["POST"])
def write_to_db(state):
    try:
        conn = sqlite3.connect('users.db')
        name_temp = str(request.form.get('name'))
        language_temp = str(request.form.get('language'))
        course_temp = str(request.form.get('course'))
        grade_temp = str(request.form.get('grade'))
        cur = conn.cursor()
        if state == "new_element":
            sql_add_item = f"""
                INSERT INTO user (name, language, course, grade)
                VALUES ( '{name_temp}', '{language_temp}', '{course_temp}', '{grade_temp}');
            """

            cur.execute(sql_add_item)
        else:
            sql_add_item = f"""
                UPDATE user
                SET name = '{name_temp}', language = '{language_temp}', course = '{course_temp}', grade = '{grade_temp}'
                WHERE id = {state}
            """
            print(sql_add_item)
            cur.execute(sql_add_item)

        conn.commit()
        return redirect("/show_base_elements")
    finally:
        conn.close()


@app.get("/writing_menu_db/<key>")
def writing_menu_db(key):
    if key == 'new_element':
        return render_template("add_menu.html", student=None, state=key)
    else:
        temp_list = read_from_db()
        temp_val = 0
        for temp in temp_list:
            if temp[0] == int(key):
                temp_val = temp
        return render_template("add_menu.html", student=temp_val, state=key)


#@app.route("/write_into_db", methods = ["POST"])
#def write_into_db():

@app.route("/read_from_db", methods = ["POST"])
def read_from_db():
    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = """
            SELECT * FROM user;
        """
        cur.execute(sql)

        return cur.fetchall()
    finally:
        conn.close()

@app.route("/show_base_elements", methods = ["GET"])
def show_base_elements():
        temp_list = read_from_db()
        return render_template("show_student_list.html",student_list=temp_list)

@app.route("/")
def show_items():
    return render_template("main_screen.html")


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)

