# -*- coding: utf-8 -*-
import sublime, sublime_plugin
import webbrowser
import urllib

class SearchInGoogleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        googleURL = u"http://www.google.com.hk/search?ie=UTF-8&q={0}"
        for region in self.view.sel():
            if not region.empty():
                word = self.view.substr(region)
                quoted = urllib.quote(word.encode('utf-8'))
                url = googleURL.format(quoted)
                webbrowser.open_new(url)