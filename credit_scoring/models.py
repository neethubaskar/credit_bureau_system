from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class AuditModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="%(class)s_created", on_delete=models.SET_NULL, null=True, blank=True)
    modified_by = models.ForeignKey(User, related_name="%(class)s_modified", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Overrides save method to set modified_by automatically.
        `created_by` should be set only on creation (if not set already).
        """
        if not self.pk:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        super().save(*args, **kwargs)


class Question(AuditModel):
    question_text = models.CharField(max_length=255)
    answer_A = models.CharField(max_length=255)
    answer_B = models.CharField(max_length=255)
    answer_C = models.CharField(max_length=255)
    answer_D = models.CharField(max_length=255)
    score_A = models.IntegerField()
    score_B = models.IntegerField()
    score_C = models.IntegerField()
    score_D = models.IntegerField()

    def __str__(self):
        """
        Returns the question text as a string representation 
        of the model instance.
        """
        return self.question_text

class UserResponse(AuditModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

    def __str__(self):
        """
        Returns a string representation of the user's response, displaying
        the user, question, and selected answer.
        """
        return f'{self.user} - {self.question} - {self.answer}'
