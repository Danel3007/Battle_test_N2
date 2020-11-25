import json

def write_state(state, filename="state.json"):
    data = json.dumps(state, ensure_ascii=False)

    file = open(filename, "w")
    file.write(data)
    file.close()

def read_state(filename="state.json"):
    file = open(filename, "r")

    data = file.read()
    file.close()
    return json.loads(data)