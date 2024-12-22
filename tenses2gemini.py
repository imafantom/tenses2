import streamlit as st
import random

# ---------------------------------------------------------
# Session State Initialization
# ---------------------------------------------------------
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

# ---------------------------------------------------------
# Tenses Data
# ---------------------------------------------------------
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
            "Short actions happening now (e.g., sports commentary).",
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
            {"title": "Present commentary",
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
    "3": {
        "name": "Present Continuous",
        "formation": {
            "Positive": "Subject + am/is/are + verb-ing (e.g., 'I am eating')",
            "Negative": "Subject + am/is/are + not + verb-ing (e.g., 'I am not eating')",
            "Question": "Am/Is/Are + subject + verb-ing? (e.g., 'Are you eating?')",
            "Short answer": "'Yes, I am.' / 'No, I'm not.'"
        },
        "usage_explanation": [
            "Actions happening right now, at this moment.",
            "Temporary situations, not always true but happening around now.",
            "Trends or changing situations.",
            "Annoying habits (often with 'always')."
        ],
        "usage_cases": [
            {"title": "Actions happening now",
             "question": "What are you doing at this very moment?"},
            {"title": "Temporary situations",
             "question": "Are you staying with your parents this week?"},
            {"title": "Trends",
             "question": "Is online learning becoming more popular these days?"},
            {"title": "Changing situations",
             "question": "Is your town growing quickly?"},
            {"title": "Annoying habits",
             "question": "Are you always forgetting your keys?"},
            {"title": "Unusual behavior",
             "question": "Are you eating more vegetables than usual lately?"},
            {"title": "Current projects",
             "question": "Are you working on any new skills right now?"},
            {"title": "Near-future plans",
             "question": "Are you meeting your friends later today?"},
            {"title": "Ongoing processes",
             "question": "Are they building a new mall in your neighborhood?"},
            {"title": "Temporary states",
             "question": "Is your friend studying abroad this semester?"}
        ],
        "extra_examples": [
            "I am studying English right now.",
            "She is currently watching a documentary.",
            "We are planning a trip for the holidays.",
            "He is getting better at playing the guitar.",
            "They are always arguing over small things."
        ]
    },
    "4": {
        "name": "Past Continuous",
        "formation": {
            "Positive": "Subject + was/were + verb-ing (e.g., 'I was eating')",
            "Negative": "Subject + was/were + not + verb-ing (e.g., 'I was not eating')",
            "Question": "Was/Were + subject + verb-ing? (e.g., 'Were you eating?')",
            "Short answer": "'Yes, I was.' / 'No, I wasn't.'"
        },
        "usage_explanation": [
            "Actions in progress at a specific moment in the past.",
            "Background activities interrupted by another event.",
            "Two ongoing actions happening at the same time in the past.",
            "Setting a scene or giving context in a narrative."
        ],
        "usage_cases": [
            {"title": "Action in progress at a specific time",
             "question": "What were you doing at 8 PM yesterday?"},
            {"title": "Interrupted actions",
             "question": "What were you doing when the phone rang?"},
            {"title": "Background actions",
             "question": "Were you reading a book while it started to rain?"},
            {"title": "Parallel actions",
             "question": "Were they watching TV while you were cooking dinner?"},
            {"title": "Setting a scene",
             "question": "Were people talking loudly during the presentation?"},
            {"title": "Ongoing past habit",
             "question": "Were you always coming late to class last year?"},
            {"title": "Emphasis on duration",
             "question": "Were you studying for hours before the exam?"},
            {"title": "Temporary past states",
             "question": "Were you living with your grandparents last summer?"},
            {"title": "Action before a specific event",
             "question": "Were you already waiting for the bus when it arrived?"},
            {"title": "Ongoing background detail",
             "question": "Were you listening to music while you worked on the report?"}
        ],
        "extra_examples": [
            "I was reading a book when you knocked on the door.",
            "She was sleeping at noon yesterday.",
            "They were discussing the plan while I listened.",
            "We were watching a movie when the power went out.",
            "He was working late all last week."
        ]
    },
    "5": {
        "name": "Present Perfect",
        "formation": {
            "Positive": "Subject + have/has + past participle (e.g., 'I have eaten')",
            "Negative": "Subject + have/has + not + past participle (e.g., 'I have not eaten')",
            "Question": "Have/Has + subject + past participle? (e.g., 'Have you eaten?')",
            "Short answer": "'Yes, I have.' / 'No, I haven't.'"
        },
        "usage_explanation": [
            "Actions that happened at an unspecified time or continue until now.",
            "Life experiences without mentioning a specific time.",
            "Actions that started in the past and continue in the present.",
            "Recent events with words like 'just' or 'already'.",
            "Repeated actions up to now."
        ],
        "usage_cases": [
            {"title": "Life experiences",
             "question": "Have you ever traveled to an exotic country?"},
            {"title": "Actions with an unspecified time",
             "question": "Have you finished reading that novel yet?"},
            {"title": "Recent events",
             "question": "Have you already eaten breakfast today?"},
            {"title": "Repeated actions up to now",
             "question": "How many times have you seen that movie?"},
            {"title": "Actions continuing until now",
             "question": "How long have you lived in this city?"},
            {"title": "Past events with present relevance",
             "question": "Have you heard the latest news about the new policy?"},
            {"title": "Using 'just'",
             "question": "Have you just arrived at the station?"},
            {"title": "Using 'yet'",
             "question": "Have you submitted your assignment yet?"},
            {"title": "Using 'already'",
             "question": "Have you already called your parents today?"},
            {"title": "Achievements in your life",
             "question": "Have you won any competitions recently?"}
        ],
        "extra_examples": [
            "I have visited London three times.",
            "She has lost her keys again!",
            "They have never tried sushi before.",
            "We have already watched that film.",
            "He has just finished his homework."
        ]
    },
    "6": {
        "name": "Future Simple",
        "formation": {
            "Positive": "Subject + will + base form (e.g., 'I will eat')",
            "Negative": "Subject + will + not + base form (e.g., 'I will not eat')",
            "Question": "Will + subject + base form? (e.g., 'Will you eat?')",
            "Short answer": "'Yes, I will.' / 'No, I won't.'"
        },
        "usage_explanation": [
            "Decisions made at the moment of speaking.",
            "Predictions about the future.",
            "Promises or offers.",
            "Future facts or certainties."
        ],
        "usage_cases": [
            {"title": "Spontaneous decisions",
             "question": "What will you do if it starts raining now?"},
            {"title": "Predictions",
             "question": "Will computers eventually replace teachers?"},
            {"title": "Promises",
             "question": "Will you help me move these boxes?"},
            {"title": "Offers",
             "question": "Will you have some tea?"},
            {"title": "Future facts",
             "question": "Will the sun rise at 6 AM tomorrow?"},
            {"title": "Immediate plans",
             "question": "Will you go shopping after work?"},
            {"title": "Looking ahead",
             "question": "Will you travel abroad next year?"},
            {"title": "Future routines",
             "question": "Will we see each other every weekend?"},
            {"title": "Predicted success",
             "question": "Will you achieve your language goals soon?"},
            {"title": "Change of mind",
             "question": "Will you still want that gift tomorrow?"}
        ],
        "extra_examples": [
            "I will talk to you later.",
            "They will be here soon.",
            "She will probably come to the party.",
            "We will see what happens next.",
            "He will finish the project on time."
        ]
    },
    "7": {
        "name": "Future Continuous",
        "formation": {
            "Positive": "Subject + will be + verb-ing (e.g., 'I will be eating')",
            "Negative": "Subject + will + not + be + verb-ing (e.g., 'I will not be eating')",
            "Question": "Will + subject + be + verb-ing? (e.g., 'Will you be eating?')",
            "Short answer": "'Yes, I will.' / 'No, I won't.'"
        },
        "usage_explanation": [
            "Actions that will be in progress at a specific time in the future.",
            "Polite inquiries about someone's plans.",
            "Future events that are expected to be continuing.",
            "Overlapping actions or background activities in the future."
        ],
        "usage_cases": [
            {"title": "Action in progress at a future time",
             "question": "What will you be doing at 8 PM tomorrow?"},
            {"title": "Polite inquiries",
             "question": "Will you be joining us for dinner later?"},
            {"title": "Expected future events",
             "question": "Will they be traveling throughout Europe next month?"},
            {"title": "Overlapping future actions",
             "question": "Will you be working while they visit your house?"},
            {"title": "Scene setting in the future",
             "question": "Will the team be practicing on the field at that time?"},
            {"title": "Future background action",
             "question": "Will the dog be sleeping when we get home?"},
            {"title": "Predicting a continuing state",
             "question": "Will you be living in the city or the countryside next year?"},
            {"title": "Alternative future plans",
             "question": "Will we be taking the train or driving ourselves to the conference?"},
            {"title": "Scheduled but extended actions",
             "question": "Will you be studying at the library all evening?"},
            {"title": "Establishing a future timeline",
             "question": "Will you be waiting for us at the airport when we arrive?"}
        ],
        "extra_examples": [
            "I will be working at 8 PM tomorrow.",
            "She will be studying abroad next semester.",
            "They will be driving through the mountains this weekend.",
            "We will be waiting for your call.",
            "He will be sleeping by the time you get home."
        ]
    }
}

# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------
def reset_questions():
    """Reset answers, submitted questions, and review mode. Also reshuffle motivational messages."""
    st.session_state.answers = []
    st.session_state.submitted_questions = set()
    st.session_state.review_mode = False
    random.shuffle(st.session_state.randomized_messages)

def personalized_name():
    """Return the user's name if provided, or 'You' otherwise."""
    name = st.session_state.user_name.strip()
    return name if name else "You"

# ---------------------------------------------------------
# Layout: Sidebar Tense Selection
# ---------------------------------------------------------
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
    # No tense selected from the dropdown
    st.session_state.selected_tense_key = None
    reset_questions()

# ---------------------------------------------------------
# Main Screens
# ---------------------------------------------------------
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

    # Fireworks + Cat GIF
    st.markdown('<img src="https://media.giphy.com/media/l0Exk8EUzSLsrErEQ/giphy.gif" width="300">', unsafe_allow_html=True)
    st.markdown('<div id="catgif"><img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" width="200"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="custom-welcome-title">Welcome to the Grammar Genius Game! 🎉✨🎮</div>
    """, unsafe_allow_html=True)

    st.write("""
    Get ready to boost your English grammar skills in a fun and interactive way!
    
    1. (Optional) Enter your name to personalize your experience.
    2. Use the sidebar to pick a tense (Present Simple, Past Simple, Present Continuous, etc.).
    3. Read how it's formed, when to use it, and see extra examples.
    4. Answer the 10 questions. Receive motivational feedback after each one!
    5. Once you finish all questions, enjoy a celebratory screen with a dancing cat.

    Let's begin!
    """)
    st.text_input("Your name:", key="user_name")
    st.balloons()

def show_review(tense_info):
    """Display all answered questions and the user’s responses."""
    st.header("Review Your Answers")
    for i, case in enumerate(tense_info["usage_cases"]):
        answer_key = f"answer_{st.session_state.selected_tense_key}_{i}"
        st.write(f"**{case['title']}**")
        st.write(f"Question: {case['question']}")
        user_answer = st.session_state.get(answer_key, "")
        st.write(f"Your answer: {user_answer}")
    st.write("Great job! Feel free to choose another tense from the sidebar if you like.")

def show_explanation_and_questions():
    key = st.session_state.selected_tense_key
    if key is None:
        return

    tense_info = tenses_data[key]

    # Fade-out cat gif at top
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

    # Additional Examples
    with st.expander("More Examples"):
        if "extra_examples" in tense_info:
            for ex in tense_info["extra_examples"]:
                st.write("- " + ex)

    st.subheader("Practice Questions")

    total_questions = len(tense_info["usage_cases"])
    answered_count = len(st.session_state.answers)

    if st.session_state.review_mode:
        show_review(tense_info)
        return

    st.write(f"Questions answered: {answered_count}/{total_questions}")
    st.write("Below are several usage cases of this tense. Please answer each question accordingly.")

    # If all questions answered, show celebration
    if answered_count == total_questions:
        st.success(f"Congratulations, {personalized_name()}! You've answered all the questions!")
        st.markdown('<img src="https://media.giphy.com/media/5Zesu5VPNGJlm/giphy.gif" width="300">', unsafe_allow_html=True)
        st.balloons()
        if st.button("Review Your Answers"):
            st.session_state.review_mode = True
        return

    # Display unanswered questions
    for i, case in enumerate(tense_info["usage_cases"]):
        answer_key = f"answer_{key}_{i}"
        submit_key = f"submit_{key}_{i}"

        # Already answered?
        if submit_key in st.session_state.submitted_questions:
            # Show question + user's final answer
            st.write(f"**{case['title']}**")
            st.write(case["question"])
            user_answer = st.session_state.get(answer_key, "")
            st.write(f"Your answer: {user_answer}")
            continue

        # Not answered yet
        st.write(f"**{case['title']}**")
        st.write(case["question"])
        st.text_input("Your answer:", key=answer_key)

        if st.button("Submit", key=submit_key):
            user_answer = st.session_state.get(answer_key, "")
            st.session_state.answers.append(user_answer)
            st.session_state.submitted_questions.add(submit_key)
            msg_index = len(st.session_state.answers) - 1

            # Display motivational message
            if msg_index < len(st.session_state.randomized_messages):
                msg = st.session_state.randomized_messages[msg_index]
            else:
                msg = st.session_state.randomized_messages[-1]
            # Personalize it
            if msg and msg[0].isupper():
                personalized_msg = f"{personalized_name()}, {msg[0].lower() + msg[1:]}"
            else:
                personalized_msg = f"{personalized_name()}, {msg}"

            st.success(personalized_msg)
            # Show the user's answer immediately
            st.write(f"Your answer: {user_answer}")

# ---------------------------------------------------------
# Main Execution
# ---------------------------------------------------------
def main():
    """Decide whether to show the welcome screen or the tense practice screen."""
    if st.session_state.selected_tense_key is None:
        show_welcome()
    else:
        show_explanation_and_questions()

if __name__ == "__main__":
    main()
