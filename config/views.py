from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

#로그인 구현 
def main(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password = password) #입력한 ID, pw 확인
        
        if user is not None:
            login(request, user) # 세션에 로그인 상태 저장 
            return redirect('customer_management:customer_list')
        
        else: 
            return render(request, 'main.html',{'error': '아이디 또는 비밀번호가 잘못되었습니다.'})
    return render(request, "main.html")

