from django import forms
from .models import Question

class UserResponseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user from the kwargs
        super().__init__(*args, **kwargs)
        
        # Fetch questions specific to the user (optional, can be based on their history, etc.)
        questions = Question.objects.all()  # You can filter if needed
        
        for question in questions:
            # Dynamically create choice fields for each question
            self.fields[f'answer_{question.id}'] = forms.ChoiceField(
                label=question.question_text,
                choices=[
                    ('A', question.answer_A),
                    ('B', question.answer_B),
                    ('C', question.answer_C),
                    ('D', question.answer_D),
                ],
                widget=forms.RadioSelect,
                required=True,
            )
