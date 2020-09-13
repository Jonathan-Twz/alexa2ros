#!/usr/bin/python

from flask import Flask
from flask_ask import Ask, statement, question, session

import rospy
import threading

from std_msgs.msg import Bool, String

"""
This node uses flask-ask server to listen on http server for a connection from Amazon Alexa Skill
ASK is named 
"""

app = Flask(__name__)
ask = Ask(app, '/')


@ask.launch
def launch():
	return question('mini cheetah voice control launching, whats your command')

@ask.intent('AMAZON.CancelIntent')
def cancel_intent():
	pass

@ask.intent('AMAZON.HelpIntent')
def help_intent():
	pass

@ask.intent('Go')
def go_intent():
	rospy.loginfo("go intent recived")
	util.amsg = 'go'
	util.pub.publish(util.amsg)
	return statement("mini cheetah start to move")

@ask.intent('Stop')
def stop_intent():
	rospy.loginfo("stop intent recived")
	util.amsg = 'stop'
	util.pub.publish(util.amsg)
	return statement("mini cheetah is stopping")

class Utils():
	"""docstring for Utils"""
	def __init__(self):
		rospy.init_node('alexa_listener')
		self.pub = rospy.Publisher('alexa_listener_commands', String, queue_size=1)
		rospy.loginfo("alexa_listener is running....")
		self.amsg = String()


def main():
	global util 

	util = Utils()
	alexa_thread = threading.Thread(target = app.run)
	alexa_thread.daemon = True
	rospy.loginfo("alexa_thread is running...........")
	alexa_thread.start()

	rospy.spin()


if __name__ == '__main__':
	main()
