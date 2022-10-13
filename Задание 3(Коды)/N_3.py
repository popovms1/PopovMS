# -- coding: utf-8 --
n=int(input('Введите кол-во минут\n'))
if n >1440:
 print('Недопустимое количество минут')
else:
   h=n//60;
   m=n%60;
   if m>9 :
    print('Время','',h,':',m)
   else:
    print('Время','',h,':','0',m)