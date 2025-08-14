from flask import Flask, request
app = Flask(__name__)
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        print("[HONEY] Creds:", request.form.get("user"), request.form.get("pass"))
        return "OK"
    return "<form method=post><input name=user><input name=pass type=password><button>Login</button></form>"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
