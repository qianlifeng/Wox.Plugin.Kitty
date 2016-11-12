# encoding=utf-8
import json
import os
import subprocess
import urllib.parse
from wox import Wox
from os import listdir
from os.path import isfile, join
import winreg

SESSIONS_LOCATIONS = ["file", "registry"]


class Kitty(Wox):

    def load_session(self, kitty_path, session_location='file'):
        if session_location == 'file':
            session_path = os.path.join(kitty_path, "Sessions")
            files = [urllib.parse.unquote(f) for f in listdir(session_path) if isfile(join(session_path, f))]
            return files
        else:
            sessions = []
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\9bis.com\KiTTY\Sessions')
            for i in range(0, winreg.QueryInfoKey(key)[0]):
                skey_name = winreg.EnumKey(key, i)
                sessions.append(skey_name)
            key.Close()
            return sessions

    def query(self, query):
        with open(os.path.join(os.path.dirname(__file__), "config.json"), "r") as content_file:
            config = json.loads(content_file.read())
        kitty_folder_path = os.path.expandvars(config["kittyPath"])
        kitty_path = self.find_kitty_path(kitty_folder_path)
        kitty_sessions_location = config.get("sessions_location", 'file').lower()
        if kitty_sessions_location not in SESSIONS_LOCATIONS:
            kitty_sessions_location = "file"
        sessions = self.load_session(kitty_folder_path, kitty_sessions_location)
        res = []
        for p in sessions:
            if query in p:
                res.append({"Title": p, "IcoPath": "kitty.png", "JsonRPCAction": {"method": "open_session", "parameters": [kitty_path.replace("\\","\\\\"),p]}})
        return res

    def open_session(self, kitty_path, session_name):
        subprocess.call('{} -load "{}"'.format(kitty_path, session_name))

    def find_kitty_path(self, kitty_folder_path):
        """Returns the full path to the user's kitty executable"""

        exe_names = ['kitty.exe', 'kitty_portable.exe']
        for exe_name in exe_names:
            attempted_kitty_exe = os.path.join(kitty_folder_path, exe_name)
            if isfile(attempted_kitty_exe):
                return attempted_kitty_exe

        raise Exception("Could not find Kitty executable in %s" % kitty_folder_path)

if __name__ == "__main__":
    Kitty()
