from django.shortcuts import render
import json
from mtgsdk import Card, Supertype, Subtype, Type
from pprint import pprint
import sys
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from .models import *
from django.core import serializers
from django.contrib.auth.models import User

@csrf_exempt

def index(request):
	return render(request, 'app/index.html', {})

@login_required(login_url='loginUser')
def createDecks(request):
	current_user = request.user
	if request.POST:
		deck = Deck()
		deck.deckName = request.POST.get('nameDeck')
		deck.userId = current_user.id
		deck.save()
		return JsonResponse('success', status=200, safe=False)
	return JsonResponse('error', status=500, safe=False)
	return render(request, 'app/decks.html', {})

@login_required(login_url='loginUser')
def decks(request):
	currentUserId = request.user.id
	decks = Deck.objects.filter(userId=currentUserId)
	return render(request, 'app/decks.html', {'decks' : decks, 'currentUserId' : currentUserId})

def search(request):
	Colors = Color.objects.all()
	tab = []
	for color in Colors:
		tab.append(color.color)

	T = Types.objects.all()
	typeTab = []
	for type in T:
		typeTab.append(type.type)
	return render(request, 'app/search.html', {'dump':tab, 'type':typeTab})	

def resultCard(request):
	if request.POST:
		rarity = request.POST.get('rarity')
		name = request.POST.get('name')
		cmc = request.POST.get('cmc')
		results = CardU.objects.filter(rarity=rarity, cmc=cmc)
		"""resultsName = CardU.objects.filter(cardName=name)"""
		return JsonResponse(serializers.serialize('json', results), status=200, safe=False)
	return JsonResponse('error',status=500, safe=False)

def addCard(request):
	post = request.POST['id']
	return JsonResponse('success',status=200, safe=False)

def loginPage(request):
	return render(request, 'app/login.html', {})

def loginUser(request):
	if request.POST.get('username') and request.POST.get('password'):
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return JsonResponse('success', status=200, safe=False)
		else:
			return JsonResponse('noUser', status=200, safe=False)
	else:
		return JsonResponse('empty', status=400, safe=False)

def logoutUser(request):
	logout(request)
	return render(request, 'app/index.html', {})

@login_required(login_url='login')
def importCard(request):
	supertypes = Supertype.all()
	for supertypes in supertypes:
		types = SuperTypes()
		types.supertype = supertypes
		types.save()
	subtypes = Subtype.all()
	for subtype in subtypes:
		sub = SubTypes()
		sub.subtype = subtype
		sub.save()
	types = Type.all()
	for type in types:
		t = Types()
		t.type = type
		t.save()
	color1 = Color()
	color1.color ="White"
	color1.colorIdentity = "W"
	color1.save()
	color2 = Color()
	color2.color = "Red"
	color2.colorIdentity = "R"
	color2.save()
	color3 = Color()
	color3.color = "Green"
	color3.colorIdentity = "G"
	color3.save()
	color4 = Color()
	color4.color = "Black"
	color4.colorIdentity = "B"
	color4.save()
	color = Color()
	color.color = "Uncolor"
	color.colorIdentity = "U"
	color.save()
	color.color = "Blue"
	color.colorIdentity = "B"
	color.save()
	i = 0
	while i <= 0:
		cards = Card.where(page=i).where(pageSize=300).all()
		if len(cards) > 0:
			for card in cards:
				c = CardU()
				c.cardName = card.name
				c.cmc = card.cmc
				c.type = card.type
				c.rarity = card.rarity
				c.text = card.text
				c.number = card.number
				if hasattr(card, 'manaCost'):
					c.mana = card.manaCost
				if card.colors:
					identity = card.colors[0]
					colors = Color.objects.filter(color=identity).values()
				c.power = card.power
				if hasattr(card, 'multiverseid'):
						c.multiverseid = card.multiverseid
				if hasattr(card, 'foreignNames'):
					for translate in card.foreignnames:
						if translate.language == "French":
							frenchTrad = CardTraduction()
							frenchTrad.imageUrl = translate.imageUrl
							frenchTrad.language = "French"
							frenchTrad.text = translate.text
							frenchTrad.cardId = translate.multiverseid
							frenchTrad.save()
							c.traduction = frenchTrad.id
				c.save()
			i += 1
		else:
			i = 1
	return render(request, 'app/search.html', {"len": len(cards)})

		
