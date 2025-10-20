import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def home(request):
    random_place = None
    random_place_index = None

    if not request.session.session_key:
        request.session.create()

    places = request.session.get('places', [])

    if request.GET.get('random') == 'true':
        if places:
            weights = [p['rating'] for p in places]
            random_place_index = random.choices(range(len(places)), weights=weights, k=1)[0]
            random_place = places[random_place_index]
        else:
            messages.info(request, 'You don’t have any places added yet. Add your first one!')

    return render(request, 'PlaceApp/home.html', {
        'random_place': random_place,
        'random_place_index': random_place_index
    })

def place_list(request):
    if not request.session.session_key:
        request.session.create()

    places = request.session.get('places', [])
    places_with_index = [{'index': i, **p} for i, p in enumerate(places)]
    return render(request, 'PlaceApp/place_list.html', {'places': places_with_index})


def place_detail(request, index):
    places = request.session.get('places', [])
    if index < 0 or index >= len(places):
        from django.http import Http404
        raise Http404("Place not found")
    place = places[index]
    return render(request, 'PlaceApp/place_detail.html', {'place': place})


def add_place(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()
        place_type = request.POST.get('place_type', '').strip() or "Another"
        location = request.POST.get('location', '').strip() or "Secret place👀"
        try:
            rating = int(request.POST.get('rating', 1))
            if rating < 1 or rating > 5:
                raise ValueError
        except ValueError:
            messages.error(request, "Rating must be an integer from 1 to 5")
            return redirect('add_place')

        place = {
            'name': name,
            'description': description,
            'place_type': place_type,
            'location': location,
            'rating': rating,
            'created_at': str(request.session.get('datetime', 'Today'))
        }

        if 'places' not in request.session:
            request.session['places'] = []
        request.session['places'].append(place)
        request.session.modified = True

        messages.success(request, 'Place added!')
        return redirect('place_list')

    return render(request, 'PlaceApp/place_form.html')





