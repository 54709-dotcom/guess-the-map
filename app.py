# -*- coding: utf-8 -*-
"""
app.py
เกมทายชื่อประเทศจากรูปร่างแผนที่ (Guess The Country)
รันด้วยคำสั่ง: streamlit run app.py
"""

import json
import os
import random
import time

import plotly.express as px
import streamlit as st
from streamlit_autorefresh import st_autorefresh

from data import (
    DIFFICULTY_EMOJI,
    DIFFICULTY_TIME_LIMIT,
    all_country_names,
    build_hints,
    get_countries_by_difficulty,
)

# --------------------------------------------------------------------------
# ตั้งค่าหน้าเว็บ
# --------------------------------------------------------------------------
st.set_page_config(
    page_title="Guess The Country 🌍",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="expanded",
)

HIGHSCORE_FILE = os.path.join(os.path.dirname(__file__), "highscore.json")


def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "style.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def load_high_scores():
    if os.path.exists(HIGHSCORE_FILE):
        try:
            with open(HIGHSCORE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"Easy": 0, "Medium": 0, "Hard": 0, "All": 0}


def save_high_scores(scores: dict):
    try:
        with open(HIGHSCORE_FILE, "w", encoding="utf-8") as f:
            json.dump(scores, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


# --------------------------------------------------------------------------
# จัดการ session state
# --------------------------------------------------------------------------
def init_state(difficulty: str, timer_mode: bool):
    pool = get_countries_by_difficulty(difficulty)
    random.shuffle(pool)
    st.session_state.queue = pool
    st.session_state.difficulty = difficulty
    st.session_state.timer_mode = timer_mode
    st.session_state.score = 0
    st.session_state.total_played = 0
    st.session_state.correct_count = 0
    st.session_state.game_over = False
    st.session_state.high_scores = load_high_scores()
    next_country()


def next_country():
    """ดึงประเทศถัดไปจากคิว (สุ่มไม่ซ้ำ) หากคิวหมด -> จบเกม"""
    queue = st.session_state.get("queue", [])
    if not queue:
        st.session_state.game_over = True
        st.session_state.current_country = None
        return
    st.session_state.current_country = queue.pop()
    st.session_state.queue = queue
    st.session_state.hint_level = 0
    st.session_state.solved = False
    st.session_state.feedback = None
    st.session_state.feedback_type = None
    st.session_state.start_time = time.time()
    # เปลี่ยนหมายเลขรอบ เพื่อให้ widget คำตอบ (text_input/selectbox) เป็นค่าว่างใหม่ทุกครั้ง
    # โดยไม่ต้องไปยุ่งกับ session_state ของ widget เดิมโดยตรง (ซึ่ง Streamlit ไม่อนุญาต
    # หากมีการสร้าง widget นั้นไปแล้วในรอบสคริปต์เดียวกัน)
    st.session_state.round_id = st.session_state.get("round_id", 0) + 1


def normalize(text: str) -> str:
    return text.strip().lower().replace(" ", "")


def check_answer(user_answer: str):
    country = st.session_state.current_country
    correct = normalize(user_answer) in (
        normalize(country["name_th"]),
        normalize(country["name_en"]),
    )
    if correct:
        st.session_state.score += 1
        st.session_state.correct_count += 1
        st.session_state.total_played += 1
        st.session_state.solved = True
        st.session_state.feedback = "🎉 ถูกต้อง!"
        st.session_state.feedback_type = "correct"
        update_high_score()
    else:
        st.session_state.feedback = "❌ ลองใหม่"
        st.session_state.feedback_type = "wrong"


def handle_timeout():
    country = st.session_state.current_country
    st.session_state.total_played += 1
    st.session_state.solved = True
    st.session_state.feedback = f"⏰ หมดเวลา! คำตอบคือ {country['name_th']} ({country['name_en']})"
    st.session_state.feedback_type = "timeout"


def handle_skip():
    st.session_state.total_played += 1
    st.session_state.feedback = None
    next_country()


def update_high_score():
    diff = st.session_state.difficulty
    current_high = st.session_state.high_scores.get(diff, 0)
    if st.session_state.score > current_high:
        st.session_state.high_scores[diff] = st.session_state.score
        save_high_scores(st.session_state.high_scores)


# --------------------------------------------------------------------------
# วาดรูปร่าง (silhouette) ของประเทศ โดยไม่แสดงชื่อ
# --------------------------------------------------------------------------
def render_country_shape(iso3: str):
    fig = px.choropleth(
        locations=[iso3],
        locationmode="ISO-3",
        color=[1],
        color_continuous_scale=[[0, "#FFD93D"], [1, "#FFD93D"]],
    )
    fig.update_traces(
        marker_line_color="#0f0c29",
        marker_line_width=1.2,
        hoverinfo="skip",
        hovertemplate=None,
        showscale=False,
    )
    fig.update_geos(
        visible=False,
        showcountries=False,
        showcoastlines=False,
        showland=True,
        landcolor="#1b1f3b",
        showocean=True,
        oceancolor="#0d0f1a",
        showlakes=False,
        showframe=False,
        fitbounds="locations",
        projection_type="natural earth",
    )
    fig.update_layout(
        coloraxis_showscale=False,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=360,
        dragmode=False,
    )
    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False, "scrollZoom": False, "staticPlot": True},
    )


# --------------------------------------------------------------------------
# UI หลัก
# --------------------------------------------------------------------------
def main():
    load_css()

    st.markdown('<p class="game-title">🌍 Guess The Country</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="game-subtitle">ทายชื่อประเทศจากรูปร่างแผนที่ ให้ได้คะแนนสูงสุด!</p>',
        unsafe_allow_html=True,
    )

    # ---------------- Sidebar: ตั้งค่าเกม ----------------
    with st.sidebar:
        st.header("⚙️ ตั้งค่าเกม")
        difficulty = st.radio(
            "🎯 ระดับความยาก",
            options=["Easy", "Medium", "Hard", "All"],
            format_func=lambda d: f"{DIFFICULTY_EMOJI.get(d, '🌐')} {d}",
            index=0,
            key="selected_difficulty",
        )
        timer_mode = st.checkbox("⏱️ เปิดโหมดจับเวลา", value=False, key="selected_timer")

        st.markdown("---")
        if st.button("🔄 เริ่มเกมใหม่", use_container_width=True):
            init_state(difficulty, timer_mode)
            st.rerun()

        st.markdown("---")
        st.subheader("🔥 คะแนนสูงสุด")
        hs = st.session_state.get("high_scores", load_high_scores())
        for d in ["Easy", "Medium", "Hard", "All"]:
            st.write(f"{DIFFICULTY_EMOJI.get(d,'🌐')} {d}: **{hs.get(d, 0)}**")

    # ---------------- เริ่มต้นสถานะเกม (ครั้งแรก) ----------------
    if "current_country" not in st.session_state:
        init_state(difficulty, timer_mode)

    # ถ้าผู้ใช้เปลี่ยนระดับความยาก/โหมดจับเวลา ให้เริ่มเกมใหม่อัตโนมัติ
    if (
        st.session_state.get("difficulty") != difficulty
        or st.session_state.get("timer_mode") != timer_mode
    ):
        init_state(difficulty, timer_mode)

    # ---------------- แถวสถิติ ----------------
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(
            f'<div class="stat-box"><div class="stat-value">{st.session_state.score}</div>'
            f'<div class="stat-label">คะแนน</div></div>',
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f'<div class="stat-box"><div class="stat-value">{st.session_state.total_played}</div>'
            f'<div class="stat-label">เล่นไปแล้ว</div></div>',
            unsafe_allow_html=True,
        )
    with col3:
        remaining = len(st.session_state.get("queue", [])) + (
            0 if st.session_state.get("game_over") else 1
        )
        st.markdown(
            f'<div class="stat-box"><div class="stat-value">{remaining}</div>'
            f'<div class="stat-label">เหลืออีก</div></div>',
            unsafe_allow_html=True,
        )
    with col4:
        hs_current = st.session_state.high_scores.get(st.session_state.difficulty, 0)
        st.markdown(
            f'<div class="stat-box"><div class="stat-value">{hs_current}</div>'
            f'<div class="stat-label">สูงสุด</div></div>',
            unsafe_allow_html=True,
        )

    st.write("")
    st.markdown(
        f'<span class="difficulty-badge">{DIFFICULTY_EMOJI.get(st.session_state.difficulty,"🌐")} '
        f'ระดับ: {st.session_state.difficulty}</span>',
        unsafe_allow_html=True,
    )

    # ---------------- จบเกม: แสดงสรุปคะแนน ----------------
    if st.session_state.get("game_over"):
        acc = (
            round(100 * st.session_state.correct_count / st.session_state.total_played, 1)
            if st.session_state.total_played > 0
            else 0
        )
        st.markdown(
            f"""
            <div class="summary-box">
                <h2>🏁 จบเกมแล้ว!</h2>
                <p style="font-size:1.1rem;">คุณทายประเทศครบทุกข้อในระดับ <b>{st.session_state.difficulty}</b> แล้ว</p>
                <p style="font-size:1.3rem;">คะแนนรวม: <b>{st.session_state.score}</b> / {st.session_state.total_played}</p>
                <p>ความแม่นยำ: <b>{acc}%</b></p>
                <p>🔥 คะแนนสูงสุด (ระดับนี้): <b>{st.session_state.high_scores.get(st.session_state.difficulty,0)}</b></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        if st.button("🔄 เริ่มเกมใหม่", key="restart_after_gameover", use_container_width=True):
            init_state(difficulty, timer_mode)
            st.rerun()
        return

    country = st.session_state.current_country
    if country is None:
        st.warning("ไม่พบข้อมูลประเทศ กรุณากด 'เริ่มเกมใหม่'")
        return

    # ---------------- ตัวจับเวลา ----------------
    time_limit = DIFFICULTY_TIME_LIMIT.get(country["difficulty"], 25)
    if st.session_state.timer_mode and not st.session_state.solved:
        st_autorefresh(interval=1000, key="timer_refresh")
        elapsed = time.time() - st.session_state.start_time
        remaining_time = max(0, int(time_limit - elapsed))
        badge_class = "timer-warn" if remaining_time <= 5 else "timer-ok"
        st.markdown(
            f'<span class="timer-badge {badge_class}">⏱️ เวลาที่เหลือ: {remaining_time} วินาที</span>',
            unsafe_allow_html=True,
        )
        if remaining_time <= 0:
            handle_timeout()
            st.rerun()

    # ---------------- แสดงรูปร่างแผนที่ ----------------
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    render_country_shape(country["iso3"])
    st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- ข้อความผลลัพธ์ ----------------
    if st.session_state.feedback:
        css_class = f"feedback-{st.session_state.feedback_type}"
        st.markdown(
            f'<div class="{css_class}">{st.session_state.feedback}</div>',
            unsafe_allow_html=True,
        )

    # ---------------- โซนคำใบ้ ----------------
    hints = build_hints(country)
    with st.expander("💡 ต้องการคำใบ้ไหม?"):
        if st.session_state.hint_level == 0:
            st.write("ยังไม่ได้เปิดคำใบ้ กดปุ่มด้านล่างเพื่อดูคำใบ้ทีละข้อ")
        for h in hints[: st.session_state.hint_level]:
            st.write(h)

        hint_disabled = st.session_state.hint_level >= len(hints) or st.session_state.solved
        if st.button(
            "💡 ขอคำใบ้เพิ่ม" if st.session_state.hint_level < len(hints) else "💡 ไม่มีคำใบ้เพิ่มแล้ว",
            disabled=hint_disabled,
            use_container_width=True,
        ):
            st.session_state.hint_level += 1
            st.rerun()

    # ---------------- ช่องตอบคำถาม ----------------
    if not st.session_state.solved:
        round_id = st.session_state.get("round_id", 0)
        with st.form(key=f"answer_form_{round_id}", clear_on_submit=False):
            typed = st.text_input(
                "✍️ พิมพ์ชื่อประเทศ (ไทยหรืออังกฤษ)",
                key=f"answer_text_{round_id}",
                placeholder="เช่น ไทย หรือ Thailand",
            )
            chosen = st.selectbox(
                "หรือเลือกจากรายการ",
                options=["-- เลือกชื่อประเทศ --"] + all_country_names(),
                key=f"answer_select_{round_id}",
            )
            col_submit, col_skip = st.columns(2)
            with col_submit:
                submitted = st.form_submit_button("✅ ตอบ", use_container_width=True)
            with col_skip:
                skipped = st.form_submit_button("⏭️ ข้ามประเทศ", use_container_width=True)

        if submitted:
            answer = typed.strip()
            if not answer and chosen != "-- เลือกชื่อประเทศ --":
                answer = chosen
            if answer:
                check_answer(answer)
            else:
                st.session_state.feedback = "⚠️ กรุณาพิมพ์หรือเลือกชื่อประเทศก่อนตอบ"
                st.session_state.feedback_type = "wrong"
            st.rerun()

        if skipped:
            handle_skip()
            st.rerun()
    else:
        st.info(f"เฉลย: **{country['name_th']}** ({country['name_en']})")
        if st.button("▶️ ข้อถัดไป", use_container_width=True, key="next_after_solved"):
            next_country()
            st.rerun()


if __name__ == "__main__":
    main()
