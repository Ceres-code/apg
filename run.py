from app import create_app

app = create_app()

if __name__ == '__main__':
    # Enable debug mode if running in a development environment
    app.run(debug=True)