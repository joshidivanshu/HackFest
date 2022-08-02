from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib import messages
from django.views import View
from .models import Artist
import requests
import time

# Create your views here.
class GetArtistList(View):
    def get(self, request):
        artists_list = Artist.objects.all()
        return render(request, 'music/artist.html',{'artists':artists_list,})


class ArtistDetail(View):
    def get(self, request, artist_id):
        artist = Artist.objects.get(id=artist_id)
        print(artist)

        related_artist_url =  "https://spotify-scraper.p.rapidapi.com/v1/artist/related"
        querystring = {"artistId":artist_id}
        headers = {
	        "X-RapidAPI-Key": "8f134e4a72msh5b93c5b1eacac5ap1334cdjsnff86f9e7d77b",
	        "X-RapidAPI-Host": "spotify-scraper.p.rapidapi.com"
        }
        related_artist_response = requests.request("GET", related_artist_url , headers=headers, params=querystring).json()

        print("related artists response")
        print(related_artist_response)

        time.sleep(1)

        artist_album_url = "https://spotify-scraper.p.rapidapi.com/v1/artist/albums"

        querystring = {"artistId":artist_id}


        artist_album_response = requests.request("GET", artist_album_url, headers=headers, params=querystring).json()

        time.sleep(1)

        artist_details_url = "https://spotify-scraper.p.rapidapi.com/v1/artist/overview"

        querystring = {"artistId":artist_id}

        artist_details_response = requests.request("GET", artist_details_url, headers=headers, params=querystring).json()

        print("artist details")
        print(artist_details_response)

        return render(request, 'music/artist_details.html',{"related_artist_response": related_artist_response, "artist_album_reponse": artist_album_response, "artist_details_response": artist_details_response})



class Concerts(View):
    def get(self, request, artist_id):


        artist_concert_url = "https://spotify-scraper.p.rapidapi.com/v1/artist/concerts"

        querystring = {"artistId":artist_id}

        headers = {
            "X-RapidAPI-Key": "8f134e4a72msh5b93c5b1eacac5ap1334cdjsnff86f9e7d77b",
            "X-RapidAPI-Host": "spotify-scraper.p.rapidapi.com"
        }

        artist_concert_response = requests.request("GET", artist_concert_url, headers=headers, params=querystring).json()

        print("artist_concert_details")
        print(artist_concert_response)

        return render(request, 'music/Concerts.html', {"concerts": artist_concert_response })
