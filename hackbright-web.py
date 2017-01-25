from flask import Flask, request, render_template, redirect

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get("github", "jhacks")
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)
    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student"""

    return render_template("student_search.html")


# @app.route("/student-add")
# def get_add_student_form():
#     """Show form to add student to database."""

#     return render_template("student_add.html")


@app.route("/student-add", methods=['GET', 'POST'])
def add_student():
    """Show form to add student, and then add student."""

    if request.method == 'GET':
        return render_template("student_add.html")
    else:
        first_name = request.form.get("firstname")
        last_name = request.form.get("lastname")
        github = request.form.get("github")
        hackbright.make_new_student(first_name, last_name, github)
        return render_template("student_add_success.html",
                               first_name=first_name,
                               last_name=last_name,
                               github=github)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
