from django.db import models

class TelegramUser(models.Model):
    user_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.username or self.first_name} ({self.user_id})"

class Message(models.Model):
	FILE_TYPE_CHOICES = [
        ('text', 'Text'),
        ('photo', 'Photo'),
        ('document', 'Document'),
    ]

	user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, related_name='messages')

	text = models.TextField()
	message_id = models.IntegerField(blank=True, null=True)

	types = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES, default='text')

	created_at = models.DateTimeField(auto_now_add=True)
	is_bot = models.BooleanField(default=False)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		sender = "BOT" if self.is_bot else "USER"
		content = self.text if self.types == 'text' else f"{self.types}({self.message_id})"
		return f"[{sender}] ({self.user.user_id}): {content}"
          