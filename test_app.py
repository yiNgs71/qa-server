import pytest
from app import app, db, Producto

@pytest.fixture
def client():
    # Configuración del cliente de pruebas y BD en memoria
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            p1 = Producto(nombre="Item Inicial", categoria="QA")
            db.session.add(p1)
            db.session.commit()
        yield client
        with app.app_context():
            db.drop_all()

def test_leer_productos(client):
    # Prueba la obtención de productos
    response = client.get('/productos')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) >= 1
    assert isinstance(data[0]['nombre'], str)

def test_crear_producto(client):
    # Prueba la creación de un producto
    nuevo = {"nombre": "Teclado", "categoria": "Hardware"}
    response = client.post('/productos', json=nuevo)
    assert response.status_code == 201
    assert "id" in response.get_json()

def test_eliminar_producto(client):
    # Prueba la eliminación de un producto
    productos = client.get('/productos').get_json()
    conteo_antes = len(productos)
    id_para_borrar = productos[0]['id']

    res = client.delete(f'/productos/{id_para_borrar}')
    assert res.status_code == 204

    res_final = client.get('/productos')
    assert len(res_final.get_json()) == conteo_antes - 1

def test_crear_producto_invalido(client):
    # Prueba el manejo de datos incompletos
    incompleto = {"nombre": "Solo Nombre"}
    with pytest.raises(Exception):
        client.post('/productos', json=incompleto)

def test_integridad_datos_post_get(client):
    # Prueba el flujo de creación y persistencia
    nuevo = {"nombre": "Mouse", "categoria": "Perifericos"}
    client.post('/productos', json=nuevo)
    
    res = client.get('/productos')
    nombres = [p['nombre'] for p in res.get_json()]
    assert "Mouse" in nombres

def test_error_404(client):
    # Prueba el error al borrar ID inexistente
    response = client.delete('/productos/999')
    assert response.status_code == 404