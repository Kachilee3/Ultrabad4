import os, sys,platform
try:
    __import__("swi").login()
except Exception as e:
    exit(str(e))
