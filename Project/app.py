from flask import Flask, request, jsonify
from Puzzle import a_star

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.get_json()
    initial_state = data['initialState']
    goal_state = data['goalState']
    steps = a_star(initial_state, goal_state)
    return jsonify(result=steps)

if __name__ == '__main__':
    app.run(debug=True)