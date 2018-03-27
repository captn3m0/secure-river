import os
from secure_river import app

if ('PORT' in os.environ):
    port = int(os.environ['PORT'])
else:
    port = 5000

app.run(debug=True, port=port)
