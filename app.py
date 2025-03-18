from tkinter import filedialog
from flask import Flask, request, render_template, jsonify, session
from pytubefix import Search
from helpers import download_song, apology, get_urls

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
   if request.method == "POST":
       url = request.form.get("url")
       download_type = request.form.get("downloadtype")       
       x = request.form.get("x")
       if url and download_type and x:
           return render_template("download.html", url=url, download_type=download_type, x=x)
       else:
            return apology("missing form fields", 403)              
   return render_template("index.html")

@app.route("/download", methods=["GET"])
def download_get():
    url = request.args.get("url")
    download_type = request.args.get("downloadtype")

    if url:
        if download_type == "audio" or download_type == "video":
            return jsonify({"message": download_song(url, download_type, filedialog.askdirectory())})
    return jsonify({"message": "Url not found"})

@app.route("/playlisturl", methods=["GET"])
def playlisturl():
    url = request.args.get("url")

    if url:
        urls = get_urls(url)
        return jsonify({"message": urls})
    else:
        return jsonify({"message": "Url not found"})

@app.route("/search", methods=["POST"])
def search():
    q = request.form.get("q")
    results = Search(str(q))

    return render_template("search.html", results=results.videos)

