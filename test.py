import json

from modules import Physics, Chemistry, Biology, Earth
from modules import Gemini, Lender

ph = Physics()
ch = Chemistry()
bi = Biology()
er = Earth()


def solve(pt):
    bard = Gemini("gemini-1.5-flash")
    response = bard(pt)
    lender = Lender(response)
    print(pt)
    print("===" * 8)
    problems = lender.parse_all()
    print(json.dumps(problems, ensure_ascii=False))


pts = [
    ph("역학과 에너지", "운동"),
    ch("역동적인 화학 반응", "동적 평형"),
    bi("생태계와 상호 작용", "개체군의 특성"),
    er("지구의 역사", "지질시대의 환경과 생물"),
]

solve(pts[1])
