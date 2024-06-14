from flask.views import MethodView
from flask_smorest import Blueprint

from schemas import TagSchema

from models import StoreModel


blp = Blueprint("Tags", "tags", description="Operation on tags")


@blp.route("/store/<string:store_id>/tag")
class TagsInStore(MethodView):
    @blp.response(200, TagSchema(many=True))
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)

        return store.tags.all()