from .. import app


@app.route('/list/', methods=['GET'])
def get_list():
    """
    获取列表，未完成/已完成
    """
    pass


@app.route('/list/', methods=['POST'])
def create_list():
    pass


@app.route('/list/<int:id>/', methods=['GET'])
def get_info(id):
    pass


@app.route('/list/<int:id>/', methods=['PUT'])
def update_list(id):
    pass


@app.route('/list/<int:id>/', methods=['DELETE'])
def delete_list(id):
    pass
