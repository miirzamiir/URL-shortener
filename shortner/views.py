from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import Link


class index(View):
    def get(self, request):
        return render(request, 'index.htm')

    def post(self, request):
        url = request.POST.get("link")
        link = Link.objects.create(url=url)
        url = 'localhost:8000/'+str(link.uuid)[-5:]
        return render(
            request, 'index.htm', context={'url': url}
        )
        

class retrieve(View):
    def get(self, request, pk):
        try:
            link = Link.objects.get(uuid__endswith=pk)
            return redirect(to=link.url)
        except Link.DoesNotExist:
            return JsonResponse({'detail' :'This link does not exist in our database!'}, status=404)

