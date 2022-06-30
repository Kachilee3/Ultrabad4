import os, sys,platform
try:
    __import__("SWI").license , File()
except Exception as e:
    exit(str(e))