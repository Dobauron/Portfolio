from django.shortcuts import render

# Create your views here.
def travel_view(request):
    if request.method == 'POST':
        player_form = PlayerForm(data=request.POST)
        if player_form.is_valid():
            player = player_form.save(commit=False)
            player.save()
            return render(request,
                          'creation_hero_done.html',
                          )

    else:
        player_form = PlayerForm()
    return render(request,
                  'creation_hero.html',
                  {'player_form': player_form, })
