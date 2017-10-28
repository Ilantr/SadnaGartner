"""Application Config"""
import os


MQTT_HOST = os.environ.get("mqtt-host", 'm21.cloudmqtt.com')
MQTT_USER = os.environ.get("mqtt-user", 'ahffqpwk')
MQTT_PWD = os.environ.get("mqtt-pwd", 'P7tB9Ao6nFho')
MQTT_PORT = int(os.environ.get("mqtt-port", 10554))
MQTT_FB_WEBHOOK_TOPIC_NAME = 'fb-posts-updates'
WEB_PORT = int(os.environ.get("PORT", 5000))