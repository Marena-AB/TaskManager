from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['GET', 'POST'])
def manage_tasks():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
        return redirect(url_for('manage_tasks'))

    return render_template('index.html', tasks=tasks)

@app.route('/tasks/<task>', methods=['DELETE'])
def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        return jsonify({'message': 'Task deleted'}), 200
    return jsonify({'message': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

