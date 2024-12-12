import streamlit as st
import random
import time

st.set_page_config(page_title="English Grammar Practice", page_icon="📚")

# Custom CSS for large font
st.markdown(
    """
    <style>
    .big-font {
        font-size:48px !important;
        font-weight: bold;
        color: #3498db; /* Example color */
        text-shadow: 2px 2px 4px #000000; /* Example shadow */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Motivational messages
motivational_messages = [
    "You're doing great, {}!",
    "Keep up the amazing work, {}!",
    "You're a grammar superstar, {}!",
    "Every step counts, {}!",
    "You're making progress, {}!",
    "Don't give up, {}!",
    "You're a language master in the making, {}!",
    "You've got this, {}!",
    "Learning is a journey, not a race, {}!",
    "You're inspiring, {}!",
    "Your effort is paying off, {}!",
    "You're a true learner, {}!",
    "You're shining bright, {}!",
    "You're on the right track, {}!",
    "You're a grammar whiz, {}!",
    "You're doing fantastic, {}!",
    "You're a language pro, {}!",
    "You're a star, {}!",
    "You're rocking it, {}!",
    "You're simply amazing, {}!"
]

# Tenses data (simplified example)
tenses = {
    "Present Simple": {
        "explanation": "Used for habits, facts, and general truths.",
        "usage": "Expressing daily routines, stating facts.",
        "examples": ["I eat breakfast every morning.", "The sun rises in the east."],
        "questions": [
            {"scenario": "Habits", "question": "What do you usually do on weekends?"},
            {"scenario": "Facts", "question": "Where do you live?"},
            {"scenario": "Daily Routines", "question": "What time do you wake up?"},
            {"scenario": "Likes/Dislikes", "question": "Do you like pizza?"},
            {"scenario": "General Truths", "question": "Is water wet?"},
            {"scenario": "Schedules", "question": "When does the train leave?"},
            {"scenario": "Repeated Actions", "question": "How often do you go to the gym?"},
            {"scenario": "States", "question": "Do you understand this?"},
            {"scenario": "Instructions", "question": "How do you make tea?"},
            {"scenario": "Future Timetable", "question": "When does the movie start?"}
        ],
    },
    "Past Simple": {
        "explanation": "Used for completed actions in the past.",
        "usage": "Describing finished events.",
        "examples": ["I went to the store yesterday.", "She studied hard for the exam."],
        "questions": [
        {"scenario": "Completed Actions", "question": "What did you do last weekend?"},
            {"scenario": "Specific Time", "question": "Where did you go last night?"},
            {"scenario": "Series of Actions", "question": "What did you do after you woke up?"},
            {"scenario": "Habits in the Past", "question": "What did you usually do as a child?"},
            {"scenario": "Duration in the Past", "question": "How long did you live there?"},
            {"scenario": "Past Facts", "question": "Where were you born?"},
            {"scenario": "Past States", "question": "Were you happy yesterday?"},
            {"scenario": "Past Events", "question": "What happened at the party?"},
            {"scenario": "Past Experiences", "question": "Did you ever travel abroad?"},
            {"scenario": "Short Actions", "question": "What did you eat for breakfast?"}
        ],
    },
}

if "user_name" not in st.session_state:
    st.session_state.user_name = None
if "motivational_messages" not in st.session_state:
    random.shuffle(motivational_messages)
    st.session_state.motivational_messages = motivational_messages
if "current_message_index" not in st.session_state:
    st.session_state.current_message_index = 0
if "answered_questions" not in st.session_state:
    st.session_state.answered_questions = {}

if st.session_state.user_name is None:
    st.markdown("<p class='big-font'>Welcome to Grammar Practice!</p>", unsafe_allow_html=True)
    st.image("typing_cat.gif", use_column_width=True)
    time.sleep(10)
    st.session_state.user_name = st.text_input("Please enter your name:")
    if st.session_state.user_name:
        st.balloons()
        st.experimental_rerun() #Force a rerun to proceed to the next section
else:
    if "why_here" not in st.session_state:
        st.write(f"<p class='big-font'>{st.session_state.user_name} – Why are you here?!</p>", unsafe_allow_html=True)
        why_here = st.radio("", ("Because I love learning English with all my heart", "My teacher made me use this app"))
        if st.button("Continue"):
            st.session_state.why_here = True
            st.experimental_rerun()
    else:
        st.sidebar.title("Select a Tense")
        selected_tense = st.sidebar.selectbox("", list(tenses.keys()))

        if selected_tense:
            tense_data = tenses[selected_tense]
            st.write(f"## {selected_tense}")
            st.write(f"**Explanation:** {tense_data['explanation']}")
            st.write(f"**Usage:** {tense_data['usage']}")
            with st.expander("More Examples"):
                for example in tense_data["examples"]:
                    st.write(f"- {example}")

            if selected_tense not in st.session_state.answered_questions:
                st.session_state.answered_questions[selected_tense] = [None] * 10

            for i, question_data in enumerate(tense_data["questions"]):
                st.write(f"### {question_data['scenario']}")
                st.write(question_data['question'])

                user_answer = st.text_input("", key=f"{selected_tense}_{i}")

                if st.button("Submit", key=f"submit_{selected_tense}_{i}"):
                    st.write(st.session_state.motivational_messages[st.session_state.current_message_index % len(st.session_state.motivational_messages)].format(st.session_state.user_name))
                    st.session_state.answered_questions[selected_tense][i] = user_answer
                    st.write(f"Your answer: {user_answer}")
                    st.session_state.current_message_index += 1
                if st.session_state.answered_questions[selected_tense][i] is not None:
                    st.write(f"Your previous answer: {st.session_state.answered_questions[selected_tense][i]}")
                answered_count = sum(1 for x in st.session_state.answered_questions[selected_tense] if x is not None)
                st.write(f"Questions answered: {answered_count}/10")

            if all(x is not None for x in st.session_state.answered_questions[selected_tense]):
                st.balloons()
                st.image("dancing_cat.gif", use_column_width=True)
                st.success(f"Congratulations {st.session_state.user_name}! You've completed all questions for {selected_tense}!")