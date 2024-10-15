from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

cellar = {
    "cigars": [],
    "wines": [],
    "spirits": []
}

@app.route('/')
def index():
    return render_template('index.html', cellar=cellar)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        category = request.form['category']
        name = request.form['name']
        quantity = request.form['quantity']
        description = request.form['description']

        item = {
            'name': name,
            'quantity': quantity,
            'description': description
        }

        if category in cellar:
            cellar[category].append(item)

        return redirect(url_for('index'))
    return render_template('add_item.html')

if __name__ == '__main__':
    app.run(debug=True)
