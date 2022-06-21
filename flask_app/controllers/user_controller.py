from flask_app import app
# Models imported to call their resepective class methods
from flask import redirect, render_template, request
from flask_app.models.user_model import User

# ++++++++ FORM ROUTES ++++++++++


@app.route('/')
@app.route('/user_form')
def show_user_form():

    return render_template("create_user.html")


@app.route('/user_form/submit', methods=['POST'])
def submit_user_form():
    data = {
        'user_first_name': request.form['user_first_name'],
        'user_last_name': request.form['user_last_name'],
        'user_email': request.form['user_email']
    }

    User.create_one_user(data)
    return redirect('/all_users')

# +++++++DISPLAY ROUTES ++++++


@ app.route('/all_users')
def display_all_users():

    all_users = User.get_all_users()

    return render_template('all_users.html', all_users=all_users)


@ app.route("/user/<int:user_id>")
def display_one_user(user_id):
    data = {
        "id": id
    }
    user = User.get_one_user(data)
    return render_template('user.html')


# +++++++EDIT ROUTES ++++++

# Choose differernt naming for routes/classes/constructors

@app.route("/show_user/<int:user_id>")
def view_user(user_id):

    data = {
        "user_id": user_id
    }

    show_user = User.get_one_user(data)
    return render_template('show_user.html', show_user=show_user)


@app.route("/edit_user/<int:user_id>")
def show_edit_one_user(user_id):

    data = {
        "user_id": user_id
    }

    show_user = User.get_one_user(data)
    return render_template("edit_user.html", one_user=show_user)


@app.route("/user_form/submit/<int:user_id>", methods=['POST'])
def edit_one_user(user_id):

    data = {
        'first_name': request.form['user_first_name'],
        'last_name': request.form['user_last_name'],
        'email': request.form['user_email'],
        'user_id': user_id
    }

    User.edit_one_user(data)
    return redirect('/all_users')


# +++++++DELETE ROUTES ++++++

@app.route('/delete_user/<int:user_id>')
def delete_one_user(user_id):

    data = {
        'user_id': user_id
    }
    User.delete_one_user(data)
    return redirect('/all_users')
