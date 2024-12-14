import streamlit as st
import random

# ---------------------------
# Session State Initialization
# ---------------------------
if "selected_tense_key" not in st.session_state:
    st.session_state.selected_tense_key = None
if "answers" not in st.session_state:
    st.session_state.answers = []
if "submitted_questions" not in st.session_state:
    st.session_state.submitted_questions = set()
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "review_mode" not in st.session_state:
    st.session_state.review_mode = False
if "randomized_messages" not in st.session_state:
    motivational_sentences = [
        "You're on fire! 🔥",
        "Keep smashing it! 💥",
        "Fantastic answer! Your words are shining brighter now! 🌟",
        "You're a grammar wizard! Conjugations bend to your will! 🧙‍♂️",
        "Way to go, champ! That sentence just leapt off the page! 🏆",
        "Bravo! That's the spirit! Your linguistic muscles are flexing! 👏",
        "Grammar genius at work! Your sentences sparkle like diamonds! 🧠",
        "Outstanding! The grammar gods are smiling upon you now! 🥳",
        "You're unstoppable! The universe is taking notes from your syntax! 🚀",
        "Wonderful! Each answer you give writes poetry in the sky! 🎩✨",
        "You're dazzling! These sentences are lining up to be in your presence! ✨🌈",
        "Impressive! Your answers radiate confidence and linguistic flair! 💎💃",
        "Marvelous! The grammar galaxy bows before your might! 🌌🏅",
        "Astonishing! Every verb you conjure becomes a masterpiece! 🎉📚",
        "Magnificent! Even dictionaries blush at your command of words! 🦄📖",
        "Incredible! Grammarians form fan clubs in your honor! 🎶💫",
        "Stupendous! Your verb forms could charm the toughest critics! 🍀💬",
        "Glorious! Your tense usage now inspires entire textbooks! 🦋🔥",
        "Remarkable! Each reply is like a linguistic symphony in action! 🎼🌍",
        "Spectacular! Your English prowess bursts forth like cosmic fireworks! 💥🚀🎉"
    ]
    random.shuffle(motivational_sentences)
    st.session_state.randomized_messages = motivational_sentences

# ---------------------------
# Tenses Data
# ---------------------------
tenses_data = {
    "1": {
        "name": "Present Simple",
        "formation": {
            "Positive": "Subject + base form (e.g., 'I eat')",
            "Negative": "Subject + do not/does not + base form (e.g., 'I do not eat')",
            "Question": "Do/Does + subject + base form? (e.g., 'Do you eat?')",
            "Short answer": "'Yes, I do.' / 'No, I don't.'"
        },
        "usage_explanation": [
            "General or always true facts.",
            "Situations that are more or less permanent.",
            "Habits or things done regularly.",
            "Short actions happening now (e.g., in sports commentary).",
            "Regular events (often with always, often, never)."
        ],
        "usage_cases": [
            {"title": "Expressing facts and general truths",
             "question": "Does water boil if you heat it up?"},
            {"title": "Describing habits",
             "question": "What do you usually do after waking up?"},
            {"title": "Talking about permanent situations",
             "question": "Where do you live?"},
            {"title": "Regular events",
             "question": "How often do you go to the gym?"},
            {"title": "Describing routines",
             "question": "What time do you start work every day?"},
            {"title": "Present commentary (sports/narration)",
             "question": "Does the commentator describe the players' actions as they happen?"},
            {"title": "General preferences",
             "question": "Which type of music do you prefer?"},
            {"title": "Timetabled events",
             "question": "When does the train leave?"},
            {"title": "Stating a general ability",
             "question": "Do you speak Spanish fluently?"},
            {"title": "Describing personality traits",
             "question": "Does your friend often help others?"}
        ],
        "extra_examples": [
            "I always wake up at 7 AM.",
            "My brother doesn't eat fish.",
            "Do we need more milk?",
            "The Earth revolves around the Sun.",
            "They never watch TV in the morning."
        ]
    },
    "2": {
        "name": "Past Simple",
        "formation": {
            "Positive": "Subject + past form (e.g., 'I ate')",
            "Negative": "Subject + did not + base form (e.g., 'I did not eat')",
            "Question": "Did + subject + base form? (e.g., 'Did you eat?')",
            "Short answer": "'Yes, I did.' / 'No, I didn't.'"
        },
        "usage_explanation": [
            "Completed actions in the past.",
            "Actions that happened at a specific time.",
            "A series of actions in the past.",
            "Past habits or situations (often with 'used to')."
        ],
        "usage_cases": [
            {"title": "Completed actions at a specific time",
             "question": "What did you do yesterday evening?"},
            {"title": "A specific past event",
             "question": "Did you attend the concert last Friday?"},
            {"title": "A series of events",
             "question": "What happened after you arrived home?"},
            {"title": "Past habits",
             "question": "Where did you usually spend your summer holidays as a child?"},
            {"title": "Situations that no longer exist",
             "question": "Did you live in another country before?"},
            {"title": "Historical facts",
             "question": "Which year did the Second World War end?"},
            {"title": "Personal achievements",
             "question": "What was the best meal you ever cooked?"},
            {"title": "Past trips or experiences",
             "question": "Where did you travel last year?"},
            {"title": "Old favorites",
             "question": "Which TV shows did you like when you were younger?"},
            {"title": "Childhood memories",
             "question": "Did you have a favorite toy when you were a kid?"}
        ],
        "extra_examples": [
            "I visited my grandparents last weekend.",
            "They watched a movie yesterday.",
            "Did you talk to your friend about the issue?",
            "She cooked dinner last night.",
            "We didn’t see them at the party."
        ]
    },
}

# ---------------------------
# Helper Functions
# ---------------------------
def reset_questions():
    st.session_state.answers = []
    st.session_state.submitted_questions = set()
    st.session_state.review_mode = False
    random.shuffle(st.session_state.randomized_messages)

def personalized_name():
    name = st.session_state.user_name.strip()
    return name if name else "You"

# ---------------------------
# Layout: Sidebar Tense Selection
# ---------------------------
st.sidebar.title("Grammar Tense Selection")
tense_options = ["Select a tense..."] + [f"{key}. {tenses_data[key]['name']}" for key in tenses_data]
selected_option = st.sidebar.selectbox("Choose a tense to practice:", tense_options)

if selected_option != "Select a tense...":
    current_tense_key = selected_option.split('.')[0].strip()
    # If a new tense is chosen, reset the questions and messages
    if current_tense_key != st.session_state.selected_tense_key:
        st.session_state.selected_tense_key = current_tense_key
        reset_questions()
else:
    # No tense selected, reset to welcome state
    st.session_state.selected_tense_key = None
    reset_questions()

# ---------------------------
# Main Screens
# ---------------------------

def show_welcome():
    # CSS for fade-out animation
    st.markdown("""
    <style>
    @keyframes fadeOut {
      from {opacity: 1;}
      to {opacity: 0;}
    }
    #catgif {
      animation: fadeOut 10s forwards;
    }
    .custom-welcome-title {
      font-size: 3rem;
      font-family: Arial, sans-serif;
      font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    # Fireworks and cat gif
    st.markdown('<img src="https://media.giphy.com/media/l0Exk8EUzSLsrErEQ/giphy.gif" width="300">', unsafe_allow_html=True)
    st.markdown('<div id="catgif"><img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" width="200"></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="custom-welcome-title">Welcome to the Grammar Genius Game! 🎉✨🎮</div>
    """, unsafe_allow_html=True)

    st.write("""
    Get ready to boost your English grammar skills in a fun and interactive way!
    
    1. Enter your name below (optional, but more fun!).
    2. Use the sidebar to choose an English tense.
    3. Read how it's formed, when to use it, and review sample usage cases.
    4. Answer the questions under each usage case.
    5. Receive motivational feedback as you progress!

    Let's get started!
    """)
    st.text_input("Your name:", key="user_name")
    st.balloons()

def show_review(tense_info):
    st.header("Review Your Answers")
    for i, case in enumerate(tense_info["usage_cases"]):
        answer_key = f"answer_{st.session_state.selected_tense_key}_{i}"
        st.write(f"**{case['title']}**")
        st.write(f"Question: {case['question']}")
        user_answer = st.session_state.get(answer_key, "")
        st.write(f"Your answer: {user_answer}")
    st.write("Great job! Feel free to choose another tense from the sidebar.")

def show_explanation_and_questions():
    key = st.session_state.selected_tense_key
    if key is None:
        return

    tense_info = tenses_data[key]

    # Fade-out GIF at top
    st.markdown("""
    <style>
    @keyframes fadeOut {
      from {opacity: 1;}
      to {opacity: 0;}
    }
    #catgif {
      animation: fadeOut 10s forwards;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<div id="catgif"><img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" width="200"></div>', unsafe_allow_html=True)

    st.header(tense_info["name"])
    st.subheader("How is it formed?")
    for form_type, form_rule in tense_info["formation"].items():
        st.write(f"**{form_type}:** {form_rule}")

    st.subheader("When do we use it?")
    for usage in tense_info["usage_explanation"]:
        st.write("- " + usage)

    # Additional examples on demand
    with st.expander("More Examples"):
        if "extra_examples" in tense_info:
            for ex in tense_info["extra_examples"]:
                st.write("- " + ex)

    st.subheader("Practice Questions")

    total_questions = len(tense_info["usage_cases"])
    answered_count = len(st.session_state.answers)

    if st.session_state.review_mode:
        # Show review mode
        show_review(tense_info)
        return

    st.write(f"Questions answered: {answered_count}/{total_questions}")
    st.write("Below are several usage cases of this tense. Please answer each question accordingly.")

    if answered_count == total_questions:
        # All answered
        st.success(f"Congratulations, {personalized_name()}! You've answered all the questions!")
        # Replace the final GIF with a dancing cat GIF:
        st.markdown('<img src="https://media.giphy.com/media/5Zesu5VPNGJlm/giphy.gif" width="300">', unsafe_allow_html=True)
        st.balloons()
        if st.button("Review Your Answers", on_click=lambda: setattr(st.session_state, 'review_mode', True)):
            pass
        return

    # Display questions not yet answered
    for i, case in enumerate(tense_info["usage_cases"]):
        answer_key = f"answer_{key}_{i}"
        submit_key = f"submit_{key}_{i}"

        if submit_key in st.session_state.submitted_questions:
            continue  # Already answered this one

        st.write(f"**{case['title']}**")
        st.write(case["question"])
        
        if answer_key not in st.session_state:
            st.session_state[answer_key] = ""
        user_answer = st.text_input("Your answer:", key=answer_key)

        if st.button("Submit", key=submit_key, on_click=lambda: [
            st.session_state.answers.append(user_answer),
            st.session_state.submitted_questions.add(submit_key),
            st.success(f"{personalized_name()}, {st.session_state.randomized_messages[len(st.session_state.answers) - 1]}")
        ]):
            pass

# ---------------------------
# Main Execution
# ---------------------------
def main():
    if st.session_state.selected_tense_key is None:
        show_welcome()
    else:
        show_explanation_and_questions()

if __name__ == "__main__":
    main()
