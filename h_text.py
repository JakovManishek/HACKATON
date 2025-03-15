
# Pagina
first_page_answer = "Вы находитесь на первой странице."

def now_page_answer(page: int, cnt: int) -> str:
    return f"Вы находитесь на {page} из {cnt} страниц."

last_page_answer = "Вы находитесь на последней странице."




# Errors
long_name_error = "Слишком длинное название. Пожалуйста, используйте не более 50 симолов в имени папки."

# public_autor_error = "Эта публична папка. Ее может изменять только создатель этой папки."

private_folder_error = "Эта папка приватная. Ее нельзя добавить."

link_is_not_valid_error = "Ссылка на папку не действительна."

doublicate_folder_error = "Нельзя добавить в папку туже самую папку."



incorrectly_private_chosen_error = "Пожалуйста, выберите один из вариантов из списка ниже:"

incorrectly_text_error = "Неизвестная команда.\nНажмите /help, чтобы ознакомиться с ботом."

incorrectly_media_error = "Неправильные входные данные. Пришлите медиа."


technical_job_text = "Bot не работает. Происходят технические работы."


# Keyboards
head_text_kb = "Нажмите кнопку \"Очистить текст\", если хотите вернуть текст папки к изначальному."

choose_private_kb = "Выберите режим приватности:"

media_group_kb = "Нажмите кнопку \"Завершить добавление\", если загрузились все файлы."


# Another text
add_vertex_text = "Пришлите медиа (оно добавится в эту папку).\n\n"\
    "Если хотите добавить папку - пришлите название новой папки или ссылку на уже существующую папку:"

# del_vertex_text = "Нажмите на папки или медиа, которые хотите удалить."

complete_head_text = "Текст добавлен."

choose_name_text = "Выберите приватность папки:"

add_head_text = "Напишите текст (например, описание папки или заметка). Он будет отображаться под названием папки."

def folder_is_create_text(private: str, folder_name: str) -> str:
    return f"Создана {private} папка с именем: {folder_name}."

add_group_folder_text = "Добавление \"Папки группы\" по ссылке."\
    "\n\n"\
    "Добавленная папка является полностью публичной, "\
    "т.е. все ее могут редактировать (возможность создания папок с одним редактором "\
    "будет добавлена в следующих обновлениях)."\
    "\n\n"\
    "Изменять эту и все папки в ней могут все пользователи. Чтобы другим пользователям "\
    "изменять эту папку - им нужно по ссылке добавить папку к себе (в личные сообщения с ботом)."


# Commands
new_chat_message = "Добро пожаловать в Бот Folders!\nЧтобы ознакомится с <b>Инcтрукцией пользования ботом</b> нажмите: /help"

help_instruction = "<b>Инcтрукция пользования ботом Folder:</b>"\
    "\n\n"\
    "Данный бот реализует метод хранения <b><i>медиа (файлы, фото, видео)</i></b> и <b><i>текстовых заметок</i></b> "\
    "по папкам."\
    "\n\n\n"\
    "<b>Пользователь может создать папку в одном из двух режимов:</b>"\
    "\n"\
    "   <b><i>1. Публичная папка</i></b> – Любой пользователь может добавить эту папку к себе по ссылке. Никто кроме "\
    "создателя этой папки не может изменять содержимое папки. Создатель не может редактировать имя этой папки."\
    "\n"\
    "   <b><i>2. Приватная папка</i></b> – Никто кроме создателя папки не может получить доступ к ней. Создатель может "\
    "изменять содержимое папки, а также редактировать имя этой папки."\
    "\n\n\n"\
    "<b>Взаимодействие в ботом:</b>"\
    "\n"\
    "   <b><i>•  Создать папку</i></b> – Пользователь создает папку, указывая название папки и режим приватности. "\
    "<i>Названия приватных папок не могут повторятся!</i>"\
    "\n"\
    "   <b><i>•  Добавить папку</i></b> – Пользователь добавляет Публичную папку к себе по ссылке. "\
    "<i>Пользователь не может никак ее изменять!</i>"\
    "\n"\
    "   <b><i>•  Удалить папку</i></b> – Удаление папки у пользователя без дальнейшего ее возмановления, если папка приватная. "\
    "Если папка публичная, то ее можно будет востановить по ссылке, если эта папка есть у хотя бы одного пользователя, "\
    "иначе папка так же стирается без востановления."\
    "\n"\
    "   <b><i>•  Переименовать папку</i></b> – Переименовать можно только приватную папку. "\
    "<i>Названия приватных папок не могут повторятся!</i>"\
    "\n"\
    "   <b><i>•  Изменить текстовую заметку в папке</i></b> – Текстовое пояснение к папке, расположенное перед файлами."\
    "\n"\
    "   <b><i>•  Добавить файл</i></b> – Пользователь добавляет файл в папку."\
    "<i>Названия файлов не могут повторятся в одной папке!</i>"\
    "\n"\
    "   <b><i>•  Удалить файл</i></b> – Удаление файла из папки."\
    "\n\n\n"\
    "<b>   Команды, доступные пользователю:</b>"\
    "\n"\
    "   /start – Начало работы с ботом. Команда очищает историю чата (за последние два дня) и показывает "\
    "пользователю все его папки по страницам."\
    "\n"\
    "   /help – Подробная инструкция пользования ботом."

# create_group_folder_instruction = "Создание \"Папки группы\"."\
#     "\n\n"\
#     "Отправьте название папки. Она будет автоматически создана полностью публичной, "\
#     "т.е. все ее могут редактировать (возможность создания папок с одним редактором "\
#     "будет добавлена в следующих обновлениях)."\
#     "\n\n"\
#     "В группе с ботом вызовите команду /start и отправьте туда ссылку на эту папку."\
#     "\n\n"\
#     "Изменять эту и все папки в ней могут все пользователи. Чтобы другим пользователям "\
#     "изменять эту папку - им нужно по ссылке добавить папку к себе (в личные сообщения с ботом)."



add_group_folder = "Отправьте название папки"
add_group_link = "Отправьте ссылку на папку"


made_by_text = "FoldersTelegramBot Version 2.0"\
    "\n\n"\
    "Designed and created by @Jakov_Manishek."\
    "\n"\
    "Сreated based on the library aiogram 3+."\
    "\n\n"\
    "Git проекта: <code>https://github.com/JakovManishek/FoldersTelegramBot</code>"\
    "\n\n"\
    "Следующие обновления: Уменьшение спама. Общее исправление ошибок."



# Main message
def name_fold_text(folder_name: str, private_mode: int, vertex_type: str) -> str:
    if vertex_type != "U":
        return f"Открыта <b>{'приватная' if private_mode == 1 else 'публичная'}</b> папка:\n{folder_name}."
    else:
        return f"Открыта папка:\n{folder_name}."


def link_fold_text(folder_link: str) -> str:
    return f"Ссылка на папку:\n<code>{folder_link}</code>."


empty_text = "Тут пока пусто."

not_empty_text = "Снизу рассположены папки и медиа."

public_located_vertices = "Чтобы <b>Добавить</b> папку или медиа - нажмите на кнопку \"<b>Добавить</b>\"."

private_located_vertices = "Это приватная папка. Изменять ее содержимое может только создатель."

delete_vertices = "Чтобы <b>Удалить</b> папку или медиа - нажмите на папку/медиа."


def dif_head_text(head_text: str, private_mode: int, is_empty: bool) -> str:

    if head_text != "":
        return head_text

    if is_empty:
        head_ans = empty_text
    else:
        head_ans = not_empty_text

    if private_mode == 0:
        head_ans += f" {public_located_vertices}"
    else:
        head_ans += f" {private_located_vertices}"

    return head_ans
        



def start_text(chat_type: str,
               folder_link: str,
               folder_name: str,
               vertex_type: str,
               private_mode: int,
               delete_mode: bool,
               is_empty: bool,
               head_text: str | None = ""
               ) -> str:
    
    if vertex_type == "U" and chat_type == "private":
        answer_text = ""
    else:
        answer_text = f"{name_fold_text(folder_name, private_mode, vertex_type)}\n\n"
    
    if delete_mode:
        answer_text += delete_vertices
        return answer_text
    
    if vertex_type == "U" and chat_type == "private":
        answer_text += f"{head_text}\n\n{empty_text if is_empty else not_empty_text} {public_located_vertices}"
    elif vertex_type == "U":
        answer_text += f"{link_fold_text(folder_link)}\n\n"
        if head_text != "":
            answer_text += f"{head_text}\n\n{empty_text if is_empty else not_empty_text}"
        else:
            answer_text += empty_text if is_empty else not_empty_text
    else:
        answer_text += f"{link_fold_text(folder_link)}\n\n"
        answer_text += dif_head_text(head_text, private_mode, is_empty)

    return answer_text



