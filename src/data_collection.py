import wikipediaapi

def fetch_wikipedia_page(title: str) -> str:
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(title)
    
    if page.exists():
        return page.text
    else:
        raise ValueError(f"Page titled '{title}' does not exist on Wikipedia.")
