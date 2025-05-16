from flask import Flask, render_template, request, redirect, url_for
from bypasser import *
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/bypass', methods=['POST'])
def bypass():
    url = request.form['url']
    service = identify_service(url)
    
    try:
        if service == "katdrive":
            result = katdrive_dl(url, os.getenv('KATCRYPT'))
        elif service == "hubdrive":
            result = hubdrive_dl(url, os.getenv('HCRYPT'))
        elif service == "drivefire":
            result = drivefire_dl(url, os.getenv('DCRYPT'))
        elif service == "kolop":
            result = kolop_dl(url, os.getenv('KCRYPT'))
        elif service == "mediafire":
            result = mediafire(url)
        elif service == "zippyshare":
            result = zippyshare(url)
        elif service == "filecrypt":
            result = filecrypt(url)
        elif service == "dropbox":
            result = dropbox(url)
        elif service == "shareus":
            result = shareus(url)
        elif service == "shortingly":
            result = shortlingly(url)
        elif service == "gyanilinks":
            result = gyanilinks(url)
        elif service == "anonfiles":
            result = anonfile(url)
        elif service == "pixl":
            result = pixl(url)
        elif service == "shorte":
            result = sh_st_bypass(url)
        elif service == "gofile":
            result = gofile_dl(url)
        elif service == "psa":
            result = psa_bypasser(url)
        elif service == "sharer":
            result = sharer_pw(url, os.getenv('LARAVEL_SESSION'), os.getenv('XSRF_TOKEN'))
        elif service == "gdtot":
            result = gdtot(url, os.getenv('GDTOT_CRYPT'))
        elif service == "adfly":
            result = adfly(url)['bypassed_url']
        elif service == "gplinks":
            result = gplinks(url)
        elif service == "droplink":
            result = droplink(url)
        elif service == "linkvertise":
            result = linkvertise(url)
        elif service == "ouo":
            result = ouo(url)
        elif service == "mdisk":
            result = mdisk(url)
        elif service == "rocklinks":
            result = rocklinks(url)
        elif service == "pixeldrain":
            result = pixeldrain(url)
        elif service == "wetransfer":
            result = wetransfer(url)
        elif service == "megaup":
            result = megaup(url)
        elif service in ["appdrive", "driveapp", "gdflix", "drivesharer", "drivebit", "drivelinks", "driveace", "drivepro", "drivehub"]:
            result = unified(url)
        else:
            result = others(url)
    except Exception as e:
        result = f"Error: {str(e)}"
    
    return render_template('result.html', original_url=url, result_url=result, service=service)

def identify_service(url):
    if "katdrive" in url:
        return "katdrive"
    elif "hubdrive" in url:
        return "hubdrive"
    elif "drivefire" in url:
        return "drivefire"
    elif "kolop" in url:
        return "kolop"
    elif "mediafire" in url:
        return "mediafire"
    elif "zippyshare" in url:
        return "zippyshare"
    elif "filecrypt" in url:
        return "filecrypt"
    elif "dropbox" in url:
        return "dropbox"
    elif "shareus" in url:
        return "shareus"
    elif "shortingly" in url:
        return "shortingly"
    elif "gtlinks" in url:
        return "gyanilinks"
    elif "anonfiles" in url:
        return "anonfiles"
    elif "pixl" in url:
        return "pixl"
    elif "shorte" in url:
        return "shorte"
    elif "gofile" in url:
        return "gofile"
    elif "psa" in url:
        return "psa"
    elif "sharer" in url:
        return "sharer"
    elif "gdtot" in url:
        return "gdtot"
    elif "adfly" in url:
        return "adfly"
    elif "gplinks" in url:
        return "gplinks"
    elif "droplink" in url:
        return "droplink"
    elif "linkvertise" in url:
        return "linkvertise"
    elif "ouo" in url:
        return "ouo"
    elif "mdisk" in url:
        return "mdisk"
    elif "rocklinks" in url:
        return "rocklinks"
    elif "pixeldrain" in url:
        return "pixeldrain"
    elif "wetransfer" in url:
        return "wetransfer"
    elif "megaup" in url:
        return "megaup"
    elif any(x in url for x in ["appdrive", "driveapp", "gdflix", "drivesharer", "drivebit", "drivelinks", "driveace", "drivepro", "drivehub"]):
        return "appdrive"
    else:
        return "others"

if __name__ == '__main__':
    app.run(debug=True)
