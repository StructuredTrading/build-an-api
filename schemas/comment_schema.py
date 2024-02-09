from main import ma
from marshmallow import fields

class CommentSchema(ma.Schema):
    class Meta:
        ordered = True
        # Fields to expose. Card is not included as comments will be shown always attached to a Card.
        fields = ("id", "message", "user")
    user =  fields.Nested("UserSchema", only=("email",))  
      
comment_schema = CommentSchema()

comments_schema = CommentSchema(many=True)