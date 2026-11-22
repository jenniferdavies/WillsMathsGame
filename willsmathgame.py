import random
import streamlit as st

st.set_page_config(page_title="Maths Game", page_icon="🎮")
st.title("🎮 Maths Game")

# Streamlit reruns this file after each button click.
# Session state remembers the game between those reruns.
if "question_number" not in st.session_state:
    st.session_state.question_number = 0
if "questions" not in st.session_state:
    st.session_state.questions = []
if "feedback" not in st.session_state:
    st.session_state.feedback = ""


def make_questions(mode, times_table, digits):
    questions = []

    if mode in ("Multiplication", "Division"):
        numbers = list(range(1, 13))
        random.shuffle(numbers)
        for n in numbers:
            if mode == "Multiplication":
                questions.append((f"What is {times_table} × {n}?", times_table * n))
            else:
                questions.append((f"What is {times_table * n} ÷ {times_table}?", n))
    else:
        # The original game uses 1–9, 10–99 and 100–999.
        minimum, maximum = {1: (1, 9), 2: (10, 99), 3: (100, 999)}[digits]
        for _ in range(12):
            x = random.randint(minimum, maximum)
            y = random.randint(minimum, maximum)
            if mode == "Addition":
                questions.append((f"What is {x} + {y}?", x + y))
            else:
                # Keep subtraction answers at zero or above.
                if y > x:
                    x, y = y, x
                questions.append((f"What is {x} − {y}?", x - y))

    return questions


def restart():
    st.session_state.question_number = 0
    st.session_state.questions = []
    st.session_state.feedback = ""


if st.session_state.question_number == 0:
    st.write("Choose what you'd like to practise.")
    mode = st.radio(
        "Maths game",
        ["Multiplication", "Division", "Addition", "Subtraction"],
    )

    times_table = 3
    digits = 1
    if mode in ("Multiplication", "Division"):
        times_table = st.number_input(
            "Which times table?", min_value=1, value=3, step=1
        )
    else:
        digits = st.radio("How many digits?", [1, 2, 3], horizontal=True)

    if st.button("Start game", type="primary"):
        st.session_state.questions = make_questions(mode, times_table, digits)
        st.session_state.question_number = 1
        st.session_state.feedback = ""
        st.rerun()

elif st.session_state.question_number <= 12:
    number = st.session_state.question_number
    question, correct_answer = st.session_state.questions[number - 1]

    st.write(f"**Question {number} of 12**")
    st.progress((number - 1) / 12)
    st.subheader(question)

    if st.session_state.feedback:
        if st.session_state.feedback.startswith("Correct"):
            st.success(st.session_state.feedback)
        else:
            st.error(st.session_state.feedback)

    with st.form(key=f"answer_form_{number}", clear_on_submit=True):
        answer = st.number_input("Your answer", min_value=0, step=1, value=None, placeholder="Type your answer")
        submitted = st.form_submit_button("Check answer", type="primary")

    if submitted and answer is None:
        st.warning("Please enter an answer!")
    
    if submitted:
        if answer == correct_answer:
            st.session_state.question_number += 1
            st.session_state.feedback = "Correct! Well done!"
        else:
            st.session_state.feedback = "Wrong! Try again."
        st.rerun()

    if st.button("Start over"):
        restart()
        st.rerun()

else:
    st.progress(1.0)
    st.success("🏆 Game over! You completed all 12 questions!")
    if st.button("Play again", type="primary"):
        restart()
        st.rerun()
