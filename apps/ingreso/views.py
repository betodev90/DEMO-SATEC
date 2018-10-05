from django.shortcuts import render
from .forms import LoginForm
from django.contrib import auth
from django.http.response import JsonResponse, HttpResponse,\
    HttpResponseRedirect
from django.views.generic import View
from django.contrib import messages
from django.shortcuts import render_to_response, redirect, reverse

def login_view(request):
    return render(request, 'ingreso/login.html', {})


class LoginView(View):
    title = 'Iniciar Sesión'
    form_class = LoginForm
    initial = {}
    template_name = 'ingreso/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {'form': form, 'title': self.title}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.cleaned_data['user']
            password = form.cleaned_data['password']
            # no_expire = form.cleaned_data['not_expire']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Íngreso exitoso')
                    return redirect(reverse('home'))
                else:
                    message = 'Su usuario ha sido desactivado, consulte a la secretaría docente.'
                   ## messages.add_message(request, messages.ERROR, message)
                    messages.error(request, message)
                    context = {'form': form, 'title': self.title}
                    return render(request, self.template_name, context)
            else:
                message = 'Usuario o contraseña inválidos.'
                messages.add_message(request, messages.ERROR, message)
                context = {'form': form, 'title': self.title}
                return render(request, self.template_name, context)

        message = 'Debe introducir un usuario y una contraseña válidas.'
        messages.add_message(request, messages.ERROR, message)
        context = {'form': form, 'title': self.title}
        return render(request, self.template_name, context)
        # return render_to_response(self.template_name, RequestContext(request, context))
