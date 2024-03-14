from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'
# @app.route('/get_stream_url', methods=['GET'])
# def get_stream_url():
# 	channel_url = request.args.get('channel')
# 	if not channel_url:
# 		return jsonify({'error': 'Параметр channel отсутствует'}), 400

# 	try:
# 		streams = streamlink.streams(channel_url)
# 	except Exception as e:
# 		return jsonify({'error': 'Ошибка при получении потока: {}'.format(str(e))}), 500

# 	if streams:
# 		# Выбираем лучшее качество потока
# 		best_quality = streams['best']
# 		return jsonify({'stream_url': best_quality.url})
# 	else:
# 		return jsonify({'error': 'Stream не найден.'}), 404

# if __name__ == '__main__':
# 	app.run(debug=True)