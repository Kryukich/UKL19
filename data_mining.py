"""
Blue chips in Russia

1) Сбербанк            9) Новатэк
2) Лукойл              10) Роснефть
3) Газпром             11) Татнефть
4) АЛРОСА              12) ВТБ
5) X5 Retail Group     13) Яндекс
6) Магнит              14) Северсталь
7) МТС                 15) Норникель
8) Сургутнефтегаз

data resource https://www.finam.ru/profile/moex-akcii/company_name/export
"""
import urllib

file_link = 'http://export.finam.ru/\
GAZP_190722_190722.csv?\
market=1&em=16842&code=GAZP&apply=0&df=22&mf=6&yf=2019&\
from=22.07.2019&dt=22&mt=6&yt=2019&to=22.07.2019&p=7&\
f=GAZP_190722_190722&e=.csv&cn=GAZP&dtf=1&tmf=1&MSOR=1&\
mstime=on&mstimever=1&sep=3&sep2=1&datf=1&at=1'

'http://export.finam.ru/SBER_190723_190723.txt?market=1&em=3&code=SBER&apply=0&df=23&mf=6&yf=2019&from=23.07.2019&dt=23&mt=6&yt=2019&to=23.07.2019&p=7&f=SBER_190723_190723&e=.txt&cn=SBER&dtf=1&tmf=1&MSOR=1&mstime=on&mstimever=1&sep=1&sep2=1&datf=1&at=1'

urllib.request.urlretrieve(file_link, '/Users/Belyakov.VA/Desktop/UKL19/DATA\
/test_file.csv')
f = open("company_quotes.txt", "w")
content = page.read()
f.write(content)
f.close()
