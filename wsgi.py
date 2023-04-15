import sys

project_home = '/home/satriobio/lapbul-generator'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from flask_app import app as application 
application.run(host='0.0.0.0', port=5000, debug=True)