"""Flask app for generating memes."""

import random
import os
import shutil
import requests
from flask import Flask, render_template, abort, request

from MemeGenerator import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # quote_files variable
    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    # images within the images images_path directory
    images = []
    for root, dirs, files in os.walk(images_path):
        images = [os.path.join(root, name) for name in files]

    return quotes, images


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # download image
    image_url = request.form['image_url']
    file_extension = image_url.split('.')[-1]
    if file_extension not in meme.allowed_extensions:
        abort(400, f'Wrong file type. Allowed file types: {", ".join(meme.allowed_extensions)}.')
    tmp_file = os.path.join('./tmp', f'base_img_{random.randint(0, 10000)}.{file_extension}')
    r = requests.get(image_url, stream=True)
    if r.status_code == 200:
        with open(tmp_file, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    else:
        abort(400, f'Unable to download file from {image_url}.')

    # generate meme
    body = request.form['body']
    author = request.form['author']
    path = meme.make_meme(tmp_file, body, author)
    os.remove(tmp_file)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
