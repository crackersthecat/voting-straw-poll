from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from vote.models import Response, Constituency, Party


def index(request):
    constituencies = Constituency.objects.all()
    parties = Party.objects.all()
    context = {'constituencies': constituencies, 'parties': parties}
    return render(request, "vote/index.html", context)


def process_response(request):

    if ('will_you_vote' in request.POST):
        if (request.POST['will_you_vote'] == 'yes'):
            #If they are going to vote we need a constituency and a party
            #throws value error if constituency not selected
            try:
                selected_constituency = Constituency.objects.get(id=request.POST['constituency'])
                #selected_party = Party.objects.get(request.POST['party'])
            except (ValueError):
                # Redisplay the voting form.
                return render(request, 'vote/index.html', {
                    'error_message': "Please choose a valid constituency.",
                    'constituencies': Constituency.objects.all(),
                    'parties': Party.objects.all()
                })

            try:
                selected_party = Party.objects.get(id=request.POST['party'])
            except (ValueError):
                # Redisplay the voting form.
                return render(request, 'vote/index.html', {
                    'error_message': "Please choose a valid party.",
                    'constituencies': Constituency.objects.all(),
                    'parties': Party.objects.all()
                })

            response = Response.create(
                will_you_vote=request.POST['will_you_vote'],
                constituency=selected_constituency,
                party=selected_party
            )
            response.save()

        else:
            #record a 'no' vote, ignoring anything they may have 
            #set for consituency and party
            response = Response.create(
                will_you_vote=False,
                constituency=None,
                party=None
            )
            response.save()
    else:
        return render(request, 'vote/index.html', {
            'error_message': "Please say whether you are going to vote.",
            'constituencies': Constituency.objects.all(),
            'parties': Party.objects.all()
        })

    return HttpResponseRedirect(reverse('results_all'))


def results_all(request):
    yes_votes = Response.objects.filter(will_you_vote=True).count()
    no_votes = Response.objects.filter(will_you_vote=False).count()
    parties = Party.objects.all()
    all_party_votes = []
    for party in parties:
        party_votes = {}
        party_votes['party'] = party.party_name
        party_votes['votes'] = Response.objects.filter(party=party).count()
        all_party_votes.append(party_votes)
    context = {
        'yes_votes': yes_votes,
        'no_votes': no_votes,
        'all_party_votes': all_party_votes,
        'constituency': '',
    }
    return render(request, "vote/results.html", context)


def select_constituency(request):
    constituencies = Constituency.objects.all()
    context = {'constituencies': constituencies}
    return render(request, "vote/select_constituency.html", context)


def constituency_chosen(request):
    try:
        selected_constituency = Constituency.objects.get(id=request.GET['constituency'])
    except (ValueError):
        return render(request, 'vote/select_constituency.html', {
            'error_message': "You didn't select a constituency.",
            'constituencies': Constituency.objects.all()
        })
    return HttpResponseRedirect(reverse('results_by_constituency', args=(selected_constituency.id,)))


def results_by_constituency(request, constituency_id):
    constituency = get_object_or_404(Constituency, pk=constituency_id)
    yes_votes = Response.objects.filter(
        constituency=constituency_id,
        will_you_vote=True
    ).count()
    no_votes = Response.objects.filter(
        constituency=constituency_id,
        will_you_vote=False
    ).count()
    parties = Party.objects.all()
    all_party_votes = []
    for party in parties:
        party_votes = {}
        party_votes['party'] = party.party_name
        party_votes['votes'] = Response.objects.filter(constituency=constituency_id, party=party).count()
        all_party_votes.append(party_votes)
    context = {
        'yes_votes': yes_votes,
        'no_votes': no_votes,
        'all_party_votes': all_party_votes,
        'constituency': constituency.constituency_name
    }
    return render(request, "vote/results.html", context)
