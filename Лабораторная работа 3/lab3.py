import fpdf

stats = []

# Data from 1st lab
out_calls = 36.23  # min duration
sms = 15 # 15 sms used
in_calls = 12.34 # min duration 

# cost for one out/in/sms
out_calls_cost_per1 = 2
in_calls_cost_per1 = 0
sms_cost_per1 = '1р, если 10+'

# total cost for out/in/sms
out_calls_cost = 72.46
in_calls_cost = 0
sms_cost = 5

# phone cost
phone_cost = 77.46 # rouble

# Data from 2nd lab
stats_for_internet = 172.6 # in mb
internet_cost = 86.3 # rouble

# total cost
total =  '163.76' #77.46(phone) + 86.3(internet)

# Needed for converting
stats.append(('Исходящие звонки', str(out_calls), 'Минуты', str(out_calls_cost_per1), str(out_calls_cost)))
stats.append(('СМС', str(sms), 'Штук', sms_cost_per1, str(sms_cost)))
stats.append(('Входящие звонки', str(in_calls), 'Минуты', str(in_calls_cost_per1), str(in_calls_cost)))
stats.append(('Интернет траффик', str(stats_for_internet), 'Мб', str(0.5), str(internet_cost)))

file = 'lab3.pdf'
bank_name = 'Мой Банк'
inn = 'ИНН'
kpp = 'КПП'
bik = 'БИК'
recipient = 'Захаров'
acc_num1 = '1'
acc_num2 = '2'
bill_num = '1'
bill_date = '15.05.2020'
provider = 'ОАО Мой Провайдер'
customer = 'Захаров'
cause = 'Стандартная подписка'


def converting_to_pdf():
    pdf = fpdf.FPDF()
    pdf.set_right_margin(15)
    pdf.set_left_margin(15)
    pdf.add_page()
    # adding fonts for russian letters
    pdf.add_font('DejaVu', '', os.path.join('.', 'fonts_for_fpdf', 'DejaVuSansCondensed.ttf'), uni=True)
    pdf.add_font('DejaVu', 'B', os.path.join('.', 'fonts_for_fpdf', 'DejaVuSansCondensed-Bold.ttf'), uni=True)

    pdf.set_font('DejaVu', '', 10)
    headers = [[f'Банк получателя: {bank_name}', f'БИК: {bik}'],
               [f'ИНН: {inn}', f'КПП: {kpp}', f'Сч. № {acc_num1}'],
               [f'Получатель: {recipient}', f'Сч. № {acc_num2}']]
    col_width = (pdf.w - 30) / 2
    row_height = pdf.font_size * 2
    for row in headers:
        for col in row:
            pdf.cell(col_width / 2 if 'ИНН' in col or 'КПП' in col else col_width, row_height,
                     txt=col, border=1)
        pdf.ln(row_height)

    pdf.set_font('DejaVu', 'B', 14)
    s = f'Счёт №{bill_num} от {bill_date} г.'
    margins = int((pdf.w - pdf.get_string_width(s) - 30) / 2 / pdf.get_string_width(' ')) * ' '
    pdf.write(14, margins + s)
    pdf.ln(5)
    pdf.write(14, '_' * int((pdf.w - 30) / pdf.get_string_width('_')))

    pdf.set_font('DejaVu', '', 10)
    pdf.ln(10)
    pdf.write(10, 'Поставщик')
    pdf.ln(5)
    pdf.write(10, f'(Исполнитель): {provider}')
    pdf.ln(10)
    pdf.write(10, 'Покупатель')
    pdf.ln(5)
    pdf.write(10, f'(Заказчик): {customer}')
    pdf.ln(10)
    pdf.write(10, f'Основание: {cause}')
    pdf.ln(10)

    row_height = pdf.font_size * 2
    pdf.cell(10, row_height, txt='№', border=1)  # №
    pdf.cell(70, row_height, txt='Наименование работ, услуг', border=1)  # Наименование
    pdf.cell(15, row_height, txt='Кол-вo', border=1)  # Кол-во
    pdf.cell(30, row_height, txt='Ед.', border=1)  # Ед.
    pdf.cell(25, row_height, txt='Цена', border=1)  # Ценна
    pdf.cell(25, row_height, txt='Сумма', border=1)  # Сумма
    pdf.ln(row_height)
    for row_num, row in enumerate(stats):
        pdf.cell(10, row_height, txt=str(row_num + 1), border=1)  # №
        pdf.cell(70, row_height, txt=row[0], border=1)  # Наименование
        pdf.cell(15, row_height, txt=row[1], border=1)  # Кол-во
        pdf.cell(30, row_height, txt=row[2], border=1)  # Ед.
        pdf.cell(25, row_height, txt=row[3], border=1)  # Ценна
        pdf.cell(25, row_height, txt=row[4], border=1)  # Сумма
        pdf.ln(row_height)

    strings = [f'Итого: {total} руб.', f'В том числе НДС: 0 руб.', f'Всего к оплате: {total} руб.']
    pdf.set_font('DejaVu', 'B', 10)
    for s in strings:
        margins = int((pdf.w - pdf.get_string_width(s) - 36) / pdf.get_string_width(' ')) * ' '
        pdf.write(10, margins + s)
        pdf.ln(5)
    pdf.ln(5)

    pdf.set_font('DejaVu', '', 10)
    strings = ['Внимание!', 'Оплата данного счета означает согласие с условиями поставки товара.',                'Уведомление об оплате обязательно, в противном случае не гарантируется наличие товара на складе.',                'Товар отпускается по факту прихода денег на р/с Поставщика, самовывозом, при наличии',
               'доверенности и паспорта.']
    for s in strings:
        pdf.write(10, s)
        pdf.ln(5)
    pdf.set_font('DejaVu', 'B', 14)
    pdf.write(14, '_' * int((pdf.w - 30) / pdf.get_string_width('_')))
    pdf.ln(20)
    pdf.set_font('DejaVu', '', 10)
    margins = int((pdf.w - pdf.get_string_width('РуководительБухгалтер') - 30) / 2 / pdf.get_string_width('_')) * '_'
    pdf.write(10, f'Руководитель{margins}Бухгалтер{margins}')

    pdf.output(name=file)


converting_to_pdf()


# In[ ]:





# In[ ]:




