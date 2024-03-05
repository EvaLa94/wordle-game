# For future reference:
## Get the information about the current timezone:

*settings.py*:
```py
TIME_ZONE = 'CET'
```

*file.py*:
```py
from django.utils import timezone

print('current time: ' + str(timezone.localtime()))
```

## How to insert the words in the database:
Open the shell in the terminal:
```py
python manage.py shell
```

Read the words from the file and save them in the database:
```py
from solver.models import FiveCharWord
with open('../words/five-char-words.txt') as reader:
    line = reader.readline().replace('\n', '')
    while line != '':
        w = FiveCharWord(word=line)
        w.save()
        line = reader.readline()
```
Check if all the words have been imported:
```py
FiveCharWord.objects.count()
```