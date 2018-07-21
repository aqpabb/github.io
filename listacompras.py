# -- coding: utf-8 --
from datetime import datetime
import subprocess

#Variáveis Globais
LC=[]   # Lista de Compras

#Declarações de Funções
#-----------------------------------------------------------
def leListaCompras():
	del LC[:]
	try:
		with open('listacompras.txt', 'r') as arq:
			for linha in arq:
				try:
					linha = linha.replace('\n','')
					s = linha.split(",")
					if(len(s)>2):
						LC.append(s[0] + ',' + s[1] + ',' + s[2])
				except ValueError:
					pass
	except IOError as err:
		print('Erro Arquivo: listacompras.txt' + str(err))

#-----------------------------------------------------------
def verLista():
    # Verifica/Atualiza Lista de Compras
    subprocess.call('notepad.exe listacompras.txt', shell=True)

#-----------------------------------------------------------
def retDataHora():
	now = datetime.now()
	return('%d/%d/%d às %d:%d:%d' % (now.day,now.month,now.year,now.hour,now.minute,now.second))

#-----------------------------------------------------------
def criaHTML():
	pagina = open("index.html","w",encoding="ISO-8859-15")
	pagina.write("""
<html lang="pt-br">
<head>
	<meta charset="ISO-8859-15"/>
	<title>Lista de Preços</title>
<style type="text/css">
body {
    background-color: white; 
} 
h1 { 
    color: red; 
    padding: 0px; 
	font-size: 50px;
}
h2 { 
    color: blue; 
    padding: 0px; 
	font-size: 20px;
	text-align: center;
}
h3 { 
    color: green; 
    padding: 0px; 
	font-size: 35px;
}
div#cabecalho {
	font-family: 'FonteLogo', sans-serif;
	color: #606060;
	text-shadow: 1px 1px 1px rgba(0,0,0,.6);
	margin-bottom: 0px;
	text-align: center;
}
table#tablista {
	border: 3px solid #606060;
	border-spacing: 5px;
	margin-left: auto;
	margin-right: auto;	
	font-size: 30px;
	font-weight: bolder;
}
</style>
<script>
	function EscreveData() {
		var mydate=new Date()
		var year=mydate.getYear()
		if (year < 1000)
			year+=1900
		var day=mydate.getDay()
		var month=mydate.getMonth() + 1
		var daym=mydate.getDate()
		if (daym<10)
			daym="0"+daym
		document.write(daym +"/"+month + "/" +year)
}
</script>
</head>

<body>
<div id="cabecalho">
	<h1>Lista de Compras<h1>
	<h2>Data Atual:<script>EscreveData();</script></h2>
</div>

<table id="tablista" border='1'>

""")
	pagina.write('<h2>Atualizada em: ' + retDataHora() +'<h2>\n')
	for linha in LC:
		pagina.write('<tr>\n')
		s = linha.split(',')
		pagina.write('<td>' + s[0] + '</td>\n')
		pagina.write('<td>' + s[1] + '</td>\n')
		pagina.write('<td>' + s[2] + '</td>\n')
		pagina.write('</tr>\n')
	pagina.write("""
</table>
</body>
</html>
""")

#-----------------------------------------------------------
def abreComandosGit():
    subprocess.call('notepad.exe comandos_git.txt', shell=True)

#-----------------------------------------------------------
# Aqui começa o programa

#verLista()
leListaCompras()
criaHTML()
abreComandosGit()







