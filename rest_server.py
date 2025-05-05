from flask import Flask, request, jsonify
from taskdao import taskDAO

app = Flask(__name__)

@app.route('/tasks', methods=['GET'])
def getAll():
    return jsonify(taskDAO.getAll())

if __name__ == "__main__":
    app.run(debug=True)