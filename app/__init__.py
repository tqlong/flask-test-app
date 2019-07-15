from flask import Flask, render_template, Response
import time

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/message")
def message_stream():
    def event_stream():
        count = 0
        while count < 10:
            count += 1
            time.sleep(2)
            yield "data: pending #{}\n\n".format(count)
        yield "data: END-OF-STREAM\n\n"

    return Response(event_stream(), mimetype="text/event-stream")
