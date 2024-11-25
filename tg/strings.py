default_lang = None

TEXT = {
    "WELCOME": {
        "en": "Welcome {name} 🤠\n\n"
        "🪪 In this bot you can get the id of any group, channel, user or bot\n\n"
        "📤 To use the bot, click on the buttons below and share the chat whose ID you want to know."
        " - In response, the bot will return the ID of the chat you shared\n\n"
        "> 🇺🇸 To change the language send the /lang command\n\n"
        "> 📝 You can get the ID in many other ways. Send the /help command\n\n"
        "> 🤑 Want to donate to me? Send the /donate command\n\n"
        "📢 For updates on the bot subscribe to @GetChatID_Updates",
        "he": "ברוך הבא {name} 🤠\n\n"
        "\u200f🪪 בבוט זה תוכל לקבל מזהה של כל קבוצה, ערוץ, משתמש או בוט\n\n"
        "📤 בכדי להשתמש בבוט לחץ על הכפתורים למטה ושתף את הצ'אט שברצונך לדעת מה המזהה שלו. "
        "- בתגובה הבוט יחזיר לך את המזהה של הצ'אט אותו שיתפת\n\n"
        "> \u200f🇺🇸 לשינוי השפה שלח את הפקודה /lang\n\n"
        "> 📝 ניתן לקבל את המזהה בעוד הרבה דרכים נוספות. שלח את הפקודה /help\n\n"
        "> 🤑 רוצה לתרום לי? שלח את הפקודה /donate\n\n"
        "📢 לעדכונים על הבוט הירשם ל-@GetChatID_Updates",
        "ru": "Добро пожаловать {name} 🤠\n\n"
        "🪪 В этом боте вы можете получить ID любой группы, канала, пользователя или бота\n\n"
        "📤 Чтобы использовать бота, нажмите на кнопки ниже и поделитесь чатом, ID которого вы хотите узнать."
        " - В ответ бот вернет вам ID чата, которым вы поделились\n\n"
        "> 🇺🇸 Чтобы изменить язык, отправьте команду /lang\n\n"
        "> 📝 Вы можете получить ID многими другими способами. Отправьте команду /help\n\n"
        "> 🤑 Хотите пожертвовать мне? Отправьте команду /donate\n\n"
        "📢 Чтобы получать обновления о боте, подпишитесь на @GetChatID_Updates",
        "ar": "مرحبًا {name} 🤠\n\n"
        "🪪 في هذا البوت يمكنك الحصول على معرف أي مجموعة أو قناة أو مستخدم أو بوت\n\n"
        "📤 لاستخدام البوت، انقر على الأزرار أدناه وشارك الدردشة التي تريد معرفة معرفها."
        " - في الرد، سيعيد لك البوت معرف الدردشة التي شاركتها\n\n"
        "> 🇺🇸 لتغيير اللغة أرسل الأمر /lang\n\n"
        "> 📝 يمكنك الحصول على المعرف بطرق أخرى عديدة. أرسل الأمر /help\n\n"
        "> 🤑 هل تريد التبرع لي؟ أرسل الأمر /donate\n\n"
        "📢 للحصول على تحديثات حول البوت اشترك في @GetChatID_Updates",
    },
    "USER": {
        "en": "👤 User",
        "he": "👤 משתמש",
        "ru": "👤 Пользователь",
        "ar": "👤 مستخدم",
    },
    "BOT": {
        "en": "🤖 Bot",
        "he": "🤖 בוט",
        "ru": "🤖 Бот",
        "ar": "🤖 بوت",
    },
    "CHANNEL": {
        "en": "📢 Channel",
        "he": "📢 ערוץ",
        "ru": "📢 Канал",
        "ar": "📢 قناة",
    },
    "GROUP": {
        "en": "👥 Group",
        "he": "👥 קבוצה",
        "ru": "👥 Группа",
        "ar": "👥 مجموعة",
    },
    "ID_USER": {
        "en": "🪪 The ID of {} is: `{}`",
        "he": "‏🪪 ה ID  של {} הוא: `{}`",
        "ru": "🪪 ID {}: `{}`",
        "ar": "🪪 معرف {} هو: `{}`",
    },
    "ID_USERS": {
        "en": "🪪 The ID of: \n{}",
        "he": "‏🪪 ה ID של: \n{}",
        "ru": "🪪 ID:\n{}",
        "ar": "🪪 معرف:\n{}",
    },
    "ID_CHANNEL_OR_GROUP": {
        "en": "🪪 The ID of {} is: `{}`",
        "he": "‏🪪 ה ID של {} הוא: \u200e`{}`",
        "ru": "🪪 ID {}: `{}`",
        "ar": "🪪 معرف {} هو: `{}`",
    },
    "ID_CHANNELS_OR_GROUPS": {
        "en": "🪪 The ID of: \n{}",
        "he": "‏🪪 ה ID של: \u200e{}",
        "ru": "🪪 ID:\n{}",
        "ar": "🪪 معرف:\n{}",
    },
    "ID_HIDDEN": {
        "en": "🪪 The ID is hidden. \n{name}",
        "he": "‏🪪 ה ID מוסתר \n{name}",
        "ru": "🪪 ID скрыт. \n{name}",
        "ar": "🪪 المعرف مخفي. \n{name}",
    },
    "CHOICE_LANG": {
        "en": "🤳 Select your language.",
        "he": "🤳 בחר את השפה שלך.",
        "ru": "🤳 Выберите ваш язык.",
        "ar": "🤳 اختر لغتك.",
    },
    "DONE": {
        "en": "The selected language is {}",
        "he": "השפה שנבחרה היא {}",
        "ru": "Выбранный язык: {}",
        "ar": "اللغة المحددة هي {}",
    },
    "NOT_HAVE_ID": {
        "en": "❌ The contact you sent has no ID",
        "he": "❌ לאיש הקשר ששלחת אין ID",
        "ru": "❌ Контакт, который вы отправили, не имеет ID",
        "ar": "❌ جهة الاتصال التي أرسلتها ليس لها معرف",
    },
    "CAN_NOT_GET_THE_ID": {
        "en": "❌ It is not possible to get the ID of this chat",
        "he": "❌ אי אפשר לקבל את הID של הצ'אט הזה",
        "ru": "❌ Невозможно получить ID этого чата",
        "ar": "❌ لا يمكن الحصول على معرف هذه الدردشة",
    },
    "CHAT_MANAGER": {
        "en": "👮 By clicking the buttons below you can see all the groups and channels you manage and get their ID",
        "he": "👮 בלחיצה על הכפתורים למטה תוכל לראות את כל הקבוצות והערוצים שאתה מנהל בהם ולקבל את המזהה שלהם",
        "ru": "👮 Нажав на кнопки ниже, вы можете увидеть все группы и каналы, שבהх вы управляете, и получить их ID",
        "ar": "👮 بالنقر على الأزرار أدناه، يمكنك رؤية جميع المجموعات والقنوات التي تديرها والحصول على معرفاتها",
    },
    "REQUEST_CHAT": {
        "en": "📤 request chat",
        "he": "📤 שיתוף צ'אט",
        "ru": "📤 запросить чат",
        "ar": "📤 طلب الدردشة",
    },
    "INFO_REQUEST_CHAT": {
        "en": "**📤 request chat**\n\n"
        "Click on the buttons below and share the chat whose ID you want to know."
        "\n- In response, the bot will return the ID of the chat you shared",
        "he": "**📤 שיתוף צ'אט**\n\n"
        "לחץ על הכפתורים למטה ושתף את הצ'אט שברצונך לדעת מה המזהה שלו."
        "\n- בתגובה הבוט יחזיר לך את המזהה של הצ'אט אותו שיתפת",
        "ru": "**📤 Запросить чат**\n\n"
        "Нажмите на кнопки ниже и поделитесь чатом, ID которого вы хотите узнать."
        "\n- В ответ бот вернет вам ID чата, которым вы поделились",
        "ar": "**📤 طلب الدردشة**\n\n"
        "انقر على الأزرار أدناه وشارك الدردشة التي تريد معرفة معرفها."
        "\n- في الرد، سيعيد لك البوت معرف الدردشة التي شاركتها",
    },
    "FORWARD": {
        "en": "⏩ forward",
        "he": "⏩ העברה",
        "ru": "⏩ переслать",
        "ar": "⏩ إعادة توجيه",
    },
    "INFO_FORWARD": {
        "en": "**⏩ forward message**\n\n"
        "Forward any message to the bot (forward with quotes) "
        "and the bot will return the ID of the chat from which the message was sent.",
        "he": "**⏩ העברת הודעה**\n\n"
        "העבירו כל הודעה לבוט (עם קרדיט) והבוט יחזיר לכם את המזהה של הצ'אט ממנו ההודעה הועברה",
        "ru": "**⏩ Переслать сообщение**\n\n"
        "Перешлите любое сообщение боту (пересылка с цитатой) "
        "и бот вернет вам ID чата, из которого было отправлено сообщение.",
        "ar": "**⏩ إعادة توجيه الرسالة**\n\n"
        "أعد توجيه أي رسالة إلى البوت (مع الاقتباس) "
        "وسيعيد لك البوت معرف الدردشة التي تم إرسال الرسالة منها.",
    },
    "STORY": {
        "en": "📝 story",
        "he": "📝 סטורי",
        "ru": "📝 история",
        "ar": "📝 قصة",
    },
    "INFO_STORY": {
        "en": "**📝 Story**\n\n" "Transfer a story and get their ID.",
        "he": "**📝 סטורי**\n\n" "העבירו סטורי לבוט וקבלו את המזהה של הצ'אט",
        "ru": "**📝 История**\n\n" "Перешлите историю и получите их ID.",
        "ar": "**📝 قصة**\n\n" "أعد توجيه قصة إلى البوت واحصل على معرف الدردشة.",
    },
    "SEARCH_USERNAME": {
        "en": "🔍 username",
        "he": "🔍 שם משתמש",
        "ru": "🔍 имя пользователя",
        "ar": "🔍 اسم المستخدم",
    },
    "INFO_SEARCH_USERNAME": {
        "en": "**🔍 Search by Username**\n\n"
        "Send the username to the bot and the bot will return the ID of the chat with that username.",
        "he": "**🔍 חיפוש באמצעות שם משתמש**\n\n"
        "שלח שם משתמש לבוט והבוט יחזיר לך את המזהה של הצ'אט הזה",
        "ru": "**🔍 Поиск по имени пользователя**\n\n"
        "Отправьте имя пользователя боту, и бот вернет вам ID чата с этим именем пользователя.",
        "ar": "**🔍 البحث عن طريق اسم المستخدم**\n\n"
        "أرسل اسم المستخدم إلى البوت وسيعيد لك البوت معرف الدردشة لهذا المستخدم.",
    },
    "REPLY_TO_ANOTHER_CHAT": {
        "en": "↩️ reply to",
        "he": "↩️ הגב ל",
        "ru": "↩️ ответить на",
        "ar": "↩️ الرد على",
    },
    "INFO_REPLY_TO_ANOTHER_CHAT": {
        "en": "**↩️ Reply to Another Chat**\n\n"
        "Reply to any message in another chat, "
        "and the bot will return the ID of the chat from which the message was replied.",
        "he": "**↩️ הגב לצ'אט אחר**\n\n"
        "הגב לכל הודעה מצ'אט אחר, "
        "והבוט יחזיר לך את המזהה של הצ'אט ממנו נשלחה ההודעה.",
        "ru": "**↩️ Ответить в другом чате**\n\n"
        "Ответьте на любое сообщение в другом чате, "
        "и бот вернет вам ID чата, из которого было получено сообщение.",
        "ar": "**↩️ الرد على دردشة أخرى**\n\n"
        "قم بالرد على أي رسالة في دردشة أخرى، "
        "وسيعيد لك البوت معرف الدردشة التي تم الرد منها.",
    },
    "CONTACT": {
        "en": "🪪 contact",
        "he": "\u200f🪪 איש קשר",
        "ru": "🪪 контакт",
        "ar": "🪪 جهة اتصال",
    },
    "INFO_CONTACT": {
        "en": "**🪪 Contact**\n\n"
        "Share a contact to the bot and the bot will return the contact's ID to you",
        "he": "**\u200f🪪 איש קשר**\n\n"
        "שתף איש קשר לבוט והבוט יחזיר לך את המזהה של האיש קשר",
        "ru": "**🪪 Контакт**\n\n"
        "Поделитесь контактом с ботом, и бот вернет вам ID контакта",
        "ar": "**🪪 جهة اتصال**\n\n"
        "شارك جهة اتصال مع البوت وسيعيد لك البوت معرف جهة الاتصال",
    },
    "REQUEST_ADMIN": {
        "en": "👮‍♂️ admin",
        "he": "👮‍♂️ ניהולים",
        "ru": "👮‍♂️ админ",
        "ar": "👮‍♂️ المشرف",
    },
    "INFO_REQUEST_ADMIN": {
        "en": "**👮‍ Request Admin**\n\n"
        "Send the command /admin to get all the chats you have name management.",
        "he": "**👮 צ'אטים בניהולך**\n\n"
        "שלחו את הפקודה /admin לקבלת כל הצ'אטים שיש לכם ניהול שם",
        "ru": "**👮 Запросить админа**\n\n"
        "Отправьте команду /admin, чтобы получить все чаты, в которых у вас есть права администратора.",
        "ar": "**👮 طلب المشرف**\n\n"
        "أرسل الأمر /admin للحصول على جميع الدردشات التي لديك فيها صلاحيات الإدارة.",
    },
    "ME": {
        "en": "👤 me",
        "he": "👤 אני",
        "ru": "👤 я",
        "ar": "👤 أنا",
    },
    "INFO_ME": {
        "en": "**👤 Get your ID**\n\n" "Send the command /me to get your ID",
        "he": "**👤 קבל את המזהה שלך**\n\n" "שלח את הפקודה /me בכדי לקבל את המזהה שלך",
        "ru": "**👤 Получить ваш ID**\n\n"
        "Отправьте команду /me, чтобы получить ваш ID",
        "ar": "**👤 الحصول على معرفك**\n\n" "أرسل الأمر /me للحصول على معرفك",
    },
    "LANGUAGE": {
        "en": "🇺🇸 language",
        "he": "\u200f🇺🇸 שפה",
        "ru": "🇺🇸 язык",
        "ar": "🇺🇸 اللغة",
    },
    "INFO_LANGUAGE": {
        "en": "**🇺🇸 Language**\n\n" "To change the language send the /lang command.",
        "he": "**\u200f🇺🇸 שפה**\n\n" "לשינוי השפה שלחו את הפקודה /lang",
        "ru": "**🇺🇸 Язык**\n\n" "Чтобы изменить язык, отправьте команду /lang.",
        "ar": "**🇺🇸 اللغة**\n\n" "لتغيير اللغة أرسل الأمر /lang.",
    },
    "INFO_GROUP": {
        "en": "**👥 Group**\n\n"
        "Add the bot to the group with the command `/add` "
        "and get the id of the group members with the command `/id`",
        "he": "**👥 קבוצה**\n\n"
        "הוסף את הבוט לקבוצה עם הפקודה `/add`"
        " וקבל את המזהה של חברי הקבוצה באמצעות הפקודה `/id`",
        "ru": "**👥 Группа**\n\n"
        "Добавьте бота в группу с командой `/add` "
        "и получите ID участников группы с помощью команды `/id`",
        "ar": "**👥 مجموعة**\n\n"
        "أضف البوت إلى المجموعة باستخدام الأمر `/add` "
        "واحصل على معرفات أعضاء المجموعة باستخدام الأمر `/id`",
    },
    "SHOW_ALL": {
        "en": "📕 show all",
        "he": "📕 הצג הכל",
        "ru": "📕 показать все",
        "ar": "📕 عرض الكل",
    },
    "NEXT": {
        "en": "next ➡️",
        "he": "➡️ הבא",
        "ru": "далее ➡️",
        "ar": "التالي ➡️",
    },
    "BACK": {
        "en": "⬅️ back",
        "he": "חזור ⬅️",
        "ru": "⬅️ назад",
        "ar": "⬅️ العودة",
    },
    "MENU": {
        "en": "🏘 menu",
        "he": "🏘 תפריט ראשי",
        "ru": "🏘 меню",
        "ar": "🏘 القائمة",
    },
    "INFO_MENU": {
        "en": "🏘 menu help",
        "he": "🏘 תפריט עזרה",
        "ru": "🏘 помощь по меню",
        "ar": "🏘 مساعدة القائمة",
    },
    "ABOUT": {
        "en": "ℹ️ about",
        "he": "ℹ️ אודות",
        "ru": "ℹ️ о боте",
        "ar": "ℹ️ حول",
    },
    "INFO_ABOUT": {
        "en": "ℹ️ **Details about the bot**\n\n"
        "Language: [Python](https://www.python.org/) \n"
        "Library: [pyrotgfork](https://telegramplayground.github.io/pyrogram/) \n"
        "Bot creator: @yehudalev 👨‍💻\n\n"
        "Donations: You can support the bot creator with the /donate command\n\n"
        "The bot is open source on GitHub 🖤\n"
        "https://github.com/yehuda-lev/Get_Chat_ID_Bot\n\n"
        "📢 For updates on the bot, subscribe to @GetChatID_Updates,",
        "he": "\u200fℹ️ **פרטים על הבוט**\n\n"
        "שפה: [Python](https://www.python.org/) \n"
        "ספרייה: [pyrotgfork](https://telegramplayground.github.io/pyrogram/) \n"
        "יוצר הבוט: @yehudalev  👨‍💻\n\n"
        "תרומות: ניתן לתמוך ביוצר הבוט באמצעות הפקודה /donate\n\n"
        "הבוט בקוד פתוח בגיטהאב 🖤\n"
        "https://github.com/yehuda-lev/Get_Chat_ID_Bot\n\n"
        "📢 לעדכונים על הבוט הירשמו ל-@GetChatID_Updates",
        "ru": "ℹ️ **Информация о боте**\n\n"
        "Язык: [Python](https://www.python.org/) \n"
        "Библиотека: [pyrotgfork](https://telegramplayground.github.io/pyrogram/) \n"
        "Создатель бота: @yehudalev 👨‍💻\n\n"
        "Пожертвования: Вы можете поддержать создателя бота с помощью команды /donate\n\n"
        "Бот с открытым исходным кодом на GitHub 🖤\n"
        "https://github.com/yehuda-lev/Get_Chat_ID_Bot\n\n"
        "📢 Для обновлений о боте под��ишитесь на @GetChatID_Updates",
        "ar": "ℹ️ **تفاصيل حول البوت**\n\n"
        "اللغة: [Python](https://www.python.org/) \n"
        "المكتبة: [pyrotgfork](https://telegramplayground.github.io/pyrogram/) \n"
        "منشئ البوت: @yehudalev 👨‍💻\n\n"
        "التبرعات: يمكنك دعم منشئ البوت باستخدام الأمر /donate\n\n"
        "البوت مفتوح المصدر على GitHub 🖤\n"
        "https://github.com/yehuda-lev/Get_Chat_ID_Bot\n\n"
        "📢 للحصول على تحديثات حول البوت، اشترك في @GetChatID_Updates",
    },
    "BUTTON_DEV": {
        "en": "Send message👨‍💻",
        "he": "לשליחת הודעה למתכנת 👨‍💻",
        "ru": "Отправить сообщение👨‍💻",
        "ar": "إرسال رسالة👨‍💻",
    },
    "LINK_DEV": {
        "en": "https://t.me/yehudalev",
        "he": "https://t.me/yehudalev",
        "ru": "https://t.me/yehudalev",
        "ar": "https://t.me/yehudalev",
    },
    "CHOSE_CHAT_TYPE": {
        "en": "Choose chat type",
        "he": "בחר את סוג הצ'אט",
        "ru": "Выберите тип чата",
        "ar": "اختر نوع الدردشة",
    },
    "BUTTON_ADD_BOT_TO_GROUP": {
        "en": "Add bot to group",
        "he": "הוסף את הבוט לקבוצה",
        "ru": "Добавить бота в группу",
        "ar": "أضف البوت إلى المجموعة",
    },
    "ADD_BOT_TO_GROUP": {
        "en": "**Add bot to group**\n\n"
        "Click on the button to add the bot to the group to get id's of members in the group",
        "he": "**הוספת הבוט לקבוצה**\n\n"
        "לחץ על הכפתור בכדי להוסיף את הבוט לקבוצה בשביל לקבל מזהים של חברים בקבוצה",
        "ru": "**Добавить бота в группу**\n\n"
        "Нажмите на кнопку, чтобы добавить бота в группу и получить ID участников группы",
        "ar": "**إضافة البوت إلى المجموعة**\n\n"
        "انقر على الزر لإضافة البوت إلى المجموعة للحصول על معرفات الأعضاء في المجموعة",
    },
    "BOT_ADDED_TO_GROUP": {
        "en": "**Bot added to group**\n\n"
        "The bot was added to the group {group_name} • `{group_id}`\n"
        "to get ids of members in the group, send the command `/id` in the group",
        "he": "**הוספת הבוט לקבוצה**\n\n"
        "\u200fהבוט נוסף לקבוצה {group_name} • `{group_id}`\n"
        "כדי לקבל מזהים של חברים בקבוצה, שלח את הפקודה `/id` בקבוצה",
        "ru": "**Бот добавлен в группу**\n\n"
        "Бот был добавлен в группу {group_name} • `{group_id}`\n"
        "Чтобы получить ID участников группы, отправьте команду `/id` в группе",
        "ar": "**تم إضافة البوت إلى المجموعة**\n\n"
        "تم إضافة البوت إلى المجموعة {group_name} • `{group_id}`\n"
        "للحصول على معرفات الأعضاء في المجموعة، أرسل الأمر `/id` في المجموعة",
    },
    "BUSINESS": {
        "en": "🔗 Business connection",
        "he": "🔗 חיבור עסקי",
        "ru": "🔗 Бизнес-подключение",
        "ar": "🔗 اتصال الأعمال",
    },
    "INFO_BUSINESS": {
        "en": "**🔗 Business connection**\n\n"
        "You can connect the bot to your business and get the ID of any chat."
        "\n> Go to settings > Telegram Business > Chatbot > and select this bot"
        "\nThen you can send the command `.id` in any private chat to get the chat ID."
        "\nYou can also get the ID without sending a message in the chat!"
        "\n> Go to the chat and then click on the bot management button "
        "and the bot will send the ID of the chat you came from",
        "he": "**🔗 חיבור עסקי**\n\n"
        "ניתן לחבר את הבוט לעסק שלך ולקבל מזהה של כל צ'אט."
        "\n> כנס להגדרות > טלגרם ביזנס > צ'אטבוט > ובחר בבוט הזה"
        "\nלאחר מכן תוכל לשלוח את הפקודה `.id` "
        "בכל צ'אט פרטי כדי לקבל את המזהה של הצ'אט."
        "\nניתן גם לקבל את הID ללא שליחת הודעה בצ'אט!"
        "\n> כנס לצ'אט ואז לחץ על כפתור ניהול הבוט והבוט ישלח את המזהה של הצ'אט שממנו הגעת",
        "ru": "**🔗 Бизнес-подключение**\n\n"
        "Вы можете подключить бота к вашему бизнесу и получать ID любого чата."
        "\n> Перейдите в настройки > Telegram Business > Chatbot > и выберите этого бота"
        "\nЗатем вы можете отправить команду `.id` в любом приватном чате, чтобы получить ID чата."
        "\nВы также можете получить ID, не отправляя сообщение в чат!"
        "\n> Перейдите в чат и нажмите на кнопку управления ботом, "
        "и бот отправит ID чата, из которого вы пришли",
        "ar": "**🔗 اتصال الأعمال**\n\n"
        "يمكنك ربط البوت بعملك والحصول على معرف أي دردشة."
        "\n> اذهب إلى الإعدادات > Telegram Business > Chatbot > واختر هذا البوت"
        "\nثم يمكنك إرسال الأمر `.id` في أي دردشة خاصة للحصول على معرف الدردشة."
        "\nيمكنك أيضًا الحصول على المعرف دون إرسال رسالة في الدردشة!"
        "\n> انتقل إلى الدردشة ثم انقر على زر إدارة البوت "
        "وسيرسل البوت معرف الدردشة التي أتيت منها",
    },
    "BUSINESS_CONNECTION": {
        "en": "**🔗 Business connection**"
        "\nHi, thanks for connecting with me! "
        "\nYou can use me by sending the command `.id` "
        "in any chat (private) to get the chat ID."
        "\n> You can also get the ID without sending a message in the chat!"
        "\n> Go to the chat and then click on the bot management button "
        "and the bot will send the ID of the chat you came from",
        "he": "**🔗 חיבור עסקי**"
        "\nהיי, תודה שהתחברת לצ'אט בוט שלי! "
        "\nאתה יכול להשתמש בי על ידי שליחה של הפקודה `.id` "
        "בכל צ'אט (פרטי) כדי לקבל את המזהה של הצ'אט."
        "\n> ניתן גם לקבל את הID ללא שליחת הודעה בצ'אט!"
        "\n> כנס לצ'אט ואז לחץ על כפתור ניהול הבוט והבוט ישלח את המזהה של הצ'אט שממנו הגעת",
        "ru": "**🔗 Бизнес-подключение**"
        "\nПривет, спасибо, что подключились ко мне! "
        "\nВы можете использовать меня, отправив команду `.id` "
        "в любом чате (приватном), чтобы получить ID чата."
        "\n> Вы также можете получить ID, не отправляя сообщение в чат!"
        "\n> Перейдите в чат и нажмите на кнопку управления ботом, "
        "и бот отправит ID чата, из которого вы пришли",
        "ar": "**🔗 اتصال الأعمال**"
        "\nمرحبًا، شكرًا لاتصالك بي! "
        "\nيمكنك استخدامي عن طريق إرسال الأمر `.id` "
        "في أي دردشة (خاصة) للحصول على معرف الدردشة."
        "\n> يمكنك أيضًا الحصول على المعرف دون إرسال رسالة في الدردشة!"
        "\n> اذهب إلى الدردشة ثم انقر على زر إدارة البوت "
        "وسيرسل البوت معرف الدردشة التي أتيت منها",
    },
    "BUSINESS_CONNECTION_DISABLED": {
        "en": "**🔗 Business connection**"
        "\nI'm sorry, but I can't reply to your messages. "
        "If you want to get the chat ID, enable the permission to reply to messages.",
        "he": "**🔗 חיבור עסקי**"
        "\nאני מצטער, אבל אני לא יכול לענות על ההודעות שלך. "
        "אם ברצונך לקבל את מזהה הצ'אט, הפעל את ההרשאה להשיב על הודעות.",
        "ru": "**🔗 Бизнес-подключение**"
        "\nИзвините, но я не могу ответить на ваши сообщения. "
        "Если вы хотите получить ID чата, включите разрешение на ответ на сообщения.",
        "ar": "**🔗 اتصال الأعمال**"
        "\nآسف، لكن لا يمكنني الرد على رسائلك. "
        "إذا كنت تريد الحصول على معرف الدردشة، فعِّل إذن الرد على الرسائل.",
    },
    "BUSINESS_CONNECTION_REMOVED": {
        "en": "**🔗 Business connection**"
        "\nI'm sorry to see you go, but I'm always here if you need me.",
        "he": "**🔗 חיבור עסקי**"
        "\nאני מצטער שהתנתקת מהחיבור לבוט."
        "תוכל לחזור בכל עת ולהתחבר אלי שוב.",
        "ru": "**🔗 Бизнес-подключение**"
        "\nЖаль видеть, что вы уходите, но я всегда здесь, если вы будете нуждаться во мне.",
        "ar": "**🔗 اتصال الأعمال**"
        "\nأنا آسف لرؤيتك ترحل، لكنني دائمًا هنا إذا احتجتني.",
    },
    "ID_BY_MANAGE_BUSINESS": {
        "en": "🪪 The ID of the chat you came from is: `{}`",
        "he": "‏🪪 ה ID של הצ'אט ממנו באת הוא: `{}`",
        "ru": "🪪 ID чата, из которого вы пришли: `{}`",
        "ar": "🪪 معرف الدردشة التي أتيت منها هو: `{}`",
    },
    "ASK_AMOUNT_TO_PAY": {
        "en": "Hi, thanks for wanting to donate to me 🥰\n"
        "Choose the donation amount you want to give 👇",
        "he": "היי, תודה שאתם רוצים לתרום לי 🥰\n" "בחרו את סכום התרומה שתרצו לתת 👇",
        "ru": "Привет, спасибо, что хотите пожертвовать мне 🥰\n"
        "Выберите сумму пожертвования, которую вы хотите дать 👇",
        "ar": "مرحبًا، شكرًا لرغبتك في التبرع لي 🥰\n"
        "اختر مبلغ التبرع الذي تريد تقديمه 👇",
    },
    "SUPPORT_ME": {
        "en": "Support me 🙏",
        "he": "תמכו בי 🙏",
        "ru": "Поддержите меня 🙏",
        "ar": "ادعمني 🙏",
    },
    "TEXT_SUPPORT_ME": {
        "en": "Support me with {} ⭐️",
        "he": "תמכו בי ב-{} ⭐️",
        "ru": "Поддержите меня на {} ⭐️",
        "ar": "ادعمني بـ {} ⭐️",
    },
    "PAYMENT_SUCCESS": {
        "en": "🎉 Thank you for your donation 🎉\n" "I received your donation of {} ⭐️",
        "he": "🎉 תודה על התרומה שלך 🎉\n" "קיבלתי את התרומה שלך של {} ⭐️",
        "ru": "🎉 Спасибо за ваше пожертвование 🎉\n"
        "Я получил ваше пожертвование на {} ⭐️",
        "ar": "🎉 شكرًا لتبرعك 🎉\n" "لقد تلقيت تبرعك بقيمة {} ⭐️",
    },
    "SOMTHING_WENT_WRONG": {
        "en": "Something went wrong",
        "he": "משהו השתבש",
        "ru": "Что-то пошло не так",
        "ar": "حدث خطأ ما",
    },
    "LINK_TO_CHAT": {
        "en": "🔗 Link to chat `{}`",
        "he": "‏🔗 קישור לצ'אט \u200e`{}`",
        "ru": "🔗 Ссылка на чат `{}`",
        "ar": "🔗 رابط الدردشة `{}`",
    },
    "BUTTON_GET_LINK": {
        "en": "🔗 Link to chat",
        "he": "🔗 קישור לצ'אט",
        "ru": "🔗 Ссылка на чат",
        "ar": "🔗 رابط الدردشة",
    },
    "FORMAT_LINK": {
        "en": "Send the command with the chat ID\n" "For example:\n> `/link 777000`",
        "he": "שלח את הפקודה עם המזהה של הצ'אט" "\nלדוגמה:\n> `/link 777000`",
        "ru": "Отправьте команду с ID чата\n" "Например:\n> `/link 777000`",
        "ar": "أرسل الأمر مع معرف الدردشة\n" "على سبيل المثال:\n> `/link 777000`",
    },
}


def get_text(*, key: str, lang: str) -> str:
    if default_lang is not None:
        lang = default_lang
    else:
        lang = lang if lang in TEXT[key].keys() else "en"

    try:
        return TEXT[key][lang]
    except KeyError:
        return "Error"
