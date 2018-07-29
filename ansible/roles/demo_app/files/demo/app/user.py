import datetime
import logging

import connexion
from connexion import NoContent

import orm

db_session = None

def getUserByName(username):
    user = db_session.query(orm.User).filter(orm.User.id == username).one_or_none()
    return user.dump() if user is not None else ('Not found', 404)

logging.basicConfig(level=logging.INFO)
db_session = orm.init_db(os.environ['DATABASE_URI'])
app = connexion.FlaskApp(__name__)
app.add_api('swagger.yaml')

application = app.app


@application.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(debug=True)
