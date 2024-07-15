import mistletoe

from bs4 import BeautifulSoup as Soup


class Lender:
    def __init__(self, markdown: str) -> None:
        self.markdown = markdown

    @property
    def html(self) -> str:
        return mistletoe.markdown(self.markdown)

    @property
    def split_by_hr(self) -> list:
        return self.html.split("<hr />")

    def parse_problem(self, problem: str) -> dict:
        soup = Soup(problem, "html.parser")
        
        h2 = soup.find_all('h2')
        h3 = soup.find_all('h3')
        
        titles = h2
        if titles == []:
            titles = h3
        else:
            titles = [*h2, *h3]
        

        title = titles[0].text
        try:
            detail = '\n'.join([detail.text for detail in titles[1:]])
        except:
            detail = ''
        
        return {
            "title": title,
            "detail": detail,
            "body": [body.text for body in soup.find_all('p')],
            "choices": [
                f"{idx + 1}. {li.text}" for idx, li in enumerate(soup.find_all("li"))
            ],
        }

    def parse_explain(self, explain: str) -> dict:
        soup = Soup(explain, "html.parser")
        explain_lines = soup.find_all("li")
        answer = explain_lines[0]
        explain = explain_lines[1:]
        return {
            "answer": answer.text,
            "explain": "\n".join([expl.text for expl in explain]),
        }

    def parse(self, problem: str, raw: bool = False) -> str:
        soup = Soup(problem, "html.parser")

        blockquote = soup.find("blockquote")
        if raw:
            exp = str(blockquote).strip()
        else:
            exp = self.parse_explain(str(blockquote))

        blockquote.decompose()
        if raw:
            prob = str(soup).strip()
        else:
            prob = self.parse_problem(str(soup))

        return {
            "problem": prob,
            "explain": exp,
        }

    def parse_all(self, raw: bool = False) -> list:
        return [self.parse(problem, raw) for problem in self.split_by_hr]

    def hide_blockquote(self):
        soup = Soup(self.split_by_hr, 'html.parser')