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
                li.text for li in soup.find_all("li")
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
        print(str(soup))

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

    @staticmethod
    def to_html(quiz: dict):
        problem = quiz['problem']
        explain = quiz['explain']
        
        title  = f"<h2>{problem['title']}</h2>"
        detail = f"<h3>{problem['detail']}</h3>"

        body = "<ul>"
        for line in problem['body']:
            body += f"<li>{line}</li>"
        body += "</ul>"
        
        choices = "<ol>"
        for line in problem['choices']:
            choices += f"<li>{line}</li>"
        choices += "</ol>"
        
        answer  = "<details><summary>정답 및 해설</summary>"
        answer += f"<span>{explain['answer']}</span><br>"
        answer += f"<span>{explain['explain']}</span>"
        answer += "</details>"
        
        return (
            title + \
            detail + \
            body + \
            choices + \
            answer
        )