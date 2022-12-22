from flask import Flask, render_template, request
from student import student_info_to_file, load_student_info, student_dict_to_string
app = Flask(__name__)


@app.route("/")
def hello_index():
    return render_template('index.html')


@app.route("/student")
def capture_student_info():
    return render_template('capture_student_info.html')

@app.route("/capture", methods=['POST'])
def capture():
    name = request.form['name']
    dob = request.form['dob']
    marks_physics = request.form['marks_physics']
    marks_chemistry = request.form['marks_chemistry']
    marks_maths = request.form['marks_maths']
    student_info_to_file(name, dob, marks_physics, marks_chemistry, marks_maths)
    return render_template("cap_student_confirm.html", inp_name=name, inp_dob=dob)

# @app.route("/select", methods=['POST'])
# def select():
#     selection = request.form['selection']
#     if selection == 'display':
#         return display_info()
#     elif selection == 'capture':
#         return capture_student_info()

@app.route("/display")
def display_info():
    students = load_student_info()
    html_string = "<p>Name | DOB | Physics | Chemistry | Maths<br>"
    for s in students:
        html_string = html_string+student_dict_to_string(s)+"<br>"
    html_string = html_string+"</p>"
    print(html_string)
    return html_string

if __name__ == "__main__":
    app.run()