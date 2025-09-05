# คำสั่ง Brake / Continue 
# brake ใน loop ทำงานเมื่อใด จบ loop ทันที
# continue ใน loop ทำงานเมื่อใด จบ loop รอบนั้นทันที ให้ไปรอบต่อไป 

for aa in range(5) :
    if aa == 2 :
        break
    print(aa, 'Hi...')

print('------------------------------------')
for aa in range(5) :
    if aa == 2 :
        continue
    print(aa, 'Hi...')
    