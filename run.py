from Backend import create_app
import os

app = create_app()


if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT', 8080)))
