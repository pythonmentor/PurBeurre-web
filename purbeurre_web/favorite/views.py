from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views.generic import ListView

from core.models import Category, Product
from .models import Favorite


@login_required(login_url='login')
def save_favorite(request):
    """
    This function is used to register a product in the Favorite table.
    The user must be logged in to register a product.
    This function interacts with an AJAX script.
    """
    product_code = request.POST['product_code']
    product_selected = Product.objects.get(code=product_code)

    name_substitute_for = request.POST['product_sub_for']
    code_substitute_for = [p.code for p in Product.objects.filter(name__iexact=name_substitute_for)][0]

    user = request.user

    Favorite(name=product_selected.name,
             code=product_selected.code,
             nutrition_grade=product_selected.nutrition_grade,
             code_substitute_for=code_substitute_for,
             name_substitute_for=name_substitute_for,
             url=product_selected.url,
             category=product_selected.category,
             user=user).save()

    response_data = {
        'status': 'ok'
    }
    return JsonResponse(response_data)


@method_decorator(login_required, name='dispatch')
class FavoriteList(ListView):
    """
    This view retrieves the user's registered products
    and displays them using the template favorite-list.html.
    The user must be logged in to access his registered products.
    """
    model = Favorite
    context_object_name = "favorite_list"
    template_name = "favorite-list.html"

    def get_queryset(self):
        user = self.request.user
        return Favorite.objects.filter(user=user).order_by('nutrition_grade')
