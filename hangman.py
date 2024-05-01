import random
word_list = ["ardvark", "baboon", "camel" ]
chosen_word = random.choice(word_list)
print(f"chosen_word : '{chosen_word}'")
char_hint = []
for char in chosen_word:
    char_hint += char
print(f"char_hint : {char_hint}")
char_hint_len = len(chosen_word)
# print(type(char_hint_len))
print(f"char_hint_len : {char_hint_len}")
char_check = []
for i in range(char_hint_len):
    char_check += "⬜"
print(f"char_check : {char_check}")
guess = input("Guess a letter: ? ")

index =[]

idx = 0
print(f"Guess : {guess}")
len_ckeck = 0
len_index = 0
attempt = 0
while char_hint != char_check:
    if guess in char_hint:
        for i in char_hint:
            if guess == i:
                print(i)        
                index.append(idx)
                char_check[idx]=guess

            idx += 1  
        print(f"index :{index}")
        len_index += len(index)
        print(f"len_index : {len_index}")
        len_ckeck = char_hint_len - len(index)
        print(f"len_check : {len_ckeck}")
        print(f"char_hint_len : {char_hint_len}")
        print(f"char_check : {char_check}")
        if char_check == char_hint:
            print("You win")
            break
        elif attempt == 5: 
            print("เสียใจด้วย! คุณใช้ครบทุกครั้งลองแล้ว คำคำตอบคือ:", chosen_word)
            break
        else:
            guess = input("Guess a letter: ")
            print(f"Guess : {guess}")           
        idx = 0
        index = []
    elif attempt < 6: 
        print("ตัวอักษรนี้ไม่อยู่ในคำ!")
        attempt += 1
        print(f"ความพยายามครั้งที่ : {attempt}")
        if attempt == 5: 
            print("เสียใจด้วย! คุณใช้ครบทุกครั้งลองแล้ว คำคำตอบคือ:", chosen_word)
            break
        guess = input("Guess a letter :? ")
   
#  ตรวจสอบว่าตัวอักษรที่ผู้เล่นใส่อยู่มีในคำหรือไม่ และต้องแสดงตำแหน่งของตัวอักษรนั้นถ้ามี โดยการเปลี่ยนบรรทัดที่ 19-30 เป็น:
# if guess in chosen_word:
#         for i, char in enumerate(chosen_word):
#             if guess == char:
#                 index.append(i)
#                 char_check[i] = guess
#         print("อยู่ในคำ!")
#     else:
#         print("ไม่อยู่ในคำ!")        