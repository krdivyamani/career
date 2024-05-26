from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': "ML Engineer",
    'salary': 100000
}, {
    'id': 2,
    'title': "Robotics Engineer",
    'salary': 150000
}, {
    'id': 3,
    'title': "CV Engineer",
    'salary': 1100000
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS)


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
