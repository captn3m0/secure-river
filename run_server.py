from secure_river import app
app.run(debug=True)

import sys
from os.path import dirname, abspath
sys.path.append(abspath(dirname(__file__)))
