from django.shortcuts import render



from users.models import User_profile

from django.urls import reverse

from django.views.generic import DetailView, UpdateView

class Detail_user_profile(DetailView):
    model = User_profile
    template_name= 'user/detail_user_profile.html'

class Update_user_profile(UpdateView):
    model = User_profile
    template_name = 'user/update_user_profile.html'
    fields = ['name','mail', 'profile_image']

    def get_success_url(self):
        return reverse('detail_user_profile', kwargs = {'pk':self.object.pk})