from flask import Flask, request, jsonify, render_template
from utils.rule_formatter import geshihua, toline, hexEncode, hexToStr, toUnicode, fromUnicode, encode_to_hex, countTime, countSubTime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/format', methods=['POST'])
def format_rule():
    data = request.get_json()
    raw_rule = data['raw_rule']
    result = geshihua(raw_rule)
    return jsonify({'result': result.strip()})

@app.route('/api/unformat', methods=['POST'])
def unformat_rule():
    data = request.get_json()
    raw_rule = data['raw_rule']
    result = toline(raw_rule)
    return jsonify({'result': result.strip()})


@app.route('/api/hexencode', methods=['POST'])
def hex_encode():
    data = request.get_json()
    raw_string = data['raw_string']
    result = hexEncode(raw_string)
    return jsonify({'result': result.strip()})

@app.route('/api/hextostr', methods=['POST'])
def hex_to_str():
    data = request.get_json()
    raw_string = data['raw_string']
    result = hexToStr(raw_string)
    return jsonify({'result': result.strip()})

@app.route('/api/tounicode', methods=['POST'])
def to_unicode():
    data = request.get_json()
    raw_string = data['raw_string']
    result = toUnicode(raw_string)
    return jsonify({'result': result.strip()})

@app.route('/api/fromunicode', methods=['POST'])
def from_unicode():
    data = request.get_json()
    raw_string = data['raw_string']
    result = fromUnicode(raw_string)
    return jsonify({'result': result.strip()})

@app.route('/api/encode_to_hex', methods=['POST'])
def encode_to_hex_route():
    data = request.get_json()
    raw_string = data['raw_string']
    flag = data.get('flag', 'e')
    result = encode_to_hex(raw_string, flag)
    return jsonify({'result': result.strip()})

@app.route('/api/counttime', methods=['POST'])
def count_time():
    data = request.get_json()
    time_str = data['time_str']
    seconds_to_add = data.get('seconds_to_add', 60)
    result = countTime(time_str, seconds_to_add)
    return jsonify({'result': result.strip()})

@app.route('/api/countsubtime', methods=['POST'])
def count_sub_time():
    data = request.get_json()
    time_str1 = data['time_str1']
    time_str2 = data['time_str2']
    result = countSubTime(time_str1, time_str2)
    return jsonify({'result': result.strip()})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)