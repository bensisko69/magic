from django.contrib import admin

from .models import *

class CardUAdmin(admin.ModelAdmin):
	list_display = ('id', 'cardName', 'rarity', 'cmc', 'power')
	list_display_links = ('id', 'rarity')
	list_filter = ('cmc', 'rarity')

class SuperTypesAdmin(admin.ModelAdmin):
	list_display = ('id', 'supertype')

class ColorAdmin(admin.ModelAdmin):
	list_display = ('id', 'color', 'colorIdentity')

class SubTypesAdmin(admin.ModelAdmin):
	list_display = ('id', 'subtype')

class typeAdmin(admin.ModelAdmin):
	list_display = ('id', 'type')

class CardTraductionAdmin(admin.ModelAdmin):
	list_display = ('id', 'language')
	
class DeckAdmin(admin.ModelAdmin):
	list_display = ('id', 'deckName')

admin.site.register(CardU, CardUAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(SubTypes, SubTypesAdmin)
admin.site.register(SuperTypes, SuperTypesAdmin)
admin.site.register(Types, typeAdmin)
admin.site.register(CardTraduction, CardTraductionAdmin)
admin.site.register(Deck, DeckAdmin)