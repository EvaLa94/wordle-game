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

## Insert the words in the database:
Open the shell in the terminal:
```py
python manage.py shell
```

Read the words from the file and save them in the database:
```py
from solver.models import FiveCharWord
with open('../words/five-char-words.txt') as reader:
    line = reader.readline()
    while line != '':
        line = line.replace('\n', '')
        w = FiveCharWord(word=line)
        w.save()
        line = reader.readline()
```
Check if all the words have been imported:
```py
FiveCharWord.objects.count()
```

## Clean the table:
```py
from solver.models import FiveCharWord
FiveCharWord.objects.all().delete()
```

## Query the database with regex:
```py
from django.db.models import Q
from solver.models import FiveCharWord

green_letters = '.a..o' # . means every character
yellow_letters = 'ao'
grey_letters = 'tuisflbcmp'

condition = Q(word__regex=r'{}'.format(green_letters)) 
condition &= Q(word__regex=r'[{}]'.format(yellow_letters)) # include letters
condition &= ~Q(word__regex=r'[{}]'.format(grey_letters)) #exclude letters

FiveCharWord.objects.filter(condition)
```