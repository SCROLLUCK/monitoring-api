from paho.mqtt.client import Client
import os


class MQTTListener:
  client: Client
  def __init__(self):
    self.client = Client("client-id")
    self.client.on_connect = self.on_connect 
    self.client.on_disconnect = self.on_disconnect
    self.client.on_message = self.on_message
    self.client.on_subscribe = self.on_subscribe
    self.client.on_unsubscribe = self.on_unsubscribe
    self.client.on_publish = self.on_publish
    self.client.connect(os.getenv('BROKER_HOST'), os.getenv('BROKER_PORT'))
    self.client.loop_start()
    
  def on_connect(client, flags, rc, properties):
    print('Connected')
    client.subscribe('TEST/#', qos=0)

  def on_message(client, topic, payload, qos, properties):
    print('RECV MSG:', payload)


  def on_disconnect(client, packet, exc=None):
    client.loop_stop()
    print('Disconnected')


  def on_subscribe(client, mid, qos, properties):
    print('SUBSCRIBED')

