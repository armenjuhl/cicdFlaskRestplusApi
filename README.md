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
Being no other guidelines were given, I created a single file REST Api application using the Flask RESTPlus framework. I utilized Flask RESTPlus because it of its implementation of Swagger which gives the API an easy to interact with UI. The application currently uses in-memory persistence rather than a database. I utilized the Data Access Object Design Pattern (DAO). This decouple's CRUD operations and the database layer which enables the project to be easily refactor to implement a database and data models in the future. 
<br/><br/>
<strong>To create a production quality API with this project a minimum of the following tasks need to be completed.</strong>
<br/>
<h4>Todos:</h4>
<ul>
  <li>Refactor app file structure according to Flask RESTPlus and/ or company conventions</li>
  <li>Incorporate SQLAlchemy models</li>
  <li>Incorporate database (MySql, Postgre SQL, MariaDB, MongoDB, etc)</li>
  <li>Refactor DAO Classes data source to implement persistence layer in CRUD operations</li>
  <li>Optional: Incorporate Marshmallow or similar marshalling framework for increased input validation</li>
</ul>

<h1>Screenshot</h1>
<img src="https://github.com/armenjuhl/cicdFlaskRestplusApi/blob/master/screencapture-127-0-0-1-5000-2020-04-13-08_21_53.png?raw=true"/>

<h1>Dependencies</h1>
<p>
aniso8601==8.0.0<br/>
attrs==19.3.0<br/>
click==7.1.1<br/>
Flask==1.1.2<br/>
flask-restplus==0.13.0<br/>
Flask-SQLAlchemy==2.1<br/>
itsdangerous==1.1.0<br/>
Jinja2==2.11.1<br/>
jsonschema==3.2.0<br/>
MarkupSafe==1.1.1<br/>
pyrsistent==0.16.0<br/>
pytz==2019.3<br/>
six==1.14.0<br/>
SQLAlchemy==1.3.16<br/>
Werkzeug==0.16.1<br/>
</p>
