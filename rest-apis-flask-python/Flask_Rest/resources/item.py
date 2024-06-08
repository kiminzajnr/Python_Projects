import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ItemSchema, ItemUpdateSchema

from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel

blp = Blueprint("Items", __name__, description="Operations on items")

@blp.arguments(ItemSchema)
@blp.response(201, ItemSchema)
def post(self, item_data):
    item = ItemModel(**item_data)

    try:
        db.session.add(item)
        db.session.commit()
    except SQLAlchemyError:
        abort(500, message="An error occured while inserting the item.")

    return item

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item

    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        raise NotImplementedError("Deleting an item is not implemented.")
    
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        item = ItemModel.query.get_or_404(item_id)
        raise NotImplementedError("Updating an item is not implemented.")
    
@blp.route("/item")
class ItemList(MethodView):
    @blp.response(201, ItemSchema)
    def get(self):
        return {"items": list(items.values())}

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        for item in items.values():
            if (
                item_data["name"] == item["name"]
                and item_data["store_id"] == item["store_id"]
            ):
                abort(400, message=f"Item already exists.")

        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item

        return item