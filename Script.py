import os

class script(object):

    START_TXT = """<b>Hᴇʟʟᴏ {}\n\n
 ɪ ᴀᴍ ᴛʜᴇ ᴍᴏꜱᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ᴡɪᴛʜ ᴘʀᴇᴍɪᴜᴍ ꜰᴇᴀᴛᴜʀᴇꜱ, ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ cʜᴀɴɴᴇʟ ᴀɴᴅ ᴇɴᴊᴏʏ
 
 ‣ <blockquote>🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/Morning006">Dev</a></blockquote></b>
 """
    HELP_TXT = """•••[( 𝘎𝘦𝘵 𝘏𝘦𝘭𝘱 )]•••

❗ 𝗔𝗹𝗲𝗿𝘁 ❗

• Aᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ғᴜʟʟ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.
• Usᴇ ᴄᴏᴍᴍᴀɴᴅ ɢɪᴠᴇ ʙᴇʟᴏᴡ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋ ɪɴ ᴄʜᴀɴɴᴇʟ.
• Kᴇᴇᴘ ғɪʟᴇ ᴡɪᴛʜᴏᴜᴛ ғᴏʀᴡᴀʀᴅ ᴛᴀɢ.

•> /set_cap - Sᴇᴛ Nᴇᴡ Cᴀᴘᴛɪᴏɴ Iɴ ʏᴏᴜʀ Cʜᴀɴɴᴇʟ
•> /del_cap - Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ

𝑭𝒐𝒓𝒎𝒂𝒕

`{file_name}` = Oʀɪɢɪɴᴀʟ Fɪʟᴇ Nᴀᴍᴇ
`{file_size}` = Oʀɪɢɪɴᴀʟ Fɪʟᴇ Sɪᴢᴇ 
`{language}` = Lᴀɴɢᴜᴀɢᴇ Oғ Fɪʟᴇ Nᴀᴍᴇ
`{year}` = Yᴇᴀʀ Oғ Fɪʟᴇ
`{default_caption}` = Rᴇᴀʟ Cᴀᴘᴛɪᴏɴ Oғ Fɪʟᴇ.

Eg:- `/set_cap
{file_name}

⚙️ Size » {file_size}

╔═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗
💥 𝙅𝙊𝙄𝙉 :- ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ 
💥 𝙅𝙊𝙄𝙉 :- ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ
╚═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝`
"""

    ABOUT_TXT = """<b>╔════❰ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣
║┣⪼📃ʙᴏᴛ : <a href='https://t.me/Dev_Advance_caption_bot'>Auto Caption</a>
║┣⪼👦Cʀᴇᴀᴛᴏʀ : <a href='https://t.me/Morning006'>Dev ⚠️</a>
║┣⪼🤖Uᴘᴅᴀᴛᴇ : <a href='https://t.me/MoviesEmpire_Backup'>Backup 😀</a>
║┣⪼📡Hᴏsᴛᴇᴅ ᴏɴ : buffalo 
║┣⪼🗣️Lᴀɴɢᴜᴀɢᴇ : Jo tuja samj ma aay
║┣⪼📚Lɪʙʀᴀʀʏ : ghar ka pass vali
║┣⪼🗒️Vᴇʀsɪᴏɴ : latest [ᴍᴏsᴛ sᴛᴀʙʟᴇ]
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁</b>"""
