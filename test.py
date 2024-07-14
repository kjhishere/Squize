from modules import Physics, Chemistry, Biology, Earth
from modules import Gemini

ph = Physics()
ch = Chemistry()
bi = Biology()
er = Earth()

print(ph("역학과 에너지", "운동"))
print(ch("역동적인 화학 반응", "동적 평형"))
print(bi("생태계와 상호 작용", "개체군의 특성"))
print(er("지구의 역사", "지질시대의 환경과 생물"))

bard = Gemini()
print(ph("역학과 에너지", "운동"))
print(bard(ph("역학과 에너지", "운동")))
