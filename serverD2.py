import os
import sentry_sdk

from bottle import route, run

sentry_sdk.init("https://506f40bc874d44c9970751bccb532651@sentry.io/1855120")


"""


Необходимо написать простой веб-сервер с помощью фреймворка Bottle. 
Все ошибки приложения должны попадать в вашу информационную панель Sentry. 
Приложение должно размещаться на Heroku, иметь минимум два маршрута:

/success, который должен возвращать как минимум HTTP ответ со статусом 200 OK
/fail, который должен возвращать "ошибку сервера" (на стороне Bottle это может 
быть просто RuntimeError), то есть HTTP ответ со статусом 500

"""
a = []

@route("/success")
def example_api_response_1():
    return ''

@route("/fail")
def example_api_response_2():
    return a[1]

if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
