from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import allCourses, details


def courses(request):
    ac = allCourses.objects.all()
    template = loader.get_template('courseApp/courses.html')
    context = {'ac': ac}
    return HttpResponse(template.render(context, request))


def details(request, course_id):
    course = get_object_or_404(allCourses, pk=course_id)
    return render(request, 'courseApp/details.html', {'course': course})


def yourchoice(request, course_id):
    course = get_object_or_404(allCourses, pk=course_id)
    try:
        selected_ct = course.details_set.get(pk=request.POST['choice'])
    except (KeyError, allCourses.DoesNotExist):
        return render(request, 'courseApp/details.html',
                      {'course': course,
                       'error_message': 'invalid option, try again?'})
    else:
        selected_ct.your_choice = True
        selected_ct.save()
        return render(request, 'courseApp/details.html', {'course': course})
