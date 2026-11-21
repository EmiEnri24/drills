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