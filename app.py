from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Updated task list to store both title and description
tasks = []

@app.route('/tasks', methods=['GET', 'POST'])
def manage_tasks():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        # Store task as a dictionary with title and description
        task = {'title': title, 'description': description}
        tasks.append(task)
        return redirect(url_for('manage_tasks'))

    return render_template('index.html', tasks=tasks)

@app.route('/tasks/delete/<task_title>', methods=['DELETE'])
def delete_task(task_title):
    # Find the task by its title and remove it
    task_to_remove = next((task for task in tasks if task['title'] == task_title), None)
    if task_to_remove:
        tasks.remove(task_to_remove)
        return jsonify({'message': 'Task deleted'}), 200
    return jsonify({'message': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
