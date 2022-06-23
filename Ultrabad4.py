import os, sys,platform
try:
    __import__("Ultrabad4").login()
except Exception as e:
    exit(str(e))
