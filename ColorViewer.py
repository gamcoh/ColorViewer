# coding: utf-8

import sublime
import sublime_plugin
from re import search


class ColorViewerCommand(sublime_plugin.EventListener):
	def on_hover(self, view, point, hover_zone):
		# if the mouse is on the code
		if hover_zone == sublime.HOVER_TEXT:
			region = view.find(".*", point)
			line = view.full_line(point)
			code = view.substr(sublime.Region(line.a, line.b))

			# color code
			path = search("(#[A-Za-z0-9]{6})", code)

			# if the mouse is on a color code
			if path:
				color = path.group(1)
				popup='<div style="width: 100px; height: 100px; background-color: '+color+'">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div>'
				view.show_popup(popup, flags=sublime.HIDE_ON_MOUSE_MOVE_AWAY, location=point, max_width=500, max_height=500)
				return 
















