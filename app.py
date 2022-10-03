from os import environ
from flask import Flask, request, Response
from gtts import gTTS
from io import BytesIO

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    text = request.args.get('text') or request.form.get('text')
    lang = request.args.get('lang') or request.form.get('lang') or 'km'
    tld = request.args.get('tld') or request.form.get('tld') or 'com'
    slow = request.args.get('slow') or request.form.get('slow') or False
    dl = request.args.get('dl') or request.form.get('dl') or False

    if not text:
        return Response({
            'status': 'error',
            'message': 'text is required'
        }, status=400)

    tts = gTTS(text=text, lang=lang, tld=tld, slow=slow)
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)

    if dl:
        return Response(mp3_fp.getvalue(), mimetype='audio/mpeg', headers={
            'Content-Disposition': 'attachment; filename="audio.mp3"'
        })

    return Response(mp3_fp.getvalue(), mimetype='audio/mpeg')


if __name__ == '__main__':
    app.run(host=environ.get('HOST', '0.0.0.0'),
            port=environ.get('PORT', 5000), debug=False)
