numeros=list(range(1,101))

pares_div=[numero for numero in numeros if numero % 4 == 0]

print(pares_div)

pares_div2=(numero for numero in numeros if numero % 4 == 0)

print(type(pares_div2))

pares_div2=tuple(numero for numero in numeros if numero % 4 == 0)

print(pares_div2)
