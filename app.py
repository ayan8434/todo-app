from flask import Flask, request, jsonify
app = Flask(_name_)

todos = []

@app.route("/", methods=["GET"])
def home():
    return "Todo App is running"

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos), 200

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    if not data or "task" not in data:
        return jsonify({"error": "task required"}), 400
    todo = {"id": len(todos) + 1, "task": data["task"]}
    todos.append(todo)
    return jsonify(todo), 201

@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return jsonify({"message": "deleted"}), 200

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
