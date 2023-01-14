#SISTEMA AVALIATIVO DE NOTAS
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
aulas = int(input('Aulas assistidas: '))

media = (nota1+nota2+nota3)/3
if media >= 6 and aulas >= 40:
 print('Aluno Aprovado!')
else:
 print('Aluno Reprovado!')
