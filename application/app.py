from flask import Flask, render_template, request
from ugly_youtube import UglyYoutube

youtube_api_key = "INSERT YOU API KEY HERE"
yt = UglyYoutube(youtube_api_key)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    context = {}
    if request.method == "POST":
        context["query"] = request.form["query"]
        context["videos"] = yt.search(context["query"])
    return render_template("index.html", **context)

if __name__ == "__main__":
    app.run(port=8000, debug=True)