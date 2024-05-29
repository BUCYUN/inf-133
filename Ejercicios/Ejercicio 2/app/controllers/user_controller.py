#from flask import Blueprint, request, jsonify
#from models.user_model import User
#from flask_jwt_extended import create_access_token
#from werkzeug.security import check_password_hash
#
#user_bp = Blueprint("user", __name__)
#
#
#
#@user_bp.route("/register", methods=["POST"])
#def register():
#    data = request.json
#    username = data.get("username")
#    password = data.get("password")
#    roles = data.get("roles")
#
#    if not username or not password:
#        return jsonify({"error": "Se requieren nombre de usuario y contraseña"}), 400
#
#    existing_user = User.find_by_username(username)
#    if existing_user:
#        return jsonify({"error": "El nombre de usuario ya está en uso"}), 400
#
#    new_user = User(username, password, roles)
#    new_user.save()
#
#    return jsonify({"message": "Usuario creado exitosamente"}), 201
#
#
#@user_bp.route("/login", methods=["POST"])
#def login():
#    data = request.json
#    username = data.get("username")
#    password = data.get("password")
#
#    user = User.find_by_username(username)
#    if user and check_password_hash(user.password_hash, password):
#        # Si las credenciales son válidas, genera un token JWT
#        access_token = create_access_token(
#            identity={"username": username, "roles": user.roles}
#        )
#        return jsonify(access_token=access_token), 200
#    else:
#        return jsonify({"error": "Credenciales inválidas"}), 401
#
from flask import Blueprint, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

# Importamos el decorador de roles
from utils.decorator import roles_required

# Importamos la vista de usuarios
from views import dulce_views

# Importamos el modelo de usuario
from models.user_model import User

# Un Blueprint es un objeto que agrupa
# rutas y vistas
user_bp = Blueprint("user", __name__)


# Ruta de la página raíz redirige a
# la página de inicio de sesión
@user_bp.route("/")
def index():
    return dulce_views.registro()
    #if current_user.is_authenticated:
    #    return redirect(url_for("user.profile", id=current_user.id))
    #return redirect(url_for("user.login"))


@user_bp.route("/users")
#@login_required
#@roles_required(roles=["admin"])
def list_users():
    # Obtenemos todos los usuarios
    users = User.get_all()
    # Llamamos a la vista de usuarios
    return dulce_views.usuarios(users)


# Definimos la ruta "/users" asociada a la función registro
# que nos devuelve la vista de registro
@user_bp.route("/users/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        # Obtenemos los datos del formulario
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("El nombre de usuario ya está en uso", "error")
            return redirect(url_for("user.create_user"))
        # Creamos un nuevo usuario
        user = User(first_name, last_name, username, password, role=role)
        user.set_password(password)
        # Guardamos el usuario
        user.save()
        flash("Usuario registrado exitosamente", "success")
        return redirect(url_for("user.list_users"))
    # Llamamos a la vista de registro
    return dulce_views.registro()


# Actualizamos la información del usuario por su id
# Ya estamos en la vista de actualizar
# por lo que obtenemos los datos del formulario
# y actualizamos la información del usuario
@user_bp.route("/users/<int:id>/update", methods=["GET", "POST"])
#@login_required
#@roles_required(roles=["admin"])
def update_user(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    if request.method == "POST":
        # Obtenemos los datos del formulario
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        # Actualizamos los datos del usuario
        user.first_name = first_name
        user.last_name = last_name
        # Guardamos los cambios
        user.update()
        return redirect(url_for("user.list_users"))
    return dulce_views.actualizar(user)


@user_bp.route("/users/<int:id>/delete")
#@login_required
#@roles_required(roles=["admin"])
def delete_user(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    user.delete()
    return redirect(url_for("user.list_users"))


# Ruta para el inicio de sesión
@user_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.get_user_by_username(username)
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash("Inicio de sesión exitoso", "success")
            if user.has_role("admin"):
                # Redirigir a su perfil si el usuario es de rol "admin"
                return redirect(url_for("user.list_users"))
            else:
                # Redirigir a la lista de usuarios para otros roles
                return redirect(url_for("user.profile", id=user.id))
        else:
            flash("Nombre de usuario o contraseña incorrectos", "error")
    return dulce_views.login()


# Ruta para cerrar sesión
@user_bp.route("/logout")
#@login_required
def logout():
    logout_user()
    flash("Sesión cerrada exitosamente", "success")
    return redirect(url_for("user.login"))


@user_bp.route("/profile/<int:id>")
#@login_required
def profile(id):
    user = User.get_by_id(id)
    return dulce_views.perfil(user)
