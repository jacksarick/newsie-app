from gmail import Gmail

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

g = Gmail()
g.login("test@newsie.club", "mypassword1")
print "connected"
print [rfetch(m) for m in g.inbox().mail()]
g.logout()
print "bye"