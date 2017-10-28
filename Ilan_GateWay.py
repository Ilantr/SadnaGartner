from flask import Flask
from flask import json
from flask import Response
from flask import request
import os
import logging
import settings as Config
from mqtt import MqttClient
from msg import Msg

"""Server class"""
class Server(object):
    app = Flask(__name__)
    MQTTC = MqttClient()

    """webhook api"""
    @app.route("/webhook", methods=['GET'])
    def verify():
    	return request.args.get('hub.challenge')

    @app.route("/webhook", methods=['POST'])
    def fb_feeds_webhook():
	    """webhook api"""
	    logging.debug('Handling webhook request!!')
	    content = request.get_json()
	    if content['entry'][0]['changes'][0]['value']['item'] == 'like':
		    Server.MQTTC.publish(
		    	Config.MQTT_FB_WEBHOOK_TOPIC_NAME, Msg(
				    int(content['entry'][0]['time']),'LIKE',
				    content['entry'][0]['changes'][0]['value']['user_id']))

	    logging.info('Handled webhook request ' + str(content))
	    return ''

    if __name__ == '__main__':
	    app.debug = True
	    app.run(host = '0.0.0.0', port = int(os.environ.get("PORT", 5000)))