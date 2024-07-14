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
        return {
            "title": soup.find("h3").text,
            "choices": [
                f"{idx + 1}. {li.text}" for idx, li in enumerate(soup.find_all("li"))
            ],
        }

    def parse_explain(self, explain: str) -> dict:
        soup = Soup(explain, "html.parser")
        answer, explain = soup.find_all("li")
        return {
            "answer": answer.text,
            "explain": explain.text,
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
