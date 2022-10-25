from django.shortcuts import render,redirect
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView, FormMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User, auth
import folium
import geocoder
from . import models
from .forms import ChatForm

#login
class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')

# dashboard view.
def dashboard(request):
    m = folium.Map(location=[10.5276, 76.2144],
                    zoom_start=10)
    folium.Marker(location=[10.5187472, 76.2030061],
              icon=folium.Icon(icon='glyphicon-asterisk', color='red'),
              popup=folium.Popup('<i>Poothole\nNumber of Visit=0</i>'),
              tooltip='Poothole '
              ).add_to(m)
    folium.Marker(location=[10.566486, 76.195763],
              icon=folium.Icon(icon='glyphicon-asterisk', color='blue'),
              popup=folium.Popup('<i>Kuttoor \nNumber of Visit=14</i>'),
              tooltip='Kuttoor'
              ).add_to(m)
    folium.Marker(location=[10.5263547, 76.1885071],
              icon=folium.Icon(icon='glyphicon-asterisk', color='orange'),
              popup=folium.Popup('<i>Ayyanthole\nNumber of Visit=5</i>'),
              tooltip='Ayyanthole'
              ).add_to(m)

    folium.Marker(location=[10.5539107, 76.2218334],
              icon=folium.Icon(icon='glyphicon-asterisk', color='blue'),
              popup=folium.Popup('<i>Viyyur\nNumber of Visit=11</i>'),
              tooltip='Viyyur'
              ).add_to(m)
    folium.Marker(location=[10.5053, 76.2105],
              icon=folium.Icon(icon='glyphicon-asterisk', color='blue'),
              popup=folium.Popup('<i>Koorkenchery\nNumber of Visit=7</i>'),
              tooltip='Koorkenchery'
              ).add_to(m)
    folium.Marker(location=[10.5352, 76.2015],
              icon=folium.Icon(icon='glyphicon-asterisk', color='green'),
              popup=folium.Popup("<i>Punkunnam\nNumber of Visit=18</i>", max_width=300),
              tooltip='Punkunnam'
              ).add_to(m)

    folium.Marker(location=[10.5164, 76.2132],
              icon=folium.Icon(icon='glyphicon-asterisk', color='green'),
              popup=folium.Popup("<i>Veliyannur\nNumber of Visit=23</i>", max_width=300),
              tooltip='Veliyannur'
              ).add_to(m)
    m = m._repr_html_()
    context = {
        'm': m,  
    }
   
    return render(request,'dashboard.html', context)
#sign up page
class SignupPage(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignupPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return super(SignupPage, self).get(*args, **kwargs)