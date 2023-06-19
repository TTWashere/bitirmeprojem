import requests
import time
from bs4 import BeautifulSoup
import pandas as pd





tür_secim = input("İndirmek istediğiniz film türünü seçiniz:\n1 - Aksiyon\n2 - Macera\n3 - Animasyon\n4 - Biyografi\n5 - "
                  "Komedi\n6 - Suç\n7 - Dram\n8 -  Aile\n9 - Fantezi\n10 - Western\n11 - History\n"
                  "12 - Horror\n13 - Music\n14 - Musical\n15 - Mystery\n16 - Romance\n17 - Sci-Fi\n18 - Sport\n19 - Thriller\n20 - War\n")




class filmöneri():
        def __init__(self,tür_secim):
            self.aksiyon_pd=[]
            self.macera_pd=[]
            self.animasyon_pd=[]
            self.biyografi_pd=[]
            self.komedi_pd=[]
            self.suc_pd=[]
            self.dram_pd=[]
            self.aile_pd=[]
            self.fantezi_pd=[]
            self.western_pd=[]
            self.history_pd =[]
            self.horror_pd=[]
            self.music_pd=[]
            self.musical_pd=[]
            self.mystery_pd=[]
            self.romance_pd=[]
            self.scifi_pd=[]
            self.sport_pd=[]
            self.thriller_pd=[]
            self.war_pd=[]

            if tür_secim=="1":
                self.veri_cekme(tür_secim)
                df = pd.DataFrame(self.aksiyon_pd)
                df.to_csv("aksiyon_filmleri.csv")
                print("Veri seti başarılı şekilde indirildi..")

            elif tür_secim=="2":
                self.veri_cekme(tür_secim)
                df = pd.DataFrame(self.macera_pd)
                df.to_csv("macera_filmleri.csv")
                print("Veri seti başarılı şekilde indirildi..")

            elif tür_secim=="3":
                self.veri_cekme(tür_secim)
                df = pd.DataFrame(self.animasyon_pd)
                df.to_csv("animasyon_filmleri.csv")
                print("Veri seti başarılı şekilde indirildi..")


            elif tür_secim == "4":
                self.veri_cekme(tür_secim)
                df = pd.DataFrame(self.biyografi_pd)
                df.to_csv("biyografi_filmleri.csv")
                print("Veri seti başarılı şekilde indirildi..")

            elif tür_secim == "5":
                self.veri_cekme(tür_secim)
                df = pd.DataFrame(self.komedi_pd)
                df.to_csv("komedi_filmleri.csv")
                print("Veri seti başarılı şekilde indirildi..")


            elif tür_secim == "6":
                self.veri_cekme(tür_secim)
                df = pd.DataFrame(self.suc_pd)
                df.to_csv("suc_filmleri.csv")
                print("Veri seti başarılı şekilde indirildi..")

            elif tür_secim == "7":
                self.veri_cekme(tür_secim)
                df = pd.DataFrame(self.dram_pd)
                df.to_csv("dram_filmleri.csv")
                print("Veri seti başarılı şekilde indirildi..")

            elif tür_secim == "8":
                self.veri_cekme(tür_secim)
                df = pd.DataFrame(self.aile_pd)
                df.to_csv("aile_filmleri.csv")
                print("Veri seti başarılı şekilde indirildi..")

            elif tür_secim == "9":
                self.veri_cekme(tür_secim)
                df = pd.DataFrame(self.fantezi_pd)
                df.to_csv("fantezi_filmleri.csv")
                print("Veri seti başarılı şekilde indirildi..")

            elif tür_secim == "10":
                self.veri_cekme(tür_secim)
                df = pd.DataFrame(self.western_pd)
                df.to_csv("western_filmleri.csv")
                print("Veri seti başarılı şekilde indirildi..")

            elif tür_secim == "11":
                self.veri_cekme(tür_secim)
                df = pd.DataFrame(self.history_pd)
                df.to_csv("history_filmleri.csv")
                print("Veri seti başarılı şekilde indirildi..")

            elif tür_secim == "12":
                self.veri_cekme(tür_secim)
                df = pd.DataFrame(self.horror_pd)
                df.to_csv("horror_filmleri.csv")
                print("Veri seti başarılı şekilde indirildi..")

            elif tür_secim == "13":
                self.veri_cekme(tür_secim)
                df = pd.DataFrame(self.music_pd)
                df.to_csv("music_filmleri.csv")
                print("Veri seti başarılı şekilde indirildi..")

            elif tür_secim == "14":
                self.veri_cekme(tür_secim)
                df = pd.DataFrame(self.musical_pd)
                df.to_csv("musical_filmleri.csv")
                print("Veri seti başarılı şekilde indirildi..")

            elif tür_secim == "15":
                self.veri_cekme(tür_secim)
                df = pd.DataFrame(self.mystery_pd)
                df.to_csv("mystery_filmleri.csv")
                print("Veri seti başarılı şekilde indirildi..")

            elif tür_secim == "16":
                self.veri_cekme(tür_secim)
                df = pd.DataFrame(self.romance_pd)
                df.to_csv("romance_filmleri.csv")
                print("Veri seti başarılı şekilde indirildi..")

            elif tür_secim == "17":
                self.veri_cekme(tür_secim)
                df = pd.DataFrame(self.scifi_pd)
                df.to_csv("scifi_filmleri.csv")
                print("Veri seti başarılı şekilde indirildi..")

            elif tür_secim == "18":
                self.veri_cekme(tür_secim)
                df = pd.DataFrame(self.sport_pd)
                df.to_csv("sport_filmleri.csv")
                print("Veri seti başarılı şekilde indirildi..")

            elif tür_secim == "19":
                self.veri_cekme(tür_secim)
                df = pd.DataFrame(self.thriller_pd)
                df.to_csv("thriller_filmleri.csv")
                print("Veri seti başarılı şekilde indirildi..")

            elif tür_secim == "20":
                self.veri_cekme(tür_secim)
                df = pd.DataFrame(self.war_pd)
                df.to_csv("war_filmleri.csv")
                print("Veri seti başarılı şekilde indirildi..")



        def veri_cekme(self,tür_secim):
            if tür_secim=="1":

                 idenfity=[1,51,101,151,201,251]
                 for first in idenfity:
                  sayfaların_linki=["https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&sort=user_rating,desc&start="+str(first)+"&ref_=adv_nxt"]
                  for sayfaxx in sayfaların_linki:

                    rr = requests.get(sayfaxx)
                    soup2 = BeautifulSoup(rr.content, "lxml")
                    time.sleep(2)
                    filmisim = soup2.find_all("div", attrs={"class": "lister-item mode-advanced"})
                    for step1 in filmisim:
                        step2 = step1.find("h3", attrs={"class": "lister-item-header"})
                        step3 = step2.a.text  #Film İsmini Çeken Kod
                        step4 = step2.find("span", attrs={"class": "lister-item-year text-muted unbold"}).text  #Film Tarihini Çeken Kod
                        step5=step1.find("span",attrs={"class":"runtime"}).text.strip() #Film Süresini Çeken Kod
                        step6=step1.find("span",attrs={"class":"genre"}).text.strip() #Ekstra Türleri Çeken Kod
                        if step1.find("span", attrs={"class": "certificate"}):
                            step99 = step1.find("span", attrs={"class": "certificate"}).text.strip() #Yaş Sınırını Çeken Kod
                        else:
                            step99 = ("---")

                        step69=step1.find("div",attrs={"class":"ratings-bar"}).find("strong").text #Ratingi Çeken Kod
                        step33 = step1.find_all("p",attrs={"class":"text-muted"})
                        step333 = step33[1].text  #Storyline

                        finish=step3,step4,step99,step5,step6,step69,step333
                        self.aksiyon_pd.append(finish)

            elif tür_secim=="2":
                idenfity = [1, 51, 101, 151, 201, 251]
                for first in idenfity:
                    sayfaların_linki = [
                        "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=adventure&sort=user_rating,desc&start=" + str(
                            first) + "&ref_=adv_nxt"]
                    for sayfalarxtxt in sayfaların_linki:
                     rr = requests.get(sayfalarxtxt)
                     soup2 = BeautifulSoup(rr.content, "lxml")
                     time.sleep(2)
                     filmisim = soup2.find_all("div", attrs={"class": "lister-item mode-advanced"})
                     for step1 in filmisim:
                         step2 = step1.find("h3", attrs={"class": "lister-item-header"})
                         step3 = step2.a.text  #Film İsmini Çeken Kod
                         step4 = step2.find("span", attrs={"class": "lister-item-year text-muted unbold"}).text #Film Tarihini Çeken Kod
                         step5 = step1.find("span", attrs={"class": "runtime"}).text.strip() #Film Süresini Çeken Kod
                         step6 = step1.find("span", attrs={"class": "genre"}).text.strip() #Ekstra Türleri Çeken Kod
                         if step1.find("span", attrs={"class": "certificate"}):
                             step99 = step1.find("span", attrs={"class": "certificate"}).text.strip() #Yaş Sınırını Çeken Kod

                         else:
                             step99 = ("---")

                         step69 = step1.find("div", attrs={"class": "ratings-bar"}).find("strong").text #Ratingi Çeken Kod
                         step33 = step1.find_all("p", attrs={"class": "text-muted"})
                         step333 = step33[1].text     #Storyline
                         finish = step3, step4, step99, step5, step6, step69 , step333
                         self.macera_pd.append(finish)

            elif tür_secim == "3":
                idenfity = [1, 51, 101, 151, 201, 251]
                for first in idenfity:
                    sayfaların_linki = [
                        "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=animation&sort=user_rating,desc&start=" + str(
                            first) + "&ref_=adv_nxt"]
                    for sayfaxtxt in sayfaların_linki :
                        rr = requests.get(sayfaxtxt)
                        soup2 = BeautifulSoup(rr.content, "lxml")
                        time.sleep(2)

                        filmisim = soup2.find_all("div", attrs={"class": "lister-item mode-advanced"})
                        for step1 in filmisim:
                            step2 = step1.find("h3", attrs={"class": "lister-item-header"})
                            step3 = step2.a.text  #Film İsmini Çeken Kod

                            step4 = step2.find("span", attrs={"class": "lister-item-year text-muted unbold"}).text  #Film Tarihini Çeken Kod
                            step5 = step1.find("span", attrs={"class": "runtime"}).text.strip() #Film Süresini Çeken Kod
                            step6 = step1.find("span", attrs={"class": "genre"}).text.strip() #Ekstra Türleri Çeken Kod
                            if step1.find("span", attrs={"class": "certificate"}):
                                step99 = step1.find("span", attrs={"class": "certificate"}).text.strip() #Yaş Sınırını Çeken Kod

                            else:
                                step99 = ("---")

                            step69=step1.find("div",attrs={"class":"ratings-bar"}).find("strong").text  #Ratingi Çeken Kod
                            step33 = step1.find_all("p", attrs={"class": "text-muted"})
                            step333 = step33[1].text  #Storyline
                            finish = step3, step4, step99, step5, step6, step69 ,step333
                            self.animasyon_pd.append(finish)


            elif tür_secim == "4":
                idenfity = [1, 51, 101, 151, 201, 251]
                for first in idenfity:
                    sayfaların_linki = [
                        "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=biography&sort=user_rating,desc&start=" + str(
                            first) + "&ref_=adv_nxt"]
                    for sayfaxt in sayfaların_linki:
                        rr=requests.get(sayfaxt)
                        soup2 = BeautifulSoup(rr.content, "lxml")
                        time.sleep(2)

                        filmisim = soup2.find_all("div", attrs={"class": "lister-item mode-advanced"})
                        for step1 in filmisim:
                            step2 = step1.find("h3", attrs={"class": "lister-item-header"})
                            step3 = step2.a.text  # filmadı

                            step4 = step2.find("span", attrs={"class": "lister-item-year text-muted unbold"}).text  #Film Tarihini Çeken Kod
                            step5 = step1.find("span", attrs={"class": "runtime"}).text.strip() #Film Süresini Çeken Kod
                            step6 = step1.find("span", attrs={"class": "genre"}).text.strip()  #Ekstra Türleri Çeken Kod
                            if step1.find("span", attrs={"class": "certificate"}):
                                step99 = step1.find("span", attrs={"class": "certificate"}).text.strip() #Yaş Sınırını Çeken Kod

                            else:
                                step99 = ("---")

                            step69=step1.find("div",attrs={"class":"ratings-bar"}).find("strong").text  #Ratingi Çeken Kod
                            step33 = step1.find_all("p", attrs={"class": "text-muted"})
                            step333 = step33[1].text   #Storyline
                            finish = step3, step4, step99, step5, step6, step69 ,step333
                            self.biyografi_pd.append(finish)


            elif tür_secim == "5":
                idenfity = [1, 51, 101, 151, 201, 251]
                for first in idenfity:
                    sayfaların_linki = [
                        "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=comedy&sort=user_rating,desc&start=" + str(
                            first) + "&ref_=adv_nxt"]
                    for sayfaxtxt in sayfaların_linki:
                        rr = requests.get(sayfaxtxt)
                        soup2 = BeautifulSoup(rr.content, "lxml")
                        time.sleep(2)

                        filmisim = soup2.find_all("div", attrs={"class": "lister-item mode-advanced"})
                        for step1 in filmisim:
                            step2 = step1.find("h3", attrs={"class": "lister-item-header"})
                            step3 = step2.a.text  # filmadı

                            step4 = step2.find("span", attrs={"class": "lister-item-year text-muted unbold"}).text   #Film Tarihini Çeken Kod
                            step5 = step1.find("span", attrs={"class": "runtime"}).text.strip() #Film Süresini Çeken Kod
                            step6 = step1.find("span", attrs={"class": "genre"}).text.strip()  #Ekstra Türleri Çeken Kod
                            if step1.find("span", attrs={"class": "certificate"}):
                                step99 = step1.find("span", attrs={"class": "certificate"}).text.strip() #Yaş Sınırını Çeken Kod

                            else:
                                step99 = ("---")

                            step69=step1.find("div",attrs={"class":"ratings-bar"}).find("strong").text  #Ratingi Çeken Kod
                            step33 = step1.find_all("p", attrs={"class": "text-muted"})
                            step333 = step33[1].text   #Storyline
                            finish = step3, step4, step99, step5, step6, step69 ,step333
                            self.komedi_pd.append(finish)


            elif tür_secim == "6":
                idenfity = [1, 51, 101, 151, 201, 251]
                for first in idenfity:
                        sayfaların_linki = [
                            "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=crime&sort=user_rating,desc&start=" + str(
                                first) + "&ref_=adv_nxt"]
                        for sayfaxtxt in sayfaların_linki:

                            rr = requests.get(sayfaxtxt)
                            soup2 = BeautifulSoup(rr.content, "lxml")
                            time.sleep(2)

                        filmisim = soup2.find_all("div", attrs={"class": "lister-item mode-advanced"})
                        for step1 in filmisim:
                            step2 = step1.find("h3", attrs={"class": "lister-item-header"})
                            step3 = step2.a.text  # filmadı

                            step4 = step2.find("span", attrs={"class": "lister-item-year text-muted unbold"}).text  #Film Tarihini Çeken Kod
                            step5 = step1.find("span", attrs={"class": "runtime"}).text.strip() #Film Süresini Çeken Kod
                            step6 = step1.find("span", attrs={"class": "genre"}).text.strip()  #Ekstra Türleri Çeken Kod
                            if step1.find("span", attrs={"class": "certificate"}):
                                step99 = step1.find("span", attrs={"class": "certificate"}).text.strip() #Yaş Sınırını Çeken Kod
                            else:
                                step99 = ("---")

                            step69=step1.find("div",attrs={"class":"ratings-bar"}).find("strong").text  #Ratingi Çeken Kod
                            step33 = step1.find_all("p", attrs={"class": "text-muted"})
                            step333 = step33[1].text   #Storyline
                            finish = step3, step4, step99, step5, step6, step69 ,step333
                            self.suc_pd.append(finish)


            elif tür_secim=="7":
                idenfity = [1, 51, 101, 151, 201, 251]
                for first in idenfity:
                     sayfaların_linki = [
                        "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=drama&sort=user_rating,desc&start=" + str(
                            first) + "&ref_=adv_nxt"]
                     for sayfaxtxt in sayfaların_linki:

                         rr=requests.get(sayfaxtxt)
                         soup2 = BeautifulSoup(rr.content, "lxml")
                         time.sleep(2)

                         filmisim = soup2.find_all("div", attrs={"class": "lister-item mode-advanced"})
                         for step1 in filmisim:
                             step2 = step1.find("h3", attrs={"class": "lister-item-header"})
                             step3 = step2.a.text  # filmadı

                             step4 = step2.find("span", attrs={"class": "lister-item-year text-muted unbold"}).text #Film Tarihini Çeken Kod
                             step5 = step1.find("span", attrs={"class": "runtime"}).text.strip() #Film Süresini Çeken Kod
                             step6 = step1.find("span", attrs={"class": "genre"}).text.strip()  #Ekstra Türleri Çeken Kod
                             if step1.find("span", attrs={"class": "certificate"}):
                                    step99 = step1.find("span", attrs={"class": "certificate"}).text.strip() #Yaş Sınırını Çeken Kod
                             else:
                                    step99 = ("---")

                             step69=step1.find("div",attrs={"class":"ratings-bar"}).find("strong").text  #Ratingi Çeken Kod
                             step33 = step1.find_all("p", attrs={"class": "text-muted"})
                             step333 = step33[1].text   #Storyline
                             finish = step3, step4, step99, step5, step6, step69 ,step333
                             self.dram_pd.append(finish)


            elif tür_secim == "8":
                idenfity = [1, 51, 101, 151, 201, 251]
                for first in idenfity:
                    sayfaların_linki = [
                        "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=family&sort=user_rating,desc&start=" + str(
                            first) + "&ref_=adv_nxt"]
                    for sayfaxtxt in sayfaların_linki:
                     rr = requests.get(sayfaxtxt)
                     soup2 = BeautifulSoup(rr.content, "lxml")
                     time.sleep(2)

                     filmisim = soup2.find_all("div", attrs={"class": "lister-item mode-advanced"})
                     for step1 in filmisim:
                         step2 = step1.find("h3", attrs={"class": "lister-item-header"})
                         step3 = step2.a.text  # filmadı

                         step4 = step2.find("span", attrs={"class": "lister-item-year text-muted unbold"}).text  #Film Tarihini Çeken Kod
                         step5 = step1.find("span", attrs={"class": "runtime"}).text.strip() #Film Süresini Çeken Kod
                         step6 = step1.find("span", attrs={"class": "genre"}).text.strip()  #Ekstra Türleri Çeken Kod
                         if step1.find("span", attrs={"class": "certificate"}):
                                step99 = step1.find("span", attrs={"class": "certificate"}).text.strip() #Yaş Sınırını Çeken Kod
                         else:
                                step99 = ("---")

                         step69=step1.find("div",attrs={"class":"ratings-bar"}).find("strong").text  #Ratingi Çeken Kod
                         step33 = step1.find_all("p", attrs={"class": "text-muted"})
                         step333 = step33[1].text   #Storyline
                         finish = step3, step4, step99, step5, step6, step69 ,step333
                         self.aile_pd.append(finish)


            elif tür_secim == "9":
                idenfity = [1, 51, 101, 151, 201, 251]
                for first in idenfity:
                    sayfaların_linki = [
                        "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=fantasy&sort=user_rating,desc&start=" + str(
                            first) + "&ref_=adv_nxt"]
                    for sayfaxtxt in sayfaların_linki:
                        rr = requests.get(sayfaxtxt)
                        soup2 = BeautifulSoup(rr.content, "lxml")
                        time.sleep(2)

                        filmisim = soup2.find_all("div", attrs={"class": "lister-item mode-advanced"})
                        for step1 in filmisim:
                             step2 = step1.find("h3", attrs={"class": "lister-item-header"})
                             step3 = step2.a.text  # filmadı

                             step4 = step2.find("span", attrs={"class": "lister-item-year text-muted unbold"}).text  #Film Tarihini Çeken Kod
                             step5 = step1.find("span", attrs={"class": "runtime"}).text.strip() #Film Süresini Çeken Kod
                             step6 = step1.find("span", attrs={"class": "genre"}).text.strip()  #Ekstra Türleri Çeken Kod
                             if step1.find("span", attrs={"class": "certificate"}):
                                    step99 = step1.find("span", attrs={"class": "certificate"}).text.strip() #Yaş Sınırını Çeken Kod
                             else:
                                    step99 = ("---")

                             step69=step1.find("div",attrs={"class":"ratings-bar"}).find("strong").text  #Ratingi Çeken Kod
                             step33 = step1.find_all("p", attrs={"class": "text-muted"})
                             step333 = step33[1].text   #Storyline
                             finish = step3, step4, step99, step5, step6, step69 ,step333
                             self.fantezi_pd.append(finish)


            elif tür_secim == "10":
                idenfity = [1, 51, 101, 151, 201, 251]
                for first in idenfity:
                    sayfaların_linki = [
                        "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=western&sort=user_rating,desc&start=" + str(
                            first) + "&ref_=adv_nxt"]
                    for sayfaxtxt in sayfaların_linki:
                        rr=requests.get(sayfaxtxt)
                        soup2 = BeautifulSoup(rr.content, "lxml")
                        time.sleep(2)

                        filmisim = soup2.find_all("div", attrs={"class": "lister-item mode-advanced"})
                        for step1 in filmisim:
                             step2 = step1.find("h3", attrs={"class": "lister-item-header"})
                             step3 = step2.a.text  # filmadı

                             step4 = step2.find("span", attrs={"class": "lister-item-year text-muted unbold"}).text #Film Tarihini Çeken Kod
                             step5 = step1.find("span", attrs={"class": "runtime"}).text.strip() #Film Süresini Çeken Kod
                             step6 = step1.find("span", attrs={"class": "genre"}).text.strip()  #Ekstra Türleri Çeken Kod
                             if step1.find("span", attrs={"class": "certificate"}):
                                    step99 = step1.find("span", attrs={"class": "certificate"}).text.strip() #Yaş Sınırını Çeken Kod
                             else:
                                    step99 = ("---")

                             step69=step1.find("div",attrs={"class":"ratings-bar"}).find("strong").text  #Ratingi Çeken Kod
                             step33 = step1.find_all("p", attrs={"class": "text-muted"})
                             step333 = step33[1].text   #Storyline
                             finish = step3, step4, step99, step5, step6, step69 ,step333
                             self.western_pd.append(finish)

            elif tür_secim == "11":
                idenfity = [1, 51, 101, 151, 201, 251]
                for first in idenfity:
                    sayfaların_linki = [
                        "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=history&sort=user_rating,desc&start=" + str(
                            first) + "&ref_=adv_nxt"]
                    for sayfaxtxt in sayfaların_linki:
                        rr=requests.get(sayfaxtxt)
                        soup2 = BeautifulSoup(rr.content, "lxml")
                        time.sleep(2)

                        filmisim = soup2.find_all("div", attrs={"class": "lister-item mode-advanced"})
                        for step1 in filmisim:
                             step2 = step1.find("h3", attrs={"class": "lister-item-header"})
                             step3 = step2.a.text  # filmadı

                             step4 = step2.find("span", attrs={"class": "lister-item-year text-muted unbold"}).text  #Film Tarihini Çeken Kod
                             step5 = step1.find("span", attrs={"class": "runtime"}).text.strip() #Film Süresini Çeken Kod
                             step6 = step1.find("span", attrs={"class": "genre"}).text.strip()  #Ekstra Türleri Çeken Kod
                             if step1.find("span", attrs={"class": "certificate"}):
                                    step99 = step1.find("span", attrs={"class": "certificate"}).text.strip() #Yaş Sınırını Çeken Kod
                             else:
                                    step99 = ("---")

                             step69=step1.find("div",attrs={"class":"ratings-bar"}).find("strong").text  #Ratingi Çeken Kod
                             step33 = step1.find_all("p", attrs={"class": "text-muted"})
                             step333 = step33[1].text   #Storyline
                             finish = step3, step4, step99, step5, step6, step69 ,step333
                             self.history_pd.append(finish)

            elif tür_secim == "12":
                idenfity = [1, 51, 101, 151, 201, 251]
                for first in idenfity:
                    sayfaların_linki = [
                        "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=horror&sort=user_rating,desc&start=" + str(
                            first) + "&ref_=adv_nxt"]
                    for sayfaxtxt in sayfaların_linki:
                        rr=requests.get(sayfaxtxt)
                        soup2 = BeautifulSoup(rr.content, "lxml")
                        time.sleep(2)

                        filmisim = soup2.find_all("div", attrs={"class": "lister-item mode-advanced"})
                        for  step1 in filmisim:
                             step2 = step1.find("h3", attrs={"class": "lister-item-header"})
                             step3 = step2.a.text  # filmadı

                             step4 = step2.find("span", attrs={"class": "lister-item-year text-muted unbold"}).text  #Film Tarihini Çeken Kod
                             step5 = step1.find("span", attrs={"class": "runtime"}).text.strip() #Film Süresini Çeken Kod
                             step6 = step1.find("span", attrs={"class": "genre"}).text.strip()  #Ekstra Türleri Çeken Kod
                             if step1.find("span", attrs={"class": "certificate"}):
                                    step99 = step1.find("span", attrs={"class": "certificate"}).text.strip() #Yaş Sınırını Çeken Kod
                             else:
                                    step99 = ("---")

                             step69=step1.find("div",attrs={"class":"ratings-bar"}).find("strong").text  #Ratingi Çeken Kod
                             step33 = step1.find_all("p", attrs={"class": "text-muted"})
                             step333 = step33[1].text   #Storyline
                             finish = step3, step4, step99, step5, step6, step69 ,step333
                             self.horror_pd.append(finish)

            elif tür_secim == "13":
                idenfity = [1, 51, 101, 151, 201, 251]
                for first in idenfity:
                    sayfaların_linki = [
                        "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=music&sort=user_rating,desc&start=" + str(
                            first) + "&ref_=adv_nxt"]
                    for sayfaxtxt in sayfaların_linki:
                        rr=requests.get(sayfaxtxt)
                        soup2 = BeautifulSoup(rr.content, "lxml")
                        time.sleep(2)

                        filmisim = soup2.find_all("div", attrs={"class": "lister-item mode-advanced"})
                        for step1 in filmisim:
                             step2 = step1.find("h3", attrs={"class": "lister-item-header"})
                             step3 = step2.a.text  # filmadı

                             step4 = step2.find("span", attrs={"class": "lister-item-year text-muted unbold"}).text  #Film Tarihini Çeken Kod
                             step5 = step1.find("span", attrs={"class": "runtime"}).text.strip() #Film Süresini Çeken Kod
                             step6 = step1.find("span", attrs={"class": "genre"}).text.strip()  #Ekstra Türleri Çeken Kod
                             if step1.find("span", attrs={"class": "certificate"}):
                                    step99 = step1.find("span", attrs={"class": "certificate"}).text.strip() #Yaş Sınırını Çeken Kod
                             else:
                                    step99 = ("---")

                             step69=step1.find("div",attrs={"class":"ratings-bar"}).find("strong").text  #Ratingi Çeken Kod
                             step33 = step1.find_all("p", attrs={"class": "text-muted"})
                             step333 = step33[1].text   #Storyline
                             finish = step3, step4, step99, step5, step6, step69 ,step333
                             self.music_pd.append(finish)

            elif tür_secim == "14":
                idenfity = [1, 51, 101, 151, 201, 251]
                for first in idenfity:
                    sayfaların_linki = [
                        "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=musical&sort=user_rating,desc&start=" + str(
                            first) + "&ref_=adv_nxt"]
                    for sayfaxtxt in sayfaların_linki:
                        rr=requests.get(sayfaxtxt)
                        soup2 = BeautifulSoup(rr.content, "lxml")
                        time.sleep(2)

                        filmisim = soup2.find_all("div", attrs={"class": "lister-item mode-advanced"})
                        for step1 in filmisim:
                             step2 = step1.find("h3", attrs={"class": "lister-item-header"})
                             step3 = step2.a.text  # filmadı

                             step4 = step2.find("span", attrs={"class": "lister-item-year text-muted unbold"}).text  #Film Tarihini Çeken Kod
                             step5 = step1.find("span", attrs={"class": "runtime"}).text.strip() #Film Süresini Çeken Kod
                             step6 = step1.find("span", attrs={"class": "genre"}).text.strip()  #Ekstra Türleri Çeken Kod
                             if step1.find("span", attrs={"class": "certificate"}):
                                    step99 = step1.find("span", attrs={"class": "certificate"}).text.strip() #Yaş Sınırını Çeken Kod
                             else:
                                    step99 = ("---")

                             step69=step1.find("div",attrs={"class":"ratings-bar"}).find("strong").text  #Ratingi Çeken Kod
                             step33 = step1.find_all("p", attrs={"class": "text-muted"})
                             step333 = step33[1].text   #Storyline
                             finish = step3, step4, step99, step5, step6, step69 ,step333
                             self.musical_pd.append(finish)

            elif tür_secim == "15":
                idenfity = [1, 51, 101, 151, 201, 251]
                for first in idenfity:
                    sayfaların_linki = [
                        "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=mystery&sort=user_rating,desc&start=" + str(
                            first) + "&ref_=adv_nxt"]
                    for sayfaxtxt in sayfaların_linki:
                        rr=requests.get(sayfaxtxt)
                        soup2 = BeautifulSoup(rr.content, "lxml")
                        time.sleep(2)

                        filmisim = soup2.find_all("div", attrs={"class": "lister-item mode-advanced"})
                        for step1 in filmisim:
                             step2 = step1.find("h3", attrs={"class": "lister-item-header"})
                             step3 = step2.a.text  # filmadı

                             step4 = step2.find("span", attrs={"class": "lister-item-year text-muted unbold"}).text  #Film Tarihini Çeken Kod
                             step5 = step1.find("span", attrs={"class": "runtime"}).text.strip() #Film Süresini Çeken Kod
                             step6 = step1.find("span", attrs={"class": "genre"}).text.strip()  #Ekstra Türleri Çeken Kod
                             if step1.find("span", attrs={"class": "certificate"}):
                                    step99 = step1.find("span", attrs={"class": "certificate"}).text.strip() #Yaş Sınırını Çeken Kod
                             else:
                                    step99 = ("---")

                             step69=step1.find("div",attrs={"class":"ratings-bar"}).find("strong").text  #Ratingi Çeken Kod
                             step33 = step1.find_all("p", attrs={"class": "text-muted"})
                             step333 = step33[1].text   #Storyline
                             finish = step3, step4, step99, step5, step6, step69 ,step333
                             self.mystery_pd.append(finish)

            elif tür_secim == "16":
                idenfity = [1, 51, 101, 151, 201, 251]
                for first in idenfity:
                    sayfaların_linki = [
                        "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=romance&sort=user_rating,desc&start=" + str(
                            first) + "&ref_=adv_nxt"]
                    for sayfaxtxt in sayfaların_linki:
                        rr=requests.get(sayfaxtxt)
                        soup2 = BeautifulSoup(rr.content, "lxml")
                        time.sleep(2)

                        filmisim = soup2.find_all("div", attrs={"class": "lister-item mode-advanced"})
                        for step1 in filmisim:
                             step2 = step1.find("h3", attrs={"class": "lister-item-header"})
                             step3 = step2.a.text  # filmadı

                             step4 = step2.find("span", attrs={"class": "lister-item-year text-muted unbold"}).text  #Film Tarihini Çeken Kod
                             step5 = step1.find("span", attrs={"class": "runtime"}).text.strip() #Film Süresini Çeken Kod
                             step6 = step1.find("span", attrs={"class": "genre"}).text.strip()  #Ekstra Türleri Çeken Kod
                             if step1.find("span", attrs={"class": "certificate"}):
                                    step99 = step1.find("span", attrs={"class": "certificate"}).text.strip() #Yaş Sınırını Çeken Kod
                             else:
                                    step99 = ("---")

                             step69=step1.find("div",attrs={"class":"ratings-bar"}).find("strong").text  #Ratingi Çeken Kod
                             step33 = step1.find_all("p", attrs={"class": "text-muted"})
                             step333 = step33[1].text   #Storyline
                             finish = step3, step4, step99, step5, step6, step69 ,step333
                             self.romance_pd.append(finish)

            elif tür_secim == "17":
                idenfity = [1, 51, 101, 151, 201, 251]
                for first in idenfity:
                    sayfaların_linki = [
                        "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=sci_fi&sort=user_rating,desc&start=" + str(
                            first) + "&ref_=adv_nxt"]
                    for sayfaxtxt in sayfaların_linki:
                        rr=requests.get(sayfaxtxt)
                        soup2 = BeautifulSoup(rr.content, "lxml")
                        time.sleep(2)

                        filmisim = soup2.find_all("div", attrs={"class": "lister-item mode-advanced"})
                        for step1 in filmisim:
                             step2 = step1.find("h3", attrs={"class": "lister-item-header"})
                             step3 = step2.a.text  # filmadı

                             step4 = step2.find("span", attrs={"class": "lister-item-year text-muted unbold"}).text  #Film Tarihini Çeken Kod
                             step5 = step1.find("span", attrs={"class": "runtime"}).text.strip() #Film Süresini Çeken Kod
                             step6 = step1.find("span", attrs={"class": "genre"}).text.strip()  #Ekstra Türleri Çeken Kod
                             if step1.find("span", attrs={"class": "certificate"}):
                                    step99 = step1.find("span", attrs={"class": "certificate"}).text.strip() #Yaş Sınırını Çeken Kod
                             else:
                                    step99 = ("---")

                             step69=step1.find("div",attrs={"class":"ratings-bar"}).find("strong").text  #Ratingi Çeken Kod
                             step33 = step1.find_all("p", attrs={"class": "text-muted"})
                             step333 = step33[1].text   #Storyline
                             finish = step3, step4, step99, step5, step6, step69 ,step333
                             self.scifi_pd.append(finish)

            elif tür_secim == "18":
                idenfity = [1, 51, 101, 151, 201, 251]
                for first in idenfity:
                    sayfaların_linki = [
                        "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=sport&sort=user_rating,desc&start=" + str(
                            first) + "&ref_=adv_nxt"]
                    for sayfaxtxt in sayfaların_linki:
                        rr=requests.get(sayfaxtxt)
                        soup2 = BeautifulSoup(rr.content, "lxml")
                        time.sleep(2)

                        filmisim = soup2.find_all("div", attrs={"class": "lister-item mode-advanced"})
                        for step1 in filmisim:
                             step2 = step1.find("h3", attrs={"class": "lister-item-header"})
                             step3 = step2.a.text  # filmadı

                             step4 = step2.find("span", attrs={"class": "lister-item-year text-muted unbold"}).text  #Film Tarihini Çeken Kod
                             step5 = step1.find("span", attrs={"class": "runtime"}).text.strip() #Film Süresini Çeken Kod
                             step6 = step1.find("span", attrs={"class": "genre"}).text.strip()  #Ekstra Türleri Çeken Kod
                             if step1.find("span", attrs={"class": "certificate"}):
                                    step99 = step1.find("span", attrs={"class": "certificate"}).text.strip() #Yaş Sınırını Çeken Kod
                             else:
                                    step99 = ("---")

                             step69=step1.find("div",attrs={"class":"ratings-bar"}).find("strong").text  #Ratingi Çeken Kod
                             step33 = step1.find_all("p", attrs={"class": "text-muted"})
                             step333 = step33[1].text   #Storyline
                             finish = step3, step4, step99, step5, step6, step69 ,step333
                             self.sport_pd.append(finish)

            elif tür_secim == "19":
                idenfity = [1, 51, 101, 151, 201, 251]
                for first in idenfity:
                    sayfaların_linki = [
                        "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=thriller&sort=user_rating,desc&start=" + str(
                            first) + "&ref_=adv_nxt"]
                    for sayfaxtxt in sayfaların_linki:
                        rr=requests.get(sayfaxtxt)
                        soup2 = BeautifulSoup(rr.content, "lxml")
                        time.sleep(2)

                        filmisim = soup2.find_all("div", attrs={"class": "lister-item mode-advanced"})
                        for step1 in filmisim:
                             step2 = step1.find("h3", attrs={"class": "lister-item-header"})
                             step3 = step2.a.text  # filmadı

                             step4 = step2.find("span", attrs={"class": "lister-item-year text-muted unbold"}).text  #Film Tarihini Çeken Kod
                             step5 = step1.find("span", attrs={"class": "runtime"}).text.strip() #Film Süresini Çeken Kod
                             step6 = step1.find("span", attrs={"class": "genre"}).text.strip()  #Ekstra Türleri Çeken Kod
                             if step1.find("span", attrs={"class": "certificate"}):
                                    step99 = step1.find("span", attrs={"class": "certificate"}).text.strip() #Yaş Sınırını Çeken Kod
                             else:
                                    step99 = ("---")

                             step69=step1.find("div",attrs={"class":"ratings-bar"}).find("strong").text  #Ratingi Çeken Kod
                             step33 = step1.find_all("p", attrs={"class": "text-muted"})
                             step333 = step33[1].text   #Storyline
                             finish = step3, step4, step99, step5, step6, step69 ,step333
                             self.thriller_pd.append(finish)

            elif tür_secim == "20":
                idenfity = [1, 51, 101, 151, 201, 251]
                for first in idenfity:
                    sayfaların_linki = [
                        "https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=war&sort=user_rating,desc&start=" + str(
                            first) + "&ref_=adv_nxt"]
                    for sayfaxtxt in sayfaların_linki:
                        rr=requests.get(sayfaxtxt)
                        soup2 = BeautifulSoup(rr.content, "lxml")
                        time.sleep(2)

                        filmisim = soup2.find_all("div", attrs={"class": "lister-item mode-advanced"})
                        for step1 in filmisim:
                             step2 = step1.find("h3", attrs={"class": "lister-item-header"})
                             step3 = step2.a.text  # filmadı

                             step4 = step2.find("span", attrs={"class": "lister-item-year text-muted unbold"}).text  #Film Tarihini Çeken Kod
                             step5 = step1.find("span", attrs={"class": "runtime"}).text.strip() #Film Süresini Çeken Kod
                             step6 = step1.find("span", attrs={"class": "genre"}).text.strip()  #Ekstra Türleri Çeken Kod
                             if step1.find("span", attrs={"class": "certificate"}):
                                    step99 = step1.find("span", attrs={"class": "certificate"}).text.strip() #Yaş Sınırını Çeken Kod
                             else:
                                    step99 = ("---")

                             step69=step1.find("div",attrs={"class":"ratings-bar"}).find("strong").text  #Ratingi Çeken Kod
                             step33 = step1.find_all("p", attrs={"class": "text-muted"})
                             step333 = step33[1].text   #Storyline
                             finish = step3, step4, step99, step5, step6, step69 ,step333
                             self.war_pd.append(finish)




filmmm=filmöneri(tür_secim)












