from flask import Flask, render_template, request
from predict import predict_attack

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def dashboard():
    result = None
    confidence = None

    if request.method == "POST":
        features = {
            "duration": int(request.form["duration"]),
            "src_bytes": int(request.form["src_bytes"]),
            "dst_bytes": int(request.form["dst_bytes"]),
            "failed_logins": int(request.form["failed_logins"])
        }

        result, confidence = predict_attack(features)

    return render_template("dashboard.html", result=result, confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True)
