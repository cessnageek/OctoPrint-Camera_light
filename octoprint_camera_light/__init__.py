# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin
#import testCustom

class camera_lightPlugin(octoprint.plugin.StartupPlugin, octoprint.plugin.SimpleApiPlugin, octoprint.plugin.TemplatePlugin):
	#def on_after_startup(self):
		#self.__logger.info("Staring Camera Light plugin!")

	def on_api_get(self, request):
		print("In api get!!!!!!_--------------")
		f = open("testfile.txt", "a")
		f.write("clicked button\n")
		f.close()
		return "Success"

__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = camera_lightPlugin()

