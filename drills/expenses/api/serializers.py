from rest_framework import serializers
from expenses.models import Expense


class ExpenseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    amount = serializers.DecimalField( max_digits=10,decimal_places=2)
    category= serializers.ChoiceField(choices=Expense.Category.choices)
    spent_on = serializers.DateField()
    created_at = serializers.DateTimeField(read_only=True)
    
    def validate_amount(self,value):
            # Confirm the amount is >0
            if value<=0:
                raise serializers.ValidationError("Amount is not greater than 0")
            else:
                return value

    def create(self,validated_data):
        '''return an expense  given the validated data'''
        return Expense.objects.create(**validated_data)

"""
    def update(self, instance, validated_data):
        #Update and return an existing Expense instance, given the validated data
        
        instance.title = validated_data.get("title",instance.title)
        instance.amount = validated_data.get("amount",instance.amount)
        instance.category = validated_data.get("category",instance.category)
        instance.spent_on = validated_data.get("spent_on",instance.spent_on)
        instance.save()
        return instance
"""
     
"""
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Expense
        fields = ["id","title","amount","category","spent_on"]
"""