from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserResponse, Question
from .forms import UserResponseForm
from .utils import calculate_credit_score

class QuestionPopupView(LoginRequiredMixin, FormView):

    template_name = 'credit_scoring/popup.html'
    form_class = UserResponseForm
    success_url = reverse_lazy('results')

    def get_form_kwargs(self):
        """
        Adds the current user to the form's keyword arguments, enabling the form to
        fetch questions and manage responses for that specific user.

        Returns:
            dict: Form keyword arguments, including the current user instance.
        """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        """
        Processes the valid form data, saving or updating the user's responses
        to each question in the database.

        Args:
            form (UserResponseForm): The validated form instance.

        Returns:
            HttpResponse: Redirects to the success URL after saving responses.
        """
        for field_name, answer in form.cleaned_data.items():
            question_id = field_name.split('_')[-1]
            question = Question.objects.get(id=question_id)
            UserResponse.objects.update_or_create(
                user=self.request.user,
                question=question,
                defaults={'answer': answer}
            )
        return super().form_valid(form)


class ResultsView(LoginRequiredMixin, TemplateView):
    template_name = 'credit_scoring/results.html'

    def get_context_data(self, **kwargs):
        """
        Adds the calculated credit score to the context data, enabling the
        template to display the user's score.

        Returns:
            dict: Context data with the user's credit score.
        """
        context = super().get_context_data(**kwargs)
        context['score'] = calculate_credit_score(self.request.user)
        return context
