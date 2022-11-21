# Tutorial:
# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
# https://www.geeksforgeeks.org/flask-creating-first-simple-application/

from flask import Flask, jsonify, abort, make_response, request, url_for, \
                    render_template, redirect
import base64 # to decode MIME base64 encoded by canvas.toDataURI() in JavaScript
import mimetypes

from textdetect import textdetect as td


app = Flask(__name__,template_folder='.')


@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template("index.html")
    return render_template("/app/templates/index.html")


@app.route('/canvas', methods = ['POST'])
def save_image():
    
    image_data = request.form['image']
    image_data_str = image_data.split(',')[1]    
    image_data_decode = base64.b64decode(image_data_str)

    text_list,codes_dict = td.text_detect(image_data_decode)

    # retry until it gets 2 keys, each containing 2 items
    # TODO tune 2 to be the number of codes expected
    if len(codes_dict.keys()) != 2:
        print("not that time",codes_dict)
        return save_image()

    print(" === Finish text_detect ===")
    print(text_list)

    text_list2 = [{'text': t['text'], 'conf': str(t['conf'])} for t in text_list]

    return jsonify(text_list2)

@app.route('/data/<item_id>', methods = ['GET'])
def show_data(item_id):
    data = find_item()
    return render_template('data.html', item_id=item_id, data=data)


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
