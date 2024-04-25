from flask import Flask, render_template, request
import subprocess


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    ip1 = request.form['ip1']
    ip2 = request.form['ip2']
    ip3 = request.form['ip3']
    public_key = request.form['public_key']

    try:
        command = f"./upload.sh '{public_key}' {ip1} {ip2} {ip3}"
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return render_template("success.html", message=result)
    except subprocess.CalledProcessError as e:
        e_message = f"Error: {e.output}"
        return render_template("error.html", message=e_message)

if __name__ == "__main__":
    app.run(debug=True)
