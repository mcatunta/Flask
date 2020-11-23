from flask import Flask, jsonify

from api.exceptions import ApplicationException, AuthorizeException

def register_error_handler(app: Flask):

    @app.errorhandler(Exception)
    def handle_exception_error(e):
        print(e)
        return jsonify({'msg': 'Internal server error'}), 500

    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify({'msg': 'Method not allowed'}), 405

    @app.errorhandler(403)
    def handle_403_error(e):
        return jsonify({'msg': 'Forbidden error'}), 403

    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({'msg': 'Not Found error'}), 404
    
    @app.errorhandler(AuthorizeException)
    def handle_authorize_exception(e):
        return jsonify({'msg': str(e)}), 401

    @app.errorhandler(ApplicationException)
    def handle_application_exception(e):
        return jsonify({'msg': str(e)}), 400 