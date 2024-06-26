import requests

BASE_URL = 'http://localhost:5000'

# ----- USER API -----


# DZIAŁA POPRAWNIE
def add_user(username, email, password):
    url = f'{BASE_URL}/users'
    data = {
        "username": username,
        "email": email,
        "password": password
    }
    response = requests.post(url, json=data)
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Błąd dekodowania JSON:", response.text)


# DZIAŁA POPRAWNIE
def modify_user(user_id, username, email, password):
    url = f'{BASE_URL}/users/{user_id}'
    new_data = {
        "username": username,
        "email": email,
        "password": password
    }
    response = requests.put(url, json=new_data)
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Błąd dekodowania JSON:", response.text)


# DZIAŁA POPRAWNIE
def delete_user(user_id):
    url = f'{BASE_URL}/users/{user_id}'
    response = requests.delete(url)
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Błąd dekodowanie JSON:", response.text)


# ----- GNOME API -----


# DZIAŁA POPRAWNIE
def add_gnome(name, description, location, image):
    url = f'{BASE_URL}/gnomes'
    data = {
        "name": name,
        "description": description,
        "location": location,
        "image": image
    }
    response = requests.post(url, json=data)
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Błąd dekodowania JSON:", response.text)


# DZIAŁA POPRAWNIE
def modify_gnome(gnome_id, name, description, location, image):
    url = f'{BASE_URL}/gnomes/{gnome_id}'
    new_data = {
        "name": name,
        "description": description,
        "location": location,
        "image": image
    }
    response = requests.put(url, json=new_data)
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Błąd dekodowania JSON:", response.text)


# DZIAŁA POPRAWNIE
def delete_gnome(gnome_id):
    url = f'{BASE_URL}/delete_gnome/{gnome_id}'
    response = requests.delete(url) 
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Błąd dekodowania JSON:", response.text)


# ----- VISITED GNOMES API -----


# DZIAŁA POPRAWNIE
def add_visited_gnome(user_id, gnome_id):
    url = f'{BASE_URL}/users/{user_id}/gnomes/{gnome_id}'
    response = requests.post(url)
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Błąd dekodowania JSON:", response.text)


# ----- ACHIEVEMENT API -----


# DZIAŁA POPRAWNIE
def add_achievement(name, condition):
    url = f'{BASE_URL}/achievements'
    data = {
        "name": name,
        "condition": condition
    }
    response = requests.post(url, json=data)
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Błąd dekodowania JSON:", response.text)


# DZIAŁA POPRAWNIE
def modify_achievement(achievement_id, name, condition):
    url = f'{BASE_URL}/achievements/{achievement_id}'
    new_data = {
        "name": name,
        "condition": condition
    }
    response = requests.put(url, json=new_data)
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Błąd dekodowania JSON:", response.text)


# ----- USERS' ACHIEVEMENTS API -----


# DZIAŁA POPRAWNIE
def unlock_achievement(user_id, achievement_id):
    url = f'{BASE_URL}/users/{user_id}/achievements/{achievement_id}'
    response = requests.post(url)
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Błąd dekodowania JSON:", response.text)


# ----- OTHER -----


# DZIAŁA, ALE ZBĘDNE
def list_gnomes():
    url = f'{BASE_URL}/gnomes'
    response = requests.get(url)
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Błąd dekodowania JSON:", response.text)

def list_user_gnome(user_id, gnome_id):
    url = f'{BASE_URL}/users/{user_id}/gnomes/{gnome_id}'
    response = requests.get(url)
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Błąd dekodowania JSON:", response.text)


if __name__ == '__main__':
    # ----- TESTS -----

    # add_user("art", "something@gmal.com", "thisispassword")
    """
    add_gnome("Papa Krasnal", "Najstarszy w mieście", "51.107175, 17.031997|Świdnicka", "papa.png")
    add_gnome("Grajek", "Utalentowany wirtuoz gitary", "51.108622, 17.035058|Oławska 11", "grajek.png")
    add_gnome("Życzliwek", "Jeden z najsłynniejszych we Wrocławiu", "51.110578, 17.031292|Rynek Ratusz 7/9", "zyczliwek.png")
    add_gnome("Syzyfki", "Od lat pchają tę samą kulę, niczym Syzyf", "51.108928, 17.032869|Świdnicka 1", "syzyfki.png")
    add_gnome("Rzeźnik", "Krasnoludzki sprzedawca wędlin", "51.112078, 17.030964|Jatki 11", "rzeznik.png")
    add_gnome("Pracz Odrzański", "Nieprzerwanie myje w Odrze ubrania", "51.113636, 17.040031|Katedralna przy moście Piaskowym", "pracz.png")
    add_gnome("Szermierz z parasolem", "Stoi dumnie przy uniwersytecie", "51.113981, 17.034247|plac Uniwersytecki 1", "szermierz.png")
    add_gnome("Strażnik Śpioch", "Niech nikt go nie budzi na służbie", "51.111261, 17.030681|Św. Mikołaja 1", "straznik.png")
    add_gnome("Więziennik", "Odsiedział swoje, jednak ku przestrodze innym nadal siedzi za kratami", "51.112514, 17.032489|Więzienna 6", "wieziennik.png")
    add_gnome("Helpik", "Razem z Bulbulkiem obserwują ludzi w wodzie", "51.105569, 17.034528|Teatralna 10/12", "helpik.png")
    add_gnome("Bulbulek", "Pływanie to jego pasja", "51.105569, 17.034528|Teatralna 10/12", "bulbulek.png")
    # add_gnome("Test", "Test API", "Jakiś adres", "test.png")
    # modify_gnome(1, "Papa Krasnal", "Najstarszy w mieście", "Świdnicka", "papa.png")
    # modify_gnome(11, "Test2", "Test API 2", "Jakiś adres 2", "test2.png")
    # delete_gnome(11)
    add_gnome("Meloman", "Znawca dobrej muzyki", "51.108622, 17.035058|Oławska 11", "meloman.png")
    add_gnome("Krasnale wodne: Puszczający Stateczki", "Robienie papierowych statków to dla niego chleb powszedni", "51.105378, 17.0331|pl. Teatralny 4", "kwstateczki.png")
    add_gnome("Krasnale wodne: Karmiący Ptaki", "Dzięki niemu żaden ptaszek nie zazna głodu", "51.105379, 17.0331|pl. Teatralny 4", "kwptaki.png")
    add_gnome("Krasnale wodne: Ogrodnik", "Gruntownie dba o krzaki przy fontannie", "51.105377, 17.0331|pl. Teatralny 4", "kwogrodnik.png")
    add_gnome("Krasnale wodne: Aktor", "Zaprasza przechodniów na seans", "51.105378, 17.0331|pl. Teatralny 4", "kwaktor.png")
    add_gnome("Krasnale wodne: Parasolnik", "Chroni żabę w koronie przed wodą", "51.105378, 17.0328|pl. Teatralny 4", "kwparasolnik.png")
    add_gnome("Krasnale wodne: Wierzbownik", "Króluje nad okolicą w centrum fontanny", "51.105376, 17.0328|pl. Teatralny 4", "kwwierzbownik.png")
    add_gnome("Krasnale wodne: Zbierający Wodę", "U niego żadna kropla nie może się zmarnować", "51.105379, 17.0331|pl. Teatralny 4", "kwzbierajacy.png")
    add_gnome("Obieżysmak", "Nic, co jadalne, nie jest mu obce", "51.110686, 17.032772|Rynek 49", "obiezysmak.png")
    add_gnome("Teatroman", "Zaprasza gości na do środka teatru", "51.112122, 17.028761|Rzeźnicza 12", "teatroman.png")
    add_gnome("Pierożnik", "Wie wszystko o pierogach", "51.111025, 17.033772|Kuźnicza 10", "pieroznik.png")
    add_gnome("Wykształciuch", "Nauka to jego pasja", "51.107244, 17.059433|wyb. Wyspiańskiego C-13", "wyksztalciuch.png")
    add_gnome("Kinoman", "Pilnuje tego, żeby taśma filmowa kręciła się nadal", "51.109056, 17.026528|św. Antoniego 1", "kinoman.png")
    add_gnome("Bibliofil", "Koneser czytania książek", "51.105567, 17.032817|pl. Teatralny 5", "bibliofil.png")
    add_gnome("Geolog", "Wie wszystko o przeróżnych skałach i kamieniach", "51.116206, 17.030653|Cybulskiego 30-34", "geolog.png")
    add_gnome("W-Skers", "Brak mocy w nogach nie powstrzymuje go od podziwiania piękna okolicy", "51.109661, 17.031686|pod Ratuszem", "wskers.png")
    add_gnome("Ślepak", "Brak wzroku nie oznacza brak możliwości cieszenia się miastem", "51.109662, 17.031686|pod Ratuszem", "slepak.png")
    add_gnome("Głuchak", "Proszę mówić głośno i wyraźnie", "51.109660, 17.031686|pod Ratuszem", "gluchak.png")
    add_gnome("Telesfor", "Jego marzeniem jest nakręcić sagę o wrocławskich krasnalach", "51.072147, 17.006697|Karkonoska 8", "telesfor.png")
    add_gnome("Manifest", "Krasnal o niecodziennych poglądach", "51.110589, 17.031822|Rynek Ratusz 10", "manifest.png")
    add_gnome("Arcik Podróźnik", "Podróżnik, uwielbia zatrzymywać się w Art Hotelu", "51.112253, 17.030075|Kiełbaśnicza 20", "arcik.png")
    add_gnome("Żaczek", "Pomaga uczyć się dzieciom", "51.106047, 17.035689|Mennicza 21/23 SP nr 63", "zaczek.png")
    add_gnome("Szczęściarze", "Podrapać ich w nosek, a na pewno przyniosą szczęście", "51.113981, 17.034247|Wojszycka 8", "szczesciarze.png")
    add_gnome("Zakupoholik", "Kocha kupować artykuły w EPI", "51.098808, 17.028214|Komandorska 21", "zakupoholik.png")
    add_gnome("Koszykarze", "Bracia O'hurt wspólnie pilnują wózka sklepowego", "51.098808, 17.028214|Komandorska 21", "koszykarze.png")
    add_gnome("Promocjusz i Przecennik", "Dbają o naszą kieszeń przy zakupach", "51.098808, 17.028213|Komandorska 21", "promocjuszprzecennik.png")
    add_gnome("Halabardnik", "Pilnuje naszego bezpieczeństwa dzień i noc", "51.101253, 17.037631|Sukiennice 12", "halabardnik.png")
    add_gnome("Gołębnik", "Patroluje okolicę na swoim wiernym gołębiu", "51.109986, 17.031097|Rynek, restauracja Spiż", "golebnik.png")
    add_gnome("Dryndek", "Woził kiedyś listy z Gołębnikiem, teraz używa do tego telefonu", "51.109994, 17.033347|Rynek, restauracja Bernard", "dryndek.png")
    add_gnome("Kuźnik", "Metalurgia i sztuka kowalstwa nie są dla niego niczym obcym", "51.110628, 17.033653|ul. Wita Stwosza 57/58", "kuznik.png")
    add_gnome("Świetlik", "Podróżuje tramwajem 2703, nie lada wyczyn go spotkać", "51.110628, 17.033653|Tramwaj 2703", "swietlik.png")
    add_gnome("Tynkuś", "Dostał zlecenie z ratusza aby zadbać o wrocławskie kamieniczki", "51.110033, 17.031708|Sukiennice 6", "tynkus.png")
    add_gnome("Panna Pychotka", "Stoi dumnie ze swoją patelnią", "51.105122, 17.022822|Krasińskiego 36", "pychotka.png")
    add_gnome("Nowożeńcy", "Młoda para wrocławskich krasnali, dają przykład że warto znaleźć drugą połówkę", "51.110625, 17.022783|Włodkowica 20/22", "nowozency.png")
    add_gnome("Giermek", "Nie odstępuje swojego człowieka na krok", "51.112233, 17.05865|pl. Grunwaldzki 22, koło Pasażu", "giermek.png")
    add_gnome("Gasiorek", "Daje znać strażakom, kiedy pora ruszać na pomoc", "51.081536, 17.036275|Borowska 138", "gasiorek.png")
    add_gnome("Kupczyk", "Jest stałym doradcą Gildii Kupieckiej", "51.094769, 17.028319|Komandorska 66", "kupczyk.png")
    add_gnome("Ekonomek", "Rozmarzył się o dniu, kiedy będzie spał na pieniądzach", "51.090383, 17.026128|Komandorska 118/120 UE", "ekonomek.png")
    add_gnome("Ołbiniusz", "Jest rycerzem, który dba o porządek, zgodę w szkole i opiekuje się uczniami", "51.119978, 17.049675|ul. Prusa 64/74, SP nr 107", "olbiniusz.png")
    add_gnome("Botanik", "Jego ulubiona forma relaksu to wygrywanie popularnych standardów jazzowych na saksofonie z nasturcji", "51.116347, 17.047283|Sienkiewicza 23, Ogród Botaniczny", "botanik.png")
    add_gnome("Ogrodnik", "Dzielnie pcha taczkę wypełnioną...Kierownikiem", "51.116303, 17.047167|Sienkiewicza 23, Ogród Botaniczny", "ogrodnik.png")
    add_gnome("Kierownik", "Leży sobie w taczce Ogrodnika i trzyma wór z pieniędzmi", "51.116302, 17.047167|Sienkiewicza 23, Ogród Botaniczny", "kierownik.png")
    
    # add_user("jkowalski", "jkowalski@gmail.com", "jkowal")
    # add_user("anowak", "anowak@gmail.com", "anow")
    # add_user("twisniewski", "twisniewski@gmail.com", "twisnie")
    # delete_user(2)
    # delete_user(3)
    # modify_user(3, "twisniewska", "twisniewska@gmail.com", "twisnia")

    # add_visited_gnome(3, 1)
    # add_visited_gnome(2, 1)
    # add_visited_gnome(2, 3)
    # add_visited_gnome(2, 5)
    # add_visited_gnome(2, 7)
    # add_visited_gnome(2, 9)
    # add_visited_gnome(1, 9)
    # add_visited_gnome(1, 2)
    # add_visited_gnome(1, 4)
    # add_visited_gnome(1, 6)
    # add_visited_gnome(1, 8)
    # add_visited_gnome(1, 10)
    # add_visited_gnome(2, 10)
    # add_visited_gnome(1, 1)
    # add_visited_gnome(1, 2)
    # add_visited_gnome(1, 4)

    # add_achievement("first Step", "complete the tutorial")
    # modify_achievement(1, "Pierwsze kroki", "Zakończ samouczek")
    # modify_achievement(2, "Poszukiwacz krasnali", "Odwiedź 10 krasnali")
    # modify_achievement(3, "Łowca krasnali", "Odwiedź 50 krasnali")
    # modify_achievement(4, "Znawca krasnali", "Odwiedź 100 krasnali")
    # add_achievement("Pierwszy krasnal", "Odźwiedź swojego pierwszego krasnala")
    # add_achievement("Gnome seeker", "Visit 10 gnomes")
    # add_achievement("Gnome hunter", "Visit 50 gnomes")
    # add_achievement("Gnome expert", "Visit 100 gnomes")
    add_achievement("Wielki ojciec krasnali", "Odnajdź Papę Krasnala")
    # modify_achievement(6, "Więzienny los", "Odnajdź Więziennika")
    # add_achievement("Wielki ojciec krasnali", "Odnajdź Papę Krasnala")
    add_achievement("Dobroduszny", "Odnajdź Życzliwka")
    add_achievement("Trzeba sobie wyobrazić...", "Odnajdź Syzyfki")
    # add_achievement("Wegetarianizm? Co to?", "Odnajdź Rzeźnika")
    # add_achievement("Ma ubiór być na blask", "Odnajdź Pracza Odrzańskiego")
    # add_achievement("Niezwykły dżentelmen", "Odnajdź Szermierza z parasolem")
    # add_achievement("Ćśśśś...", "Odnajdź Strażnika Śpiocha")
    # add_achievement("Pora na kąpiel!", "Odnajdź Helpika lub Bulbulka")
    # add_achievement("Muzyczny odkrywca", "Odnajdź Grajka lub Melomana")
    # add_achievement("Zapraszamy na seans!", "Odnajdź co najmniej jednego Krasnala Wodnego")
    # add_achievement("Podano do stołu", "Odnajdź Obieżysmaka")
    # add_achievement("Sztuka nie zna granic", "Odnajdź Teatromana")
    # add_achievement("Ruskie czy Ukraińskie?", "Odnajdź Pierożnika")
    # add_achievement("Nauka to potęgi klucz", "Odnajdź Wykształciucha")
    # add_achievement("Niech film trwa nadal", "Odnajdź Kinomana")
    # add_achievement("Mól książkowy", "Odnajdź Bibliofila")
    # add_achievement("Żaden głaz mi nie straszny", "Odnajdź Geologa")
    # add_achievement("Ciało to tylko powłoka", "Odnajdź W-Skersa, Ślepaka lub Głuchaka")
    # add_achievement("W dzisiejszym wydaniu wiadomości...", "Odnajdź Telesfora")
    # add_achievement("Krasnale wszystkich krajów, łączcie się!", "Odnajdź Manifesta")
    # add_achievement("Dookoła świata", "Odnajdź Arcika Podróżnika")
    # add_achievement("Para za parą, główka za główką!", "Odnajdź Żaczka")
    # add_achievement("Podkowa symbolem szczęścia", "Odnajdź Szczęściarzy")
    # add_achievement("Udanych zakupów!", "Odnajdź co najmniej jednego krasnala przy EPI")
    # add_achievement("Na czatach", "Odnajdź Halabardnika")
    # add_achievement("Poczta gołębia", "Odnajdź Gołębnika")
    # add_achievement("Tak słucham?", "Odnajdź Dryndka")
    # add_achievement("Kuj żelazo, póki gorące", "Odnajdź Kuźnika")
    # add_achievement("Witamy w tramwaju 2703!", "Odnajdź Świetlika")
    # add_achievement("Konsweracja zabytków", "Odnajdź Tynkusia")
    # add_achievement("Opiekunka ogniska domowego", "Odnajdź Pannę Pychotkę")
    # add_achievement("...i że cię nie opuszczę aż do śmierci", "Odnajdź Nowożeńców")
    # add_achievement("Mały krasnal, wielka odwaga", "Odnajdź Giermka")
    # add_achievement("Strażacki bohater", "Odnajdź Gasiorka")
    # add_achievement("Mistrz handlu", "Odnajdź Kupczyka")
    # add_achievement("Bogate marzenia", "Odnajdź Ekonoma")
    # add_achievement("Honor najważniejszą z cnót", "Odnajdź Ołbiniusza")
    # add_achievement("Wśród zieleni", "Odnajdź conajmniej jednego krasnala botanicznego")
    # modify_achievement(44, "Wśród zieleni", "Odnajdź co najmniej jednego krasnala botanicznego")

    # unlock_achievement(1, 1)
    # unlock_achievement(2, 1)
    # unlock_achievement(1, 2)
    # unlock_achievement(2, 2)
    # unlock_achievement(1, 5)
    # unlock_achievement(2, 5)
    # unlock_achievement(1, 6)

    add_visited_gnome(1, 1)
    add_visited_gnome(1, 3)
    add_visited_gnome(1, 4)
    unlock_achievement(1, 1)
    unlock_achievement(1, 2)
    unlock_achievement(1, 3)
    """
    list_user_gnome(1,1)
    list_user_gnome(1,2)
    list_user_gnome(2,2)
    