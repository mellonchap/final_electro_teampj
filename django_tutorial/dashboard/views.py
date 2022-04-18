from urllib import request
from django.shortcuts import redirect, render

from .forms import CountryDataForm
from .models import CountryData

# Create your views here.
def dashboard(request):
    #각 나라의 인구 가져오기
    data = CountryData.objects.all()
    #add 버튼 클릭, 값입력 요청 처리
    if request.method== "POST":
        #DB 입력
        form = CountryDataForm(request.POST)

        if form.is_valid():
            #폼에 입력한 나라
            input_country = form.data.get('country', None)
            #폼에 입력한 인구수
            input_num= form.data.get('population', None)
            #DB에 나라이름이 중복확인
            #CRUD
            CountryData.objects.update_or_create(
                #filter
                country = input_country,
                #new_value
                defaults={
                    'country' : input_country,
                    'population':input_num
                }

            )
            #form.save()
            return redirect('.')
    #form cnffur
    else:
        form = CountryDataForm()
    
    #그래프 반영

    #form객체 생성
    form = CountryDataForm()
    context = {'dataset':data, 'form':form}
    return render(request, 'dashboard/dashboard.html' ,context )
    


# class CountryData(models.Model):
#     country = models.CharField(max_length=100)
#     population = models.IntegerField()