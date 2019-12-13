import os
import sentry_sdk

from bottle import Bottle
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://506f40bc874d44c9970751bccb532651@sentry.io/1855120",
    integrations=[BottleIntegration()]
)

app = Bottle()

@app.route("/success")
def example_api_response_1():
    return ''

@app.route("/fail")
def example_api_response_2():
    raise RuntimeError("Все пропало шеф! Сервер загнулся!")
    return

if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080, debug=True)
