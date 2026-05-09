from rest_framework import serializers

from .models import *


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class GetCategorySerilizers(serializers.ModelSerializer):
    class Meta:
        model = GetCategory
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    main_game = GetCategorySerilizers()
    class Meta:
        model = Question
        fields = [
            'id',
            'main_game',
            'question',
            'answer_1',
            'answer_2',
            'answer_3',
            'answer_4',
            'status',
            'correct_answer',
            'explanation',
            'attachment'
            # 'other_information_r'
        ]
    def to_representation(self, instance):
        data = super().to_representation(instance)
        correct_index = int(instance.correct_answer)

        formatted = {
            "id": data["id"],
            "question": data["question"],
            "answers": [
                {"text": data["answer_1"], "isCorrect": correct_index == 1},
                {"text": data["answer_2"], "isCorrect": correct_index == 2},
                {"text": data["answer_3"], "isCorrect": correct_index == 3},
                {"text": data["answer_4"], "isCorrect": correct_index == 4},
            ],
            "status":data["status"],
            "explanation":data["explanation"],
            "attachment":data["attachment"],            
        }

        return formatted
    

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = ['main_game', 'last_question']
