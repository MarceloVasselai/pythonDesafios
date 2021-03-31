num=int(input('numero: '))

a = str(num%10)
b = str(num//10%10)
c = str(num//100%100)

inverso = int(a+b+c)

soma = num+inverso

if soma < 999:

    print ('numero {} + inverso {} é igual {}'.format(num,inverso,num+inverso))

    dig1 = (soma//100%10 * 1) + (soma//10%10 * 2) + (soma%10 * 3)

    print(dig1)

    print(dig1%10)

else:

    print ('numero {} + inverso {} é igual {}'.format(num,inverso,num+inverso))

    dig1 = (soma // 1000 % 10 * 1) + (soma // 100 % 10 * 2) + (soma // 10 % 10 * 3) + (soma % 10 * 4)

    print(soma)

    print(soma // 1000 % 10 * 1)
    print(soma //  100 % 10 * 2)
    print(soma //   10 % 10 * 3)
    print(soma %         10 * 4)

    print(dig1)

    print(dig1 % 10)

