import os
def logo():
	
	if os.name=='nt':
		os.system('cls')
	else:
		os.system('clear')
	print('''
##### ###### #####  #    # #    # #    #          ####  #####  #   # 
  #   #      #    # ##  ## #    #  #  #          #      #    #  # #  
  #   #####  #    # # ## # #    #   ##            ####  #    #   #   
  #   #      #####  #    # #    #   ##                # #####    #   
  #   #      #   #  #    # #    #  #  #          #    # #        #   
  #   ###### #    # #    #  ####  #    #          ####  #        #   
                                         #######    
                                         created by AnoniwQwerty
                                         my chanel: @anonims_blog  ''')




def warning():
	if os.name=='nt':
		os.system('cls')
	else:
		os.system('clear')

	print('''MIT License

Copyright (c) 2020 anonimQwerty

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


AUTHOR ISN'T RESPONSIBLE FOR THE USE OF THE SCRIPT!!!!!!!!!!!!!!!!!!











''')
	print('''Лицензия MIT
Copyright © 2020 anonimQwerty
Данная лицензия разрешает лицам, получившим копию
данного программного обеспечения и сопутствующей документации (в дальнейшем именуемыми «Программное Обеспечение»), 
безвозмездно использовать Программное Обеспечение без ограничений, включая неограниченное право 
на использование, копирование, изменение, слияние, публикацию, распространение, сублицензирование и/или продажу 
копий Программного Обеспечения, а также лицам, которым предоставляется данное Программное Обеспечение, при соблюдении следующих условий:

Указанное выше уведомление об авторском праве и данные условия 
должны быть включены во все копии или значимые части данного Программного Обеспечения.

ДАННОЕ ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПРЕДОСТАВЛЯЕТСЯ «КАК ЕСТЬ», БЕЗ КАКИХ-ЛИБО ГАРАНТИЙ, ЯВНО ВЫРАЖЕННЫХ ИЛИ 
ПОДРАЗУМЕВАЕМЫХ, ВКЛЮЧАЯ ГАРАНТИИ ТОВАРНОЙ ПРИГОДНОСТИ, СООТВЕТСТВИЯ ПО ЕГО КОНКРЕТНОМУ 
НАЗНАЧЕНИЮ И ОТСУТСТВИЯ НАРУШЕНИЙ, НО НЕ ОГРАНИЧИВАЯСЬ ИМИ. 
НИ В КАКОМ СЛУЧАЕ АВТОРЫ ИЛИ ПРАВООБЛАДАТЕЛИ НЕ НЕСУТ ОТВЕТСТВЕННОСТИ ПО КАКИМ-ЛИБО ИСКАМ, 
ЗА УЩЕРБ ИЛИ ПО ИНЫМ ТРЕБОВАНИЯМ, В ТОМ ЧИСЛЕ, ПРИ ДЕЙСТВИИ КОНТРАКТА, ДЕЛИКТЕ ИЛИ ИНОЙ СИТУАЦИИ, 
ВОЗНИКШИМ ИЗ-ЗА ИСПОЛЬЗОВАНИЯ ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ ИЛИ ИНЫХ ДЕЙСТВИЙ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ.

ДРУГИМИ СЛОВАМИ АВТОРУ(ТОЕСТЬ МНЕ) АБСОЛЮТНО ПОХУЙ КАК ВЫ БУДЕТЕ ИСПОЛЬЗОВАТЬ МОЙ СКРИПТ ВЕДЬ 
ОТВЕТСВЕННОСТЬ ЗА ЕГО ИСПОЛЬЗОВАНИЕ Я(АВТОР СКРИПТА) НЕ НЕСУ!!!!!!!!)

ПРОДОЛЖАЯ ИСПОЛЬЗОВАТЬ МОЙ СКРИПТ ВЫ РИСКУЕТЕ СЕСТЬ НА БУТЫЛКУ ЗА СОЗДАНИЕ ВРЕДОНОСНОГО ПО.
МОЙ СКРИПТ ВЫ ИСПОЛЬЗУЕТЕ НА СВОЙ СТРАХ И РИСК!!!!!!!

ЕСЛИ ВЫ СОГЛАШАЕТЕСЬ С ДАННЫМ СОГЛАШЕНИЕМ НАЖМИТЕ У.
''')
	answer=input('Continue y/n: ')
	if answer.lower()=='y':
		print(123)
		logo()
	else:
		pass