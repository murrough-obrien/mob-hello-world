# -------------------------------------------
# |  Murrough O'Brien, application support  |
# |   Cloud Foundary/Pivotal demonstrator   |
# |        Version 1.00, April 2016         |
# |                                         |
# -------------------------------------------

# start the main routine, import the sys module

import json

import os
reload(os)
# Library routines, flask seemed the easiest of the CF and python web builders
from flask import Flask

#default settings
app = Flask(__name__)
port = int(os.getenv("PORT", 9099))
@app.route('/')

# start of claseses
def hello_world():
	"""short little hellow world one-liner"""
	return 'Murrough says Hello World, I am running on port ' + str(port)

# start of program, call the main routine, then exit
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=port)




