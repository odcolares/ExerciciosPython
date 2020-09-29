from random import randint
from time import sleep
comp = randint(0, 5)
jg = int(input('Qual o numero que eu escolhi? '))
print('Loading...')
sleep(1)
if jg == comp:
    print('Parabens vc escolhe o numero {} o mesmo que eu pensei {}'.format(jg, comp))
else:
    print('Ha ha ha vc errou eu escolhe o numero {} e nao {}'.format(comp, jg))
