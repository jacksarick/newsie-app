import json
from gmail import Gmail
from werkzeug.wrappers import Request, Response

def rfetch(msg):
	msg.fetch()
	return {
		"sender": msg.fr,
		"date": msg.sent_at.date().isoformat(),
		"title": msg.subject,
		"body": msg.body.replace("\r\n", "<br>"),
		"read": msg.is_read(),
		"id": msg.message_id
	}

def get_all_mail(username, password):
	try:
		g = Gmail()
		g.login(username, password)
		print "connected"
		inbox = [rfetch(m) for m in g.inbox().mail()]
		g.logout()
		print "bye"
		return inbox
	except Exception as e:
		print e
		return ['login failed']

@Request.application
def application(request):
	if request.method == "POST":
		path = request.path
		print path
		print request.form
		post = request.form

		if path == "/data":
			if ("user" and "pass") in post:
				return Response(json.dumps(get_all_mail(post['user'] + "@newsie.club", post['pass'])))
			else:
				return ["incorrect login"]

		else:
			return ["No data here"]

	else:
		return Response("You probably issued a GET request, probably by accident")

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 2015, application)