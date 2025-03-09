# ML Mikroservisi

* Predmet: Napredne softverske arhitehture
* Autor: Luka Perković
* Broj indeksa: 2023410428
* Profesor: Miodrag Živković

----

## Opis rada

Aplikacija za opisivanje slike, odnosno unošenje http(s) URL-a slike pronađene na internetu, aplikacija će vratiti nazad tekstualni opis te iste slike.

U ovom repozitorijumu, nalazi se kod za zadatak o mikroservisima i sadrži četiri glavna komponenta:
1. Frontend: Python biblioteka Streamlit
2. Backend: Python biblioteka FastAPI
3. Model: HuggingFace model
4. k8s: Kubernetes konfiguracije

Frontend će poslati URL Backend servisu, koji će potom proslediti isti taj URL Model servisu u odgovarajućem formatu. Nakon što model izvrši generaciju teksta, Backend servis vraća rezultat nazad Frontend servisu.
Ukoliko dođe do fatalne greške na bilo kom od servisa, isključujući Frontend, aplikacija (ili website) će ostati operabilan. Ukoliko dođe do greške samo na Frontend servisu, rezultati će moći da se dobiju upotrebom 
post zahteva u odgovarajućem formatu.

Kubernetes je tu da ukoliko dođe do fatalne greške, da aplikacija bude dostupna tako što će provizirati redudantne replike i generalno imati bolju kontrolu nad deployment-om.


## Instrukcije

Da bi se ova aplikacija pokrenula na lokalnom računaru i Linux operativnom sistemu, neophodno je imati instaliran `minikube`, `docker`, i `kubectl`.

Klaster se pokreće sa `minikube start` i gasi sa `minikube stop`.
Treba primeniti konfiguracije i za to je upotrebiti:
```
./apply.sh
```

Nakon toga, da bi aplikacija bila dostupna i upotrebljiva neophodno je lansirati servis sa komandom

```
minikube service frontend-service
```
