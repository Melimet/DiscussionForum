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

## Linkkejä

Test account: username = tester password = tester

Heroku : https://civilizeddiscussionforum.herokuapp.com/

Nykyinen tietokantakaavio(Muutoksia todennäköisesti tulossa): https://github.com/Melimet/DiscussionForum/blob/master/documentation/DiscussionForumDatabaseChart.png

Userstories: https://github.com/Melimet/DiscussionForum/blob/master/documentation/userstories.md

Create table-lausekkeet: https://github.com/Melimet/DiscussionForum/blob/master/documentation/CreateTableCommands
