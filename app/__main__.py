from . import app, db
from . import models


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)