from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import PermissionDenied

from memory.models import Memory
from user.decorators import class_login_required

import utils


@class_login_required
class MemoryCreate(View):
    template_name = 'memory/memory_create.html'

    def get(self, request):
        return render(request, self.template_name,
                      { 'display_memory': utils.get_memory()})

    def post(self, request):
        memory_text = request.POST['memory_text']
        user = request.user
        memory = Memory(post=memory_text, user=user)
        memory.save()
        user.userprofile.added_memories = True
        user.userprofile.save()
        # get a list of this user's memory entries
        return redirect('memory_list')



@class_login_required
class MemoryList(View):
    template_name = 'memory/memory_edit_list.html'

    def get(self, request):
        user_memories = Memory.objects.filter(user=request.user)
        return render(request, self.template_name,
                      { 'display_memory': utils.get_memory(),
                        'user_memories': user_memories })


@class_login_required
class MemoryEdit(View):
    template_name = 'memory/memory_edit.html'

    def get(self, request, memory_id=None):
        memory = Memory.objects.get(pk=memory_id)
        if request.user == memory.user:
            return render(request, self.template_name,
                          {'display_memory': utils.get_memory(),
                           'memory': Memory.objects.get(pk=memory_id)})
        else:
            raise PermissionDenied

    def post(self, request, memory_id=None):
        current_memory = Memory.objects.get(pk=memory_id)
        if request.user == current_memory.user:
            current_memory.post = request.POST['memory_text']
            current_memory.save()
            return redirect('memory_list')
        else:
            raise PermissionDenied


@class_login_required
class MemoryDelete(View):
    template_name = 'memory/memory_delete.html'

    def get(self, request, memory_id=None):
        memory = Memory.objects.get(pk=memory_id)
        if request.user == memory.user:
            return render(request, self.template_name,
                          {'display_memory': utils.get_memory(),
                           'memory': Memory.objects.get(pk=memory_id)})
        else:
            raise PermissionDenied

    def post(self, request, memory_id=None):
        current_memory = Memory.objects.get(pk=memory_id)
        user = request.user
        if user == current_memory.user:
            current_memory.delete()
            if Memory.objects.filter(user=user).count() == 0:
                user.userprofile.added_memories = False
                user.userprofile.save()
            return redirect('memory_list')
        else:
            raise PermissionDenied

