import streamlit as st

def ask_question(prompt, options, step):
    """
    Display the question prompt and options, then get a valid response.
    """
    st.write(f"**{prompt}**")
    # Display radio button without any pre-selected option
    choice = st.radio("Your choice:", options, key=f"question_{step}_{prompt}", index=None)
    
    # Ensuring the user selects an option before moving forward
    if choice is None:
        st.warning("Please select an option to proceed.")
    
    return choice

def symptom_pathway():
    # Initialize session state for tracking question progress
    if "step" not in st.session_state:
        st.session_state.step = 0  # Start from the first step
    
    st.title("Headache Diagnosis Bot")

    # Step 1: Initial Symptom Identification
    if st.session_state.step == 0:
        response = ask_question("Are you experiencing a headache right now or recently?", ["Yes", "No"], st.session_state.step)
        if response == "No":
            st.write("Bot: No further symptom pathway needed.")
            return
        else:
            if st.button('Next', key=f"next_{st.session_state.step}"):  # Unique key added
                st.session_state.step = 1  # Proceed to next step

    # Step 2: Headache Duration and Onset
    if st.session_state.step == 1:
        duration = ask_question("How long has your headache lasted?", [
            "Less than 30 minutes",
            "30 minutes to 4 hours",
            "4 hours to 72 hours",
            "More than 72 hours"
        ], st.session_state.step)
        onset = ask_question("When did your headache start?", ["Gradual onset", "Sudden onset"], st.session_state.step)

        if onset == "Sudden onset":
            st.warning("This may be a medical emergency. Seek urgent care as it could indicate a serious condition (e.g., subarachnoid hemorrhage or stroke).")
            return
        else:
            if st.button('Next', key=f"next_{st.session_state.step}"):  # Unique key added
                st.session_state.step = 2  # Proceed to next step

    # Step 3: Headache Location
    if st.session_state.step == 2:
        location = ask_question("Where is the pain located?", [
            "One side of the head (unilateral)",
            "Both sides of the head (bilateral)",
            "Back of the head and neck",
            "Forehead and behind the eyes",
            "All over the head"
        ], st.session_state.step)

        if location == "One side of the head (unilateral)":
            st.write("Bot: Unilateral pain often suggests a migraine or cluster headache.")
        elif location == "Both sides of the head (bilateral)":
            st.write("Bot: Bilateral pain may suggest a tension headache or systemic causes, like high blood pressure.")
        elif location == "Back of the head and neck":
            st.write("Bot: This could suggest a tension-type headache or a cervical origin.")
        elif location == "Forehead and behind the eyes":
            st.write("Bot: This could indicate sinusitis or eye strain.")
        else:
            st.write("Bot: Diffuse pain could have various causes, and further details are needed.")
        
        if st.button('Next', key=f"next_{st.session_state.step}"):  # Unique key added
            st.session_state.step = 3  # Proceed to next step

    # Step 4: Nature and Type of Pain
    if st.session_state.step == 3:
        nature = ask_question("What does your headache feel like?", [
            "Throbbing or pulsing",
            "Dull, aching pain",
            "Sharp or stabbing pain",
            "Pressure-like or tightening"
        ], st.session_state.step)

        if nature == "Throbbing or pulsing":
            st.write("Bot: This type of pain is often associated with migraines or vascular causes.")
        elif nature == "Dull, aching pain":
            st.write("Bot: This is common in tension-type headaches or chronic headaches.")
        elif nature == "Sharp or stabbing pain":
            st.write("Bot: Sharp, stabbing pain could indicate a cluster headache or neuralgia.")
        elif nature == "Pressure-like or tightening":
            st.write("Bot: Pressure-like pain is often seen in tension headaches.")
        
        if st.button('Next', key=f"next_{st.session_state.step}"):  # Unique key added
            st.session_state.step = 4  # Proceed to next step

    # Step 5: Associated Symptoms
    if st.session_state.step == 4:
        associated_symptoms = st.multiselect(
            "Do you have any of these symptoms with your headache?",
            [
                "Nausea or vomiting",
                "Sensitivity to light (photophobia)",
                "Sensitivity to sound (phonophobia)",
                "Aura or visual disturbances",
                "Neck stiffness",
                "Fever",
                "Runny or blocked nose",
                "Eye redness or tearing",
                "Weakness, slurred speech, or confusion"
            ],
            key=f"step5_symptoms_{st.session_state.step}"
        )

        if any(symptom in associated_symptoms for symptom in ["Nausea or vomiting", "Sensitivity to light (photophobia)", "Sensitivity to sound (phonophobia)", "Aura or visual disturbances"]):
            st.write("Bot: This could suggest a migraine.")
        if "Neck stiffness" in associated_symptoms and "Fever" in associated_symptoms:
            st.warning("This could indicate meningitis. Seek urgent care.")
        if "Runny or blocked nose" in associated_symptoms:
            st.write("Bot: This could indicate sinusitis.")
        if "Eye redness or tearing" in associated_symptoms:
            st.write("Bot: This could indicate a cluster headache.")
        if "Weakness, slurred speech, or confusion" in associated_symptoms:
            st.warning("This could indicate a neurological emergency. Seek immediate care.")
        
        if st.button('Next', key=f"next_{st.session_state.step}"):  # Unique key added
            st.session_state.step = 5  # Proceed to next step

    # Step 6: Trigger Assessment
    if st.session_state.step == 5:
        trigger = ask_question("Do any of the following trigger or worsen your headache?", [
            "Physical activity or exertion",
            "Stress or emotional strain",
            "Changes in weather",
            "Sleep disturbances",
            "Skipping meals or hunger",
            "Alcohol or certain foods (e.g., chocolate, cheese)",
            "Strong smells, bright lights, loud noises"
        ], st.session_state.step)

        if trigger == "Physical activity or exertion":
            st.write("Bot: This may suggest a migraine or exertional headache.")
        elif trigger == "Stress or emotional strain" or trigger == "Sleep disturbances":
            st.write("Bot: This could suggest a tension headache.")
        elif trigger == "Changes in weather" or trigger == "Alcohol or certain foods (e.g., chocolate, cheese)":
            st.write("Bot: These are common triggers for migraines.")

        if st.button('Next', key=f"next_{st.session_state.step}"):  # Unique key added
            st.session_state.step = 6  # Proceed to next step

    # Step 7: Medical History and Red Flags
    if st.session_state.step == 6:
        medical_history = ask_question("Do you have any of these conditions or recent events?", [
            "Recent head injury or trauma",
            "Hypertension (high blood pressure)",
            "Pregnancy or recent childbirth",
            "Cancer or immune suppression",
            "History of stroke or brain aneurysm",
            "Family history of migraines or neurological disorders"
        ], st.session_state.step)

        if medical_history == "Recent head injury or trauma":
            st.write("Bot: This could indicate a concussion or subdural hematoma. Seek urgent evaluation.")
        elif medical_history == "Hypertension (high blood pressure)":
            st.write("Bot: Check for signs of hypertensive crisis—refer for urgent care if necessary.")
        elif medical_history == "Pregnancy or recent childbirth":
            st.write("Bot: This could suggest preeclampsia—refer for immediate care.")
        elif medical_history == "Cancer or immune suppression":
            st.write("Bot: This may indicate brain metastasis or infection—refer for further evaluation.")

        if st.button('Next', key=f"next_{st.session_state.step}"):  # Unique key added
            st.session_state.step = 7  # Proceed to next step

    # Step 8: Physical Examination or Self-Assessment Suggestions
    if st.session_state.step == 7:
        self_assessment = ask_question("Are you able to check your temperature and blood pressure?", ["Yes", "No"], st.session_state.step)
        if self_assessment == "Yes":
            st.write("Bot: Fever with headache could suggest an infection (like meningitis or sinusitis). Elevated blood pressure with headache may indicate a hypertensive crisis.")

        if st.button('Next', key=f"next_{st.session_state.step}"):  # Unique key added
            st.session_state.step = 8  # Proceed to next step

    # Step 9: Final Diagnosis and Treatment Suggestions
    if st.session_state.step == 8:
        st.write("Bot: Based on your responses, here are some possible diagnoses:")
        st.write("  - Migraine, Tension-Type Headache, Cluster Headache, Sinus Headache, Hypertension-Related Headache, Thunderclap Headache/Neurological Emergency, Meningitis.")
        st.write("Bot: Suggested next steps: Over-the-counter pain relief, consult healthcare providers as needed.")
        
        if st.button('Restart', key=f"restart_{st.session_state.step}"):  # Unique key added
            st.session_state.step = 0  # Restart the process

if __name__ == "__main__":
    symptom_pathway()
