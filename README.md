Repository git del futuro sito dei Liceo Marconi Delpino

Sito creato con [Django](https://docs.djangoproject.com/en/3.0/).

---
### Come testare il sito in locale

##### Installare le dipendenze:
```bash
pip3 install -r requirements.txt
```
##### Genera il database django:
```bash
python3 manage.py migrate --run-syncdb
```

##### (Opzionale) Creare un superuser:
```bash
python3 manage.py createsuperuser
```

##### Esegui:
```bash
python3 manage.py runserver
```
---
### Struttura delle cartelle:

- La cartella *templates* contiene tutte le pagine HTML statiche.

- La cartella *news* contiene un app django e relativi templates html per pubblicare post sul sito.

- La cartella *static* contiene tutti i file css, javascript e immagini.

- La cartella *control* contiene le configurazioni django che si applicano a tutto il sito.

---
### Lavoro in corso. 