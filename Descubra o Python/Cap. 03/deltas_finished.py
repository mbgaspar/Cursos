#
# Arquivo de exemplo para uso da classe timedeltas
#
import emoji
print(emoji.emojize(':point_up:', use_aliases=True))

from datetime import date, time, datetime, timedelta

def deltaTempo():
    delta = timedelta(days = 86, hours = 8532, minutes = 7645)
    print(delta)

    hoje = datetime.now()
    print("Data no futuro: " , hoje + delta)
    print("Data no passado: ", hoje - delta)

deltaTempo()

print(emoji.emojize(':point_up:', use_aliases=True))