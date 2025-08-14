from flask import Flask, jsonify, request
import requests
app = Flask(__name__)
@app.route("/health")
def health(): return jsonify({"ok": True})
@app.route("/aggregate")
def aggregate():
    # placeholder aggregation
    indicators = [{"type":"ip","value":"1.2.3.4"},{"type":"hash","value":"abcd"*16}]
    return jsonify({"count": len(indicators), "indicators": indicators})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
