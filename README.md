# Nepgeocode *A library for easy access to geological codes of district and municipalites in Nepal.*

## Installation
```zsh
pip install nepgeocode
```

## Use
```python
from geocode.geocode import get_code

get_code('Dhankuta') #code for Dhankuta district
get_code('Kathmandu') #code for Kathmandu district
get_code('Kathmandu','Kathmandu') #code for Kathmandu municpality
```

*If there are municipalites of same name, then you must pass the district name to the function get_code() for retrieving the code.*
###For example:
```python
get_code('Tribeni') #it will return None
```
### Correct way:
```python
get_code('Tribeni','Rolpa') #it will return the code for Tribeni municipality in Rolpa
```

### Also, some of the newly named district may not be available. For eg: Nawalpur.
### You still need to use Nawaparasi East or Nawalparasi West for retrieving the code.



