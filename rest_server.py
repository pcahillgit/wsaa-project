from flask import Flask, request, jsonify, send_from_directory
from taskdao import taskDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/tasks', methods=['GET'])
def getAll():
    return jsonify(taskDAO.getAll())

@app.route('/tasks/<int:id>', methods=['GET'])
def findById(id):
    return jsonify(taskDAO.findByID(id))

@app.route('/tasks', methods=['POST'])
def create():
    task = request.json
    return jsonify(taskDAO.create(task))

@app.route('/tasks/<int:id>', methods=['PUT'])
def update(id):
    task = request.json
    return jsonify(taskDAO.update(id, task))

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify(taskDAO.delete(id))

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(debug=True)