from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from expenses.models import Expense
from expenses.api.serializers import ExpenseSerializer

@csrf_exempt
def expenses_list(request):
    '''
    List all the expenses , or creat a new expense line
    '''
    
    if request.method == "GET":
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ExpenseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
    
    else:
        return JsonResponse({"detail":"Method not allowed"}, status=405)
        #return HttpResponse(status=405)
    
@csrf_exempt
def expense_detail(request,pk):
    '''
    Retrieve, update or delete an expense
    '''
    
    try:
        expense = Expense.objects.get(pk=pk)
    except Expense.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = ExpenseSerializer(expense)
        return JsonResponse(serializer.data)
    
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ExpenseSerializer(expense,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == "DELETE":
        expense.delete()
        return HttpResponse(status=204)

    else:
        return JsonResponse({"detail":"Method not allowed"}, status=405)
 
