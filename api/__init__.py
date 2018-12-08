from flask import request, jsonify, abort, json
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
    from api.models import Project

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    #enable cors
    CORS(app)

    db.init_app(app)

    @app.route('/projects/', methods=['POST', 'GET'])
    def projects(): 
        if request.method == "POST":
            title = str(request.data.get('title', ''))
            email = str(request.data.get('email', ''))
            short_description = str(request.data.get('short_description',''))
            description = str(request.data.get('description', ''))
            url = str(request.data.get('url', ''))
            creator_name = str(request.data.get('description', ''))
            twitter = str(request.data.get('description', ''))
            instagram = str(request.data.get('description', ''))
            facebook = str(request.data.get('description', ''))
            portfolio = str(request.data.get('description', ''))
            image_url = str(request.data.get('image_url', ''))
            slug = str(request.data.get('slug', ''))

            if title and email and short_description and url:
                project = Project(title=title, email=email, short_description=short_description, description=description, url=url, creator_name=creator_name, twitter=twitter, instagram=instagram, facebook=facebook, portfolio=portfolio, slug=slug)
                project.save()
                response = jsonify({
                    'id': project.id,
                    'url': '/' + project.slug,
                    'date_created': project.date_created,
                    'date_modified': project.date_modified 
                })
                response.status_code = 201
                return response
            else: 
                response = jsonify({'error': 'Missing required fields'})
                response.status_code = 401
                return response
        else: 
            #GET
            projects = Project.get_all()
            results = []

            for project in projects:
                results.append(project.to_dict())
            response = jsonify(results)
            response.status_code = 200
            return response
    
    @app.route('/projects/status/', methods=['PUT'])
    def project_status():

        if request.method == "PUT": 
            ids = request.data.get('ids', '')
            status = str(request.data.get('status', ''))
            results = [];
            for id in ids:
                project = Project.query.filter_by(id=id).first()
                project.status = status
                project.save()
                results.append(project.to_dict())
            response = jsonify(results)
            response.status_code = 200
            return response

    @app.route('/projects/<string:slug>', methods=['GET'])
    def project_detail(slug, **kwargs):
        project = Project.query.filter_by(slug=slug).first()
        if not project:
            abort(404)

        if request.method == "GET":
            response = jsonify(project.to_dict())
            response.status_code = 200
            return response

    return app