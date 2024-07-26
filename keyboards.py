from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

keyboard = ReplyKeyboardMarkup(keyboard=[

    [KeyboardButton(
        text='Programming books'
    ),
        KeyboardButton(
            text='Psychology books'
        ), ],
    [KeyboardButton(
        text='Fairy tale books'
    ),
        KeyboardButton(
            text='Horror books'
    #     ), ],
    # [KeyboardButton(
    #     text='⬅Назад'
    # ),
    #             KeyboardButton(
    #                 text='Contact', request_contact=True
    #             ),
    #             KeyboardButton(
    #                 text='Location 📈', request_location=True
                ),],
], resize_keyboard=True)




from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton






inline = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='1', callback_data='Book111'),
        InlineKeyboardButton(text='2', callback_data='Book112'),
        InlineKeyboardButton(text='3', callback_data='Book113'),
        InlineKeyboardButton(text='4', callback_data='Book114'),
        InlineKeyboardButton(text='5', callback_data='Book115')
    ],
    [
        InlineKeyboardButton(text='6', callback_data='Book116'),
        InlineKeyboardButton(text='7', callback_data='Book117'),
        InlineKeyboardButton(text='8', callback_data='Book118'),
        InlineKeyboardButton(text='9', callback_data='Book119'),
        InlineKeyboardButton(text='10', callback_data='Book120')
    ],
], resize_keyboard=True)


inline1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='1', callback_data='1'),
        InlineKeyboardButton(text='2', callback_data='2'),
        InlineKeyboardButton(text='3', callback_data='3'),
        InlineKeyboardButton(text='4', callback_data='4'),
        InlineKeyboardButton(text='5', callback_data='5')

    ],
    [
        InlineKeyboardButton(text='6', callback_data='6'),
        InlineKeyboardButton(text='7', callback_data='7'),
        InlineKeyboardButton(text='8', callback_data='8'),
        InlineKeyboardButton(text='9', callback_data='9'),
        InlineKeyboardButton(text='10', callback_data='10'),

    ],
], resize_keyboard=True)





inline2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='1', callback_data='Book1'),
        InlineKeyboardButton(text='2', callback_data='Book2'),
        InlineKeyboardButton(text='3', callback_data='Book3'),
        InlineKeyboardButton(text='4', callback_data='Book4'),
        InlineKeyboardButton(text='5', callback_data='Book5')
    ],
    [
        InlineKeyboardButton(text='6', callback_data='Book6'),
        InlineKeyboardButton(text='7', callback_data='Book7'),
        InlineKeyboardButton(text='8', callback_data='Book8'),
        InlineKeyboardButton(text='9', callback_data='Book9'),
        InlineKeyboardButton(text='10', callback_data='Book10')
    ],
], resize_keyboard=True)


inline3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='1', callback_data='Book11'),
        InlineKeyboardButton(text='2', callback_data='Book12'),
        InlineKeyboardButton(text='3', callback_data='Book13'),
        InlineKeyboardButton(text='4', callback_data='Book14'),
        InlineKeyboardButton(text='5', callback_data='Book15')
    ],
    [
        InlineKeyboardButton(text='6', callback_data='Book16'),
        InlineKeyboardButton(text='7', callback_data='Book17'),
        InlineKeyboardButton(text='8', callback_data='Book18'),
        InlineKeyboardButton(text='9', callback_data='Book19'),
        InlineKeyboardButton(text='10', callback_data='Book20')
    ],
], resize_keyboard=True)




inline4 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="👍", callback_data='like'),
        InlineKeyboardButton(text="👎", callback_data='dislike'),
        InlineKeyboardButton(text="❌", callback_data='back')
    ],
], resize_keybord=True)







# # inline = InlineKeyboardMarkup(inline_keyboard=[
# #     [InlineKeyboardButton(
#         text='1'
#              '2'
#              '3'
#              '4'
#              '5'
#              '6'
#              '7'
#              '8'
#              '9'
#              '10',
#
#         callback_data='Psychology books'
#     ), ],
# ], resize_keyboard=True)


# b = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(
#         text='2',
#
#     callback_data='2'
#     ), ],
# ], resize_keyboard=True)
#
# c = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(
#         text='3',
#
#     callback_data='3'
#     ), ],
# ], resize_keyboard=True)
#
# e = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(
#         text='4',
#
#     callback_data='4'
#     ), ],
# ], resize_keyboard=True)
#
# i = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(
#         text='5',
#
#     callback_data='5'
#     ), ],
# ], resize_keyboard=True)
#
# f = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(
#         text='6',
#
#     callback_data='6'
#     ), ],
# ], resize_keyboard=True)
#
# d = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(
#         text='7',
#
#     callback_data='7'
#     ), ],
# ], resize_keyboard=True)

# n = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(
#         text='9',
#
#     callback_data='9'
#     ), ],
# ], resize_keyboard=True)
#
# h = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(
#         text='10',
#
#     callback_data='10'
#     ), ],
# ], resize_keyboard=True)