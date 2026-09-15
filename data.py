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
    {"name_th": "ญี่ปุ่น", "name_en": "Japan", "iso3": "JPN", "continent": "เอเชีย", "difficulty": "Easy"},
    {"name_th": "รัสเซีย", "name_en": "Russia", "iso3": "RUS", "continent": "ยุโรป/เอเชีย", "difficulty": "Easy"},
    {"name_th": "ไทย", "name_en": "Thailand", "iso3": "THA", "continent": "เอเชีย", "difficulty": "Easy"},
    {"name_th": "เกาหลีใต้", "name_en": "South Korea", "iso3": "KOR", "continent": "เอเชีย", "difficulty": "Easy"},

    # ---------------- MEDIUM ----------------
    {"name_th": "สวีเดน", "name_en": "Sweden", "iso3": "SWE", "continent": "ยุโรป", "difficulty": "Medium"},
    {"name_th": "นิวซีแลนด์", "name_en": "New Zealand", "iso3": "NZL", "continent": "โอเชียเนีย", "difficulty": "Medium"},
    {"name_th": "ฟิลิปปินส์", "name_en": "Philippines", "iso3": "PHL", "continent": "เอเชีย", "difficulty": "Medium"},
    {"name_th": "มาเลเซีย", "name_en": "Malaysia", "iso3": "MYS", "continent": "เอเชีย", "difficulty": "Medium"},
    {"name_th": "แอฟริกาใต้", "name_en": "South Africa", "iso3": "ZAF", "continent": "แอฟริกา", "difficulty": "Medium"},
    {"name_th": "โคลอมเบีย", "name_en": "Colombia", "iso3": "COL", "continent": "อเมริกาใต้", "difficulty": "Medium"},

    # ---------------- HARD ----------------
    {"name_th": "ลาว", "name_en": "Laos", "iso3": "LAO", "continent": "เอเชีย", "difficulty": "Hard"},
    {"name_th": "กัมพูชา", "name_en": "Cambodia", "iso3": "KHM", "continent": "เอเชีย", "difficulty": "Hard"},
    {"name_th": "มองโกเลีย", "name_en": "Mongolia", "iso3": "MNG", "continent": "เอเชีย", "difficulty": "Hard"},
    {"name_th": "จอร์แดน", "name_en": "Jordan", "iso3": "JOR", "continent": "เอเชีย", "difficulty": "Hard"},
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
