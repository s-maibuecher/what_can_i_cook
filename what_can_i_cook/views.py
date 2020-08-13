from django.db.models import Count, F, Case, When, IntegerField
from django.views.generic import ListView
from django.views.generic.edit import FormView

from what_can_i_cook.forms.ings_select_form import ChooseIngForm
from what_can_i_cook.models import Recipe, Ingredient


class WCICFilterView(FormView):
    template_name = "pages/wcic-start.html"

    form_class = ChooseIngForm


class WCICResultView(ListView):
    template_name = "pages/wcic-results.html"

    model = Recipe

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        context['no_of_submitted_ings'] = len(self.request.GET.getlist('ing_form'))

        # todo: dann nur noch oben content anreichern mit infos: wenn du dir noch x zutaten vom nachbarn leihst, dann
        #   kann du diesen vorschlag kochen

        return context

    def get_queryset(self):
        # URL query strings with Ingredient Ids:
        _ing_id_list = self.request.GET.getlist('ing_form')

        # build Queryset:
        # ing_queryset = Ingredient.objects.filter(id__in=_ing_id_list)

        annotated_recipe_queryset = Recipe.valuable_recipes.annotate(
            no_of_common_ings=Count(Case(When(
                ingredients__id__in=_ing_id_list, then=1), output_field=IntegerField(), )))

        return annotated_recipe_queryset.order_by('-no_of_common_ings', 'ing_counter')[:3]
