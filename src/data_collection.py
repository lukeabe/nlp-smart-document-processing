import wikipedia

def fetch_wikipedia_content(page_title, user_agent):
    wikipedia.set_user_agent(user_agent)
    try:
        content = wikipedia.page(page_title).content
        return content
    except wikipedia.exceptions.PageError:
        raise ValueError(f"The page '{page_title}' does not exist on Wikipedia.")
    except wikipedia.exceptions.DisambiguationError as e:
        raise ValueError(f"Disambiguation error: {e.options}")
