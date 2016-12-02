import random

from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import PermissionDenied

from gifts.models import Gift, Comment
from user.models import UserProfile
from user.decorators import class_login_required

import utils


@class_login_required
class GiftList(View):
    template_name = 'gifts/gift_list.html'

    def get(self, request):
        return render(request, self.template_name,
                      {'display_memory': utils.get_memory(),
                       'gift_list': Gift.objects.all().order_by('gift_number'),
                       })


@class_login_required
class SingleGift(View):
    template_name = 'gifts/single_gift.html'

    def get(self, request, giftNumber=None):
        return render(request, self.template_name,
                      {'display_memory': utils.get_memory(),
                       'gift': Gift.objects.get(gift_number = giftNumber)})


@class_login_required
class Select(View):
    template_name = 'gifts/gift_list.html'

    def get(self, request, gift_number=None):
        return render(request, self.template_name,
                      {'display_memory': utils.get_memory(),
                       'gift_number':gift_number})

    def post(self, request):
        profile = UserProfile.objects.get(user=request.user)
        current_gift = Gift.objects.get(gift_number=request.POST['giftNumber'])
        current_gift.selected = True
        current_gift.receiver = request.user
        current_gift.receiver_name = request.user.username
        current_gift.save()
        profile.gift_selected = current_gift
        profile.save()
        return redirect('gift_list')


@class_login_required
class ChangeMind(View):
    template_name = 'gifts/gift_list.html'

    def post(self, request):
        profile = UserProfile.objects.get(user=request.user)
        current_gift = Gift.objects.get(gift_number=request.POST['giftNumber'])
        current_gift.selected = False
        current_gift.receiver = None
        current_gift.receiver_name = ''
        current_gift.save()
        profile.gift_selected = None
        profile.save()
        return redirect('gift_list')


@class_login_required
class AddComment(View):
    template_name = 'gifts/comment_create.html'

    def get(self, request, gift_number=None):
        print('In AddComment.get, request = ', request)
        return render(request, self.template_name,
                      {'display_memory': utils.get_memory(),
                       'gift': Gift.objects.get(gift_number = gift_number)})

    def post(self, request, gift_number=None):
        current_gift = Gift.objects.get(gift_number=gift_number)
        new_comment = Comment(gift=current_gift,
                              user=request.user,
                              comment=request.POST['comment_text'])
        new_comment.save()
        return redirect('gift_list')


@class_login_required
class EditComment(View):
    template_name = 'gifts/comment_edit.html'

    def get(self, request, gift_number=None, comment_number=None):
        comment = Comment.objects.get(pk=comment_number)
        if request.user == comment.user:
            return render(request, self.template_name,
                          {'display_memory': utils.get_memory(),
                           'gift': Gift.objects.get(gift_number=gift_number),
                           'comment': comment})
        else:
            raise PermissionDenied

    def post(self, request, comment_number=None):
        comment = Comment.objects.get(pk=comment_number)
        if request.user == comment.user:
            comment.comment = request.POST['comment_text']
            comment.save()
            return redirect('gift_list')
        else:
            raise PermissionDenied



@class_login_required
class DeleteComment(View):
    template_name = 'gifts/comment_delete.html'

    def get(self, request, gift_number=None, comment_number=None):
        gift = Gift.objects.get(gift_number=gift_number)
        comment = Comment.objects.get(pk=comment_number)
        if request.user == comment.user:
            return render(request, self.template_name,
                          {'display_memory': utils.get_memory(),
                           'gift': gift,
                           'comment': comment}
                          )
        else:
            raise PermissionDenied

    def post(self, request, gift_number=None, comment_number=None):
        comment = Comment.objects.get(pk=comment_number)
        if request.user == comment.user:
            comment.delete()
            return redirect('gift_list')
        else:
            raise PermissionDenied
