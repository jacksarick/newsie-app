import json
from gmail import Gmail
from werkzeug.wrappers import Request, Response

username, password = "test@newsie.club", "mypassword1"

def rfetch(msg):
	msg.fetch()
	return {
		"sender": msg.fr,
		"date": msg.sent_at.date().isoformat(),
		"title": msg.subject,
		"body": "body here, but for now test", #msg.body.replace("\r\n", "<br>")
		"read": msg.is_read(),
		"id": msg.message_id
	}

def get_all_mail(username, password):
	g = Gmail()
	g.login(username, password)
	print "connected"
	inbox = [rfetch(m) for m in g.inbox().mail()]
	g.logout()
	print "bye"
	return inbox

@Request.application
def application(request):
    return Response(json.dumps(get_all_mail(username, password)))

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)