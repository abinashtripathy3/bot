import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams


def ask_question(prompt, options):
    """
    Display the question prompt and options, then get a valid response.
    """
    print(f"Bot: {prompt}")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    while True:
        try:
            choice = int(input("Your choice (enter the number): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Please enter a valid option number.")
        except ValueError:
            print("Invalid input. Please enter the number of your choice.")

def symptom_pathway():
    # Step 1: Initial Symptom Identification
    response = ask_question("Are you experiencing a headache right now or recently?", ["Yes", "No"])
    if response == "No":
        print("Bot: No further symptom pathway needed.")
        return

    # Step 2: Headache Duration and Onset
    duration = ask_question("How long has your headache lasted?", [
        "Less than 30 minutes",
        "30 minutes to 4 hours",
        "4 hours to 72 hours",
        "More than 72 hours"
    ])
    onset = ask_question("When did your headache start?", ["Gradual onset", "Sudden onset"])

    if onset == "Sudden onset":
        print("Bot: This may be a medical emergency. Seek urgent care as it could be indicative of a serious condition (e.g., subarachnoid hemorrhage or stroke).")
        return
    else:
        print("Bot: Let's proceed to further questions.")

    # Step 3: Headache Location
    location = ask_question("Where is the pain located?", [
        "One side of the head (unilateral)",
        "Both sides of the head (bilateral)",
        "Back of the head and neck",
        "Forehead and behind the eyes",
        "All over the head"
    ])

    if location == "One side of the head (unilateral)":
        print("Bot: Unilateral pain often suggests a migraine or cluster headache.")
    elif location == "Both sides of the head (bilateral)":
        print("Bot: Bilateral pain may suggest a tension headache or systemic causes, like high blood pressure.")
    elif location == "Back of the head and neck":
        print("Bot: This could suggest a tension-type headache or a cervical origin.")
    elif location == "Forehead and behind the eyes":
        print("Bot: This could indicate sinusitis or eye strain.")
    else:
        print("Bot: Diffuse pain could have various causes, and further details are needed.")

    # Step 4: Nature and Type of Pain
    nature = ask_question("What does your headache feel like?", [
        "Throbbing or pulsing",
        "Dull, aching pain",
        "Sharp or stabbing pain",
        "Pressure-like or tightening"
    ])

    if nature == "Throbbing or pulsing":
        print("Bot: This type of pain is often associated with migraines or vascular causes.")
    elif nature == "Dull, aching pain":
        print("Bot: This is common in tension-type headaches or chronic headaches.")
    elif nature == "Sharp or stabbing pain":
        print("Bot: Sharp, stabbing pain could indicate a cluster headache or neuralgia.")
    elif nature == "Pressure-like or tightening":
        print("Bot: Pressure-like pain is often seen in tension headaches.")

    # Step 5: Associated Symptoms
    associated_symptoms = ask_question("Do you have any of these symptoms with your headache?", [
        "Nausea or vomiting",
        "Sensitivity to light (photophobia)",
        "Sensitivity to sound (phonophobia)",
        "Aura or visual disturbances",
        "Neck stiffness",
        "Fever",
        "Runny or blocked nose",
        "Eye redness or tearing",
        "Weakness, slurred speech, or confusion"
    ])

    if associated_symptoms == "Nausea or vomiting" or associated_symptoms == "Sensitivity to light (photophobia)" or associated_symptoms == "Sensitivity to sound (phonophobia)" or associated_symptoms == "Aura or visual disturbances":
        print("Bot: This could suggest a migraine.")
    elif associated_symptoms == "Neck stiffness" and "Fever":
        print("Bot: This could indicate meningitis. Seek urgent care.")
    elif associated_symptoms == "Runny or blocked nose":
        print("Bot: This could indicate sinusitis.")
    elif associated_symptoms == "Eye redness or tearing":
        print("Bot: This could indicate a cluster headache.")
    elif associated_symptoms == "Weakness, slurred speech, or confusion":
        print("Bot: This could indicate a neurological emergency. Seek immediate care.")

    # Step 6: Trigger Assessment
    trigger = ask_question("Do any of the following trigger or worsen your headache?", [
        "Physical activity or exertion",
        "Stress or emotional strain",
        "Changes in weather",
        "Sleep disturbances",
        "Skipping meals or hunger",
        "Alcohol or certain foods (e.g., chocolate, cheese)",
        "Strong smells, bright lights, loud noises"
    ])

    if trigger == "Physical activity or exertion":
        print("Bot: This may suggest a migraine or exertional headache.")
    elif trigger == "Stress or emotional strain" or trigger == "Sleep disturbances":
        print("Bot: This could suggest a tension headache.")
    elif trigger == "Changes in weather" or trigger == "Alcohol or certain foods (e.g., chocolate, cheese)":
        print("Bot: These are common triggers for migraines.")

    # Step 7: Medical History and Red Flags
    medical_history = ask_question("Do you have any of these conditions or recent events?", [
        "Recent head injury or trauma",
        "Hypertension (high blood pressure)",
        "Pregnancy or recent childbirth",
        "Cancer or immune suppression",
        "History of stroke or brain aneurysm",
        "Family history of migraines or neurological disorders"
    ])

    if medical_history == "Recent head injury or trauma":
        print("Bot: This could indicate a concussion or subdural hematoma. Seek urgent evaluation.")
    elif medical_history == "Hypertension (high blood pressure)":
        print("Bot: Check for signs of hypertensive crisis—refer for urgent care if necessary.")
    elif medical_history == "Pregnancy or recent childbirth":
        print("Bot: This could suggest preeclampsia—refer for immediate care.")
    elif medical_history == "Cancer or immune suppression":
        print("Bot: This may indicate brain metastasis or infection—refer for further evaluation.")

    # Step 8: Physical Examination or Self-Assessment Suggestions
    self_assessment = ask_question("Are you able to check your temperature and blood pressure?", ["Yes", "No"])
    if self_assessment == "Yes":
        print("Bot: Fever with headache could suggest an infection (like meningitis or sinusitis). Elevated blood pressure with headache may indicate a hypertensive crisis.")

    # Step 9: Headache Frequency and Chronicity
    frequency = ask_question("How often do you experience headaches?", [
        "Rarely (less than once a month)",
        "Occasionally (1-4 times a month)",
        "Frequently (more than 4 times a month)",
        "Daily or nearly daily"
    ])

    if frequency == "Frequently (more than 4 times a month)" or frequency == "Daily or nearly daily":
        print("Bot: This may suggest chronic migraine or medication overuse headache. Follow up with a specialist for preventive treatment.")
    else:
        print("Bot: This frequency may suggest episodic tension or migraine headache.")

    # Step 10: Final Diagnosis Suggestions
    print("Bot: Based on your responses, here are some possible diagnoses:")
    print("  - Migraine: Throbbing pain, unilateral, nausea, sensitivity to light/sound, possible aura.")
    print("  - Tension-Type Headache: Dull, bilateral, stress-related, no nausea or vomiting.")
    print("  - Cluster Headache: Sharp, unilateral, eye pain, tearing, nasal congestion.")
    print("  - Sinus Headache: Pressure-like pain in the forehead, nasal congestion, worse with leaning forward.")
    print("  - Hypertension-Related Headache: Bilateral, associated with elevated blood pressure.")
    print("  - Thunderclap Headache/Neurological Emergency: Sudden severe headache, refer for emergency care.")
    print("  - Meningitis: Headache with fever, neck stiffness, urgent referral needed.")

    # Step 11: Treatment Suggestions and Referral
    print("Bot: Based on the likely diagnosis, here are some suggested next steps:")
    print("  - For migraine or tension headache: Over-the-counter pain relief (e.g., ibuprofen, acetaminophen), rest, hydration, and avoid known triggers.")
    print("  - For cluster headache: Consult a healthcare provider for specialized treatment.")
    print("  - For secondary headaches (e.g., fever, neck stiffness, trauma, high blood pressure): Seek immediate care at a healthcare facility.")

    # Step 12: Follow-Up and Monitoring
    follow_up = ask_question("Have your symptoms improved with the recommended treatment?", ["Yes", "No"])
    if follow_up == "Yes":
        print("Bot: Glad to hear that! Follow up with a healthcare provider if needed.")
    else:
        print("Bot: If symptoms persist, please consult a healthcare provider or a neurologist for further evaluation.")

# Start the bot

symptom_pathway()
