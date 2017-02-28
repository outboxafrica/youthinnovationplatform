from functools import wraps
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from users.models import Innovator, Investor, Mentor, HubManager


def check_profile_complete():
    def _check_profile_complete(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_anonymous:
                user = request.user
                if user.role == 'innovator':
                    profile = Innovator.objects.get(email=user.email)
                    if profile.has_startup:
                        print "continue normally"
                        return view_func(request, *args, **kwargs)
                    else:
                        print "redirect to another page"
                        return view_func(request, *args, **kwargs)
                elif user.role == 'investor':
                    profile = Investor.objects.get(email=user.email)
                    if profile.has_company:
                        return view_func(request, *args, **kwargs)
                    else:
                        # go to the company page
                        pass

                elif user.role == 'hub_manager':
                    pass
                else:
                    return view_func(request, *args, **kwargs)
            else:
                return view_func(request, *args, **kwargs)

