from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos de ejemplo para simular una base de datos
base_de_datos = [
    {
        "id": 1,
        "titulo": "Dragon Ball",
        "puntaje": 10,
        "tipo": "Serie",
        "season": "GT",
        "generos": "Accion"
    },
    {
        "id": 2,
        "titulo": "haykyuu",
        "puntaje": 9,
        "tipo": "Serie",
        "season": 1,
        "generos": "deporte"
    },
    {
        "id": 3,
        "titulo": "Doraemon",
        "puntaje": 10,
        "tipo": "Serie",
        "season": 2,
        "generos": "comedia"
    }
]

#Ruta para pagina principal
@app.route("/")
def inicio():
    return "Anime"

# Ruta para manejar la solicitud GET (listar animes)
@app.route('/anime', methods=['GET'])
def listar_anime():
    return jsonify(base_de_datos), 200

# Ruta para manejar la solicitud POST (crear anime)
@app.route('/anime', methods=['POST'])
def crear_anime():
    datos = request.json

    if 'titulo' in datos and 'puntaje' in datos and 'tipo' in datos and 'season' in datos and 'generos' in datos:
        nuevo_anime = {
            "id": len(base_de_datos) + 1,
            "titulo": datos['titulo'],
            "puntaje": datos['puntaje'],
            "tipo": datos['tipo'],
            "season": datos['season'],
            "generos": datos['generos']
        }
        base_de_datos.append(nuevo_anime)
        return jsonify({"mensaje": "Anime creado exitosamente", "anime": nuevo_anime}), 201
    else:
        return jsonify({"mensaje": "Faltan campos en los datos recibidos"}), 400

# Ruta para manejar la solicitud GET de un anime por su ID
@app.route('/anime/<int:anime_id>', methods=['GET'])
def obtener_anime(anime_id):
    anime = next((anime for anime in base_de_datos if anime['id'] == anime_id), None)
    if anime:
        return jsonify(anime), 200
    else:
        return jsonify({"mensaje": "Anime no encontrado"}), 404

# Ruta para manejar la solicitud PUT para actualizar un anime por su ID
@app.route('/anime/<int:anime_id>', methods=['PUT'])
def actualizar_anime(anime_id):
    datos = request.json
    anime = next((anime for anime in base_de_datos if anime['id'] == anime_id), None)

    if anime:
        anime.update(datos)
        return jsonify({"mensaje": "Anime actualizado exitosamente", "anime": anime}), 200
    else:
        return jsonify({"mensaje": "Anime no encontrado"}), 404

# Ruta para manejar la solicitud DELETE de un anime por su ID
@app.route('/anime/<int:anime_id>', methods=['DELETE'])
def eliminar_anime(anime_id):
    global base_de_datos
    anime = next((anime for anime in base_de_datos if anime['id'] == anime_id), None)

    if anime:
        base_de_datos = [a for a in base_de_datos if a['id'] != anime_id]
        return jsonify({"mensaje": "Anime eliminado exitosamente"}), 200
    else:
        return jsonify({"mensaje": "Anime no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
