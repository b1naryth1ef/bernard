from flask import Flask, jsonify
import json, sys

app = Flask(__name__)

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

CONFIG = load_config()
CARDS = {}

for card, opt in CONFIG["cards"].items():
    module, cles = card.rsplit(".", 1)
    module = "cards." + module
    __import__(module)
    cles = getattr(sys.modules[module], cles)
    CARDS[cles.__name__] = cles(opt)

@app.route("/")
def index(): pass

@app.route("/refresh")
def refresh():
    return jsonify({
        name: card.load() for name, card in CARDS.items()
    })

if __name__ == '__main__':
    app.run("0.0.0.0", port=6030, debug=True)
