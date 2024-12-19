
import os
from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('src/index.html')

    @app.route("/sozluk")
    def sozluk():
        dictionary = {"elma": "apple", "armut": "pear", "muz": "banana" "üzüm":"grape","portakal":"orange","mango":"mango","ananas":"pineapple","avakado":"avacado","çilek":"strawberry"}
        return render_template("sozluk.html", data=dictionary)

    def main():
        app.run(port=int(os.environ.get('PORT', 80)))

    if __name__ == "__main__":
        main()