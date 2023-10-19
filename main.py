from flask import Flask, render_template
from datos import productos

# crear el objeto de la App
app = Flask(__name__)

# ruta para el index
@app.route('/')
def index():
  for i, producto in enumerate(productos):
    producto['id']=i
  return render_template('index.html', productos=productos)

# ruta para los detalles del producto
@app.route('/producto/<prod_id>')
def producto(prod_id='0'):
  prod_id = int(prod_id)
  if not (0 <= prod_id <= len(productos)):
    prod_id = 0
  nombre = productos[prod_id]['nombre']
  precio = productos[prod_id]['precio']
  return render_template('producto.html', id=prod_id, nombre=nombre, precio=precio)


# principal
if __name__ == '__main__':
  # ejecutar la aplicación en cualquier IP y el puerto 8000
  app.run(host='0.0.0.0', port=8000, debug=True)
  