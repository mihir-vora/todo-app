from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from users.forms import SignUpForm, UserLoginForm

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		print(form)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')

			print(username)

			password = form.cleaned_data.get('password1')

			print(password)

			user = authenticate(username=username, password=password1)
			
			print(user)

			login(request, user)
			return redirect('login')
	else:
		form = SignUpForm()
	context = {
		'form' : form
	}

	return render(request, 'users/signup.html', context)




# def login(request):
# 	if request.method == 'POST':
# 		form = AuthenticationForm(request.POST)
# 		print(form)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')

# 			print(username)

# 			password = form.cleaned_data.get('password1')

# 			print(password)

# 			user = authenticate(username=username, password=password)

# 			login(request, user)

# 			return redirect('/')
# 	else:
# 		form = AuthenticationForm()
# 		print("elsejb kjqeb.keaj bkajebfkjb")
# 	context = {
# 		'form' : form
# 	}

# 	return render(request, 'users/login.html', context)


