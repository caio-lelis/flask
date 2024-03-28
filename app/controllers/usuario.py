from app import app
from flask import Flask, jsonify, request
from app.config import get_db_connection

@app.route('/get/usuarios', methods=['POST', 'GET'])
def get_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(usuarios)


@app.route('/post/usuario', methods=['POST', 'GET'])
def add_usuario():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome, email) VALUES (%s, %s)', (request.json['nome'], request.json['email']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'status': 'ok'})

