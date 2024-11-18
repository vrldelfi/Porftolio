from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/proyectos')
def proyectos():
    images = ['static/assets/revista-pag-uno', 'static/assets/revista-dos-pag.jpg', 'static/assets/revista-frank.jpg']
    return render_template('proyectos.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
