import quotes
import random
from flask import ( Flask, jsonify, render_template )

app = Flask(__name__, template_folder="templates", static_url_path="/static")
qs = []

@app.route('/clear')
def first():
	return render_template('clear.html')

@app.route('/')
def home():
	entry = random.choice(qs)
	return render_template('home.html', author=entry['author'], quote=entry['quote'])

@app.route('/quote')
def get_quote():
	return jsonify(random.choice(qs))

@app.route('/quotes', methods=['GET'])
def get_all_quote():
	return jsonify(qs)

@app.route('/add', methods=['POST'])
def add_quote(author, quote):
	f = open("propsed.txt", "a+")
	f.write("\n{}|{}".format(author,quote))
	f.close()




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
	with open("quotes.txt", encoding="utf8") as q:
		lines = q.readlines()

	for line in lines:
		q = line.split("|")
		qs.append({
		'author':q[0],
		'quote':q[1].rstrip() #rstrip() removes trailing \n
		})
		
	app.run(debug=True)