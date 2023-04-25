import re

chat_list = []
with open('../private-information/chat_hist.txt', encoding="utf8") as f:
    lines = f.readlines()
    chat_list.append(lines)

carryover = ""
hasCarry = False
output_chatlist = []

for i in chat_list[0][::-1]:
    if re.match('\d\d\d\d/\d\d/\d\d, \d\d:\d\d -',i):
        if hasCarry:
            i = i.strip() + " " + carryover + "\n"
            hasCarry = False
            carryover = ""
        output_chatlist.append(i)
    else:
        hasCarry = True
        carryover = i.strip() + " " + carryover

with open("../private-information/chat_hist_nocarry.txt", mode="w", encoding="utf8") as f:
     for line in output_chatlist[::-1]: f.write(line)