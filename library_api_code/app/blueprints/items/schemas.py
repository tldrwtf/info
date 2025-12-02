from app.extensions import ma
from app.models import Items, ItemDescription

class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Items
        include_fk = True

class ItemDescriptionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItemDescription

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)
item_description_schema = ItemDescriptionSchema()
item_descriptions_schema = ItemDescriptionSchema(many=True)