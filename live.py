import flask

app = flask.Flask(__name__)


@app.route("/")
def pageRoot():
    return flask.redirect("/index.html")


@app.route("/<path:page>")
def pageAny(page):
    return flask.send_file("dist/" + page)


app.run(host="0.0.0.0", port=8080)
