# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin
import RPi.GPIO as GPIO
GPIO.setup(18, GPIO.OUT)
#import testCustom

class camera_lightPlugin(octoprint.plugin.StartupPlugin, octoprint.plugin.SimpleApiPlugin, octoprint.plugin.TemplatePlugin):
	#def on_after_startup(self):
		#self.__logger.info("Staring Camera Light plugin!")

	def on_api_get(self, request):
		print("In api get!!!!!!_--------------")
		#f = open("testfile.txt", "a")
		#f.write("clicked button\n")
		#f.close()
		if GPIO.input(18):
			GPIO.output(18, GPIO.LOW)
		else:
			GPIO.output(18, GPIO.HIGH)
		return "Success"

__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = camera_lightPlugin()

