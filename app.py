from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definición del modelo de Producto
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)

# Función para insertar datos de prueba si la base está vacía
def cargar_datos_iniciales():
    if Producto.query.count() == 0:
        p1 = Producto(nombre="Laptop IBM ThinkPad", categoria="Hardware")
        p2 = Producto(nombre="Licencia Cloud", categoria="Software")
        p3 = Producto(nombre="Monitor 4K", categoria="Hardware")
        db.session.add_all([p1, p2, p3])
        db.session.commit()
        print("Base de datos poblada con datos iniciales.")

# Endpoints para listar, crear y eliminar productos
@app.route('/productos', methods=['GET'])
def listar():
    productos = Producto.query.all()
    return jsonify([{"id": p.id, "nombre": p.nombre, "categoria": p.categoria} for p in productos])

@app.route('/productos', methods=['POST'])
def crear():
    data = request.get_json()
    nuevo = Producto(nombre=data['nombre'], categoria=data['categoria'])
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({"id": nuevo.id, "mensaje": "Creado con éxito"}), 201

@app.route('/productos/<int:id>', methods=['DELETE'])
def eliminar(id):
    producto = db.session.get(Producto, id)
    if producto:
        db.session.delete(producto)
        db.session.commit()
        return '', 204
    return jsonify({"error": "No encontrado"}), 404

# Inicialización del servidor y creación de tablas
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        cargar_datos_iniciales() 
    app.run(debug=True, host='0.0.0.0', port=5000)