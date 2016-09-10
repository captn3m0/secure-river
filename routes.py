from app import app

@app.route('/jobs', methods=['GET'])
def fetch_jobs():
    print(g.networks)
    return models.job.find_by_network(network).json()

@app.route('/jobs/<id>', methods=['GET'])
def fetch_job_details(id):
    return models.job.find_by_id(id).json()

@app.route('/network/<id>', methods=['GET'])
def fetch_network_reports(id):
    return models.network.find_by_id(id).reports().json()

@app.route('/jobs/<id>/submit', methods=['POST'])
def submit_job_response(id):
    job = models.job.find(id)

@app.route('/clients', methods=['POST'])
def create_client():
    job = models.client.register()

@app.route('/')
def hello_world():
    return 'Hello, World!'
