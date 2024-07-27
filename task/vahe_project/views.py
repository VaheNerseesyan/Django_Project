from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.forms import ModelForm
from .models import Lesson


class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'image', 'description', 'price_per_month', 'lessons_count', 'lessons_duration',
                  'pupils_count', 'team_lead', 'team_lead_name', 'company_address',
                  'support_phone_number', 'start_date', 'category']


class LessonListView(ListView):
    model = Lesson
    template_name = 'lesson_list.html'
    context_object_name = 'lessons'


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'lesson_detail.html'
    context_object_name = 'lesson'


class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'lesson_form.html'
    success_url = reverse_lazy('lesson_list')


class LessonUpdateView(UpdateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'lesson_form.html'
    success_url = reverse_lazy('lesson_list')


class LessonDeleteView(DeleteView):
    model = Lesson
    template_name = 'lesson_confirm_delete.html'
    success_url = reverse_lazy('lesson_list')

