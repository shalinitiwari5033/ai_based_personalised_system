from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import json
from bot import get_bot_response
app = Flask(__name__)
app.secret_key = "f473225f97b2d2f10e6c71335e0824d65169b48ef910a85030d42cd557fb2277" 

# Load video and questions data
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Dummy user database
users = {}

@app.route('/')
def home():
    if 'username' in session:
        return render_template("index.html", username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template("login.html", error="Invalid username or password.")

    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            return render_template("register.html", error="Username already exists.")
        else:
            users[username] = password
            return redirect(url_for('login'))

    return render_template("register.html")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/get_data', methods=['POST'])
def get_data():
    if 'username' not in session:
        return jsonify({"error": "Not logged in."}), 401

    topic = request.json.get("topic")
    topic_data = data.get(topic)

    if topic_data:
        return jsonify(topic_data)
    else:
        return jsonify({"error": "Topic not found"}), 404

@app.route('/bot')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    bot_reply = get_bot_response(user_message)
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
