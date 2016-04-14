from flask import render_template


def add_routes(app):

    @app.route('/<tracking_id>')
    def tracking_page(tracking_id):
        return render_template('tracking_id.html', tracking_id=tracking_id)
