from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied

from django.http import Http404

from .models import Course
from ..mod.models import Moderator
from ..files.models import File

from ..decorators import login

# Create your views here.

@login
def index(request):
    courses = Course.objects.all()
    
    return render(request, 'class/index.html', {'classes': courses})
    
@login
def show(request, course_url):
    course = get_object_or_404(Course, url=course_url)

    is_mod = False

    try:
        mod = Moderator.objects.get(username=request.session['user'])
    except Moderator.DoesNotExist:
        is_mod = False
        return render(request, 'class/show.html', {'course': course, 'is_mod': is_mod})
        
    if mod.admin:
        is_mod = True
        
    elif course in mod.classes.all():
        is_mod = True
    
    return render(request, 'class/show.html', {'course': course, 'is_mod': is_mod})
    
@login
def approve(request, course_url, doc_id):
    course = get_object_or_404(Course, url=course_url)
    try:
        mod = Moderator.objects.get(username=request.session['user'])
    except Moderator.DoesNotExist:
        raise PermissionDenied

    if mod.admin or (course in mod.classes.all()):
        try:
            doc = course.unapproved_files.get(id=doc_id)
        except File.DoesNotExist:
            try:
                doc = course.files.get(id=doc_id)
            except File.DoesNotExist:
                raise Http404("Error: Document Not Related to this Course")
            raise Http404("Error: Document Already Approved")
        course.unapproved_files.remove(doc)
        course.files.add(doc)
        
        return render(request, 'class/approve.html', {'doc': doc, 'course': course})
    else:
        raise PermissionDenied 

@login
def remove(request, course_url, doc_id):
    course = get_object_or_404(Course, url=course_url)
    try:
        mod = Moderator.objects.get(username=request.session['user'])
    except Moderator.DoesNotExist:
        raise PermissionDenied
        
    if mod.admin or (course in mod.classes.all()):
        try:
            doc = course.files.get(id=doc_id)
        except File.DoesNotExist:
            try:
                doc = course.unapproved_files.get(id=doc_id)
            except File.DoesNotExist:
                raise Http404("Error: Document Not Related to this Course")

            course.unapproved_files.remove(doc)
            course.rejected_files.add(doc)
            
            return render(request, 'class/remove.html', {'doc': doc, 'course': course})

        course.files.remove(doc)
        course.rejected_files.add(doc)
        
        return render(request, 'class/remove.html', {'doc': doc, 'course': course})
    else:
        raise PermissionDenied 
        
@login
def undelete(request, course_url, doc_id):
    course = get_object_or_404(Course, url=course_url)
    try:
        mod = Moderator.objects.get(username=request.session['user'])
    except Moderator.DoesNotExist:
        raise PermissionDenied
        
    if mod.admin or (course in mod.classes.all()):
        try:
            doc = course.rejected_files.get(id=doc_id)
        except File.DoesNotExist:
            raise Http404("Error: Document Not Related to this Course")

        course.rejected_files.remove(doc)
        course.files.add(doc)
        
        return render(request, 'class/undelete.html', {'doc': doc, 'course': course})
    else:
        raise PermissionDenied 