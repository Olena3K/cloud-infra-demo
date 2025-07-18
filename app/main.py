from flask import Flask, render_template, jsonify
import psycopg2
import os

app = Flask(__name__)


def get_user_name():
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            database=os.environ.get("DB_NAME", "testdb"),
            user=os.environ.get("DB_USER", "testuser"),
            password=os.environ.get("DB_PASS", "testpass"),
        )
        cur = conn.cursor()
        cur.execute("SELECT name FROM users LIMIT 1;")
        result = cur.fetchone()
        cur.close()
        conn.close()
        if result:
            return result[0]
        return "No user found"
    except Exception as e:
        return f"Error: {e}"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/user")
def api_user():
    username = get_user_name()
    return jsonify({"username": username})


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
