import sublime, sublime_plugin
import webbrowser

class OpenBrowserCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        url = self.view.file_name()
        webbrowser.open_new(url)