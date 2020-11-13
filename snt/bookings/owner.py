
from django.views.generic import UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin


class OwnerUpdateView(LoginRequiredMixin, UpdateView):

    def get_queryset(self):
        print('update get_queryset called')
        qs = super(OwnerUpdateView, self).get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerDeleteView(LoginRequiredMixin, DeleteView):

    def get_queryset(self):
        print('delete get_queryset called')
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)