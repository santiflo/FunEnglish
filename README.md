# Fun English

La siguiente aplicación es servir como API REST para la aplicación FUN ENGLISH.

Las rutas que han sido ceadas para ser consumidas son las siguientes

## USER:
*Este metodo permite crear un usuario*
@app.route('/User/Create', methods = ["POST"])

*Este metodo permite listar todos los usuarios*
@app.route('/User', methods = ["GET"])

*Este metodo permite buscar un usuario mediante su id*
@app.route('/User/Search/id/<user_id>', methods = ["GET"])

*Este metodo permite actualizar un usuario*
@app.route('/User/Update', methods = ["PUT"])

*Este metodo permite actualizar la contrasena*
@app.route('/User/Update/password', methods = ["PUT"])

*Este metodo permite eliminar un usuario*
@app.route('/User/Delete/<user_id>', methods = ["DELETE"])

*Este metodo permite traer la informacion del usuario para desplegar en el menu*
@app.route('/User/Menu/<user_id>', methods = ["GET"])

*Este metodo permite traer unos campos especificos para el administrador*
@app.route('/User/Administrator', methods = ["GET"])

*Metodo que permite contar la cantidad de usuarios de la plataforma*
@app.route('/User/Amount', methods = ["GET"])

*Este metodo permite activar y desctivar un usuario*
@app.route('/User/Update/is_activate/<user_id>', methods = ["PUT"])


## Login