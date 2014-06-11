from jitterbunk_app.models import Bunk, User
from django.shortcuts import render_to_response, get_object_or_404
from forms import BunkSomeone
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.db.models import Q


def main_feed(request):
    """ Displays all bunks """
    bunk_list = Bunk.objects.all().order_by('-time')
    return render_to_response('main_feed.html', {'bunk_list': bunk_list})


def personal_feed(request, user_name):
    """ Displays bunks either from you or to you """
    user = User.objects.get(user=user_name)
    bunk_list = Bunk.objects.filter(Q(from_user=user) | Q(to_user=user))
    form = BunkSomeone()
    return render_to_response('personal_feed.html', {
        'bunk_list': bunk_list,
        'user': user_name,
        'form': form
    })


@csrf_exempt
def bunked(request):
    """ Handles processing the Bunk form on personal feeds """
    if request.method == 'POST':
            to_user_name = request.POST['user_to_bunk']
            from_user_name = request.POST['from_user']
            user_bunked = get_object_or_404(User, user=to_user_name)
            user_bunking = get_object_or_404(User, user=from_user_name)
            new_bunk = Bunk(from_user=user_bunking,
                            to_user=user_bunked)
            new_bunk.save()
            return redirect('jitterbunk_app.views.personal_feed',
                            user_name=from_user_name)
    else:
        raise Http404
