---- DESCRIÇÃO DO PROGRAMA ----

ASD-X é um jogo estilo pedra, papel e tesoura, onde 3 movimentos são realizados por turno.
Mais informações podem ser lidas dentro do jogo, no botão "guia" no menu principal.

---- COMO INICIALIZAR ----

Para iniciar o jogo, deve-se rodar o arquivo "main.py".
Os aquivos "gameSystem.py", "players.py" e "jsonVerification.py" devem estar no mesmo diretório que o arquivo "main.py".
Uma pasta chamada assets também deve estar presente, com 2 arquivos de fonte dentro e 2 outras pastas:
    A pasta img, com todas as imagens utilizadas pelo programa.
    A pasta sfx, com todos os sons utilizados no programa.
Um arquivo "resultadosASD.json" também está presente na mesma pasta com o arquivo "main.py", porém o programa consegue criar um novo causa ele estaja faltando. Ele é onde a pontuação, nome, turnos e resultado do usuário é salva.

Este programa utiliza o pacote "pygame" para sua interface gráfica. É necessario instalá-lo caso não estaja presente no computador através do pip install.
Caso utilizando VSCode para rodar o programa, certifique-se que vocé estaja no interpretador certo para o pygame (ctrl + shift + p, -> Python: Select Interpreter).

---- COMO JOGAR ----

Após iniciar o jogo, você deve escolher 3 movimentos para a rodada através das setas do teclado, contra o oponente:
    Apertando para esquerda, você escolhe ataque, que causa dano e é forte contra especial.
    Apertando para cima, você escolhe defesa, que nega qualquer dano e é forte contra ataque.
    Apertando para direita, você escolhe especial, que cura e é forte contra defesa.
Você pode cancelar um ataque apertando backspace ou a seta para baixo.
Seu oponente também escolherá 3 movimentos aleatoriamente, pórem, você poderá ver qual um deles é antes de confirmar.
Ao confirmar seus movimentos, você podera ver o resultado da rodada.
Quando a vida de pelo menos um jogador chega a 0, o jogo acaba e você recebe sua pontuação, que é salva no computador.
