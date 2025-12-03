from django.http import HttpResponse,JsonResponse

def http_test(request):
    return HttpResponse('<h1>this is a test</h1>')

def jason_test(request):
    return JsonResponse({'name': 'Amir'})