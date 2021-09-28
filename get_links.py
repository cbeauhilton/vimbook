from requests_html import HTMLSession
from urllib.parse import quote_plus

session = HTMLSession()


def get_top_links(url: str):

    r = session.get(url)
    links = [link for link in r.html.absolute_links]

    return links


def get_subject_links(url: str):
    r = session.get(url)
    subjects = r.html.find("#content", first=True)
    links = [link for link in subjects.absolute_links]
    return links


def get_html(url: str):
    r = session.get(url)
    content = r.html.find("#content", first=True)
    return content.html


links = get_top_links("https://medsites.vumc.org/commodorecompendium/introduction")

for link in links:
    try:
        subjects = get_subject_links(link)
        for subject in subjects:
                content = get_html(subject)
                file_name = f"content/{quote_plus(subject)}"
                with open(file_name, "w") as f:
                    f.write(content)
    except Exception as exc:
        print(exc)
