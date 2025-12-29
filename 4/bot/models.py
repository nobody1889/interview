from django.db import models

class TelegramUser(models.Model):
    user_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.username or self.first_name} ({self.user_id})"

class Message(models.Model):
	STATUS_CHOICES=[
		('sender', 'Sender'),
		('receiver', 'Receiver')
	]

	user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, related_name='messages')

	text = models.TextField()
	message_id = models.IntegerField()	# for later reply

	created_at = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return f"[{self.status}]: \n\t[{self.text}]"