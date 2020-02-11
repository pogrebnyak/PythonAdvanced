from flask import Flask
from flask import render_template
from flask import request
import config 

app = Flask(__name__)


@app.route('/<string:post_id>')
def show_post(post_id):
    categories_list = config.clist()
    goods_list = config.glist(post_id)
    return render_template('catgoods.html', post_id=post_id , goods_list=goods_list , categories_list=categories_list, enumerate=enumerate)

@app.route('/')
def home():
    categories_list = config.clist()
    return render_template('index.html', categories_list=categories_list)

@app.route('/addcateg', methods=['POST','GET'])
def add_categories():
    categories_message = 'Введите категорию'
    if request.method == 'POST':
        cget = request.form.get("categories_get")
        categories_message = config.categories_input(cget)
    return render_template('addcateg.html', categories_message=categories_message)


       
@app.route('/addgood', methods=['POST','GET'])
def add_good():
    categories_list = config.clist()
    if request.method == 'POST':
        cat_get = request.form.get("cat_get")
        cname = request.form.get("name_get")
        ccost = request.form.get("cost_get")
        camount = request.form.get("amount_get")
        config.good_input(cname, ccost, camount, cat_get)
    return render_template('addgood.html', categories_list=categories_list)

@app.route('/goods/<string:post_id>')
def goods(post_id):
    good_list = config.good(post_id)
    return render_template('goods.html', post_id=post_id, good_list=good_list)
	
if __name__ == '__main__':
    app.run(debug = True)
