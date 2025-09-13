import requests

SERVER = "http://127.0.0.1:8000"

def otpremi(putanja):
    with open(putanja, "rb") as f:
        fajlovi = {"fajl": (putanja, f)}
        r = requests.post(f"{SERVER}/otpremi", files=fajlovi)
        print(r.json())

def preuzmi(ime_fajla, sacuvaj_kao):
    r = requests.get(f"{SERVER}/preuzmi", params={"ime": ime_fajla}, stream=True)
    if r.status_code == 200:
        with open(sacuvaj_kao, "wb") as f:
            f.write(r.content)
        print(f"Fajl '{ime_fajla}' je preuzet i sačuvan kao '{sacuvaj_kao}'")
    else:
        print("Greška:", r.json())

if __name__ == "__main__":
    # primer: otpremi lokalni fajl test.txt i preuzmi ga nazad
    otpremi("test.txt")
    preuzmi("test.txt", "kopija.txt")
