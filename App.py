from flask import Flask, request, render_template
from search import search

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("search.html")

@app.route("/results", methods=["GET"])
def results():
    query = request.args.get("q", "")
    results = search(query)
    return render_template("results.html", query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)
