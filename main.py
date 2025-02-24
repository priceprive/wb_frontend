from website import create_app


app= create_app()
#Adding comment
if __name__ == '__main__':
    # app.run(port=8080)
    app.run(debug=True)
