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


@auth.route('/contact',methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # if len(phone)<10:
        #     flash('Phone no must be atleast 10 digit')
        # else:
            
        #     new_user = User(email=email, phone=phone)
        #     db.session.add(new_user)
        #     db.session.commit()
        #     flash('Successfully submitted')

             

        #     return redirect(url_for('auth.success'))
    return render_template('contact.html')


@auth.route('/success')
def success():
    return "<h1>Submission Successful!</h1>"



@auth.route('/')
def competitor():
    return render_template('competitor.html')


@auth.route('/pricing')
def pricing():
    return render_template('pricing.html')

@auth.route('/report')
def report():
    return render_template('report.html')

@auth.route('/services')
def services():
    return render_template('services.html')


# if __name__ == '__main__':
#     app.run(debug=True)



