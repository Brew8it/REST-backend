from flask_restplus import fields
from app.api.restplus import api

message = api.model("Message",
                    {
                        "user_id": fields.Integer(readOnly=True, description='The user identifier'),
                        "msg_id": fields.Integer(readOnly=True, description='The message unique identifier'),
                        "message": fields.String(required=True, description='The message itself')
                    })
