from flask import Flask, jsonify, request

app = Flask(__name__)

states = [{"id": "1da255c0-f023-4779-8134-2b1b40f87683", "name": "New Orleans"}, {"id": "45903748-fa39-4cd0-8a0b-c62bfe471702", "name": "Lafayette"}, {"id": "e4e40a6e-59ff-4b4f-ab72-d6d100201588", "name": "Baton rouge"}]
@app.route("/states", methods=["GET"])
def get_states():
    return jsonify({"states": states})

@app.route("/states/<state_id>", methods=["GET"])
def get_state(state_id):
    for state in states:
        if state.get("id") == state_id:
            return jsonify(state)
    return jsonify({"message": "The state you are looking for does not exist"})

@app.route("/states", methods=["POST"])
def create_state():
    state_to_add = request.get_json()
    states.append(state_to_add)
    return jsonify({"message": "Success"})

if __name__ == "__main__":
    app.run()
