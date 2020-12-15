from app import create_app, db
from app.model.plates import Plate

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'app': app, 'db': db, 'Plate': Plate}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
