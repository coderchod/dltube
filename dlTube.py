from flask import Flask, render_template, request
import pafy.pafy

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def tube():
	if request.method == 'POST':
		url = request.form['track']
		v = pafy.new(url)
		s = v.streams
		audio = v.audiostreams
		s_urls = [i.url for i in s]
		return render_template('output.html', data={'streams':s,'urls':s_urls, 'a_streams': audio})
	else:
		return render_template('home.html')
		
if __name__ == '__main__':
	app.debug = True
	app.run()
