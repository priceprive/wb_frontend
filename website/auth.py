from flask import Blueprint ,render_template,flash,request, redirect, url_for
from .models import db, User
# import openpyxl
import os


auth = Blueprint('auth',__name__)

# Path to the Excel file
# EXCEL_FILE = 'data.xlsx'


# Ensure Excel file exists with headers
# if not os.path.exists(EXCEL_FILE):
#     workbook = openpyxl.Workbook()
#     sheet = workbook.active
#     sheet.title = 'UserDetails'
#     sheet.append(['Email', 'Phone'])  
#     workbook.save(EXCEL_FILE)


@auth.route('/company',methods=['GET','POST'])
def company():
    if request.method == 'POST':
        email = request.form.get('email')
        phone = request.form.get('phone')
        
        if len(phone)<10:
            flash('Phone no must be atleast 10 digit')
        else:
            # Store the submitted data in the database
            new_user = User(email=email, phone=phone)
            db.session.add(new_user)
            db.session.commit()
            flash('Successfully submitted')

             # Append data to the Excel file
            # workbook = openpyxl.load_workbook(EXCEL_FILE)
            # sheet = workbook.active
            # sheet.append([email, phone])  
            # workbook.save(EXCEL_FILE)

            return redirect(url_for('auth.success'))
    return render_template('company.html')


@auth.route('/success')
def success():
    return "<h1>Submission Successful!</h1>"

# @auth.route('/')
# def index():
#     users = User.query.all()
#     users_data = [{'id': user.id,'email': user.email, 'phone': user.
#     phone} for user in users]
#     print(users_data)
#     return render_template("index.html", users=users)


@auth.route('/')
def home():
    return render_template('home.html')


@auth.route('/pricing')
def pricing():
    return render_template('pricing.html')

@auth.route('/product')
def product():
    return render_template('Products.html')



# if __name__ == '__main__':
#     app.run(debug=True)



