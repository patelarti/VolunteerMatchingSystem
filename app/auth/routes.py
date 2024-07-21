from flask import render_template, request, jsonify, redirect, url_for, session, Blueprint
import bcrypt
import psycopg2
import uuid


auth_bp = Blueprint('auth', __name__)

# Connect to the database
conn = psycopg2.connect(database="volunteers_db", user="postgres",
                        password="arti", host="localhost", port="5432")

testUsers = [
    {'email': 'patelarti91@gmail.com', 'password': bcrypt.hashpw('1111'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') },
    { 'email': 'rahmaaloui3199@gmail.com', 'password': bcrypt.hashpw('1234'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') },
    { 'email': 'john.doe@example.com', 'password': bcrypt.hashpw('password1'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') },
    { 'email': 'jane.smith@example.com', 'password': bcrypt.hashpw('password2'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') },
    { 'email': 'michael.brown@example.com', 'password': bcrypt.hashpw('password3'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') },
    { 'email': 'emily.jones@example.com', 'password': bcrypt.hashpw('password4'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') }
]



@auth_bp.route('/')
def index():
    return render_template('index.html')

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        # command = f"SELECT * FROM usercredentials where email='{email}';"
        # cursor = conn.cursor()
        # cursor.execute(command)
        # table_data = cursor.fetchone()
        # cursor.close()
        # print(table_data)

        user = next((user for user in testUsers if user['email'] == email), None)
        if not user or not bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            session["signed_in"] = False
            return jsonify({'message': 'Invalid email or password'}), 401

        session['signed_in'] = True
        session['email'] = email
        session['username'] = session['email'].split('@')[0]
        print("session['username']====>", session['username'])

        return jsonify({'message': 'Login successful'}), 200
        # return "login success"
    return render_template('index.html')

@auth_bp.route('/base')
def base():
    if session.get('signed_in') is None or session["signed_in"] == False:
        return render_template("index.html")
    return render_template('base.html', email=session['email'], username=session['username'])

@auth_bp.route("/logout")
def logout():
    session['signed_in'] = False
    session['email'] = ''
    session['username'] = ''
    #print("Logout....")
    return render_template("index.html")


@auth_bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirmPassword')
        print("data==>",data)

        if password != confirm_password:
            return jsonify({'message': 'Passwords do not match'}), 400

        user_exists = next((user for user in testUsers if user['email'] == email), None)
        if user_exists:
            return jsonify({'message': 'User already exists'}), 400

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        testUsers.append({'email': email, 'password': hashed_password})
        print("hashed_password==>",len(hashed_password))

        session["signed_in"] = True

        session["email"] = email
        session['username'] = session['email'].split('@')[0]

        unique_id = uuid.uuid4()
        session["user_id"] = unique_id
        print("unique_id==>", unique_id)

        command = f"INSERT INTO usercredentials (id, username, email, password) VALUES (2, '{session['username']}', '{session['email']}','{hashed_password}');"
        cursor = conn.cursor()
        cursor.execute(command)
        conn.commit()
        # table_data = cursor.fetchone()
        cursor.close()
        # print(table_data)

        return jsonify({'message': 'User registered successfully'}), 201

    return render_template('register.html')

@auth_bp.route('/forgot', methods=['GET', 'POST'])
def forgot():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')

        user = next((user for user in testUsers if user['email'] == email), None)
        if not user:
            return jsonify({'message': 'Email not found'}), 404

        reset_link = f"http://127.0.0.1:5000/reset?email={email}"
        print(f"Password reset link (simulated): {reset_link}")

        return jsonify({'message': 'Password reset link sent to your email'}), 200

    return render_template('forgot.html')

@auth_bp.route('/reset', methods=['GET', 'POST'])
def reset():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        new_password = data.get('newPassword')
        confirm_new_password = data.get('confirmNewPassword')


        if new_password != confirm_new_password:
            return jsonify({'message': 'Passwords do not match'}), 400

        user = next((user for user in testUsers if user['email'] == email), None)
        if not user:
            return jsonify({'message': 'Email not found'}), 404

        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user['password'] = hashed_password
        print("resetting password")

        return jsonify({'message': 'Password reset successfully'}), 200
    email = request.args.get('email')
    return render_template('reset.html', email=email)
