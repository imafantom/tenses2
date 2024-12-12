import streamlit as st
import random

# Motivational messages
motivational_messages = [
    "Great job, [User]! Keep it up!",
    "You're doing amazing, [User]! Stay focused!",
    "Well done, [User]! Keep going!",
    "Fantastic effort, [User]! You're a star!",
    "Keep shining, [User]! You're learning fast!",
    "You're unstoppable, [User]! Keep learning!",
    "Excellent work, [User]! Proud of you!",
    "Learning looks good on you, [User]!",
    "Way to go, [User]! Keep it rolling!",
    "You're an English master in the making, [User]!"
]

# Shuffle messages
random.shuffle(motivational_messages)

# Define tense explanations
tenses = {
    "Present Simple": {
        "Explanation": "Used for habits and general truths.",
        "Form": "Subject + base verb (add 's' for he/she/it)",
        "Usage": "E.g., I play tennis every week. She studies hard.",
        "Examples": ["The sun rises in the east.", "I enjoy reading books."]
    },
    "Past Simple": {
        "Explanation": "Used for actions completed in the past.",
        "Form": "Subject + verb-ed (regular) / irregular verb",
        "Usage": "E.g., I visited Paris last year. He went to the market.",
        "Examples": ["She walked to school.", "They played football."]
    },
}

def initialize_session_state():
    """Initialize session state variables."""
    if "user_name" not in st.session_state:
        st.session_state["user_name"] = ""
    if "tense" not in st.session_state:
        st.session_state["tense"] = ""
    if "question_number" not in st.session_state:
        st.session_state["question_number"] = 1
    if "answers" not in st.session_state:
        st.session_state["answers"] = []
    if "message_index" not in st.session_state:
        st.session_state["message_index"] = 0
    if "rerun_triggered" not in st.session_state:
        st.session_state["rerun_triggered"] = False

def trigger_rerun():
    """Trigger a safe rerun without conflicts."""
    st.session_state["rerun_triggered"] = True
    st.experimental_rerun()

def main():
    st.set_page_config(page_title="English Grammar Practice", page_icon="📚")

    initialize_session_state()

    # Home screen
    if not st.session_state["user_name"]:
        st.title("Welcome to English Grammar Practice!")
        st.markdown("## Enter your name below to get started:")
        user_name = st.text_input("What's your name?", key="name_input")
        if st.button("Continue", key="name_continue"):
            if user_name.strip():
                st.session_state["user_name"] = user_name
                st.balloons()
                trigger_rerun()

    elif not st.session_state["tense"]:
        st.title(f"Hello, {st.session_state['user_name']}!")
        st.markdown("### Why are you here?")
        reason = st.radio(
            "Choose your reason:",
            ["Because I love learning English with all my heart", "My teacher made me use this app"],
            key="reason"
        )
        if st.button("Continue", key="reason_continue"):
            st.session_state["tense"] = "Select a tense"
            trigger_rerun()

    else:
        # Practice interface
        st.sidebar.title("Choose a Tense")
        tense_selection = st.sidebar.radio("Tenses", list(tenses.keys()), key="tense_selection")
        st.session_state["tense"] = tense_selection

        st.title(f"{tense_selection} - Grammar Practice")
        tense_data = tenses[tense_selection]
        st.markdown(f"### Explanation: {tense_data['Explanation']}")
        st.markdown(f"**Form:** {tense_data['Form']}")
        st.markdown(f"**Usage:** {tense_data['Usage']}")
        with st.expander("More Examples"):
            st.write("\n".join(tense_data["Examples"]))

        if st.session_state["question_number"] <= 10:
            st.markdown(f"### Question {st.session_state['question_number']}")
            question = f"Write a sentence in {tense_selection} tense."
            user_answer = st.text_input(question, key=f"q{st.session_state['question_number']}")
            if st.button("Submit", key=f"submit{st.session_state['question_number']}"):
                feedback = motivational_messages[st.session_state["message_index"] % len(motivational_messages)]
                st.write(feedback.replace("[User]", st.session_state["user_name"]))
                st.write(f"Your answer: {user_answer}")
                st.session_state["answers"].append(user_answer)
                st.session_state["message_index"] += 1
                st.session_state["question_number"] += 1
                trigger_rerun()
        else:
            st.success("Congratulations! You've completed this practice.")
            st.image("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif", use_column_width=True)
            st.balloons()
            st.write("Select another tense from the sidebar to continue practicing!")

if __name__ == "__main__":
    main()
