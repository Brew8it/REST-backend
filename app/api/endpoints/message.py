from flask_restplus import Resource
from app.api.restplus import api
from app.api.serializers import message
from flask_pymongo import PyMongo

ns = api.namespace('Message', description='Message operations')
mongo = PyMongo()


@ns.route('/')
class Message_list(Resource):
    @ns.doc('list all messages')
    def get(self):
        """
        Displays all available messages
        """
        documents = [doc for doc in mongo.db.messages.find({}, {'_id': False})]
        return documents, 200

    @ns.doc('create_message')
    @ns.expect(message)
    @ns.response(201, '')
    def post(self):
        """
        Create a new message
        """
        mongo.db.messages.insert({'Message': api.payload})

        return "", 201

    @ns.doc('delete_message')
    @ns.expect(message)
    @ns.response(404, 'Message not found')
    @ns.response(204, 'Message deleted')
    def delete(self):
        """
        Delete a given message
        """
        result = mongo.db.messages.delete_one(
            {'Message.user_id': api.payload['user_id'], 'Message.msg_id': api.payload['msg_id'],
             "Message.message": api.payload['message']}
        )
        if result.deleted_count > 0:
            return "", 204
        else:
            return "", 404

    @ns.expect(message)
    @ns.response(204, 'Message updated')
    @ns.response(404, 'Message not found')
    def put(self):
        """
        Update a users given message
        """
        result = mongo.db.messages.update_one(
            {'Message.user_id': api.payload['user_id'], 'Message.msg_id': api.payload['msg_id']},
            {'$set': {"Message.message": api.payload['message']}}
        )
        if result.matched_count:
            return "", 204
        else:
            return "", 404
