import db.filters

default_lang = None

TEXT = {
    "WELCOME": {
        "en": "Welcome {name} 🤠\n\n"
        "In this bot you can get the id of any group, channel, user or bot\n\n"
        "To use the bot, please click on the buttons below and share the chat whose ID you want to know."
        " - In response, the bot will return the ID of the chat you shared\n\n"
        "You can also send a message to the bot (Forward with quotes) "
        "and the bot will return the ID of the chat from which the message was sent.\n\n"
        "You can transfer a story from a user and get his ID\n\n"
        "To get your ID you can send the command /me\n\n"
        "New 🆕 send the command /admin to get all the chats you have name management\n\n"
        "To change the language please send the /lang command\n\n"
        "The bot is open source on GitHub 🖤\n"
        "https://github.com/yehuda-lev/Get_Chat_ID_Bot\n\n"
        "For updates on the bot subscribe to @GetChatID_Updates",
        "he": "ברוך הבא {name} 🤠\n\n"
        "בבוט זה תוכל לקבל id של כל קבוצה, ערוץ, משתמש או בוט\n\n"
        "בשביל להשתמש בבוט אנא לחץ על הכפתורים למטה ושתף את הצאט שברצונך לדעת מה ה ID שלו. "
        "- בתגובה הבוט יחזיר לך את ה ID של הצאט אותו שיתפת\n\n"
        "ניתן גם להעביר הודעה לבוט (עם קרדיט) והבוט יחזיר לך את ה ID של הצאט ממנו ההודעה הועברה.\n\n"
        "ניתן להעביר סטורי ממשתמש ולקבל את ה-ID שלו\n\n"
        "בשביל לקבל את ה ID שלך ניתן לשלוח את הפקודה /me\n\n"
        "חדש 🆕 שלחו את הפקודה /admin לקבלת כל הצאטים שיש לכם ניהול שם\n\n"
        "לשינוי השפה אנא שלחו את הפקודה /lang\n\n"
        "הבוט בקוד פתוח בגיטהאב 🖤\n"
        "https://github.com/yehuda-lev/Get_Chat_ID_Bot\n\n"
        "לעדכונים על הבוט הירשמו ל-@GetChatID_Updates",
    },
    "USER": {"en": "User", "he": "משתמש"},
    "BOT": {"en": "Bot", "he": "בוט"},
    "CHANNEL": {"en": "Channel", "he": "ערוץ"},
    "GROUP": {"en": "Group", "he": "קבוצה"},
    "ID_USER": {"en": "The ID is: {}", "he": "ה ID הוא: {}"},
    "ID_CHANNEL_OR_GROUP": {"en": "The ID is: {}", "he": "ה ID הוא: \u200e{}"},
    "ID_HIDDEN": {"en": "The ID is hidden. \n{name}", "he": "ה ID מוסתר \n{name}"},
    "CHOICE_LANG": {"en": "Please select your language.", "he": "אנא בחר את השפה שלך."},
    "DONE": {"en": "The selected language is {}", "he": "השפה שנבחרה היא {}"},
    "NOT_HAVE_ID": {
        "en": "The contact you sent has no ID",
        "he": "לאיש הקשר ששלחת אין ID",
    },
    "CHAT_MANAGER": {
        "en": "By clicking the buttons below you can see all the groups and channels you manage and get their ID",
        "he": "בלחיצה על הכפתורים למטה תוכל לראות את כל הקבוצות והערוצים שאתה מנהל בהם ולקבל את המזהה שלהם",
    },
}


def get_text(text: str, tg_id: int) -> str:
    if default_lang is not None:
        lang = default_lang
    else:
        lang = db.filters.get_lang_by_user(tg_id=tg_id)

    try:
        return TEXT[text][lang]
    except KeyError:
        return "Error"
