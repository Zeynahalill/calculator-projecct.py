# hesap makinesi terminal?
x = float(input("lutfen islem yapmak istediginiz ilk sayiyi giriniz"))
y = float(input("lutfen islem yapmak istediginiz ilk sayiyi giriniz"))
islem = input(
    "lutfen yapmak istediginiz islemi seciniz toplama=+,cikarma=-,carpma=*,bolme=/")
if islem == "+":
    print("isleminizin sonucu ", x+y)
elif islem == "-":
    print("isleminizin sonucu ", x-y)
elif islem == "*":
    print("isleminizin sonucu ", x*y)
elif islem == "/":
    print("isleminizin sonucu ", x/y)
