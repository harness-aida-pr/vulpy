 ```python
import chardet

def detect_encoding(text):
  return chardet.detect(text)['encoding']
```