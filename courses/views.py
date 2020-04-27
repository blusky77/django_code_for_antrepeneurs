from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Course


# Base View Class = View

class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.queryset}
        return render(request, self.template_name, context)


class CourseView(View):
    template_name = 'courses/course_detail.html'

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #     return render(request, 'about.html', {})


# class CourseDetailView(View):


# HTTP methods
def my_fbv(request, *args, **kwargs):
    print(request.method)
    return render(request, 'about.html', {})
