from aiogram import F, Router, types
from aiogram.types import Message, FSInputFile, CallbackQuery, message
from aiogram import Bot
from keyboards import keyboard, inline1, inline2, inline3, inline4

from keyboards import inline


router = Router()

# pht = FSInputFile('OIP.jpg', 'OIP')
b1 = FSInputFile('01. The Humanistic Psychology and Positive Psychology Connection Implicationsfor Psychotherapy Autor Andrew M. Bland, Eugene Mario Derobertis.pdf', '1. The Humanistic Psychology and Positive Psychology Connection Implicationsfor Psychotherapy Autor Andrew M. Bland, Eugene Mario Derobertis.')
b2 = FSInputFile('02. The Humanistic Psychologist Autor Eugene M. DeRobertis and Andrew M. Bland.pdf', '2. The Humanistic Psychologist Autor Eugene M. DeRobertis and Andrew M. Bland.')
b3 = FSInputFile('03. Contributions of Humanistic Psychology to Positive Psychology Autor Arthur Warmoth, Stella Resnick, Ilene Serlin.pdf', '3. Contributions of Humanistic Psychology to Positive Psychology Autor Arthur Warmoth, Stella Resnick, Ilene Serlin.')
b4 = FSInputFile('04. Existential and Humanistic Theories Autor Paul T. P. Wong.pdf', '4. Existential and Humanistic Theories Autor Paul T. P. Wong.')
b5 = FSInputFile('05. Carl Rogers and Humanistic Education Autor The Sage of Asheville.pdf', '5. Carl Rogers and Humanistic Education Autor The Sage of Asheville')
b6 = FSInputFile('06. Humanistic Psychology (the third-force) Autor Simply Psychology.pdf', '6. Humanistic Psychology (the third-force) Autor Simply Psychology.')
b7 = FSInputFile('07. Humanist, Behavioral and Sociocultural Personality Perspectives Autor Southside Psych with Mrs. Schlicht - APPsych.pdf', '7. Humanist, Behavioral and Sociocultural Personality Perspectives Autor Southside Psych with Mrs. Schlicht')
b8 = FSInputFile('08. The Humanistic Approach Autor St Thomas More Catholic School & Sixth Form College.pdf','8. The Humanistic Approach Autor St Thomas More Catholic School & Sixth Form College.')
b9 = FSInputFile('21. Humanistic Psychology, Learning and Teaching The Whole Person (Article) Jan D. Sinnott.pdf', '9. Humanistic Psychology, Learning and Teaching The Whole Person (Article) Jan D. Sinnott.')
b10 = FSInputFile('personality and depression.pdf', '10. personality and depression.')
# music = FSInputFile('music.mp3')


e1 = FSInputFile('1. The Adventures of Pinocchio Author Carlo Collodi.pdf', '1. The Adventures of Pinocchio Author Carlo Collodi.')
e2 = FSInputFile('2. Cinderella Author Charles Perrault.pdf', '2. Cinderella Author Charles Perrault')
e3 = FSInputFile('3. The sleeping beauty in the woods Author Charles Perrault.pdf', '3. The sleeping beauty in the woods Author Charles Perrault.')
e4 = FSInputFile('4. The Little Mermaid Author Hans Christian Andersen.pdf', '4. The Little Mermaid Author Hans Christian Andersen')
e5 = FSInputFile('5. Snow White and the Seven Dwarfs Author Jacob Grimm,Wilhelm Grimm.pdf', '5. Snow White and the Seven Dwarfs Author Jacob Grimm,Wilhelm Grimm.')
e6 = FSInputFile('6. Hansel and Gretel Author Madeleine Francis.pdf', '6. Hansel and Gretel Author Madeleine Francis.')
e7 = FSInputFile('7. Little Red Riding Hood Author Hagley Primary School.pdf', '7. Little Red Riding Hood Author Hagley Primary School.')
e8 = FSInputFile('8. The Ugly Duckling Author Hans Christian Andersen.pdf', '8. The Ugly Duckling Author Hans Christian Andersen.')
e9 = FSInputFile('9. Jack and the Beanstalk Author Etherley Lane Primary School.pdf', '9. Jack and the Beanstalk Author Etherley Lane Primary School.')
e10 = FSInputFile('10. The Three Little Pigs Author All Saints Ilkley.pdf', '10. The Three Little Pigs Author All Saints Ilkley.')


h1 = FSInputFile('11. The Hand author Guy de Maupassant.pdf', '1. The Hand author Guy de Maupassant.')
h2 = FSInputFile('12.-The-Mystery-of-the-Yellow-Room-Author-Gaston-Leroux.pdf', '2.-The-Mystery-of-the-Yellow-Room-Author-Gaston-Leroux.')
h3 = FSInputFile('13. The Dunwich Horror Author H. P. Lovecraft.pdf', '3. The Dunwich Horror Author H. P. Lovecraft.')
h4 = FSInputFile('14. The Invisible Man Author H. G. Wells.pdf', '4. The Invisible Man Author H. G. Wells.')
h5 = FSInputFile('15. The Monk Author Matthew Gregory Lewis.pdf', '5. The Monk Author Matthew Gregory Lewis.')
h6 = FSInputFile('16. The Moonstone Author Wilkie Collins.pdf', '6. The Moonstone Author Wilkie Collins.')
h7 = FSInputFile('17. The Woman in White Author Wilkie Collins.pdf', '7. The Woman in White Author Wilkie Collins.')
h8 = FSInputFile('18. the-hound-of-the-baskervilles-arthur-conan-doyle.pdf', '8. the-hound-of-the-baskervilles-arthur-conan-doyle.')
h9 = FSInputFile('19. The Adventures of Sherlock Holmes Author Arthur Conan Doyle.pdf', '9. The Adventures of Sherlock Holmes Author Arthur Conan Doyle.')
h10 = FSInputFile('20. Abraham Maslow Autor Dr. C. George Boeree.pdf', '10. Abraham Maslow Autor Dr. C. George Boeree.')


p1 = FSInputFile('001. The A-Z of Programming Languages author Computerworld.pdf', '1. The A-Z of Programming Languages author Computerworld.')
p2 = FSInputFile('002. Programming Languages Application and Interpretation author Shriram Krishnamurthi.pdf', '2. Programming Languages Application and Interpretation author Shriram Krishnamurthi.')
p3 = FSInputFile('003. Objective-C Notes for Professionals, GoalKicker.pdf', '3. Objective-C Notes for Professionals, GoalKicker.')
p4 = FSInputFile('004. MIPS Assembly Language Programming using QtSpim, Ed Jorgensen.pdf', '4. MIPS Assembly Language Programming using QtSpim, Ed Jorgensen.')
p5 = FSInputFile('005. Principles of Programming Languages, David Liu.pdf', '5. Principles of Programming Languages, David Liu.')
p6 = FSInputFile('006. Principles of Programming Languages, Mike Grant, Zachary Palmer, Scott Smith.pdf', '6. Principles of Programming Languages, Mike Grant, Zachary Palmer, Scott Smith.')
p7 = FSInputFile('007. Programming Persistent Memory, Steve Scargall.pdf', '7. Programming Persistent Memory, Steve Scargall.')
p8 = FSInputFile('008. The Missing Link. An Introduction to Web Development and Programming, Michael Mendez.pdf', '8. The Missing Link. An Introduction to Web Development and Programming, Michael Mendez.')
p9 = FSInputFile('009.  Assembly Language Programming with Ubuntu.pdf', '9.  Assembly Language Programming with Ubuntu.')
p10 = FSInputFile('010. Understanding Programming Languages, M. Ben-Ari.pdf', '10. Understanding Programming Languages, M. Ben-Ari.')


@router.message(F.text == '/start')
async def start(message: Message):
    # photo = open("OIP.jpg", "rb")
    # text = p1
    # await message.answer_photo(photo, document=text, reply_markup=keyboard)

    await message.answer("Welcome to Library Bot!", reply_markup=keyboard)


# @router.message(lambda c: c.data == '⬅Назад')
# async def back_handler(message: Message):
#     await message.reply("You clicked the button 'Назад'.", reply_markup=types.ReplyKeyboardRemove())




@router.message(F.text == '/help')
async def help(message: Message):
    await message.answer_contact('+998 99 612 13 80', 'Muxlisa')
    await message.answer_location(10, 2)



# @router.message()
# async def hi(message: Message):
#     response = wikipedia.summary(message.text, sentences=2)
#     await message.answer(response)




# @router.message(F.text == 'Psychology books')
# async def python(message: Message):
#     await message.answer_document(document=b1)
#     await message.answer_document(document=b2)
#     await message.answer_document(document=b3)
#     await message.answer_document(document=b4)
#     await message.answer_document(document=b5)
#     await message.answer_document(document=b6)
#     await message.answer_document(document=b7)
#     await message.answer_document(document=b8)
#     await message.answer_document(document=b9)
#     await message.answer_document(document=b10)


# @router.message(F.text == 'Ertak kitoblar')
# async def python(message: Message):
#     await message.answer_document(document=e1)
#     await message.answer_document(document=e2)
#     await message.answer_document(document=e3)
#     await message.answer_document(document=e4)
#     await message.answer_document(document=e5)
#     await message.answer_document(document=e6)
#     await message.answer_document(document=e7)
#     await message.answer_document(document=e8)
#     await message.answer_document(document=e9)
#     await message.answer_document(document=e10)

#
# @router.message(F.text == 'Linux bo`yicha kitoblar')
# async def python(message: Message):
#     await message.answer_document(document=linux)
#
#
# @router.message(F.text == 'Algorithms bo`yicha kitoblar')
# async def python(message: Message):
#     await message.answer_document(document=algo)
#
#
# @router.message(F.text == 'Git bo`yicha kitoblar ')
# async def python(message: Message):
#     await message.answer_document(document=git)

 # @router.message(F.text == 'Contact 📞')
# # async def contact(message: Message):
# #     await message.answer('Share your Contact')
# #
# #
# # @router.message(F.text == 'Location 📈')
# # async def location(message: Message):
# #     await message.answer('Share your Location')
# #
# @router.callback_query(lambda c: c.data =='Psychology books' )
# async def mus(call: CallbackQuery, bot: Bot):
#     await bot.answer_callback_query(call.id)
#     await bot.send_document(
#         chat_id=call.from_user.id, document=b1)
#     await bot.send_document(
#         chat_id=call.from_user.id, document=b2)
#     await bot.send_document(
#         chat_id=call.from_user.id, document=b3)
#     await bot.send_document(
#         chat_id=call.from_user.id, document=b4)
#     await bot.send_document(
#         chat_id=call.from_user.id, document=b5)
#     await bot.send_document(
#         chat_id=call.from_user.id, document=b6)
#     await bot.send_document(
#         chat_id=call.from_user.id, document=b7)
#     await bot.send_document(
#         chat_id=call.from_user.id, document=b8)
#     await bot.send_document(
#         chat_id=call.from_user.id, document=b9)
#     await bot.send_document(
#         chat_id=call.from_user.id, document=b10)






@router.message(F.text == 'Programming books')
async def send_books_list(message: Message):
    pbooks = ('THIS BOOKS FOR YOU 📚. \n'
             "1. The A-Z of Programming Languages author Computerworld.\n"
             "2. Programming Languages Application and Interpretation author Shriram Krishnamurthi.\n"
             "3. Objective-C Notes for Professionals, GoalKicker.\n"
             "4. MIPS Assembly Language Programming using QtSpim, Ed Jorgensen.\n"
             "5. Principles of Programming Languages, David Liu.\n"
             "6. Principles of Programming Languages, Mike Grant, Zachary Palmer, Scott Smith.\n"
             "7. Programming Persistent Memory, Steve Scargall.\n"
             "8. The Missing Link. An Introduction to Web Development and Programming, Michael Mendez.\n"
             "9.  Assembly Language Programming with Ubuntu.\n"
             "10. Understanding Programming Languages, M. Ben-Ari."
              )
    await message.answer(pbooks, reply_markup=inline)


@router.callback_query(lambda c: c.data == 'Book111')
async def send_books(call: CallbackQuery, bot: Bot):

    await bot.answer_callback_query(call.id)
    documents = [p1]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document, reply_markup=inline4)


@router.callback_query(lambda c: c.data == 'Book112')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [p2]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document, reply_markup=inline4)


@router.callback_query(lambda c: c.data == 'Book113')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [p3]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document, reply_markup=inline4)


@router.callback_query(lambda c: c.data == 'Book114')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [p4]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document, reply_markup=inline4)

@router.callback_query(lambda c: c.data == 'Book115')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [p5]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document, reply_markup=inline4)

@router.callback_query(lambda c: c.data == 'Book116')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [p6]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document, reply_markup=inline4)

@router.callback_query(lambda c: c.data == 'Book117')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [p7]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document, reply_markup=inline4)

@router.callback_query(lambda c: c.data == 'Book118')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [p8]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document, reply_markup=inline4)

@router.callback_query(lambda c: c.data == 'Book119')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [p9]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document, reply_markup=inline4)


@router.callback_query(lambda c: c.data == 'Book120')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [p10]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document, reply_markup=inline)




@router.message(F.text == 'Psychology books')
async def send_books_list(message: Message):
    books_list = ('THIS BOOKS FOR YOU 📚. \n'
        "OIP"
        "1. The Humanistic Psychology and Positive Psychology Connection Implications for Psychotherapy - Andrew M. Bland, Eugene Mario Derobertis.\n"
        "2. The Humanistic Psychologist - Eugene M. DeRobertis and Andrew M. Bland.\n"
        "3. Contributions of Humanistic Psychology to Positive Psychology - Arthur Warmoth, Stella Resnick, Ilene Serlin.\n"
        "4. Existential and Humanistic Theories - Paul T. P. Wong.\n"
        "5. Carl Rogers and Humanistic Education - The Sage of Asheville.\n"
        "6. Humanistic Psychology (the third-force) - Simply Psychology.\n"
        "7. Humanist, Behavioral and Sociocultural Personality Perspectives - Southside Psych with Mrs. Schlicht.\n"
        "8. The Humanistic Approach - St Thomas More Catholic School & Sixth Form College.\n"
        "9. Humanistic Psychology, Learning and Teaching The Whole Person (Article) - Jan D. Sinnott.\n"
        "10. Personality and Depression."
    )
    await message.answer(books_list, reply_markup=inline1)


@router.callback_query(lambda c: c.data == '1')
async def send_books_documents_photo(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [b1]
    # photos = [pht]

    for document in documents:
    #     for photo in photos:
        await bot.send_document(chat_id=call.from_user.id, document=document, reply_markup=inline4)
            # await bot.send_photo(chat_id=call.from_user.id, photo=photo)




@router.callback_query(lambda c: c.data == '2')
async def send_books_documents(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [b2]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document, reply_markup=inline4)


@router.callback_query(lambda c: c.data == '3')
async def send_books_documents(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [b3]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document, reply_markup=inline4)


@router.callback_query(lambda c: c.data == '4')
async def send_books_documents(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [b4]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document, reply_markup=inline4)

@router.callback_query(lambda c: c.data == '5')
async def send_books_documents(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [b5]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document, reply_markup=inline4)

@router.callback_query(lambda c: c.data == '6')
async def send_books_documents(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [b6]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document, reply_markup=inline4)

@router.callback_query(lambda c: c.data == '7')
async def send_books_documents(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [b7]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)

@router.callback_query(lambda c: c.data == '8')
async def send_books_documents(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [b8]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)

@router.callback_query(lambda c: c.data == '9')
async def send_books_documents(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [b9]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)

@router.callback_query(lambda c: c.data == '10')
async def send_books_documents(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [b10]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)


@router.callback_query(lambda c: c.data == '10')
async def send_books_documents(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [b10]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)

# @router.callback_query(lambda c: c.data == '⬅️back')
# async def send_books_documents(call: CallbackQuery, bot: Bot):
#     await bot.answer_callback_query(call.id)
#     documents = [b10]
#     for document in documents:
#         await bot.send_document(chat_id=call.from_user.id, document=document)


@router.message(F.text == 'Fairy tale books')
async def send_books_list(message: Message):
    books = ('THIS BOOKS FOR YOU 📚. \n'
        "1. The Adventures of Pinocchio Author Carlo Collodi.\n"
        "2. Cinderella Author Charles Perrault.\n"
        "3. The sleeping beauty in the woods Author Charles Perrault.\n"
        "4. The Little Mermaid Author Hans Christian Andersen\n"
        "5. Snow White and the Seven Dwarfs Author Jacob Grimm,Wilhelm Grimm.\n"
        "6. Hansel and Gretel Author Madeleine Francis.\n"
        "7. Little Red Riding Hood Author Hagley Primary School.\n"
        "8. The Ugly Duckling Author Hans Christian Andersen.\n"
        "9. Jack and the Beanstalk Author Etherley Lane Primary School.\n"
        "10. The Three Little Pigs Author All Saints Ilkley."
    )
    await message.answer(books, reply_markup=inline2)





@router.callback_query(lambda c: c.data == 'Book1')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [e1]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)


@router.callback_query(lambda c: c.data == 'Book2')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [e2]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)


@router.callback_query(lambda c: c.data == 'Book3')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [e3]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)


@router.callback_query(lambda c: c.data == 'Book4')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [e4]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)

@router.callback_query(lambda c: c.data == 'Book5')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [e5]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)

@router.callback_query(lambda c: c.data == 'Book6')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [e6]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)

@router.callback_query(lambda c: c.data == 'Book7')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [e7]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)

@router.callback_query(lambda c: c.data == 'Book8')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [e8]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)

@router.callback_query(lambda c: c.data == 'Book9')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [e9]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)

@router.callback_query(lambda c: c.data == 'Book10')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [e10]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)


@router.message(F.text == 'Horror books')
async def books_list(message: Message):
    hbooks = ('THIS BOOKS FOR YOU 📚. \n'
              "1. The Hand author Guy de Maupassant.\n"
              "2.-The-Mystery-of-the-Yellow-Room-Author-Gaston-Leroux.\n"
              "3. The Dunwich Horror Author H. P. Lovecraft.\n"
              "4. The Invisible Man Author H. G. Wells.\n"
              "5. The Monk Author Matthew Gregory Lewis.\n"
              "6. The Moonstone Author Wilkie Collins.\n"
              "7. The Woman in White Author Wilkie Collins.\n"
              "8. the-hound-of-the-baskervilles-arthur-conan-doyle.\n"
              "9. The Adventures of Sherlock Holmes Author.\n"
              "10. Abraham Maslow Autor Dr. C. George Boeree."
              )
    await message.answer(hbooks, reply_markup=inline3)


@router.callback_query(lambda c: c.data == 'Book11')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [h1]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)


@router.callback_query(lambda c: c.data == 'Book12')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [h2]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)


@router.callback_query(lambda c: c.data == 'Book13')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [h3]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)


@router.callback_query(lambda c: c.data == 'Book14')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [h4]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)

@router.callback_query(lambda c: c.data == 'Book15')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [h5]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)

@router.callback_query(lambda c: c.data == 'Book16')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [h6]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)

@router.callback_query(lambda c: c.data == 'Book17')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [h7]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)

@router.callback_query(lambda c: c.data == 'Book18')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [h8]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)

@router.callback_query(lambda c: c.data == 'Book19')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [h9]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)

@router.callback_query(lambda c: c.data == 'Book20')
async def send_books(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    documents = [h10]
    for document in documents:
        await bot.send_document(chat_id=call.from_user.id, document=document)


@router.callback_query(lambda c: c.data == 'like')
async def like_dislike_callback(call: CallbackQuery):
    from main import bot
    await bot.answer_callback_query(call.id, text="You clicked like!")


@router.callback_query(lambda c: c.data == 'dislike')
async def delete_callback(call: CallbackQuery):
    from main import bot
    await bot.answer_callback_query(call.id, text="You clicked dislike!")


@router.callback_query(lambda c: c.data == 'back')
async def delete_callback(call: CallbackQuery):
    from main import bot
    await call.message.answer("You clicked back!", reply_markup=keyboard)







