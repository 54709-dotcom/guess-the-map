# -*- coding: utf-8 -*-
"""
data.py
เก็บข้อมูลประเทศทั้งหมดที่ใช้ในเกม Guess The Country
แต่ละประเทศประกอบด้วย:
    - name_th   : ชื่อประเทศภาษาไทย (คำตอบหลัก)
    - name_en   : ชื่อประเทศภาษาอังกฤษ (ใช้ตรวจคำตอบด้วย)
    - iso3      : รหัส ISO Alpha-3 (ใช้วาดรูปร่างแผนที่ด้วย Plotly)
    - continent : ทวีป (ใช้เป็นคำใบ้)
    - difficulty: ระดับความยาก (Easy / Medium / Hard)
"""

COUNTRIES = [
    # ---------------- EASY ----------------
    {"name_th": "สหรัฐอเมริกา", "name_en": "United States", "iso3": "USA", "continent": "อเมริกาเหนือ", "difficulty": "Easy"},
    {"name_th": "จีน", "name_en": "China", "iso3": "CHN", "continent": "เอเชีย", "difficulty": "Easy"},
    {"name_th": "ฝรั่งเศส", "name_en": "France", "iso3": "FRA", "continent": "ยุโรป", "difficulty": "Easy"},
    {"name_th": "ญี่ปุ่น", "name_en": "Japan", "iso3": "JPN", "continent": "เอเชีย", "difficulty": "Easy"},
    {"name_th": "บราซิล", "name_en": "Brazil", "iso3": "BRA", "continent": "อเมริกาใต้", "difficulty": "Easy"},
    {"name_th": "อินเดีย", "name_en": "India", "iso3": "IND", "continent": "เอเชีย", "difficulty": "Easy"},
    {"name_th": "รัสเซีย", "name_en": "Russia", "iso3": "RUS", "continent": "ยุโรป/เอเชีย", "difficulty": "Easy"},
    {"name_th": "สหราชอาณาจักร", "name_en": "United Kingdom", "iso3": "GBR", "continent": "ยุโรป", "difficulty": "Easy"},
    {"name_th": "เยอรมนี", "name_en": "Germany", "iso3": "DEU", "continent": "ยุโรป", "difficulty": "Easy"},
    {"name_th": "อิตาลี", "name_en": "Italy", "iso3": "ITA", "continent": "ยุโรป", "difficulty": "Easy"},
    {"name_th": "แคนาดา", "name_en": "Canada", "iso3": "CAN", "continent": "อเมริกาเหนือ", "difficulty": "Easy"},
    {"name_th": "ออสเตรเลีย", "name_en": "Australia", "iso3": "AUS", "continent": "โอเชียเนีย", "difficulty": "Easy"},
    {"name_th": "อียิปต์", "name_en": "Egypt", "iso3": "EGY", "continent": "แอฟริกา", "difficulty": "Easy"},
    {"name_th": "ไทย", "name_en": "Thailand", "iso3": "THA", "continent": "เอเชีย", "difficulty": "Easy"},
    {"name_th": "เกาหลีใต้", "name_en": "South Korea", "iso3": "KOR", "continent": "เอเชีย", "difficulty": "Easy"},
    {"name_th": "เม็กซิโก", "name_en": "Mexico", "iso3": "MEX", "continent": "อเมริกาเหนือ", "difficulty": "Easy"},
    {"name_th": "สเปน", "name_en": "Spain", "iso3": "ESP", "continent": "ยุโรป", "difficulty": "Easy"},
    {"name_th": "อาร์เจนตินา", "name_en": "Argentina", "iso3": "ARG", "continent": "อเมริกาใต้", "difficulty": "Easy"},
    {"name_th": "ซาอุดีอาระเบีย", "name_en": "Saudi Arabia", "iso3": "SAU", "continent": "เอเชีย", "difficulty": "Easy"},
    {"name_th": "อินโดนีเซีย", "name_en": "Indonesia", "iso3": "IDN", "continent": "เอเชีย", "difficulty": "Easy"},

    # ---------------- MEDIUM ----------------
    {"name_th": "เวียดนาม", "name_en": "Vietnam", "iso3": "VNM", "continent": "เอเชีย", "difficulty": "Medium"},
    {"name_th": "สวีเดน", "name_en": "Sweden", "iso3": "SWE", "continent": "ยุโรป", "difficulty": "Medium"},
    {"name_th": "นอร์เวย์", "name_en": "Norway", "iso3": "NOR", "continent": "ยุโรป", "difficulty": "Medium"},
    {"name_th": "โปแลนด์", "name_en": "Poland", "iso3": "POL", "continent": "ยุโรป", "difficulty": "Medium"},
    {"name_th": "ตุรกี", "name_en": "Turkey", "iso3": "TUR", "continent": "ยุโรป/เอเชีย", "difficulty": "Medium"},
    {"name_th": "อิหร่าน", "name_en": "Iran", "iso3": "IRN", "continent": "เอเชีย", "difficulty": "Medium"},
    {"name_th": "ไนจีเรีย", "name_en": "Nigeria", "iso3": "NGA", "continent": "แอฟริกา", "difficulty": "Medium"},
    {"name_th": "เคนยา", "name_en": "Kenya", "iso3": "KEN", "continent": "แอฟริกา", "difficulty": "Medium"},
    {"name_th": "ชิลี", "name_en": "Chile", "iso3": "CHL", "continent": "อเมริกาใต้", "difficulty": "Medium"},
    {"name_th": "เปรู", "name_en": "Peru", "iso3": "PER", "continent": "อเมริกาใต้", "difficulty": "Medium"},
    {"name_th": "ยูเครน", "name_en": "Ukraine", "iso3": "UKR", "continent": "ยุโรป", "difficulty": "Medium"},
    {"name_th": "กรีซ", "name_en": "Greece", "iso3": "GRC", "continent": "ยุโรป", "difficulty": "Medium"},
    {"name_th": "โปรตุเกส", "name_en": "Portugal", "iso3": "PRT", "continent": "ยุโรป", "difficulty": "Medium"},
    {"name_th": "เนเธอร์แลนด์", "name_en": "Netherlands", "iso3": "NLD", "continent": "ยุโรป", "difficulty": "Medium"},
    {"name_th": "สวิตเซอร์แลนด์", "name_en": "Switzerland", "iso3": "CHE", "continent": "ยุโรป", "difficulty": "Medium"},
    {"name_th": "นิวซีแลนด์", "name_en": "New Zealand", "iso3": "NZL", "continent": "โอเชียเนีย", "difficulty": "Medium"},
    {"name_th": "ฟิลิปปินส์", "name_en": "Philippines", "iso3": "PHL", "continent": "เอเชีย", "difficulty": "Medium"},
    {"name_th": "มาเลเซีย", "name_en": "Malaysia", "iso3": "MYS", "continent": "เอเชีย", "difficulty": "Medium"},
    {"name_th": "แอฟริกาใต้", "name_en": "South Africa", "iso3": "ZAF", "continent": "แอฟริกา", "difficulty": "Medium"},
    {"name_th": "โคลอมเบีย", "name_en": "Colombia", "iso3": "COL", "continent": "อเมริกาใต้", "difficulty": "Medium"},

    # ---------------- HARD ----------------
    {"name_th": "ภูฏาน", "name_en": "Bhutan", "iso3": "BTN", "continent": "เอเชีย", "difficulty": "Hard"},
    {"name_th": "มอลโดวา", "name_en": "Moldova", "iso3": "MDA", "continent": "ยุโรป", "difficulty": "Hard"},
    {"name_th": "ลาว", "name_en": "Laos", "iso3": "LAO", "continent": "เอเชีย", "difficulty": "Hard"},
    {"name_th": "กัมพูชา", "name_en": "Cambodia", "iso3": "KHM", "continent": "เอเชีย", "difficulty": "Hard"},
    {"name_th": "อุรุกวัย", "name_en": "Uruguay", "iso3": "URY", "continent": "อเมริกาใต้", "difficulty": "Hard"},
    {"name_th": "ปารากวัย", "name_en": "Paraguay", "iso3": "PRY", "continent": "อเมริกาใต้", "difficulty": "Hard"},
    {"name_th": "มองโกเลีย", "name_en": "Mongolia", "iso3": "MNG", "continent": "เอเชีย", "difficulty": "Hard"},
    {"name_th": "คาซัคสถาน", "name_en": "Kazakhstan", "iso3": "KAZ", "continent": "เอเชีย", "difficulty": "Hard"},
    {"name_th": "ตูนิเซีย", "name_en": "Tunisia", "iso3": "TUN", "continent": "แอฟริกา", "difficulty": "Hard"},
    {"name_th": "จอร์แดน", "name_en": "Jordan", "iso3": "JOR", "continent": "เอเชีย", "difficulty": "Hard"},
    {"name_th": "สโลวีเนีย", "name_en": "Slovenia", "iso3": "SVN", "continent": "ยุโรป", "difficulty": "Hard"},
    {"name_th": "สโลวาเกีย", "name_en": "Slovakia", "iso3": "SVK", "continent": "ยุโรป", "difficulty": "Hard"},
    {"name_th": "เอสโตเนีย", "name_en": "Estonia", "iso3": "EST", "continent": "ยุโรป", "difficulty": "Hard"},
    {"name_th": "ลัตเวีย", "name_en": "Latvia", "iso3": "LVA", "continent": "ยุโรป", "difficulty": "Hard"},
    {"name_th": "ลิทัวเนีย", "name_en": "Lithuania", "iso3": "LTU", "continent": "ยุโรป", "difficulty": "Hard"},
    {"name_th": "นามิเบีย", "name_en": "Namibia", "iso3": "NAM", "continent": "แอฟริกา", "difficulty": "Hard"},
    {"name_th": "บอตสวานา", "name_en": "Botswana", "iso3": "BWA", "continent": "แอฟริกา", "difficulty": "Hard"},
    {"name_th": "แซมเบีย", "name_en": "Zambia", "iso3": "ZMB", "continent": "แอฟริกา", "difficulty": "Hard"},
    {"name_th": "เมียนมา", "name_en": "Myanmar", "iso3": "MMR", "continent": "เอเชีย", "difficulty": "Hard"},
    {"name_th": "ศรีลังกา", "name_en": "Sri Lanka", "iso3": "LKA", "continent": "เอเชีย", "difficulty": "Hard"},
]

DIFFICULTY_TIME_LIMIT = {
    "Easy": 30,
    "Medium": 20,
    "Hard": 15,
}

DIFFICULTY_EMOJI = {
    "Easy": "🟢",
    "Medium": "🟡",
    "Hard": "🔴",
}


def get_countries_by_difficulty(difficulty: str):
    """คืนค่ารายชื่อประเทศทั้งหมดตามระดับความยากที่เลือก"""
    if difficulty == "All":
        return list(COUNTRIES)
    return [c for c in COUNTRIES if c["difficulty"] == difficulty]


def build_hints(country: dict):
    """สร้างคำใบ้ทีละขั้นสำหรับประเทศหนึ่ง ๆ"""
    name_th = country["name_th"]
    hints = [
        f"🌍 ทวีป: {country['continent']}",
        f"🔤 ชื่อประเทศ (ไทย) มีทั้งหมด {len(name_th)} ตัวอักษร",
        f"🔡 ตัวอักษรแรกของชื่อคือ '{name_th[0]}'",
        f"🏳️ รหัสประเทศ (ISO-3) คือ '{country['iso3']}'",
    ]
    return hints


def all_country_names():
    """คืนค่ารายชื่อประเทศ (ไทย) ทั้งหมด เรียงตามตัวอักษร สำหรับใช้ใน selectbox"""
    return sorted({c["name_th"] for c in COUNTRIES})
