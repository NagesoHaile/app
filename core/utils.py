base_url = 'http://localhost:8000'
def make_url(p,total_pages,limit):
    if p<1 or p>total_pages:
        return None
    return f"{base_url}/page={p}&limit={limit}"