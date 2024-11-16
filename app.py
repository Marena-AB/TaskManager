from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json.get('task')
    tasks.append(task)
    return jsonify({'message': 'Task added'}), 201

@app.route('/tasks/<int:index>', methods=['DELETE'])
def delete_task(index):
    if index < len(tasks):
        tasks.pop(index)
        return jsonify({'message': 'Task deleted'}), 200
    return jsonify({'message': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

