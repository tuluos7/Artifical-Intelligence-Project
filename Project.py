import re
from datetime import datetime


class LegalAdvisor:
    def __init__(self):
        self.firm_name = "SSA Legal Advisory Services"
        self.user_info = {}  # To store user information
        self.session_info = {}  # To store session information
        self.categories = {
            "Criminal": {
                "description": "Deals with offenses against the state or public",
                "lawyers": ["John Doe (Criminal Defense Specialist)", "Jane Smith (Prosecution Expert)"],
                "questions": {
                    "What should I do if I'm falsely accused of a crime?":
                        "Document all evidence, don't speak to police without a lawyer, and contact a criminal defense attorney immediately.",
                    "What's the difference between misdemeanor and felony?":
                        "Misdemeanors are less serious crimes with shorter jail sentences (typically <1 year), while felonies are more serious with longer potential sentences.",
                    "Can I get bail for a serious offense?":
                        "Bail depends on factors like flight risk, danger to community, and offense severity. A bail hearing will determine eligibility.",
                    "What are my rights if arrested?":
                        "You have the right to remain silent, to an attorney, and to be informed of charges. Never resist arrest.",
                    "How can I expunge my criminal record?":
                        "Expungement rules vary by jurisdiction and offense type. Consult an attorney about eligibility and process."
                }
            },
            "Civil": {
                "description": "Deals with disputes between individuals/organizations",
                "lawyers": ["Robert Johnson (Civil Litigation Expert)", "Emily Chen (Mediation Specialist)"],
                "questions": {
                    "How do I file a lawsuit against someone?":
                        "First consult an attorney to assess merits, then file a complaint in the appropriate court with proper jurisdiction.",
                    "What's the statute of limitations for civil cases?":
                        "Varies by case type and jurisdiction - typically 1-6 years. Consult an attorney for specific cases.",
                    "Can I represent myself in civil court?":
                        "Yes (pro se), but not recommended for complex cases. Court procedures can be challenging without legal training.",
                    "What is small claims court?":
                        "A simplified court for smaller disputes (usually under $10,000) with less formal procedures and no lawyers required.",
                    "How does alternative dispute resolution work?":
                        "ADR (mediation/arbitration) offers faster, cheaper resolution outside court with a neutral third party facilitating."
                }
            },
            "Service": {
                "description": "Deals with government and administrative matters",
                "lawyers": ["Michael Brown (Government Affairs Specialist)",
                            "Sarah Wilson (Administrative Law Expert)"],
                "questions": {
                    "How do I appeal a government decision?":
                        "File an appeal with the appropriate administrative body within their deadline, often requiring specific forms and procedures.",
                    "What are my rights when dealing with government agencies?":
                        "You have rights to due process, equal treatment, and to request records (FOIA). Procedures vary by agency.",
                    "How can I challenge a denied benefits claim?":
                        "File an appeal following the agency's process, gather supporting evidence, and consider legal representation.",
                    "What is administrative law?":
                        "The body of law governing government agencies and their interactions with the public, including rulemaking and adjudication.",
                    "How do I file a complaint against a government employee?":
                        "Follow the agency's complaint procedure, document incidents thoroughly, and consider consulting an attorney for serious matters."
                }
            }
        }

    def get_user_info(self):
        print("\n" + "=" * 60)
        print("PLEASE PROVIDE YOUR DETAILS".center(60))
        print("=" * 60)

        while True:
            name = input("Enter your full name: ").strip()
            if name:
                self.user_info['name'] = name
                break
            print("Name cannot be empty. Please try again.")

        while True:
            phone = input("Enter your phone number: ").strip()
            if phone and phone.isdigit() and len(phone) >= 10:
                self.user_info['phone'] = phone
                break
            print("Please enter a valid phone number (at least 10 digits).")

        # Record session start time
        now = datetime.now()
        self.session_info['start_time'] = now.strftime("%H:%M:%S")
        self.session_info['start_date'] = now.strftime("%Y-%m-%d")
        self.session_info['start_day'] = now.strftime("%A")

    def display_welcome(self):
        print("\n" + "=" * 60)
        print(f"WELCOME TO {self.firm_name}".center(60))
        print("Smart Legal Advisor System".center(60))
        print("=" * 60)
        print(f"\nWelcome, {self.user_info['name']}!")
        print(
            f"Session started on: {self.session_info['start_day']}, {self.session_info['start_date']} at {self.session_info['start_time']}")
        print("\nThis system provides preliminary legal guidance in three categories:")
        for i, category in enumerate(self.categories.keys(), 1):
            print(f"{i}. {category}: {self.categories[category]['description']}")
        print("\nNOTE: This is not a substitute for professional legal advice.")
        print(f"We may contact you at {self.user_info['phone']} if follow-up is needed.")

    def select_category(self):
        print("\n" + "=" * 60)
        print("SELECT A LEGAL CATEGORY".center(60))
        print("=" * 60)
        for i, category in enumerate(self.categories.keys(), 1):
            print(f"{i}. {category}")

        while True:
            try:
                choice = int(input("\nEnter category number (1-3): "))
                if 1 <= choice <= 3:
                    selected = list(self.categories.keys())[choice - 1]
                    return selected
                else:
                    print("Please enter a number between 1 and 3")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def select_lawyer(self, category):
        print("\n" + "=" * 60)
        print(f"SELECT A {category.upper()} LAWYER".center(60))
        print("=" * 60)
        lawyers = self.categories[category]["lawyers"]
        for i, lawyer in enumerate(lawyers, 1):
            print(f"{i}. {lawyer}")

        while True:
            try:
                choice = int(input("\nChoose your lawyer (1-2): "))
                if 1 <= choice <= 2:
                    print(f"\nYou've selected {lawyers[choice - 1]}")
                    return lawyers[choice - 1]
                else:
                    print("Please enter 1 or 2")
            except ValueError:
                print("Invalid input. Please enter 1 or 2.")

    def ask_question(self, category):
        # Record question time
        now = datetime.now()
        question_time = now.strftime("%H:%M:%S")

        questions = self.categories[category]["questions"]
        print("\n" + "=" * 60)
        print(f"{category.upper()} LEGAL QUESTIONS".center(60))
        print("=" * 60)
        print("Common questions in this category:")
        for i, question in enumerate(questions.keys(), 1):
            print(f"{i}. {question}")

        print("\nYou can:")
        print("1. Select a question from above")
        print("2. Ask your own question")

        while True:
            choice = input("\nEnter your choice (1/2): ")
            if choice == "1":
                while True:
                    try:
                        q_num = int(input("Enter question number: "))
                        if 1 <= q_num <= len(questions):
                            selected_q = list(questions.keys())[q_num - 1]
                            print("\n" + "=" * 60)
                            print("LEGAL ADVICE".center(60))
                            print("=" * 60)
                            print(f"Question asked at: {question_time}")
                            print(f"Question: {selected_q}")
                            print(f"\nAdvice: {questions[selected_q]}")
                            return
                        else:
                            print(f"Please enter a number between 1 and {len(questions)}")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            elif choice == "2":
                custom_q = input("\nEnter your legal question: ")
                print("\n" + "=" * 60)
                print("LEGAL ADVICE".center(60))
                print("=" * 60)
                print(f"Question asked at: {question_time}")
                print(f"Question: {custom_q}")

                # Simple NLP - check for keywords in custom question
                found = False
                for q, advice in questions.items():
                    # Check if any keywords from predefined questions match
                    keywords = re.findall(r'\w+', q.lower())
                    if any(keyword in custom_q.lower() for keyword in keywords):
                        print(f"\nAdvice: {advice}")
                        found = True
                        break

                if not found:
                    print("\nAdvice: This appears to be a complex legal matter. Based on our preliminary analysis, ")
                    print("we recommend scheduling a consultation with your selected attorney for detailed advice.")
                    print(f"Your selected attorney may contact you at {self.user_info['phone']} for follow-up.")
                return
            else:
                print("Please enter 1 or 2")

    def run(self):
        self.get_user_info()  # Get user info first
        self.display_welcome()
        while True:
            category = self.select_category()
            lawyer = self.select_lawyer(category)
            self.ask_question(category)

            another = input("\nDo you have another legal question? (yes/no): ").lower()
            if another != 'yes':
                # Record session end time
                now = datetime.now()
                self.session_info['end_time'] = now.strftime("%H:%M:%S")
                duration = now - datetime.strptime(self.session_info['start_time'], "%H:%M:%S")

                print("\n" + "=" * 60)
                print("Thank you for using SSA Legal Advisory Services".center(60))
                print(
                    f"Session started: {self.session_info['start_day']}, {self.session_info['start_date']} at {self.session_info['start_time']}".center(
                        60))
                print(
                    f"Session ended: {now.strftime('%A')}, {now.strftime('%Y-%m-%d')} at {self.session_info['end_time']}".center(
                        60))
                print(f"Duration: {duration.seconds // 60} minutes".center(60))
                print(f"Goodbye, {self.user_info['name']}!".center(60))
                print("=" * 60)
                break


if __name__ == "__main__":
    advisor = LegalAdvisor()
    advisor.run()