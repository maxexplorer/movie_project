from django.contrib import admin
from .models import Movie, Director
from django.db.models import QuerySet

# Register your models here.

admin.site.register(Director)


class RatingFilter(admin.SimpleListFilter):
    title = 'Rating filter'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<50', 'Low'),
            ('от 50 до 69', 'Middle'),
            ('>=70', 'High')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<50':
            return queryset.filter(rating__lt=50)
        if self.value() == 'от 50 до 69':
            return queryset.filter(rating__gte=50).filter(rating__lt=70)
        if self.value() == '>=70':
            return queryset.filter(rating__gte=70)
        return queryset


@admin.register(Movie)  # admin.site.register(Movie, MovieAdmin)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'director', 'rating_status', 'recommend']
    list_editable = ['rating', 'year', 'director', 'recommend']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['-rating']
    list_per_page = 10
    actions = ['set_value', 'set_yes', 'set_no']
    search_fields = ['name']
    list_filter = ['name', 'recommend', RatingFilter]

    @admin.display(ordering='rating', description='Status')
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return f'Low'
        if movie.rating < 80:
            return f'Middle'
        return f'High'

    @admin.action(description='YES')
    def set_yes(self, request, qs: QuerySet):
        count_updated = qs.update(recommend=Movie.YES)
        self.message_user(
            request,
            f'Updated {count_updated} notes'
        )

    @admin.action(description='NO')
    def set_no(self, request, qs: QuerySet):
        count_updated = qs.update(recommend=Movie.NO)
        self.message_user(
            request,
            f'Updated {count_updated} notes'
        )
