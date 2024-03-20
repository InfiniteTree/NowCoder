import sys

def handle(news, anony):
    newsChar = sorted(news)
    anonyChar = sorted(anony)
    return newsChar == anonyChar

newspaper = input().split()
anonymousLetter = input().split()
res = True
for anony in anonymousLetter:
    for i in range(len(newspaper)):
        news = newspaper[i]
        if len(anony) == len(news) and handle(news, anony):
            newspaper[i] = " "
            break
        if i == len(newspaper) - 1:
            res = False
    if not res:
        break

print(str(res).lower())