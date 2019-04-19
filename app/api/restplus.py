from flask_restplus import Api

api = Api(
    version='1.0',
    title='REST-Backend',
    desciption='REST-Backend  for CRUD operations on a message board',
    default_label='API information'
)