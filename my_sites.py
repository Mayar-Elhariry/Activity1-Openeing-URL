import webbrowser
sites = {
    1: ("Google", "https://www.google.com"),
    2: ("YouTube", "https://www.youtube.com"),
    3: ("Wikipedia", "https://www.wikipedia.org"),
    4: ("Reddit", "https://www.reddit.com"),
    5: ("GitHub", "https://www.github.com")
}
def open_site(url):
    try:
        webbrowser.open(url)
        print(f"Opening {url}...")
    except Exception as e:
        print(f"Failed to open the website. Error: {e}")