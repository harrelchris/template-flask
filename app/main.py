from flask import Flask, render_template, request


def create_app(settings="app.settings"):
    app = Flask(__name__)
    app.config.from_object(settings)
    register_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)
    register_commands(app)
    return app


def register_extensions(app: Flask):
    from app.admin import admin
    from app.login import login_manager

    admin.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app: Flask):
    from app.public.urls import bp as public
    from app.user.urls import bp as user

    app.register_blueprint(public)
    app.register_blueprint(user)


def register_error_handlers(app: Flask):
    """Server error.html with specific context for 401, 404, and 500 errors"""

    def handler(error):
        """Log error and server error.html"""

        app.logger.error(
            f"{request.remote_addr} {request.method} {request.full_path} {error.code}",
        )
        return render_template("error.html", error=error), error.code

    for code in [401, 404, 500]:
        app.register_error_handler(code, handler)


def register_commands(app):
    from app.user.commands import user

    app.cli.add_command(user)
