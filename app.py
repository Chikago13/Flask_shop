from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from cloudipsp import Api, Checkout


app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    isActive = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return self.title

@app.route('/money/<int:id>')
def item_money(id):
    item = Item.query.get(id)
    api = Api(merchant_id=1396424,
              secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "RUB",
        "amount": str(item.price)
    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)


@app.route('/')
def index():
    items = Item.query.order_by(Item.price).all()
    return render_template('index.html', data= items)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method =='POST':
        title = request.form['title']
        price = request.form['price']
        description = request.form['description']

        item = Item(title=title, price=price, description=description)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return "Произошла ошибка"
    else:
        return render_template('create.html')

@app.route('/task')
def task():
    return render_template('task.html')

@app.route('/test')
def test():
    return render_template('test.html')


if __name__ =='__main__':
    app.run(debug=True)