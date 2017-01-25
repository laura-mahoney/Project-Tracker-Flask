from flask import Flask, request, render_template, redirect

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get("github")
    first, last, github = hackbright.get_student_by_github(github)
    student_projects = hackbright.get_grades_by_github(github)
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           student_projects=student_projects)
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


@app.route("/project")
def show_project_info():
    """Shows a projects information."""

    project = request.args.get("project")
    title, description, max_grade = hackbright.get_project_by_title(project)

    return render_template("project.html",
                           title=title,
                           description=description,
                           max_grade=max_grade)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
