from django.http import HttpResponse, Http404

def about(request, day_of_the_week):
    if day_of_the_week == 'monday':
        return HttpResponse("This is Monday, start of the week, such a sad one…")
    elif day_of_the_week == 'tuesday':
        return HttpResponse("This is Tuesday, often a laborious one!")
    elif day_of_the_week == 'wednesday':
        return HttpResponse("This is Wednesday, difficult to tell, difficult to spell.")
    elif day_of_the_week == 'thursday':
        return HttpResponse("This is Thursday, half of the week but near of the end ;-).")
    elif day_of_the_week == 'friday':
        return HttpResponse("This is Friday, last run before weekend.")
    elif day_of_the_week == 'saturday':
        return HttpResponse("This is Saturday, so good! Have a rest.")
    elif day_of_the_week == 'sunday':
        return HttpResponse("This is Sunday, no so bad to be workless…")
    else:
        raise Http404("Not a day I know, surely not a day at all…")