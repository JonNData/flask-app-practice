# app folder, needed import to create_app
from app import create_app

app = create_app()

if __name__ == "__main__":
    # run this app
    app.run()