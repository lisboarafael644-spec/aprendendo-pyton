emails = ["joao@gmail.com","maria@senac.df","pedro@outlook.com","ana@senac.df"]

print("E-mails institucionais:\n")

indice = 0

while indice < len(emails):

    if "@senac.df" in emails[indice]:
        print(emails[indice])

    indice += 1