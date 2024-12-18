from datetime import datetime 
def get_time() -> str:
    now: datetime=datetime.now()
    return f'{now:%X}'
print(get_time())