
import os
from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('src/index.html')

    @app.route("/sozluk")
    def sozluk():
       dictionary = {"ADANA": "01", "ANKARA": "06", "SİVAS": "58","İSTANBUL":"34","ANTALYA":"07","BURSA":"16","ORDU":"52","İZMİR":"35","MARDİN":"47"}
        return render_template("sozluk.html", data=dictionary)

    def main():
        app.run(port=int(os.environ.get('PORT', 80)))

    if __name__ == "__main__":
        main()
