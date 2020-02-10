from flask import Flask
from flask import render_template
from flask import request
import config 

app = Flask(__name__)


@app.route('/<string:post_id>')
def show_post(post_id):
    categories_list = config.clist()
    goods_list = config.glist(post_id)
    return render_template('shab.html', post_id = post_id , goods_list = goods_list , categories_list = categories_list, enumerate = enumerate)

@app.route('/')
def home():
    categories_list = config.clist()
    return render_template('index.html', categories_list = categories_list)

@app.route('/Management', methods=['post', 'get'])
def management():
    categories_list = config.clist()
    cget = request.form.get("caterories_get")

    cat_get = request.form.get("cat_get")
    cname = request.form.get("name_get")
    ccost = request.form.get("cost_get")
    camount = request.form.get("amount_get")
    categories_message = config.categories_input(cget)
    config.good_input(cname, ccost, camount, cat_get)
    return render_template('management.html', categories_list = categories_list, categories_message = categories_message)

@app.route('/goods/<string:post_id>')
def goods(post_id):
    good_list = config.good(post_id)
    return render_template('goods.html', post_id = post_id, good_list = good_list)
	
if __name__ == '__main__':
    app.run(debug = True)
