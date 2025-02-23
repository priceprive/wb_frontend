from website import create_app


app= create_app()

#adding a temp comment to push
if __name__ == '__main__':
    # app.run(port=8080)
    app.run(debug=True)
