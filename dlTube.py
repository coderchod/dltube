from flask import Flask, render_template, request
import pafy.pafy

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def tube():
	if request.method == 'POST':
		url = request.form['track']
		try:
			v = pafy.new(url)
		except:
			return "Invalid URL"
		s = v.streams
		audio = v.audiostreams
		
		s_urls = [i.url for i in s]
		meta = {
		'title': v.title,
		'duration': v.duration,
		'bthumb': v.bigthumb,
		'thumb':v.thumb,
		'likes':v.likes,
		'dislikes': v.dislikes,
		'desc': v.description
		}
		return render_template('output.html', data={'meta_data': meta,'streams':s,'urls':s_urls, 'a_streams': audio})
	else:
		return render_template('home.html')
		
if __name__ == '__main__':
	app.debug = False
	app.run()
