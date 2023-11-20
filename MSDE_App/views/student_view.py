from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.models import Student
from MSDE_App.forms import CreateStudent
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Django course !!"
        return context


class CreateStudentView(CreateView):
    model = Student
    form_class = CreateStudent
    template_name = 'student/create_student.html'
    success_url = '/fil/students'  # Asegúrate de ajustar esto a la URL correcta

    def form_invalid(self, form):
        return render(self.request, 'student/create_student.html', {
            'form': form,
            'error': 'Please provide valid data'
        })


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student/student_detail.html'
    context_object_name = 'student'

    def get_object(self):
        student_code = self.kwargs.get('student_code')
        return get_object_or_404(Student, student_code=student_code)


class StudentsView(ListView):
    model = Student
    template_name = 'student/students.html'
    context_object_name = 'students'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_name = self.request.GET.get('search_name', '')
        name_initial = self.request.GET.get('name_initial')
        surname_initial = self.request.GET.get('surname_initial')

        if search_name:
            queryset = queryset.filter(student_name__icontains=search_name)
        if name_initial:
            queryset = queryset.filter(student_name__istartswith=name_initial)
        if surname_initial:
            queryset = queryset.filter(student_surname__istartswith=surname_initial)

        return queryset


class EditStudentView(UpdateView):
    model = Student
    form_class = CreateStudent
    template_name = 'student/edit_student.html'
    success_url = '/fil/students'  # Asegúrate de ajustar esto a la URL correcta
    def get_object(self):
        student_code = self.kwargs.get('student_code')
        return get_object_or_404(Student, student_code=student_code)


class DeleteStudentView(DeleteView):
    model = Student
    template_name = 'student/delete_student.html'
    success_url = '/fil/students'  # Asegúrate de ajustar esto a la URL correcta

    def get_object(self):
        student_code = self.kwargs.get('student_code')
        return get_object_or_404(Student, student_code=student_code)

    def post(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

