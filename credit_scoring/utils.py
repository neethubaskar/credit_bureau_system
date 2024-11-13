from .models import UserResponse

def calculate_credit_score(user):
    """
    Calculate the credit score for a given user based on their responses to questions.
    param:
        user (User): The user for whom to calculate the credit score.
    return:
        int: The total credit score calculated from all responses.
    """
    responses = UserResponse.objects.filter(user=user)
    total_score = 0

    for response in responses:
        question = response.question
        answer = response.answer
        
        if answer == 'A':
            total_score += question.score_A
        elif answer == 'B':
            total_score += question.score_B
        elif answer == 'C':
            total_score += question.score_C
        elif answer == 'D':
            total_score += question.score_D

    return total_score
