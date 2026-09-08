# 🌍 Guess The Country

เกมทายชื่อประเทศจากรูปร่างแผนที่ (silhouette) เขียนด้วย Python + Streamlit

## ติดตั้ง

```bash
pip install -r requirements.txt
```

## รันเกม

```bash
streamlit run app.py
```

จากนั้นเปิดเบราว์เซอร์ที่ลิงก์ที่ Streamlit แสดง (ปกติคือ `http://localhost:8501`)

## โครงสร้างไฟล์

- `app.py` — โค้ดหลักของเกมและ UI
- `data.py` — ข้อมูลประเทศ, ระดับความยาก, ตัวสร้างคำใบ้
- `style.css` — ตกแต่งหน้าเว็บให้สีสันสดใส ทันสมัย
- `requirements.txt` — ไลบรารีที่ต้องใช้
- `highscore.json` — ไฟล์บันทึกคะแนนสูงสุด (สร้างอัตโนมัติเมื่อเล่นครั้งแรก)
