import streamlit as st
import random
import time

# --- Data for the app ---
tenses = {
    "Present Simple": {
        "formation": """
            **Positive:** Subject + base form of verb (+ -s/-es for third person singular)
            **Negative:** Subject + do/does + not + base form of verb
            **Question:** Do/Does + subject + base form of verb?
            **Short Answers:** Yes, subject + do/does. / No, subject + do/does + not.
        """,
        "usage": "Used for habits, routines, facts, and general truths.",
        "examples": [
            "I eat breakfast every morning.",
            "She plays the piano beautifully.",
            "They don't live in the city.",
            "Does he speak English?"
        ],
        "scenarios": [
            {"title": "Habits", "question": "What do you do every morning?"},
            {"title": "Routines", "question": "What do you do before you go to bed?"},
            # ... add 8 more scenarios
        ]
    },
    "Past Simple": {
        # ... add formation, usage, examples, and scenarios for Past Simple
    },
    # ... add more tenses
}

motivational_messages = [
    "Keep up the great work, {name}!",
    "You're doing fantastic, {name}!",
    "Amazing effort, {name}!",
    # ... add more motivational messages (at least 20)
]

# --- Helper Functions ---
def show_gif(gif_path, duration=10):
    """Displays a GIF with a fade-out effect."""
    with open(gif_path, "rb") as gif_file:
        gif = gif_file.read()
    st.markdown(
        f"""
        <style>
        .gif-container {{
            position: relative;
            overflow: hidden;
            width: 100%;
            max-width: 400px; /* Adjust as needed */
            margin: 0 auto;
        }}
        .gif {{
            animation: fadeOut {duration}s linear forwards;
        }}
        @keyframes fadeOut {{
            0% {{ opacity: 1; }}
            100% {{ opacity: 0; }}
        }}
        </style>
        <div class="gif-container">
            <img src="data:image/gif;base64,{gif.encode('base64').decode()}" class="gif">
        </div>
        """,
        unsafe_allow_html=True,
    )
    time.sleep(duration)  # Wait for the animation to complete

# --- App Starts Here ---

# --- CSS for large, attractive font ---
st.markdown(
    """
    <style>
    .big-font {
        font-size: 50px !important; /* Adjust size as needed */
        font-weight: bold;
        font-family: 'Arial Black', sans-serif;
        color: #3366ff; /* Example color */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Initial Screen ---
st.markdown('<p class="big-font">Welcome to the English Grammar Guru!</p>', unsafe_allow_html=True)
show_gif("typing_cat.gif")  # Replace with your GIF path
user_name = st.text_input("Please enter your name:")

if st.button("Continue"):
    if user_name:
        st.balloons()
        # --- "Why Here" Screen ---
        st.write(f"<p class='big-font'>{user_name} – Why are you here?!</p>", unsafe_allow_html=True)
        why_here = st.radio(
            "Choose one:",
            [
                "Because I love learning English with all my heart",
                "My teacher made me use this app"
            ]
        )
        if st.button("Continue"):
            # --- Main Practice Interface ---
            st.sidebar.title("Select a Tense")
            selected_tense = st.sidebar.selectbox(
                "Tenses", list(tenses.keys())
            )

            if selected_tense:
                st.header(selected_tense)
                st.write(tenses[selected_tense]["formation"])
                st.write(tenses[selected_tense]["usage"])

                # --- More Examples Expander ---
                with st.expander("More Examples"):
                    for example in tenses[selected_tense]["examples"]:
                        st.write(example)

                # --- Practice Questions ---
                random.shuffle(motivational_messages)  # Shuffle messages at the start
                message_counter = 0
                answered_count = 0

                for scenario in tenses[selected_tense]["scenarios"]:
                    st.subheader(scenario["title"])
                    user_answer = st.text_input(scenario["question"])
                    if st.button("Submit"):
                        st.write(motivational_messages[message_counter % len(motivational_messages)].format(name=user_name))
                        message_counter += 1
                        st.write("Your answer:", user_answer)
                        answered_count += 1
                        st.write(f"You have answered {answered_count} out of 10 questions.")

                # --- Congratulatory Message and GIF ---
                if answered_count == 10:
                    st.balloons()
                    st.success("Congratulations! You have completed all the questions for this tense!")
                    show_gif("dancing_cat.gif")  # Replace with your GIF path
                    st.write("Select another tense from the sidebar to continue practicing.")
    else:
        st.error("Please enter your name to continue.")
