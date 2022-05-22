from flask import Flask, Blueprint, render_template, url_for, redirect, request, flash
from .operations import todos
from .forms import CallPoliciesForm, HuntGroupForm, NoAnswerForm, BusinessConForm
from .api_requests import get_agents, get_single_agent, post_hunt_groups
from . import db
from flask_login import login_required, current_user
from .form_parser import hunt_group_form_parser
main = Blueprint('main', __name__)


@main.route('/', methods = ['GET'])
@login_required
def homepage():
    return render_template("base.html")

@main.route('/hunt_groups', methods = ['GET'])
@login_required
def hunt_groups():
    hunt_groups = todos.all()["Calling Huntgroups"]
    form = HuntGroupForm()
    return render_template("hunt_group_list.html",  hunt_groups = hunt_groups, form=form)

@main.route('/modify_hunt_group/<hunt_group_name>', methods = ['GET'])
@login_required
def display_hunt_group(hunt_group_name):
    hunt_group = todos.get(hunt_group_name)
    form = HuntGroupForm(data=hunt_group)
    form2 = CallPoliciesForm(data=hunt_group['callPolicies'])
    form3a = NoAnswerForm(data=hunt_group['callPolicies']['noAnswer'])
    form3b = BusinessConForm(data=hunt_group['callPolicies']['businessContinuity'])

    agents_associated_ids = hunt_group['agents']
    agents_associated = [(get_single_agent(agent['id'])['id'],get_single_agent(agent['id'])['emails'][0])  for agent in agents_associated_ids]
    agents_to_add_placeholder = [(agent['id'], agent['emails'][0]) for agent in get_agents()['items']]
    agents_to_add = [agent for agent in agents_to_add_placeholder if agent not in agents_associated]

    return render_template("hunt_group_modification.html", form=form, form2=form2, form3a=form3a, form3b=form3b, hunt_group=hunt_group, agents_associated=agents_associated, agents_to_add=agents_to_add)

@main.route('/modify_hunt_group/<hunt_group_name>', methods = ['POST'])
@login_required
def modify_hunt_group(hunt_group_name):
    form = HuntGroupForm()
    form2 = CallPoliciesForm()
    form3a = NoAnswerForm()
    form3b = BusinessConForm()
    print(f'========{form3a.data}')
    print(f'>>>>>>>>{form3b.data}')
    print(f'$$$$$$$$$${form3a.destination.data}')
    print(f'**********{form3b.destination.data}')
    print(request.form.getlist('destiantion'))
    print(request.form.keys())

     
    hunt_group_json_ready = hunt_group_form_parser(form=form, form2=form2, form3a=form3a, form3b=form3b)

    for hg in todos.all()["Calling Huntgroups"]:
        if form.data['name'] ==  hunt_group_name:
            todos.update(hunt_group_name, hunt_group_json_ready)
            return redirect(url_for("main.hunt_groups"))

        elif form.data['name']== hg['name']:
            flash('There is already a hg with this name')
            return redirect(url_for('main.modify_hunt_group', hunt_group_name=hunt_group_name))

    todos.update(hunt_group_name, hunt_group_json_ready)
    return redirect(url_for("main.hunt_groups"))
   

@main.route('/add', methods = ['GET','POST'])
@login_required
def add_hunt_group():
    form = HuntGroupForm()

    if request.method == 'POST':

        for hg in todos.all()["Calling Huntgroups"]:
            if  hg['name'] == form.data['name']:
                flash('There is already a hg with this name')
                return redirect(url_for("main.hunt_groups"))
        todos.create(form.data)
        return redirect(url_for("main.hunt_groups"))
    return render_template("hunt_group_add.html", form=form)

@main.route('/create', methods = ['POST'])
@login_required
def provision_hunt_group():
    post_hunt_groups(todos)
    return redirect(url_for("hunt_groups"))











# error handlers example that we will rely on

""" @app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)

@app.route("/api/v1/books/", methods=["POST"])
def create_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    book = {
        'id': books.all()[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False,
        'date': request.json.get('date', ""),
        'genre': request.json.get('genre', "")
    }
    books.create_api(book)
    return jsonify({'book': book}), 201


@app.route("/api/v1/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = books.get_api(book_id)
    if not book:
        abort(404)
    return jsonify({"book": book}) """