import tkinter
import pandas as pd
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import customtkinter
import webview
from CTkMessagebox import CTkMessagebox


"""from tkinter import ttk
from tkinter import *
from tkinter import Tk"""

# Aksiyon filmleri dosyasının yolu
aksiyon_film_yolu = "C:/Users/Talha/Desktop/Excel Film Data/aksiyon_filmleri.csv"

# Macera filmleri dosyasının yolu
macera_film_yolu = "C:/Users/Talha/Desktop/Excel Film Data/macera_filmleri.csv"

# animasyon filmleri dosyasının yolu
animasyon_film_yolu = "C:/Users/Talha/Desktop/Excel Film Data/animasyon_filmleri.csv"

# biyografi filmleri dosyasının yolu
biyografi_film_yolu = "C:/Users/Talha/Desktop/Excel Film Data/biyografi_filmleri.csv"

# Komedi filmleri dosyasının yolu
komedi_film_yolu = "C:/Users/Talha/Desktop/Excel Film Data/komedi_filmleri.csv"

# Suç filmleri dosyasının yolu
suc_film_yolu = "C:/Users/Talha/Desktop/Excel Film Data/suc_filmleri.csv"

# Dram filmleri dosyasının yolu
dram_film_yolu = "C:/Users/Talha/Desktop/Excel Film Data/dram_filmleri.csv"

# Aile filmleri dosyasının yolu
aile_film_yolu = "C:/Users/Talha/Desktop/Excel Film Data/aile_filmleri.csv"

# Fantezi filmleri dosyasının yolu
fantezi_film_yolu = "C:/Users/Talha/Desktop/Excel Film Data/fantezi_filmleri.csv"

# Western filmleri dosyasının yolu
western_film_yolu = "C:/Users/Talha/Desktop/Excel Film Data/western_filmleri.csv"

# Korku filmleri dosyasının yolu
horror_film_yolu = "C:/Users/Talha/Desktop/Excel Film Data/horror_filmleri.csv"

# Tarih filmleri dosyasının yolu
history_film_yolu = "C:/Users/Talha/Desktop/Excel Film Data/history_filmleri.csv"

# Music filmleri dosyasının yolu
music_film_yolu = "C:/Users/Talha/Desktop/Excel Film Data/music_filmleri.csv"

# Musical filmleri dosyasının yolu
musical_film_yolu = "C:/Users/Talha/Desktop/Excel Film Data/musical_filmleri.csv"

# Gizem filmleri dosyasının yolu
mystery_film_yolu = "C:/Users/Talha/Desktop/Excel Film Data/mystery_filmleri.csv"

# Romantik filmleri dosyasının yolu
romance_film_yolu = "C:/Users/Talha/Desktop/Excel Film Data/romance_filmleri.csv"

# Bilim Kurgu filmleri dosyasının yolu
scifi_film_yolu = "C:/Users/Talha/Desktop/Excel Film Data/scifi_filmleri.csv"

# Spor filmleri dosyasının yolu
sport_film_yolu = "C:/Users/Talha/Desktop/Excel Film Data/sport_filmleri.csv"

# Gerilim filmleri dosyasının yolu
thriller_film_yolu = "C:/Users/Talha/Desktop/Excel Film Data/thriller_filmleri.csv"

# Savaş filmleri dosyasının yolu
war_film_yolu = "C:/Users/Talha/Desktop/Excel Film Data/war_filmleri.csv"




#film tarihlerindeki () işaretlerini siliyor
def dele(x):
    new = x.replace("(", "")
    new2 = new.replace(")", "")

    return new2

# Aksiyon filmleri veri seti
aksiyon_film = pd.read_csv(aksiyon_film_yolu)
aksiyon_film["1"] = aksiyon_film["1"].apply(dele)
# Macera filmleri veri seti
macera_film = pd.read_csv(macera_film_yolu)
macera_film["1"] = macera_film["1"].apply(dele)
# Aksiyon filmleri veri seti
animasyon_film=pd.read_csv(animasyon_film_yolu)
animasyon_film["1"] = animasyon_film["1"].apply(dele)
# Biyografi filmleri veri seti
biyografi_film=pd.read_csv(biyografi_film_yolu)
biyografi_film["1"] = biyografi_film["1"].apply(dele)
# Komedi filmleri veri seti
komedi_film=pd.read_csv(komedi_film_yolu)
komedi_film["1"] = komedi_film["1"].apply(dele)
# Suç filmleri veri seti
suc_film=pd.read_csv(suc_film_yolu)
suc_film["1"] = suc_film["1"].apply(dele)
# Dram filmleri veri seti
dram_film=pd.read_csv(dram_film_yolu)
dram_film["1"] = dram_film["1"].apply(dele)
# Aile filmleri veri seti
aile_film=pd.read_csv(aile_film_yolu)
aile_film["1"] = aile_film["1"].apply(dele)
# Fantezi filmleri veri seti
fantezi_film=pd.read_csv(fantezi_film_yolu)
fantezi_film["1"] = fantezi_film["1"].apply(dele)
# Western filmleri veri seti
western_film=pd.read_csv(western_film_yolu)
western_film["1"] = western_film["1"].apply(dele)
# Korku filmleri veri seti
horror_film=pd.read_csv(horror_film_yolu)
horror_film["1"] = horror_film["1"].apply(dele)
# Tarih filmleri veri seti
history_film=pd.read_csv(history_film_yolu)
history_film["1"] = history_film["1"].apply(dele)
# Music filmleri veri seti
music_film=pd.read_csv(music_film_yolu)
music_film["1"] = music_film["1"].apply(dele)
# Musical filmleri veri seti
musical_film=pd.read_csv(musical_film_yolu)
musical_film["1"] = musical_film["1"].apply(dele)
# Gizem filmleri veri seti
mystery_film=pd.read_csv(mystery_film_yolu)
mystery_film["1"] = mystery_film["1"].apply(dele)
# Gizem filmleri veri seti
romance_film=pd.read_csv(romance_film_yolu)
romance_film["1"] = romance_film["1"].apply(dele)
# Bilim Kurgu filmleri veri seti
scifi_film=pd.read_csv(scifi_film_yolu)
scifi_film["1"] = scifi_film["1"].apply(dele)
# Spor filmleri veri seti
sport_film=pd.read_csv(sport_film_yolu)
sport_film["1"] = sport_film["1"].apply(dele)
# Gerilim filmleri veri seti
thriller_film=pd.read_csv(thriller_film_yolu)
thriller_film["1"] = thriller_film["1"].apply(dele)
# Savaş filmleri veri seti
war_film=pd.read_csv(war_film_yolu)
war_film["1"] = war_film["1"].apply(dele)


# Pencere oluşturma
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
pencere = customtkinter.CTk()
pencere.title("Movie Recommendation")
pencere.geometry("1920x1280")

# Önerilen filmin bir daha çıkmasını engellemek için
# önerilen filmler listelere eklenir
aksiyon_film_onerilen = []
macera_film_onerilen = []
animasyon_film_onerilen = []
biyografi_film_onerilen = []
komedi_film_onerilen = []
suc_film_onerilen = []
dram_film_onerilen = []
aile_film_onerilen = []
fantezi_film_onerilen = []
western_film_onerilen=  []
horror_film_onerilen=   []
history_film_onerilen=  []
music_film_onerilen=    []
musical_film_onerilen=  []
mystery_film_onerilen=  []
romance_film_onerilen=  []
scifi_film_onerilen=[]
sport_film_onerilen=   []
thriller_film_onerilen= []
war_film_onerilen=  []

film_ismi = []



def default_button_color():

    aksiyon_buton.configure(fg_color="black")
    macera_buton.configure(fg_color="black")
    animasyon_buton.configure(fg_color="black")
    biyografi_buton.configure(fg_color="black")
    komedi_buton.configure(fg_color="black")
    suc_buton.configure(fg_color="black")
    dram_buton.configure(fg_color="black")
    aile_buton.configure(fg_color="black")
    fantezi_buton.configure(fg_color="black")
    western_button.configure(fg_color="black")
    history_button.configure(fg_color="black")
    horror_button.configure(fg_color="black")
    music_button.configure(fg_color   ="black")
    musical_button.configure(fg_color="black")
    mystery_button.configure(fg_color="black")
    romance_button.configure(fg_color="black")
    scifi_button.configure(fg_color="black")
    sport_button.configure(fg_color="black")
    thriller_button.configure(fg_color="black")
    war_button.configure(fg_color="black")



def aksiyon():
    film_ismi.clear()
    default_button_color()
    aksiyon_buton.configure(fg_color="purple")
    global aksiyon_film_onerilen
    print(aksiyon_film_onerilen)
    # Rastgele bir Aksiyon filmi önerisi al
    random_ = random.randint(0, aksiyon_film.shape[0]-1)
    while random_ in aksiyon_film_onerilen:
        random_ = random.randint(0, aksiyon_film.shape[0] - 1)
    row = aksiyon_film.loc[random_]
    aksiyon_film_onerilen.append(random_)
    print(random_)
    # Film önerisini ekrana yazdır
    sonuc_yazi.configure(text="Title: {}\nRelease Year: {}\nAge Rating: {}\nDuration: {}\nGenres: {}\nIMDb Rating: {}".format(row[1],row[2],row[3],row[4],row[5],row[6]))
    sonuc_yazi2.configure(text="--Storyline--" + row[7], wraplength=600)
    film_ismi.clear()
    film_ismi.append((row[1], row[2]))
    film_ismi_str = str(film_ismi[0][0]) + " " + str(film_ismi[0][1])
    film_ismi.clear()
    film_ismi.append(film_ismi_str)
    print(film_ismi)
    if len(aksiyon_film_onerilen) == aksiyon_film.shape[0]:
        aksiyon_film_onerilen.clear()
    alt_frame.pack(side="bottom", fill="x")
    cast_button.pack(padx=10, pady=10, side="top")
    youtube_button.pack(padx=10, pady=10, side="top")
    image_button.pack(padx=10, pady=10, side="top")
    fav_button.pack(padx=10, pady=10, side="top")
def macera():
    # Rastgele bir Macera filmi önerisi al
    default_button_color()
    macera_buton.configure(fg_color="purple")
    global macera_film_onerilen
    random_ = random.randint(0, macera_film.shape[0]-1)
    while random_ in macera_film_onerilen:
        random_ = random.randint(0, macera_film.shape[0] - 1)
    row = macera_film.loc[random_]
    macera_film_onerilen.append(random_)
    print(macera_film_onerilen)

    # Film önerisini ekrana yazdır
    sonuc_yazi.configure(text="Title: {}\nRelease Year: {}\nAge Rating: {}\nDuration: {}\nGenres: {}\nIMDb Rating: {}".format(row[1],row[2],row[3],row[4],row[5],row[6]))
    sonuc_yazi2.configure(text="--Storyline--" + row[7] ,wraplength=600)
    film_ismi.clear()
    film_ismi.append((row[1], row[2]))
    film_ismi_str = str(film_ismi[0][0]) + " " + str(film_ismi[0][1])
    film_ismi.clear()
    film_ismi.append(film_ismi_str)
    print(film_ismi)
    alt_frame.pack(side="bottom",fill="x")
    cast_button.pack(padx=10,pady=10,side="top")
    youtube_button.pack(padx=10,pady=10,side="top")
    image_button.pack(padx=10,pady=10,side="top")
    fav_button.pack(padx=10,pady=10,side="top")
    if len(macera_film_onerilen) == macera_film.shape[0]:
        macera_film_onerilen.clear()
def animasyon():
    # Rastgele bir animasyon filmi önerisi al
    default_button_color()
    animasyon_buton.configure(fg_color="purple")

    global animasyon_film_onerilen
    random_ = random.randint(0, animasyon_film.shape[0] - 1)
    while random_ in animasyon_film_onerilen:
        random_ = random.randint(0, animasyon_film.shape[0] - 1)
    row = animasyon_film.loc[random_]
    animasyon_film_onerilen.append(random_)
    sonuc_yazi.configure(
        text="Title: {}\nRelease Year: {}\nAge Rating: {}\nDuration: {}\nGenres: {}\nIMDb Rating: {}".format(row[1],row[2],row[3],row[4],row[5],row[6]))
    sonuc_yazi2.configure(text="--Storyline--" + row[7],  wraplength=600)
    film_ismi.clear()
    film_ismi.append((row[1], row[2]))
    film_ismi_str = str(film_ismi[0][0]) + " " + str(film_ismi[0][1])
    film_ismi.clear()
    film_ismi.append(film_ismi_str)
    print(film_ismi)
    alt_frame.pack(side="bottom",fill="x")

    cast_button.pack(padx=10,pady=10,side="top")
    youtube_button.pack(padx=10,pady=10,side="top")
    image_button.pack(padx=10,pady=10,side="top")
    fav_button.pack(padx=10,pady=10,side="top")
    if len(animasyon_film_onerilen) == animasyon_film.shape[0]:
        animasyon_film_onerilen.clear()
def biyografi():
    # Rastgele bir biyografi filmi önerisi al
    default_button_color()
    biyografi_buton.configure(fg_color="purple")

    global biyografi_film_onerilen
    random_ = random.randint(0, biyografi_film.shape[0] - 1)
    while random_ in biyografi_film_onerilen:
        random_ = random.randint(0, biyografi_film.shape[0] - 1)
    row = biyografi_film.loc[random_]
    biyografi_film_onerilen.append(random_)

    sonuc_yazi.configure(
        text="Title: {}\nRelease Year: {}\nAge Rating: {}\nDuration: {}\nGenres: {}\nIMDb Rating: {}".format(row[1],row[2],row[3],row[4],row[5],row[6]))
    sonuc_yazi2.configure(text="--Storyline--" + row[7] ,wraplength=600)
    film_ismi.clear()
    film_ismi.append((row[1], row[2]))
    film_ismi_str = str(film_ismi[0][0]) + " " + str(film_ismi[0][1])
    film_ismi.clear()
    film_ismi.append(film_ismi_str)
    print(film_ismi)
    alt_frame.pack(side="bottom",fill="x")
    cast_button.pack(padx=10,pady=10,side="top")
    youtube_button.pack(padx=10,pady=10,side="top")
    image_button.pack(padx=10,pady=10,side="top")
    fav_button.pack(padx=10,pady=10,side="top")
    if len(biyografi_film_onerilen) == biyografi_film.shape[0]:
        biyografi_film_onerilen.clear()
def komedi():
    # Rastgele bir komedi filmi önerisi al
    default_button_color()
    komedi_buton.configure(fg_color="purple")
    global komedi_film_onerilen
    random_ = random.randint(0, komedi_film.shape[0] - 1)
    while random_ in komedi_film_onerilen:
        random_ = random.randint(0, komedi_film.shape[0] - 1)
    row = komedi_film.loc[random_]
    komedi_film_onerilen.append(random_)

    sonuc_yazi.configure(
        text="Title: {}\nRelease Year: {}\nAge Rating: {}\nDuration: {}\nGenres: {}\nIMDb Rating: {}".format(row[1],row[2],row[3],row[4],row[5],row[6]))
    sonuc_yazi2.configure(text="--Storyline--" + row[7], wraplength=600)

    film_ismi.clear()
    film_ismi.append((row[1], row[2]))
    film_ismi_str = str(film_ismi[0][0]) + " " + str(film_ismi[0][1])
    film_ismi.clear()
    film_ismi.append(film_ismi_str)
    print(film_ismi)
    alt_frame.pack(side="bottom",fill="x")
    cast_button.pack(padx=10,pady=10,side="top")
    youtube_button.pack(padx=10,pady=10,side="top")
    image_button.pack(padx=10,pady=10,side="top")
    fav_button.pack(padx=10,pady=10,side="top")
    if len(komedi_film_onerilen) == komedi_film.shape[0]:
        komedi_film_onerilen.clear()

def suc():
    # Rastgele bir suc filmi önerisi al
    default_button_color()
    suc_buton.configure(fg_color="purple")
    global suc_film_onerilen
    random_ = random.randint(0, suc_film.shape[0] - 1)
    while random_ in suc_film_onerilen:
        random_ = random.randint(0, suc_film.shape[0] - 1)
    row = suc_film.loc[random_]
    suc_film_onerilen.append(random_)
    sonuc_yazi.configure(
    text="Title: {}\nRelease Year: {}\nAge Rating: {}\nDuration: {}\nGenres: {}\nIMDb Rating: {}".format(row[1],row[2], row[3],row[4],row[5],row[6]))
    sonuc_yazi2.configure(text="--Storyline--" + row[7], wraplength=600)
    film_ismi.clear()
    film_ismi.append((row[1], row[2]))
    film_ismi_str = str(film_ismi[0][0]) + " " + str(film_ismi[0][1])
    film_ismi.clear()
    film_ismi.append(film_ismi_str)
    print(film_ismi)
    alt_frame.pack(side="bottom",fill="x")
    cast_button.pack(padx=10,pady=10,side="top")
    youtube_button.pack(padx=10,pady=10,side="top")
    image_button.pack(padx=10,pady=10,side="top")
    fav_button.pack(padx=10,pady=10,side="top")

    if len(suc_film_onerilen) == suc_film.shape[0]:
        suc_film_onerilen.clear()

def dram():
    # Rastgele bir dram filmi önerisi al
    default_button_color()
    dram_buton.configure(fg_color="purple")
    global dram_film_onerilen
    random_ = random.randint(0, dram_film.shape[0] - 1)
    while random_ in dram_film_onerilen:
        random_ = random.randint(0, dram_film.shape[0] - 1)
    row = dram_film.loc[random_]
    dram_film_onerilen.append(random_)

    sonuc_yazi.configure(
        text="Title: {}\nRelease Year: {}\nAge Rating: {}\nDuration: {}\nGenres: {}\nIMDb Rating: {}".format(row[1],row[2],row[3],row[4],row[5],row[6]))

    sonuc_yazi2.configure(text="--Storyline--" + row[7], wraplength=600)
    film_ismi.clear()
    film_ismi.append((row[1], row[2]))
    film_ismi_str = str(film_ismi[0][0]) + " " + str(film_ismi[0][1])
    film_ismi.clear()
    film_ismi.append(film_ismi_str)
    print(film_ismi)
    alt_frame.pack(side="bottom",fill="x")
    cast_button.pack(padx=10,pady=10,side="top")
    youtube_button.pack(padx=10,pady=10,side="top")
    image_button.pack(padx=10,pady=10,side="top")
    fav_button.pack(padx=10,pady=10,side="top")
    if len(dram_film_onerilen) == dram_film.shape[0]:
        dram_film_onerilen.clear()
def aile():
    default_button_color()
    aile_buton.configure(fg_color="purple")
    global aile_film_onerilen
    random_ = random.randint(0, aile_film.shape[0] - 1)
    while random_ in aile_film_onerilen:
        random_ = random.randint(0, aile_film.shape[0] - 1)

    row = aile_film.loc[random_]
    aile_film_onerilen.append(random_)

    sonuc_yazi.configure(
        text="Title: {}\nRelease Year: {}\nAge Rating: {}\nDuration: {}\nGenres: {}\nIMDb Rating: {}".format(row[1],row[2],row[3],row[4],row[5],row[6]))

    sonuc_yazi2.configure(text="--Storyline--" + row[7], wraplength=600)
    film_ismi.clear()
    film_ismi.append((row[1], row[2]))
    film_ismi_str = str(film_ismi[0][0]) + " " + str(film_ismi[0][1])
    film_ismi.clear()
    film_ismi.append(film_ismi_str)
    print(film_ismi)
    alt_frame.pack(side="bottom",fill="x")
    cast_button.pack(padx=10,pady=10,side="top")
    youtube_button.pack(padx=10,pady=10,side="top")
    image_button.pack(padx=10,pady=10,side="top")
    fav_button.pack(padx=10,pady=10,side="top")
    if len(aile_film_onerilen) == aile_film.shape[0]:
        aile_film_onerilen.clear()
def fantezi():
    default_button_color()
    fantezi_buton.configure(fg_color="purple")
    global fantezi_film_onerilen
    print(fantezi_film_onerilen)
    random_ = random.randint(0, fantezi_film.shape[0] - 1)
    while random_ in fantezi_film_onerilen:
        random_ = random.randint(0, fantezi_film.shape[0] - 1)

    row = fantezi_film.loc[random_]
    fantezi_film_onerilen.append(random_)

    sonuc_yazi.configure(
        text="Title: {}\nRelease Year: {}\nAge Rating: {}\nDuration: {}\nGenres: {}\nIMDb Rating: {}".format(row[1],row[2],row[3],row[4],row[5],row[6]))

    sonuc_yazi2.configure(text="--Storyline--" + row[7], wraplength=600)
    film_ismi.clear()
    film_ismi.append((row[1], row[2]))
    film_ismi_str = str(film_ismi[0][0]) + " " + str(film_ismi[0][1])
    film_ismi.clear()
    film_ismi.append(film_ismi_str)
    print(film_ismi)
    alt_frame.pack(side="bottom",fill="x")
    cast_button.pack(padx=10,pady=10,side="top")
    youtube_button.pack(padx=10,pady=10,side="top")
    image_button.pack(padx=10,pady=10,side="top")
    fav_button.pack(padx=10,pady=10,side="top")
    if len(fantezi_film_onerilen) == fantezi_film.shape[0]:
        fantezi_film_onerilen.clear()

def western():
    default_button_color()
    western_button.configure(fg_color="purple")
    global western_film_onerilen
    print(western_film_onerilen)
    random_ = random.randint(0, western_film.shape[0] - 1)
    while random_ in western_film_onerilen:
        random_ = random.randint(0, western_film.shape[0] - 1)

    row = western_film.loc[random_]
    western_film_onerilen.append(random_)
    print(random_)
    sonuc_yazi.configure(
            text="Title: {}\nRelease Year: {}\nAge Rating: {}\nDuration: {}\nGenres: {}\nIMDb Rating: {}".format(row[1],row[2],row[3],row[4],row[5],row[6]))

    sonuc_yazi2.configure( text="--Storyline--"+row[7],wraplength=600)
    film_ismi.clear()
    film_ismi.append((row[1],row[2]))
    film_ismi_str = str(film_ismi[0][0])+" "+str(film_ismi[0][1])
    film_ismi.clear()
    film_ismi.append(film_ismi_str)
    print(film_ismi)
    alt_frame.pack(side="bottom",fill="x")
    cast_button.pack(side="top",padx=10,pady=10)
    youtube_button.pack(side="top", padx=10, pady=10)
    image_button.pack(padx=10, pady=10, side="top")
    fav_button.pack(padx=10, pady=10, side="top")
    if len(western_film_onerilen)==western_film.shape[0]:
        western_film_onerilen.clear()


def history():
    default_button_color()
    history_button.configure(fg_color="purple")
    global history_film_onerilen
    print(history_film_onerilen)
    random_ = random.randint(0, history_film.shape[0] - 1)
    while random_ in history_film_onerilen:
        random_ = random.randint(0, history_film.shape[0] - 1)

    row = history_film.loc[random_]
    history_film_onerilen.append(random_)
    print(random_)
    sonuc_yazi.configure(
        text="Title: {}\nRelease Year: {}\nAge Rating: {}\nDuration: {}\nGenres: {}\nIMDb Rating: {}".format(row[1],row[2],row[3],row[4],row[5],row[6]))

    sonuc_yazi2.configure(text="--Storyline--" + row[7], wraplength=600)
    film_ismi.clear()
    film_ismi.append((row[1], row[2]))
    film_ismi_str = str(film_ismi[0][0]) + " " + str(film_ismi[0][1])
    film_ismi.clear()
    film_ismi.append(film_ismi_str)
    print(film_ismi)
    alt_frame.pack(side="bottom",fill="x")
    cast_button.pack(padx=10,pady=10,side="top")
    youtube_button.pack(padx=10,pady=10,side="top")
    image_button.pack(padx=10,pady=10,side="top")
    fav_button.pack(padx=10,pady=10,side="top")
    if len(history_film_onerilen) == history_film.shape[0]:
        history_film_onerilen.clear()

def horror():
    default_button_color()
    horror_button.configure(fg_color="purple")
    global horror_film_onerilen
    print(horror_film_onerilen)
    random_ = random.randint(0, horror_film.shape[0] - 1)
    while random_ in horror_film_onerilen:
        random_ = random.randint(0, horror_film.shape[0] - 1)
    row = horror_film.loc[random_]
    horror_film_onerilen.append(random_)
    print(random_)
    sonuc_yazi.configure(
        text="Title: {}\nRelease Year: {}\nAge Rating: {}\nDuration: {}\nGenres: {}\nIMDb Rating: {}".format(row[1],row[2],row[3],row[4],row[5],row[6]))

    sonuc_yazi2.configure(text="--Storyline--" + row[7], wraplength=600)
    film_ismi.clear()
    film_ismi.append((row[1], row[2]))
    film_ismi_str = str(film_ismi[0][0]) + " " + str(film_ismi[0][1])
    film_ismi.clear()
    film_ismi.append(film_ismi_str)
    print(film_ismi)
    alt_frame.pack(side="bottom",fill="x")
    cast_button.pack(padx=10,pady=10,side="top")
    youtube_button.pack(padx=10,pady=10,side="top")
    image_button.pack(padx=10,pady=10,side="top")
    fav_button.pack(padx=10,pady=10,side="top")
    if len(horror_film_onerilen) == horror_film.shape[0]:
        horror_film_onerilen.clear()

def music():
    default_button_color()
    music_button.configure(fg_color="purple")
    global music_film_onerilen
    print(music_film_onerilen)
    random_ = random.randint(0, music_film.shape[0] - 1)
    while random_ in music_film_onerilen:
        random_ = random.randint(0, music_film.shape[0] - 1)

    row = music_film.loc[random_]
    music_film_onerilen.append(random_)
    print(random_)
    sonuc_yazi.configure(
        text="Title: {}\nRelease Year: {}\nAge Rating: {}\nDuration: {}\nGenres: {}\nIMDb Rating: {}".format(row[1],row[2],row[3],row[4],row[5],row[6]))
    sonuc_yazi2.configure(text="--Storyline--" + row[7], wraplength=600)
    film_ismi.clear()
    film_ismi.append((row[1], row[2]))
    film_ismi_str = str(film_ismi[0][0]) + " " + str(film_ismi[0][1])
    film_ismi.clear()
    film_ismi.append(film_ismi_str)
    print(film_ismi)
    alt_frame.pack(side="bottom",fill="x")

    cast_button.pack(padx=10,pady=10,side="top")
    youtube_button.pack(padx=10,pady=10,side="top")
    image_button.pack(padx=10,pady=10,side="top")
    fav_button.pack(padx=10,pady=10,side="top")
    if len(music_film_onerilen) == music_film.shape[0]:
        music_film_onerilen.clear()


def musical():
    default_button_color()
    musical_button.configure(fg_color="purple")
    global musical_film_onerilen
    print(musical_film_onerilen)
    random_ = random.randint(0, musical_film.shape[0] - 1)
    while random_ in musical_film_onerilen:
        random_ = random.randint(0, musical_film.shape[0] - 1)
    row = musical_film.loc[random_]
    musical_film_onerilen.append(random_)
    print(random_)
    sonuc_yazi.configure(
        text="Title: {}\nRelease Year: {}\nAge Rating: {}\nDuration: {}\nGenres: {}\nIMDb Rating: {}".format(row[1],row[2],row[3],row[4],row[5],row[6]))

    sonuc_yazi2.configure(text="--Storyline--" + row[7], wraplength=600)
    film_ismi.clear()
    film_ismi.append((row[1], row[2]))
    film_ismi_str = str(film_ismi[0][0]) + " " + str(film_ismi[0][1])
    film_ismi.clear()
    film_ismi.append(film_ismi_str)
    print(film_ismi)
    alt_frame.pack(side="bottom",fill="x")
    cast_button.pack(padx=10,pady=10,side="top")
    youtube_button.pack(padx=10,pady=10,side="top")
    image_button.pack(padx=10,pady=10,side="top")
    fav_button.pack(padx=10,pady=10,side="top")
    if len(musical_film_onerilen) == musical_film.shape[0]:
        musical_film_onerilen.clear()



def mystery():
    default_button_color()
    mystery_button.configure(fg_color="purple")
    global mystery_film_onerilen
    print(mystery_film_onerilen)
    random_ = random.randint(0, mystery_film.shape[0] - 1)
    while random_ in mystery_film_onerilen:
        random_ = random.randint(0, mystery_film.shape[0] - 1)
    row = mystery_film.loc[random_]
    mystery_film_onerilen.append(random_)
    print(random_)
    sonuc_yazi.configure(
        text="Title: {}\nRelease Year: {}\nAge Rating: {}\nDuration: {}\nGenres: {}\nIMDb Rating: {}".format(row[1],row[2],row[3],row[4],row[5],row[6]))

    sonuc_yazi2.configure(text="--Storyline--" + row[7], wraplength=600)
    film_ismi.clear()
    film_ismi.append((row[1], row[2]))
    film_ismi_str = str(film_ismi[0][0]) + " " + str(film_ismi[0][1])
    film_ismi.clear()
    film_ismi.append(film_ismi_str)
    print(film_ismi)
    alt_frame.pack(side="bottom",fill="x")
    cast_button.pack(padx=10,pady=10,side="top")
    youtube_button.pack(padx=10,pady=10,side="top")
    image_button.pack(padx=10,pady=10,side="top")
    fav_button.pack(padx=10,pady=10,side="top")
    if len(mystery_film_onerilen) == mystery_film.shape[0]:
        mystery_film_onerilen.clear()


def romance():
    default_button_color()
    romance_button.configure(fg_color="purple")
    global romance_film_onerilen
    print(romance_film_onerilen)
    random_ = random.randint(0, romance_film.shape[0] - 1)
    while random_ in romance_film_onerilen:
        random_ = random.randint(0, romance_film.shape[0] - 1)
    row = romance_film.loc[random_]
    romance_film_onerilen.append(random_)
    print(random_)
    sonuc_yazi.configure(
        text="Title: {}\nRelease Year: {}\nAge Rating: {}\nDuration: {}\nGenres: {}\nIMDb Rating: {}".format(row[1],row[2],row[3],row[4],row[5],row[6]))

    sonuc_yazi2.configure(text="--Storyline--" + row[7], wraplength=600)
    film_ismi.clear()
    film_ismi.append((row[1], row[2]))
    film_ismi_str = str(film_ismi[0][0]) + " " + str(film_ismi[0][1])
    film_ismi.clear()
    film_ismi.append(film_ismi_str)
    print(film_ismi)
    alt_frame.pack(side="bottom",fill="x")
    cast_button.pack(padx=10,pady=10,side="top")
    youtube_button.pack(padx=10,pady=10,side="top")
    image_button.pack(padx=10,pady=10,side="top")
    fav_button.pack(padx=10,pady=10,side="top")
    if len(romance_film_onerilen) == romance_film.shape[0]:
        romance_film_onerilen.clear()

def scifi():
    default_button_color()
    scifi_button.configure(fg_color="purple")
    global scifi_film_onerilen
    print(scifi_film_onerilen)
    random_ = random.randint(0, scifi_film.shape[0] - 1)
    while random_ in scifi_film_onerilen:
        random_ = random.randint(0, scifi_film.shape[0] - 1)
    row = scifi_film.loc[random_]
    scifi_film_onerilen.append(random_)
    print(random_)
    sonuc_yazi.configure(
        text="Title: {}\nRelease Year: {}\nAge Rating: {}\nDuration: {}\nGenres: {}\nIMDb Rating: {}".format(row[1],row[2],row[3],row[4],row[5],row[6]))

    sonuc_yazi2.configure(text="--Storyline--" + row[7], wraplength=600)
    film_ismi.clear()
    film_ismi.append((row[1], row[2]))
    film_ismi_str = str(film_ismi[0][0]) + " " + str(film_ismi[0][1])
    film_ismi.clear()
    film_ismi.append(film_ismi_str)
    print(film_ismi)
    alt_frame.pack(side="bottom",fill="x")
    cast_button.pack(padx=10,pady=10,side="top")
    youtube_button.pack(padx=10,pady=10,side="top")
    image_button.pack(padx=10,pady=10,side="top")
    fav_button.pack(padx=10,pady=10,side="top")
    if len(scifi_film_onerilen) == scifi_film.shape[0]:
        scifi_film_onerilen.clear()

def sport():
    default_button_color()
    sport_button.configure(fg_color="purple")
    global sport_film_onerilen
    print(sport_film_onerilen)
    random_ = random.randint(0, sport_film.shape[0] - 1)
    while random_ in sport_film_onerilen:
        random_ = random.randint(0, sport_film.shape[0] - 1)

    row = sport_film.loc[random_]
    sport_film_onerilen.append(random_)
    print(random_)
    sonuc_yazi.configure(
        text="Title: {}\nRelease Year: {}\nAge Rating: {}\nDuration: {}\nGenres: {}\nIMDb Rating: {}".format(row[1],row[2],row[3],row[4],row[5],row[6]))
    sonuc_yazi2.configure(text="--Storyline--" + row[7], wraplength=600)
    film_ismi.clear()
    film_ismi.append((row[1], row[2]))
    film_ismi_str = str(film_ismi[0][0]) + " " + str(film_ismi[0][1])
    film_ismi.clear()
    film_ismi.append(film_ismi_str)
    print(film_ismi)
    alt_frame.pack(side="bottom",fill="x")
    cast_button.pack(padx=10,pady=10,side="top")
    youtube_button.pack(padx=10,pady=10,side="top")
    image_button.pack(padx=10,pady=10,side="top")
    fav_button.pack(padx=10,pady=10,side="top")
    if len(sport_film_onerilen) == sport_film.shape[0]:
        sport_film_onerilen.clear()


def thriller():
    default_button_color()
    thriller_button.configure(fg_color="purple")
    global thriller_film_onerilen
    print(thriller_film_onerilen)
    random_ = random.randint(0, thriller_film.shape[0] - 1)
    while random_ in thriller_film_onerilen:
        random_ = random.randint(0, thriller_film.shape[0] - 1)
    row = thriller_film.loc[random_]
    thriller_film_onerilen.append(random_)
    print(random_)
    sonuc_yazi.configure(
        text="Title: {}\nRelease Year: {}\nAge Rating: {}\nDuration: {}\nGenres: {}\nIMDb Rating: {}".format(row[1],row[2],row[3],row[4],row[5],row[6]))

    sonuc_yazi2.configure(text="--Storyline--" + row[7], wraplength=600)
    film_ismi.clear()
    film_ismi.append((row[1], row[2]))
    film_ismi_str = str(film_ismi[0][0]) + " " + str(film_ismi[0][1])
    film_ismi.clear()
    film_ismi.append(film_ismi_str)
    print(film_ismi)
    alt_frame.pack(side="bottom",fill="x")
    cast_button.pack(side="top", padx=10, pady=10)
    youtube_button.pack(side="top", padx=10, pady=10)
    image_button.pack(side="top", padx=10, pady=10)
    fav_button.pack(side="top", padx=10, pady=10)
    if len(thriller_film_onerilen) == thriller_film.shape[0]:
        thriller_film_onerilen.clear()



def war():
    default_button_color()
    war_button.configure(fg_color="purple")
    global war_film_onerilen
    print(war_film_onerilen)
    random_ = random.randint(0, war_film.shape[0] - 1)
    while random_ in war_film_onerilen:
        random_ = random.randint(0, war_film.shape[0] - 1)
    row = war_film.loc[random_]
    war_film_onerilen.append(random_)
    print(random_)
    sonuc_yazi.configure(
        text="Title: {}\nRelease Year: {}\nAge Rating: {}\nDuration: {}\nGenres: {}\nIMDb Rating: {}".format(row[1],
                                                                                                             row[2],
                                                                                                             row[3],
                                                                                                             row[4],
                                                                                                             row[5],
                                                                                                             row[6]))

    sonuc_yazi2.configure(text="--Storyline--" + row[7], wraplength=600)
    film_ismi.clear()
    film_ismi.append((row[1], row[2]))
    film_ismi_str = str(film_ismi[0][0]) + " " + str(film_ismi[0][1])
    film_ismi.clear()
    film_ismi.append(film_ismi_str)
    print(film_ismi)
    alt_frame.pack(side="bottom", fill="x")
    cast_button.pack(side="top", padx=10, pady=10)
    youtube_button.pack(side="top", padx=10, pady=10)
    image_button.pack(side="top", padx=10, pady=10)
    fav_button.pack(side="top", padx=10, pady=10)
    if len(war_film_onerilen) == war_film.shape[0]:
        war_film_onerilen.clear()






    """
     liste = []

    step99 = soup.find_all("div", attrs={"id": "tab-crew"})
    print("\n\n|-- Crew --|\n")
    for step98 in step99:
        step97 = step98.find_all("h3")
        for step96 in step97:
            step95 = step96.find("span", attrs={"class": "-short"}).text
            liste.append(step95)
        step11 = step98.find_all("div", attrs={"class": "text-sluglist"})
        for step12 in step11:
            step13 = step12.find_all("a")
            print("--{}--".format(liste.pop(0)))
            for step14 in step13:

                cast_listbox.insert(tk.END, step14.text)

                print(step14.text)
            print()
    """
    # crew

    cast_button.pack_forget()





def trailer():
    wait_attention()
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.get("https://www.youtube.com/")
    search = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@id='search']")))
    search.send_keys(film_ismi, " movie fragment")
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    video_link = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//a[@id='video-title']")))
    video_link_final = video_link.get_attribute("href")
    webview.create_window("Film Fragment", video_link_final)
    webview.start()


def image():
    wait_attention()
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.get("https://www.google.com/imghp")
    time.sleep(1)
    search = browser.find_element(By.CSS_SELECTOR, ".gLFyf")
    search.send_keys(film_ismi,"imdb poster")
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    browser.find_element(By.XPATH, "//*[@id='islrg']/div[1]/div[1]").click()
    time.sleep(2)
    src_find = browser.find_element(By.XPATH,"//*[@id='Sva75c']/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]")
    time.sleep(1)
    src = src_find.get_attribute("src")
    webview.create_window("Film Poster", src)
    webview.start()


def wait_attention():
    msg = CTkMessagebox(title="Standby Time", message="This process may take some time\n(5 - 10 seconds)",
                         button_color="purple",font=("Arial",16),fade_in_duration=3)

    msg.get()

def fav_list():
    #daha önce toplevel oluşturulup oluşturulmadığı kontrol ediliyor
    if not hasattr(fav_list, 'fav'):
        fav_list.fav = customtkinter.CTkToplevel(pencere)
        fav_list.fav.geometry("350x350")
        fav_list.fav.title("Fav List")
        fav_list.fav.lift(pencere)
        box = customtkinter.CTkTextbox(fav_list.fav)
        box.pack(fill="both", expand=True)
    else:
        children = fav_list.fav.winfo_children()
        if children:
            box = children[0]
        else:
            box = customtkinter.CTkTextbox(fav_list.fav)
            box.pack(fill="both", expand=True)


    box.insert(customtkinter.END, (film_ismi))
    box.insert(customtkinter.END, "\n")

def cast_st():
    wait_attention()
    new_win = customtkinter.CTkToplevel(pencere)
    new_win.geometry("700x540")
    new_win.title("Cast Staff")
    frame = customtkinter.CTkFrame(new_win)
    frame.pack(side="left")
    frame1 = customtkinter.CTkFrame(new_win)
    frame1.pack(side="left", fill=None, expand=True)
    frame2 = customtkinter.CTkFrame(new_win)
    frame2.pack(side="left")
    label1 = customtkinter.CTkLabel(frame, text="CAST STAFF")
    label1.pack()
    box = customtkinter.CTkTextbox(frame, width=200, height=400, fg_color="#808080", text_color="black")
    label2 = customtkinter.CTkLabel(frame1, text="WHERE TO WATCH")
    label2.pack()
    box2 = customtkinter.CTkTextbox(frame1, width=200, height=200, fg_color="#808080", text_color="black")
    label3 = customtkinter.CTkLabel(frame2, text="CREW")
    label3.pack()
    box3 = customtkinter.CTkTextbox(frame2, width=200, height=400, fg_color="#808080", text_color="black")
    box.pack()
    box2.pack()
    box3.pack()
    # headless browser açma
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)

    # siteye girme ve arama yapma
    browser.get("https://letterboxd.com/")
    search = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".field.-borderless")))

    search.send_keys(film_ismi)
    search.send_keys(Keys.ENTER)

    # film sayfasına gitme ve bilgileri alma
    browser.find_element(By.CSS_SELECTOR, ".film-title-wrapper").click()

    soup = BeautifulSoup(browser.page_source, "lxml")
    # film ekibi ve oyuncuları cast bilgileri çekilir
    step2 = soup.find_all("div", attrs={"class": "cast-list"})
    print("\n\n|-- Cast --|")
    for step3 in step2:
        step4 = step3.find_all("a", attrs={"class": "text-slug tooltip"})
        for step5 in step4:
            box.insert(customtkinter.END, step5.text)
            box.insert(customtkinter.END, "\n")
            print(step5.text)

            # filmin nereden izlenebileceği bilgileri çekilir
    step6 = soup.find_all("section", attrs={"class": "services"})
    print("\n\n|-- Where To Watch --|\n")
    for step7 in step6:
        step8 = step7.find_all("span", attrs={"class": "title"})
        for step9 in step8:
            box2.insert(customtkinter.END, step9.text)
            box2.insert(customtkinter.END, "\n")

            print(step9.text)



    # ekibin listesi crew listesi çekilir
    liste = []

    step99 = soup.find_all("div", attrs={"id": "tab-crew"})
    print("\n\n|-- Crew --|\n")
    for step98 in step99:
        step97 = step98.find_all("h3")
        for step96 in step97:
            step95 = step96.find("span", attrs={"class": "-short"}).text
            liste.append(step95)
        step11 = step98.find_all("div", attrs={"class": "text-sluglist"})
        for step12 in step11:
            step13 = step12.find_all("a")
            print("--{}--".format(liste.pop(0)))
            # box3.insert(customtkinter.END ,"--{}--".format(liste.pop(0)))
            # box3.insert(customtkinter.END , "\n")

            for step14 in step13:
                box3.insert(customtkinter.END, step14.text)
                box3.insert(customtkinter.END, "\n")

                print(step14.text)
            print()



#Frame oluşturma

sag_frame = customtkinter.CTkFrame(master=pencere,fg_color="#808080")
sag_frame.pack(pady=20,padx=20,fill="none",expand=False,side="right")

sol_frame = customtkinter.CTkFrame(master=pencere,fg_color="#808080")
sol_frame.pack(pady=20,padx=20,fill="none",expand=False,side="left")

# Butonları sol_frame içinde oluşturma
aksiyon_buton = customtkinter.CTkButton(master=sol_frame, text="Action",command=aksiyon,fg_color=("black"),font=("Times New Roman",18),text_color="#F5F5F5",hover_color="purple")
aksiyon_buton.pack(padx=20,pady=20,anchor=tkinter.W)
macera_buton = customtkinter.CTkButton(sol_frame, text="Adventure",command=macera,fg_color="black",font=("Times New Roman",18),text_color="#F5F5F5",hover_color="purple")
macera_buton.pack(padx=20,pady=20,anchor=tkinter.W)
animasyon_buton = customtkinter.CTkButton(sol_frame, text="Animation",command=animasyon,fg_color="black",font=("Times New Roman",18),text_color="#F5F5F5",hover_color="purple")
animasyon_buton.pack(padx=20,pady=20,anchor=tkinter.W)
biyografi_buton = customtkinter.CTkButton(sol_frame, text="Biography",command=biyografi,fg_color="black",font=("Times New Roman",18),text_color="#F5F5F5",hover_color="purple")
biyografi_buton.pack(padx=20,pady=20,anchor=tkinter.W)
komedi_buton = customtkinter.CTkButton(sol_frame, text="Comedy",command=komedi,fg_color="black",font=("Times New Roman",18),text_color="#F5F5F5",hover_color="purple")
komedi_buton.pack(padx=20,pady=20,anchor=tkinter.W)
suc_buton = customtkinter.CTkButton(sol_frame, text="Crime",command=suc,fg_color="black",font=("Times New Roman",18),text_color="#F5F5F5",hover_color="purple")
suc_buton.pack(padx=20,pady=20,anchor=tkinter.W)
dram_buton = customtkinter.CTkButton(sol_frame, text="Drama",command=dram,fg_color="black",font=("Times New Roman",18),hover_color="purple",text_color="#F5F5F5")
dram_buton.pack(padx=20,pady=20,anchor=tkinter.W)
aile_buton = customtkinter.CTkButton(sol_frame, text="Family",command=aile,fg_color="black",font=("Times New Roman",18),text_color="#F5F5F5",hover_color="purple")
aile_buton.pack(padx=20,pady=20,anchor=tkinter.W)
fantezi_buton = customtkinter.CTkButton(sol_frame, text="Fantasy",command=fantezi,fg_color="black",font=("Times New Roman",18),text_color="#F5F5F5",hover_color="purple")
fantezi_buton.pack(padx=20,pady=20,anchor=tkinter.W)
western_button = customtkinter.CTkButton(sol_frame, text="Western",command=western,fg_color="black",font=("Times New Roman",18),text_color="#F5F5F5",hover_color="purple")
western_button.pack(padx=20,pady=20,anchor=tkinter.W)

# Butonları sag_frame içinde oluşturma
history_button = customtkinter.CTkButton(sag_frame, text="History", command=history,fg_color="black",font=("Times New Roman",18),text_color="#F5F5F5",hover_color="purple")
history_button.pack(padx=20,pady=20,anchor=tkinter.E)
horror_button = customtkinter.CTkButton(sag_frame, text="Horror", command=horror,fg_color="black",font=("Times New Roman",18),text_color="#F5F5F5",hover_color="purple")
horror_button.pack(padx=20,pady=20,anchor=tkinter.E)
music_button = customtkinter.CTkButton(sag_frame, text="Music", command=music,fg_color="black",font=("Times New Roman",18),text_color="#F5F5F5",hover_color="purple")
music_button.pack(padx=20,pady=20,anchor=tkinter.E)
musical_button = customtkinter.CTkButton(sag_frame, text="Musical", command=musical,fg_color="black",font=("Times New Roman",18),text_color="#F5F5F5" ,hover_color="purple")
musical_button.pack(padx=20,pady=20,anchor=tkinter.E)
mystery_button = customtkinter.CTkButton(sag_frame, text="Mystery", command=mystery,fg_color="black",font=("Times New Roman",18),text_color="#F5F5F5",hover_color="purple")
mystery_button.pack(padx=20,pady=20,anchor=tkinter.E)
romance_button = customtkinter.CTkButton(sag_frame, text="Romance", command=romance ,fg_color="black",font=("Times New Roman",18),text_color="#F5F5F5",hover_color="purple")
romance_button.pack(padx=20,pady=20,anchor=tkinter.E)
scifi_button = customtkinter.CTkButton(sag_frame, text="Sci-Fi", command=scifi,fg_color="black",font=("Times New Roman",18),text_color="#F5F5F5",hover_color="purple")
scifi_button.pack(padx=20,pady=20,anchor=tkinter.E)
sport_button = customtkinter.CTkButton(sag_frame, text="Sport", command=sport,fg_color="black",font=("Times New Roman",18),text_color="#F5F5F5",hover_color="purple")
sport_button.pack(padx=20,pady=20,anchor=tkinter.E)
thriller_button = customtkinter.CTkButton(sag_frame, text="Thriller", command=thriller,fg_color="black",font=("Times New Roman",18),text_color="#F5F5F5",hover_color="purple")
thriller_button.pack(padx=20,pady=20,anchor=tkinter.E)
war_button = customtkinter.CTkButton(sag_frame, text="War", command=war,fg_color="black",font=("Times New Roman",18),text_color="#F5F5F5",hover_color="purple")
war_button.pack(padx=20,pady=20,anchor=tkinter.E)



# Film önerisi sonucunu yazdırmak için etiket oluşturma
sonuc_yazi = customtkinter.CTkLabel(master=pencere,text="",wraplength=10000,font=("Times New Roman",35),text_color="white")
sonuc_yazi.pack(padx=40,pady=80)

sonuc_yazi2 = customtkinter.CTkLabel(pencere, text="",wraplength=10000, font=("Times New Roman", 25, "italic"),text_color="white")
sonuc_yazi2.pack(padx=0,pady=0)



alt_frame= customtkinter.CTkFrame(pencere,fg_color="#808080")
alt_frame.pack_forget()

# Butonları alt_frame içinde oluşturma

cast_button = customtkinter.CTkButton(alt_frame,text="Cast Staff",command=cast_st,fg_color="black")
cast_button.pack_forget()

image_button = customtkinter.CTkButton(alt_frame,text="Movie Poster",command=image,fg_color="black")
image_button.pack_forget()

fav_button = customtkinter.CTkButton(alt_frame,text="Add To Fav List",command=fav_list,fg_color="black")
fav_button.pack_forget()


youtube_button = customtkinter.CTkButton(alt_frame,text="Go To Trailer",command=trailer,fg_color="black")
youtube_button.pack_forget()









pencere.mainloop()











