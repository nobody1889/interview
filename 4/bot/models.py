from django.db import models

class Message(models.Models):
	STATUS_CHOICES=[
		('sender', 'Sender'),
		('receiver', 'Receiver')
	]
	
	text = models.TextField()
	create_at = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES)

	def __str__(self):
		return f"[{self.status}]: \n\t[{self.text}]"