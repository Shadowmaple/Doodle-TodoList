from .. import app


@app.route('/user/<int:id>/', methods = ['GET'])
def get_user_info(id):
    pass

@app.route('/user/<int:id>/', methods = ['PUT'])
def update_user_info(id):
    pass
