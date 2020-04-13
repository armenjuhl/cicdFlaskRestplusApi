# CiCi Api built using the Flask RESTPlus framework
<h1>Project Requirements</h1>

Use your choice of python web frameworks to create an nested web api that models the following objects:

- Project
- Stage
- Activity

Projects may have one or more stages, stages may have one or more activities.
Outside of their relationships to each other, each object need only contain “name" and “description” attributes.

The endpoints that need to be implemented are as follows:

/projects/ - GET
/projects/{pk}/ - GET, PUT, POST, DELETE
/projects/{project_pk}/stages/ - GET
/projects/{project_pk}/stages/{stage_pk}/ - GET, PUT, POST, DELETE
/projects/{project_pk}/stages/{stage_pk}/activities/ - GET
/projects/{project_pk}/stages/{stage_pk}/activities/{pk}/ - GET, PUT, POST, DELETE

<h1>Instructions</h1>
<ol>
  <li>git clone https://github.com/armenjuhl/cicdFlaskRestplusApi.git</li>
  <li>pip install -r requirements.txt</li>
  <li>python3 src/cicd_api.py</li>
  <li>Open <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a> on your browser</li>
  <li>Interact with endpoints under the <a href="#">api</a> toggle item with the Swagger UI</li>
</ol>

<h1>Notes</h1>
Being no other guidelines were given, I created a REST Api using the Flask RESTPlus framework to create an app that is easy to interact with by with the UI generated by Swagger.
To create a production grade API with this project a minimum of the following tasks need to be done.
Todos:
<ul>
  <li>Refactor app file structure according to Flask RESTPlus and/ or company conventions</li>
  <li>Incorporate SQLAlchemy models</li>
  <li>Incorporate database (MySql, Postgre SQL, MariaDB, MongoDB, etc)</li>
  <li>Refactor DAO implementation to use persistence layer in CRUD</li>
  <li>Optional: Incorporate Marshmallow or similar marshalling framework for increased input validation</li>
</ul>

<h1>Screenshot</h1>
<src ="https://raw.githubusercontent.com/armenjuhl/cicdFlaskRestplusApi/92d502f70f590aca1d859d1c002764adb1352859/screencapture-127-0-0-1-5000-2020-04-13-08_21_53.pdf"/>

<h1>Dependencies</h1>
<p> aniso8601==8.0.0
attrs==19.3.0
click==7.1.1
Flask==1.1.2
flask-restplus==0.13.0
Flask-SQLAlchemy==2.1
itsdangerous==1.1.0
Jinja2==2.11.1
jsonschema==3.2.0
MarkupSafe==1.1.1
pyrsistent==0.16.0
pytz==2019.3
six==1.14.0
SQLAlchemy==1.3.16
Werkzeug==0.16.1 </p>
