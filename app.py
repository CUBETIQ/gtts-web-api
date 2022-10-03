from os import environ
from flask import Flask, request, Response
from gtts import gTTS
from io import BytesIO

app = Flask(__name__)


@app.route('/')
def index():
    text = request.args.get('text')
    lang = request.args.get('lang') or 'km'

    if not text:
        return Response('No text specified', status=400)

    tts = gTTS(text=text, lang=lang)
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)

    return Response(mp3_fp.getvalue(), mimetype='audio/mpeg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=environ.get('PORT', 5000))
