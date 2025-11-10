from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)
db: Session = SessionLocal()

zora_questions = [
    {
        "text": "What is the primary purpose of Zora AI™ at Deloitte?",
        "option_a": "Financial forecasting",
        "option_b": "Building digital workforces using AI agents",
        "option_c": "Manual reporting automation",
        "option_d": "HR recruitment",
        "correct_option": "b"
    },
    {
        "text": "Which technology forms the backbone of Zora’s AI capabilities?",
        "option_a": "Blockchain",
        "option_b": "NVIDIA AI",
        "option_c": "Quantum computing",
        "option_d": "Legacy servers",
        "correct_option": "b"
    },
    {
        "text": "How does Zora AI™ interact with enterprise systems?",
        "option_a": "Replaces human processes entirely",
        "option_b": "Interacts like a digital worker alongside humans",
        "option_c": "Only automates emails",
        "option_d": "Focuses on data entry",
        "correct_option": "b"
    },
    {
        "text": "What is a unique advantage of the Zora AI agent platform?",
        "option_a": "Limited to finance use cases",
        "option_b": "Emulates human reasoning for advanced workflows",
        "option_c": "Only works on on-prem infrastructure",
        "option_d": "No transparency in operations",
        "correct_option": "b"
    },
    {
        "text": "Zora AI is designed to operate with:",
        "option_a": "Only Deloitte-built agents",
        "option_b": "Only public cloud platforms",
        "option_c": "Both Deloitte and third-party AI agents",
        "option_d": "Only on legacy systems",
        "correct_option": "c"
    },
    {
        "text": "Which Deloitte framework ensures Zora meets data safety and transparency standards?",
        "option_a": "Green Operations",
        "option_b": "Trustworthy AI™",
        "option_c": "Agile Delivery",
        "option_d": "FastTrack",
        "correct_option": "b"
    },
    {
        "text": "The main benefit of integrating Zora in an organization is:",
        "option_a": "Removing all human jobs",
        "option_b": "Augmenting human workforce with AI agents",
        "option_c": "Replacing all IT systems",
        "option_d": "Solely increasing server usage",
        "correct_option": "b"
    },
    {
        "text": "Zora AI can be used in which industries?",
        "option_a": "Banking only",
        "option_b": "All industries with a focus on horizontal processes",
        "option_c": "Retail only",
        "option_d": "Manufacturing only",
        "correct_option": "b"
    },
    {
        "text": "Which company partners with Deloitte for Zora AI’s acceleration and hardware?",
        "option_a": "Microsoft",
        "option_b": "NVIDIA",
        "option_c": "Intel",
        "option_d": "SAP",
        "correct_option": "b"
    },
    {
        "text": "In what timeframe is Zora typically implemented for clients?",
        "option_a": "Years",
        "option_b": "Weeks or months",
        "option_c": "Days only",
        "option_d": "Decades",
        "correct_option": "b"
    },
    {
        "text": "What infrastructure models can host Zora AI?",
        "option_a": "On-prem, cloud, and hybrid infrastructures",
        "option_b": "On-prem only",
        "option_c": "Cloud only",
        "option_d": "Edge only",
        "correct_option": "a"
    },
    {
        "text": "What is the approach Zora follows regarding client data?",
        "option_a": "Data leaves client environment for decision-making",
        "option_b": "Data remains within the client’s infrastructure",
        "option_c": "Only stored on Deloitte servers",
        "option_d": "Shared with third parties",
        "correct_option": "b"
    },
    {
        "text": "Which of the following is NOT a capability of Zora AI agents?",
        "option_a": "Scenario analysis and recommendations",
        "option_b": "Manual data correction",
        "option_c": "Transaction processing and anomaly detection",
        "option_d": "Self-healing workflows",
        "correct_option": "b"
    },
    {
        "text": "What is 'agentic transformation' in the context of Zora?",
        "option_a": "Manual risk assessment",
        "option_b": "Automation driven by scalable AI agents across domains",
        "option_c": "Legacy software updates",
        "option_d": "Automated hardware installation",
        "correct_option": "b"
    },
    {
        "text": "Who can best benefit from deploying Zora AI?",
        "option_a": "Only IT departments",
        "option_b": "Enterprises aiming for automation and efficiency",
        "option_c": "Small startups only",
        "option_d": "Individuals for personal use",
        "correct_option": "b"
    },
    {
        "text": "Which of the following is true about Zora’s deployment?",
        "option_a": "All clients must rebuild their systems",
        "option_b": "Zora augments existing investments and processes",
        "option_c": "Zora works independently without client input",
        "option_d": "Dedicated to a single business function",
        "correct_option": "b"
    },
    {
        "text": "What aspect of decision-making is enhanced by Zora?",
        "option_a": "Guesswork and assumptions",
        "option_b": "Data-driven, transparent, and predictable results",
        "option_c": "Randomized results",
        "option_d": "Obscured analytics",
        "correct_option": "b"
    },
    {
        "text": "How extensible is Zora in terms of new agent integration?",
        "option_a": "Fixed feature set only",
        "option_b": "Allows integration of new industry-specific capabilities",
        "option_c": "Only for Deloitte internal use",
        "option_d": "Locked after deployment",
        "correct_option": "b"
    },
    {
        "text": "What operational domains does Zora target for digital workforce integration?",
        "option_a": "Finance & procurement only",
        "option_b": "All major enterprise functions (finance, HR, supply chain, etc.)",
        "option_c": "Sales only",
        "option_d": "Marketing only",
        "correct_option": "b"
    },
    {
        "text": "Which statement summarizes Zora’s vision?",
        "option_a": "Automate a single process well",
        "option_b": "Enable actionable, scalable, and ubiquitous intelligence across organizations",
        "option_c": "Focus on legacy process maintenance",
        "option_d": "Outsource all business operations",
        "correct_option": "b"
    }
]

for q in zora_questions:
    db_q = models.Question(**q)
    db.add(db_q)

db.commit()
print("Seeded Zora questions!")