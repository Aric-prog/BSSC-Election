from election.controllers import index, user, candidate, testing

def register_all_blueprints(app):
    app.register_blueprint(candidate.bp)
    app.register_blueprint(index.bp)
    app.register_blueprint(user.bp)
    # app.register_blueprint(testing.bp)

    @app.errorhandler(404)  
    def page404(e):
        return "404"