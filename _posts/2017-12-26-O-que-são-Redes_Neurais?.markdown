---
layout: post
title:  "O que são Redes Neurais?"
date:   2017-12-26
---
<dt>Para começarmos temos que entender primeiramente o funcionamentos de nosso neurôions.</dt>

<p class="intro"><span class="dropcap"> O</span>Comportamento dos Neurônios 
<figure>
	<img src="{{ '/assets/img/Post_Img/1.jpg' | prepend: site.baseurl }}" alt=""> 	
</figure>
Os neurônios são as células que formam o nosso cérebro. Elas são compostas basicamente por três partes: os dentritos, que captam informações ou do ambiente ou de outras células, o corpo celular ou Soma, responsável pelo processamento das informações, e um axônio, para distribuir a informação processada para outros neurônios ou células do corpo. Só que uma célula dificilmente trabalha sozinha. Quanto mais células trabalharem em conjunto, mais elas podem processar e mais eficaz torna-se o trabalho. Logo, para o melhor rendimento do sistema são necessários muitos neurônios.

<p class="intro"><span class="dropcap"> D</span>os Neurônios às Redes Neurais
<figure>
	<img src="{{ '/assets/img/Post_Img/2.jpg' | prepend: site.baseurl }}" alt=""> 	
</figure>
Foi pensando em como os neurônios trabalham que pesquisadores desenvolveram neurônios artificiais. Cada um tem dois ou mais receptores de entrada, responsáveis por perceberem um determinado tipo de sinal. Eles também possuem um corpo de processadores, responsável por um sistema de feedback que modifica sua própria programação dependendo dos dados de entrada e saída. Finalmente, eles possuem uma saída binária para apresentar a resposta “Sim” ou “Não”, dependendo do resultado do processamento.
Um neurônio artificial é capaz de um único processamento. Cada entrada recebe somente um tipo de sinal ou informação. Como um neurônio pode possuir várias entradas, então ele pode perceber diferentes sinais. Porém, ligar vários neurônios similares em rede, faz com que o sistema consiga processar mais informações e oferecer mais resultados.
Por exemplo, é possível criar um sistema para identificação de bananas e maças. Para tal, cria-se neurônios sensíveis a cor e forma. Os de cor percebem o amarelo e o vermelho. Os de forma percebem o redondo e o comprido. Cada neurônio, então, possui quatro entradas, uma para cada informação.
Para obter um melhor rendimento do sistema, cria-se uma rede em camadas: uma primeira camada com quatro neurônios (um para cada sinal de entrada), uma segunda camada oculta de processamento com três neurônios e uma camada de saída com dois neurônios, um para avisar quando é uma maça e outro para avisar quando é uma banana.

<dt>O segredo não está na arquitetura dessa rede, mas na forma como ela processa: Redes Neurais não rodam programas, elas aprendem! </dt>
<figure>
	<img src="{{ '/assets/img/Post_Img/3.jpg' | prepend: site.baseurl }}" alt=""> 	
</figure>
<p class="intro"><span class="dropcap"> O</span>aprendizado das Redes Neurais

Não existe uma programação pré-definida dos neurônios artificiais, como existem nas portas lógicas utilizadas nos circuitos computacionais. Ao invés disso, eles possuem um sistema de feedback que modifica sua programação. Cada informação processada gera um peso, dependendo do resultado. Se for um acerto, ela ganha um ponto, se for um erro, ela perde meio ponto.
Dessa forma, a rede neural do exemplo acima testa várias vezes a percepção do objeto. A cada acerto, os neurônios envolvidos no processamento ganham um ponto e aquela rede é reforçada. A cada erro, esses neurônios perdem meio ponto. Dessa forma, o sistema cria a rotina de seguir o caminho com mais pontos sempre. Quanto mais tentativas, mais aprimorado fica o sistema, chegando, ao final de um processo de aprendizado, a executar tarefas quase sem erro algum.

<p class="intro"><span class="dropcap"> I</span>nteligência Artificial (IA)

As redes neurais são principalmente utilizadas para criar sistemas de inteligência artificial. Os computadores tradicionais podem fazer isso de forma simulada, mas sua principal função é seguir regras ou comandos oferecidos pelo usuário. Assim, a inteligência artificial gerada por computadores tradicionais são simulações de inteligência real, ou seja, apresentam respostas segundo regras e comandos de um programa pré-estabelecido.
<figure>
	<img src="{{ '/assets/img/Post_Img/4.jpg' | prepend: site.baseurl }}" alt=""> 	
</figure>

Acontece que a verdadeira inteligência não é a capacidade de seguir regras, mas sim a capacidade de resolver problemas. Mais inteligente é o sistema que consegue resolver problemas diferentes de forma eficaz. Baseado nisso, temos então duas formas diferentes de inteligência artificial, ou IA, a simbólica e a conexionista.
A IA simbólica simula o comportamento inteligente. Ela é baseada em uma programação que indica quais respostas devem ser dadas diante de determinados comandos. Essa IA é a utilizada em programas “inteligentes”, como corretores ortográficos ou simuladores dos mais variados. A questão é que esses programas dificilmente aprendem coisas novas, somente se você incluir novas programações. Essa é a IA mais comum.
A IA conexionista simula a estrutura do cérebro, pois acredita-se que a inteligência está na forma de processar informação e não na informação processada. Como o sistema do cérebro é inteligente, usa-se tal modelo para desenvolver IA. Assim, os sistemas de IA baseados em redes neurais conseguem aprender com seus erros e executar diferentes processos, independente de instruções.
Fonte:TehcMundo
Fonte:<a href="https://www.tecmundo.com.br/programacao/2754-o-que-sao-redes-neurais-.htm">Fonte:TehcMundo</a>




