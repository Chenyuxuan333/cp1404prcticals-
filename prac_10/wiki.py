import wikipedia

def main():
    """Program to search Wikipedia and display page details."""
    print("Wikipedia Search")
    search_term = input("Enter page title: ").strip()
    while search_term != "":
        try:
            # Search for the page with autosuggest disabled
            page = wikipedia.page(search_term, auto_suggest=False)
            print_page_details(page)
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f"Page id \"{search_term}\" does not match any pages. Try another id!")
        search_term = input("Enter page title: ").strip()
    print("Thank you.")


def print_page_details(page):
    """Print details of a Wikipedia page.

    Args:
        page: Wikipedia page object
    """
    print(page.title)
    print(page.summary)
    print(page.url)
    print()  # Add blank line for separation


if __name__ == "__main__":
    main()