with open('sayilar1') as file:
    sayilar = [int(line) for line in file]

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11
def main():
    boolean = True
    while boolean:
        girilen = input('1 İle 101 Arasında Bir Sayı Giriniz: ')
        girilen_gecerli_mi = isfloat(girilen)
        if not girilen_gecerli_mi:
            print('Harf Girmeyiniz !')
        else:
            girilen = int(girilen)
            if girilen > 100:
                print('100\'den Küçük Bir Sayı Giriniz !')
                boolean = True
            elif girilen <= 1:
                print('1\'den Büyük Bir Sayı Giriniz !')
                boolean = True
            else:
                for i in range(len(sayilar)):
                    for l in range(i+1, len(sayilar)):
                        if sayilar[i] + sayilar[l] == girilen:
                            i = i + 1
                            l = l + 1
                            print('Girilen Sayı', (i), '. Satırdaki', (sayilar[i-1]), 'Sayısı \tVe\t',
                                  (l), '. Satırdaki',(sayilar[l-1]), 'Sayısının Toplamlarına Eşittir.')
                            boolean = False
                        else:
                            boolean = False

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    main()