from flask import Flask, render_template, request, redirect, url_for
import yt_dlp


app = Flask(__name__)

def get_video_info(url):
    ydl_opts = {"quiet": True, "extract_flat": False, "noplaylist": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return info

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preview', methods=['POST'])
def preview():
    url = request.form.get('url')
    if not url:
        return redirect(url_for('index'))
    
    try:
        info = get_video_info(url)
        video_url = info['url']
        thumbnail = info['thumbnail']
        title = info['title']       
        
        return render_template('preview.html', video_url=video_url, thumbnail=thumbnail, title=title)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
