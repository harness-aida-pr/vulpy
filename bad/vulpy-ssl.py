 ```python
from secrets import token_urlsafe

app.config['SECRET_KEY'] = token_urlsafe(32)
```