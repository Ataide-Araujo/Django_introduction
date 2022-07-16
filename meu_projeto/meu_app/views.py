from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome} de {idade} anos</h1>')

def soma(request, num1:int, num2:int):
    soma = num1 + num2
    return HttpResponse(f'<h1>{num1} + {num2} = {soma}</h1>')

def subtrai(request, num1:int, num2:int):
    sub = num1 - num2
    return HttpResponse(f'<h1>{num1} - {num2} = {sub}</h1>')

def multiplica(request, num1:int, num2:int):
    mult = num1 * num2
    return HttpResponse(f'<h1>{num1} * {num2} = {mult}</h1>')

def divide(request, num1:int, num2:int):
    div = num1 / num2
    return HttpResponse(f'<h1>{num1} / {num2} = {div}</h1>')