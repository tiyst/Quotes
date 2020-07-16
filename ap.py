import random
from flask import ( Flask, jsonify, render_template, request )

app = Flask(__name__, template_folder="templates", static_url_path="/static")

@app.route('/clear')
def first():
	return render_template('clear.html')

@app.route('/')
def home():
	entry = random.choice(read_quotes_file())
	return render_template('home.html', author=entry['author'], quote=entry['quote'])

@app.route('/quote')
def get_quote():
	return jsonify(random.choice(read_quotes_file()))

@app.route('/quotes', methods=['GET'])
def get_all_quote():
	return jsonify(read_quotes_file())

@app.route('/add', methods=['POST'])
def add_quote():
	f = open("static/resources/proposed.txt", "a+")
	author = request.form.get("author")
	quote = request.form.get("quote")
	f.write("\n{}|{}".format(author,quote))
	f.close()
	return jsonify(success=True)



def read_quotes_file():
	qs = []
	with app.open_resource("static/resources/quotes.txt") as q:
		lines = q.readlines()

	for line in lines:
		q = line.decode().split("|")
		qs.append({
		'author':q[0],
		'quote':q[1].rstrip() #rstrip() removes trailing \n
		})
	return qs

### Error handlers
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

# @app.errorhandler(405)  #This crashes flask
# def method_not_allowed(e)
# 	return render_template('405.html'), 405


### launch
if __name__ == "__main__":
	app.run()