from strawberry.flask.views import GraphQLView
import os
from flask import Flask, render_template
from scripts.schema import schema

app = Flask(__name__)

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql_view", schema=schema
    ),
)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
