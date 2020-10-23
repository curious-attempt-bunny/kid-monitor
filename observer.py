from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/image', methods=['post'])
def image():
  uploaded_file = request.files['image']
  if uploaded_file.filename != '':
    uploaded_file.save('{}/{}'.format('static/images', uploaded_file.filename))

  return 'got {}'.format(uploaded_file.filename)

@app.route('/')
def index():
  images = os.listdir('static/images')
  images.sort()
  return render_template('index.html', images=images[-100:])