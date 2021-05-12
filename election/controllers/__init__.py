from election.controllers import index, user, candidate

def register_all_blueprints(app):
    app.register_blueprint(candidate.bp)
    app.register_blueprint(index.bp)
    app.register_blueprint(user.bp)

    @app.errorhandler(404)
    def page404(e):
        return "404"