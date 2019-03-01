# Civilized Discussion Forum

## Kuvaus aiheesta
Civilized Discussion Forum on keskustelufoorumi. Käyttäjät pystyvät rekisteröitymään, kirjautumaan ja muokkaamaan omia käyttäjätietojaan. Käyttäjät pystyvät luomaan lankoja(threads) ja vastaamaan(replies) niihin. Käyttäjiä on kahdenlaisia: admineita ja peruskäyttäjiä. Langoissa ja vastauksissa on tarkoituksena viestin lisäksi näkyä lähettäjän käyttäjänimi. 

## Toiminnot
  * Langan luominen
  * Lankaan vastaaminen
  * Oman langan poistaminen
  * Admineilla kaikkien lankojen poistaminen
  * Rekisteröityminen, useita samoja käyttäjänimiä ei voi luoda
  * Kirjautuminen, uloskirjautuminen ja omien käyttäjätietojen muokkaus
  * Kirjautuneena oman käyttäjätilin poisto. Poistossa poistuu myös käyttäjän tekemät langat ja siihen tulleet vastaukset. Myös kaikki muut käyttäjän vastaukset poistuvat.
  * Langalle voi antaa pisteitä haluamansa määrän.(It's a feature!)
  

## Käyttöohje
Rekisteröidy sivustolle valitsemalla sivupalkista "Register"(Ei kannata käyttää oikeita salasanoja, koska ne tallennetaan plaintextina). Tämän jälkeen voit kirjautua sivustolle sivupalkin painikkeesta "Login". Langan voi luoda sivupalkin painikkeesta Submit a thread. Kaikki langat näkee sivupalkin painikkeesta "See all threads". Threads-sivulla pystyy poistamaan, vastaamaan ja antamaan ääniä vastauksille ja langoille. Profile sivulla pystyy muokkaamaan omia käyttäjätietojaan tai poistamaan tilinsä.

## Asennusohje(Linux only)
 * Jos et vielä käytä Linuxia voit asentaa sellaisen vaikka osoitteesta https://tutorials.ubuntu.com/tutorial/tutorial-install-ubuntu-desktop#0
 * Avaa terminaali (`Control + alt + t`)
 * Asenna python3, sqlite3 ja git komennoilla `sudo apt-get install python3.6`, `sudo apt-get install sqlite3 libsqlite3-dev`
 ja `sudo apt-get install git` (Ei kannata tehdä tätä vaihetta, jos kyseiset ohjelmat jo löytyvät.)
 * Lataa repo kirjoittamalla `git clone https://github.com/Melimet/DiscussionForum.git`
 * Mene kansioon kirjoittamalla `cd DiscussionForum`
 * Luo virtual environment komennolla `python3 -m venv venv`
 * Mene äsken luotuun environmenttiin komennolla `source venv/bin/activate`
 * Asenna tarvitut kirjastot komennolla `python3 -m pip install -r requirements.txt`
 * Sovelluksen voi nyt käynnistää komennolla `python3 run.py`
 * Sovellus pyörii nyt verkossa osoitteessa `localhost:5000`
 * Lue käyttöohjeesta ohjeet sovelluksen käyttöön
 
## Loppusanat
Kaiken kaikkiaan projekti meni ihan hyvin. Alussa suunniteltuja toiminnallisuuksia piti leikata aika rankasti, jonka takia tietokantatauluihin on jäänyt käyttämättömiä attribuutteja(esimerkiksi date_created ja date_modified threads ja replies tauluissa). Dokumentaatio on ajan tasalla ja niin myös tietokantakaavio ja tietokannan alustuslauseet. 

Python ja sen kirjastojen opettelu tuotti paljon harmaita hiuksia ja vasta projektin loppuviikoilla alkoi homma luistamaan paremmin. Koodi on mielestäni järkevää ja tietokannat on toteutettu hyvin. Lankojen vastauksiin olisi pitänyt lisätä toimintoja kuten poistaminen ja muokkaaminen, mutta aika jäi kesken. Lankojen äänestämistoiminnallisuus olisi pitänyt eritellä omaan luokkaansa, jotta ääniä olisi kyennyt antamaan vain 1/käyttäjä. 

Kurssilla opin paljon Pythonista, hieman laajemmista ohjelmointiprojekteista ja aikataulutuksen tärkeydestä. Kurssi oli mielenkiintoinen ja opetti/pakotti hakemaan tietoa muualtakin kuin pelkästään kurssimateriaaleista. Projektini kuitenkin teoriassa pystyisi toimimaan ihan oikeanakin keskustelufoorumina, joten sanoisin projektini olleen onnistunut.



## Linkkejä

Test account: username = tester password = tester  (Might not work if someone has changed test account's password so just register a new account)

Heroku : https://civilizeddiscussionforum.herokuapp.com/

Nykyinen tietokantakaavio(Muutoksia todennäköisesti tulossa): https://github.com/Melimet/DiscussionForum/blob/master/documentation/DiscussionForumDatabaseChart.png

Userstories: https://github.com/Melimet/DiscussionForum/blob/master/documentation/userstories.md

Create table-lausekkeet: https://github.com/Melimet/DiscussionForum/blob/master/documentation/CreateTableCommands
