from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q
from django.http import HttpResponse, Http404
import json

from .models import Product
from favorite.models import Favorite


class Index(TemplateView):
    """
    This view is used for generating the index page.
    """
    template_name = 'index.html'


class Contact(TemplateView):
    """
    This view is used for generating the contact page.
    """
    template_name = 'contact.html'


class LegalNotice(TemplateView):
    """
    This view is used for generating the legal notice page.
    """
    template_name = 'legal-notice.html'


class AlternativeProducts(ListView):
    """
    This view lists alternative products to a desired product.
    Alternative products have a better nutritional score.
    The nutritional score of an alternative product is a, b or c.
    In the context of this view we have 3 objects:
        1- products_alt : list of alternative products
        2- search_product : product searched
        3- search_product_img_url : image of the product searched
    """

    model = Product
    context_object_name = "products_alt"
    template_name = "products-alt.html"

    def get_queryset(self):
        if self.request.method == 'GET' and 'product' in self.request.GET:
            product_name = self.request.GET['product']

            if product_name:
                user = self.request.user

                # case insensitive __iexact
                if self.product_exist(product_name):
                    cat_id = [p.category_id for p in Product.objects.filter(name__iexact=product_name)][0]
                    if user.is_authenticated:
                        # Returns products that are not saved in the user's favorites.
                        favorite = Favorite.objects.only('code').filter(user=user).values('code')
                        return Product.objects.exclude(code__in=favorite).filter(Q(category=cat_id) &
                                                                                 Q(nutrition_grade__in="abc")
                                                                                 ).order_by('nutrition_grade')[:6]
                    else:
                        return Product.objects.filter(Q(category=cat_id) &
                                                      Q(nutrition_grade__in="abc")).order_by('nutrition_grade')[:6]
                else:
                    return None
            else:
                raise Http404
        else:
            raise Http404

    def get_context_data(self, **kwargs):
        search_product = self.request.GET['product']
        context = super(AlternativeProducts, self).get_context_data(**kwargs)
        context['search_product'] = search_product.capitalize()
        if self.product_exist(search_product):
            product_full_img_url = [p.image_full_product_url
                                    for p in Product.objects.filter(name__iexact=search_product)][0]
            context['search_product_img_url'] = product_full_img_url

        return context

    @staticmethod
    def product_exist(product_name):
        """
        This method checks if a product exists in the database.
        :param product_name: product searched
        :type product_name: str
        :return: True if product exist, False when products does not exist
        :rtype: bool
        """

        product = Product.objects.filter(name__iexact=product_name)
        if product:
            return True
        else:
            return False


class ProductDetail(DetailView):
    """
    This view is used to see the detail of a product.
    We use the barcode of the product to access its detail.
    """
    context_object_name = "product"
    model = Product
    template_name = "product_details.html"


def get_products(request):
    """
    This function is used for the auto-completion of the search field.
    This function interacts with an AJAX script.
    :param request:
    :return: The list of products corresponding to the user input
    :rtype: HttpResponse JSON
    """
    if request.is_ajax():
        product_name = request.GET.get('term', '')
        all_products = Product.objects.filter(nutrition_grade__in="de").distinct('name')
        products = all_products.filter(name__icontains=product_name)
        results = []
        for prod in products:
            results.append(prod.name)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
