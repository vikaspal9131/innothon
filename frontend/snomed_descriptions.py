import numpy as np

snomed_classes = np.array([
    '111975006', '164889003', '164890007', '164909002', '164917005',
    '164934002', '17338001', '251146004', '270492004', '284470004',
    '39732003', '426177001', '426627000', '426783006', '427084000',
    '427393009', '445118002', '47665007', '59118001', '59931005',
    '63593006', '698252002', '713426002', '713427006'
], dtype=object)

snomed_descriptions = {
    "111975006": {
        "Condition Name": "Prolonged QT interval ",
        "Description": "A prolonged QT interval is an ECG abnormality where the heart's recovery time is extended, increasing the risk of dangerous arrhythmias. Causes include genetic factors, medications, or electrolyte imbalances.",
        "Symptoms/Clinical Presentation": [
            "Irregular or rapid heartbeats.",
            "Feeling lightheaded or faint.",
            "Sudden loss of consciousness or fainting.",
            "Rare but possible, particularly if arrhythmias are severe"
        ],
        "Risk Factors": [
            "Electrolyte Imbalances",
            "Heart Disease",
            "Heart Disease",
            "Obesity",
            "Diabetes"
        ],
        "Possible Causes": [
            "Blockage of a coronary artery due to plaque buildup",
            "Blood clot"
        ],
        "Diagnostic Criteria": [
            "Elevated cardiac enzymes",
            "ECG changes (e.g., ST elevation)",
            "Chest pain"
        ],
        "Treatment Options": {
            "Medication": [
                "Immediate use of aspirin",
                "Clot-busting drugs"
            ],
            "Procedures": [
                "Angioplasty"
            ],
            "Lifestyle Changes": [
                "Healthy diet",
                "Regular exercise"
            ]
        },
        "Prognosis": "Depends on the time to treatment; early intervention can significantly improve outcomes.",
        "Prevention": [
            "Regular exercise",
            "Healthy diet",
            "Avoiding smoking",
            "Managing stress"
        ],
        "Additional Resources": [
            {
                "Title": "American Heart Association - Heart Attack Information",
                "Link": "https://www.heart.org/"
            }
        ],
        "SNOMED Code": "111975006",
        "Detailed Description": "A condition resulting from the sudden blockage of a coronary artery, which leads to the death of heart muscle due to the lack of blood flow.",
        "Clinical Findings": [
            "ECG showing ST elevation",
            "Elevated troponin levels"
        ],
        "Associated Conditions": [
            "Atherosclerosis",
            "Coronary artery disease"
        ],
        "Treatment Guidelines": [
            "Follow guidelines for acute coronary syndrome management, including immediate reperfusion therapy if necessary."
        ]
    },
    "164889003": {
        "Condition Name": "Acute Myocarditis",
        "Description": "Inflammation of the heart muscle that can affect the heart's ability to pump and cause rapid or irregular heart rhythms.",
        "Symptoms/Clinical Presentation": [
            "Chest pain",
            "Shortness of breath",
            "Fatigue",
            "Fever"
        ],
        "Risk Factors": [
            "Viral infections",
            "Autoimmune diseases",
            "Recent cardiac surgery"
        ],
        "Possible Causes": [
            "Viral infections",
            "Autoimmune diseases",
            "Drug reactions"
        ],
        "Diagnostic Criteria": [
            "Elevated cardiac biomarkers",
            "ECG abnormalities",
            "Heart MRI showing inflammation"
        ],
        "Treatment Options": {
            "Medication": [
                "Anti-inflammatory drugs",
                "Heart failure medications"
            ],
            "Procedures": [
                "In severe cases, ventricular assist devices or heart transplant may be considered"
            ],
            "Lifestyle Changes": [
                "Rest",
                "Avoidance of physical exertion"
            ]
        },
        "Prognosis": "Varies widely; can range from full recovery to chronic heart failure depending on severity and response to treatment.",
        "Prevention": [
            "Vaccination against viral infections",
            "Prompt treatment of infections"
        ],
        "Additional Resources": [
            {
                "Title": "Mayo Clinic - Myocarditis",
                "Link": "https://www.mayoclinic.org/"
            }
        ],
        "SNOMED Code": "164889003",
        "Detailed Description": "An inflammatory condition of the heart muscle, often caused by infections or autoimmune disorders, leading to reduced heart function and potential heart failure.",
        "Clinical Findings": [
            "Elevated cardiac biomarkers",
            "ECG abnormalities",
            "Increased inflammatory markers"
        ],
        "Associated Conditions": [
            "Chronic heart failure",
            "Arrhythmias"
        ],
        "Treatment Guidelines": [
            "Management includes treatment of underlying cause, supportive care, and close monitoring of heart function."
        ]
    },
    "164890007": {
        "Condition Name": "Acute Pericarditis",
        "Description": "Inflammation of the pericardium, the fibrous sac surrounding the heart, often leading to chest pain and discomfort.",
        "Symptoms/Clinical Presentation": [
            "Sharp chest pain that may worsen with deep breathing",
            "Fever",
            "Pericardial friction rub"
        ],
        "Risk Factors": [
            "Viral infections",
            "Autoimmune disorders",
            "Recent heart surgery"
        ],
        "Possible Causes": [
            "Viral infections",
            "Bacterial infections",
            "Autoimmune conditions"
        ],
        "Diagnostic Criteria": [
            "ECG changes (e.g., widespread ST elevation)",
            "Echocardiogram showing pericardial effusion"
        ],
        "Treatment Options": {
            "Medication": [
                "Nonsteroidal anti-inflammatory drugs (NSAIDs)",
                "Colchicine"
            ],
            "Procedures": [
                "Pericardiocentesis if there is significant effusion"
            ],
            "Lifestyle Changes": [
                "Rest",
                "Avoidance of strenuous activity"
            ]
        },
        "Prognosis": "Good with appropriate treatment; most people recover fully with medication and rest.",
        "Prevention": [
            "Early treatment of infections",
            "Management of autoimmune conditions"
        ],
        "Additional Resources": [
            {
                "Title": "American Heart Association - Pericarditis",
                "Link": "https://www.heart.org/"
            }
        ],
        "SNOMED Code": "164890007",
        "Detailed Description": "Inflammation of the pericardium leading to chest pain and potential complications such as pericardial effusion.",
        "Clinical Findings": [
            "Pericardial friction rub",
            "ECG changes consistent with pericarditis"
        ],
        "Associated Conditions": [
            "Pericardial effusion",
            "Constrictive pericarditis"
        ],
        "Treatment Guidelines": [
            "Follow guidelines for managing pericarditis, including use of anti-inflammatory medications and monitoring for complications."
        ]
    },
    "164909002": {
        "Condition Name": "Acute Endocarditis",
        "Description": "An infection of the inner lining of the heart chambers and valves, often caused by bacteria.",
        "Symptoms/Clinical Presentation": [
            "Fever",
            "Chills",
            "Night sweats",
            "Fatigue"
        ],
        "Risk Factors": [
            "Heart valve disease",
            "Intravenous drug use",
            "Recent dental or surgical procedures"
        ],
        "Possible Causes": [
            "Bacterial infections",
            "Fungal infections"
        ],
        "Diagnostic Criteria": [
            "Blood cultures positive for causative organism",
            "Echocardiogram showing vegetations on heart valves"
        ],
        "Treatment Options": {
            "Medication": [
                "Intravenous antibiotics",
                "Antifungal agents if necessary"
            ],
            "Procedures": [
                "Surgical intervention to repair or replace affected valves in severe cases"
            ],
            "Lifestyle Changes": [
                "Good dental hygiene",
                "Avoiding drug abuse"
            ]
        },
        "Prognosis": "Depends on the timeliness of treatment; can be life-threatening if not treated promptly.",
        "Prevention": [
            "Prophylactic antibiotics before certain dental or surgical procedures in high-risk individuals",
            "Good personal hygiene"
        ],
        "Additional Resources": [
            {
                "Title": "Centers for Disease Control and Prevention - Endocarditis",
                "Link": "https://www.cdc.gov/"
            }
        ],
        "SNOMED Code": "164909002",
        "Detailed Description": "An infection of the heart valves or endocardial surface leading to significant complications if not addressed promptly.",
        "Clinical Findings": [
            "Positive blood cultures",
            "Vegetations seen on echocardiogram"
        ],
        "Associated Conditions": [
            "Heart valve dysfunction",
            "Heart failure"
        ],
        "Treatment Guidelines": [
            "Immediate initiation of appropriate antibiotics; consider surgical intervention if necessary."
        ]
    },
    "164917005": {
        "Condition Name": "Acute Heart Failure",
        "Description": "A sudden worsening of heart failure symptoms, requiring urgent medical attention to manage symptoms and prevent complications.",
        "Symptoms/Clinical Presentation": [
            "Severe shortness of breath",
            "Rapid or irregular heartbeat",
            "Swelling of legs and abdomen",
            "Persistent cough"
        ],
        "Risk Factors": [
            "Chronic heart failure",
            "Hypertension",
            "Coronary artery disease"
        ],
        "Possible Causes": [
            "Acute myocardial infarction",
            "Uncontrolled hypertension",
            "Arrhythmias"
        ],
        "Diagnostic Criteria": [
            "Elevated BNP or NT-proBNP levels",
            "Imaging showing pulmonary congestion",
            "Clinical signs of fluid overload"
        ],
        "Treatment Options": {
            "Medication": [
                "Diuretics",
                "ACE inhibitors",
                "Beta-blockers"
            ],
            "Procedures": [
                "Hospitalization for intensive monitoring and treatment",
                "In severe cases, mechanical circulatory support"
            ],
            "Lifestyle Changes": [
                "Sodium restriction",
                "Fluid management"
            ]
        },
        "Prognosis": "Can be severe and requires prompt treatment; long-term outcomes depend on the underlying cause and response to therapy.",
        "Prevention": [
            "Effective management of chronic heart failure",
            "Regular follow-ups with a cardiologist"
        ],
        "Additional Resources": [
            {
                "Title": "American Heart Association - Heart Failure",
                "Link": "https://www.heart.org/"
            }
        ],
        "SNOMED Code": "164917005",
        "Detailed Description": "A sudden and severe worsening of heart failure symptoms, often requiring urgent intervention to stabilize the patient.",
        "Clinical Findings": [
            "Elevated BNP or NT-proBNP levels",
            "Clinical signs of fluid overload",
            "Imaging showing pulmonary congestion"
        ],
        "Associated Conditions": [
            "Chronic heart failure",
            "Acute myocardial infarction"
        ],
        "Treatment Guidelines": [
            "Immediate treatment with diuretics and other medications; close monitoring and management of underlying conditions."
        ]
    },
    "164934002": {
        "Condition Name": "Atrial Flutter",
        "Description": "A type of abnormal heart rhythm characterized by rapid, regular heartbeats originating from the atria.",
        "Symptoms/Clinical Presentation": [
            "Palpitations",
            "Shortness of breath",
            "Fatigue",
            "Dizziness"
        ],
        "Risk Factors": [
            "Hypertension",
            "Coronary artery disease",
            "Heart failure",
            "Chronic lung disease"
        ],
        "Possible Causes": [
            "Heart valve disease",
            "Congenital heart defects",
            "Previous heart surgery"
        ],
        "Diagnostic Criteria": [
            "ECG showing characteristic 'sawtooth' pattern",
            "Irregular heart rate"
        ],
        "Treatment Options": {
            "Medication": [
                "Antiarrhythmic drugs",
                "Anticoagulants"
            ],
            "Procedures": [
                "Electrical cardioversion",
                "Catheter ablation"
            ],
            "Lifestyle Changes": [
                "Avoiding stimulants",
                "Managing underlying heart conditions"
            ]
        },
        "Prognosis": "Chronic condition requiring ongoing management; risk of stroke and heart failure if untreated.",
        "Prevention": [
            "Regular monitoring and management of risk factors",
            "Healthy lifestyle"
        ],
        "Additional Resources": [
            {
                "Title": "Atrial Flutter Information from Mayo Clinic",
                "Link": "https://www.mayoclinic.org/"
            }
        ],
        "SNOMED Code": "164934002",
        "Detailed Description": "A condition where the atria of the heart beat rapidly in a regular pattern, which can lead to symptoms like palpitations and increased risk of stroke.",
        "Clinical Findings": [
            "ECG with 'F-waves' or 'sawtooth' pattern",
            "Elevated heart rate"
        ],
        "Associated Conditions": [
            "Stroke",
            "Heart failure"
        ],
        "Treatment Guidelines": [
            "Follow guidelines for the management of atrial flutter, including anticoagulation and rhythm control strategies."
        ]
    },
    "17338001": {
        "Condition Name": "Ventricular Tachycardia",
        "Description": "A type of fast heart rate that arises from improper electrical activity in the ventricles of the heart.",
        "Symptoms/Clinical Presentation": [
            "Palpitations",
            "Dizziness",
            "Shortness of breath",
            "Chest pain"
        ],
        "Risk Factors": [
            "Previous heart attack",
            "Coronary artery disease",
            "Heart failure"
        ],
        "Possible Causes": [
            "Scar tissue from a previous heart attack",
            "Cardiomyopathy"
        ],
        "Diagnostic Criteria": [
            "Rapid ventricular rate on ECG",
            "Wide QRS complex"
        ],
        "Treatment Options": {
            "Medication": [
                "Antiarrhythmic drugs",
                "Beta-blockers"
            ],
            "Procedures": [
                "Implantable cardioverter-defibrillator (ICD)",
                "Catheter ablation"
            ],
            "Lifestyle Changes": [
                "Avoid stimulants",
                "Manage heart disease"
            ]
        },
        "Prognosis": "Can be life-threatening if not treated; ongoing management is often required.",
        "Prevention": [
            "Manage underlying heart conditions",
            "Regular follow-up with a cardiologist"
        ],
        "Additional Resources": [
            {
                "Title": "Ventricular Tachycardia Information",
                "Link": "https://www.heart.org/"
            }
        ],
        "SNOMED Code": "17338001",
        "Detailed Description": "A condition where the ventricles beat very quickly, which can be dangerous and may lead to cardiac arrest if not promptly treated.",
        "Clinical Findings": [
            "Rapid and regular heartbeats",
            "Loss of consciousness in severe cases"
        ],
        "Associated Conditions": [
            "Sudden cardiac arrest",
            "Heart failure"
        ],
        "Treatment Guidelines": [
            "Follow guidelines for the emergency management of ventricular tachycardia, including ACLS protocols."
        ]
    },
    "251146004": {
        "Condition Name": "Mitral Valve Prolapse",
        "Description": "A condition where the mitral valve of the heart doesn't close properly, which can lead to leakage of blood back into the left atrium.",
        "Symptoms/Clinical Presentation": [
            "Palpitations",
            "Chest pain",
            "Fatigue",
            "Shortness of breath"
        ],
        "Risk Factors": [
            "Genetic predisposition",
            "Connective tissue disorders"
        ],
        "Possible Causes": [
            "Genetic abnormalities",
            "Rheumatic fever",
            "Degenerative changes in the valve"
        ],
        "Diagnostic Criteria": [
            "ECG abnormalities",
            "Echocardiogram showing abnormal valve movement"
        ],
        "Treatment Options": {
            "Medication": [
                "Beta-blockers for symptoms",
                "Anticoagulants if atrial fibrillation is present"
            ],
            "Procedures": [
                "Mitral valve repair or replacement in severe cases"
            ],
            "Lifestyle Changes": [
                "Regular follow-up with a cardiologist",
                "Manage symptoms"
            ]
        },
        "Prognosis": "Generally good with appropriate management; severe cases may require surgical intervention.",
        "Prevention": [
            "Regular cardiac check-ups",
            "Monitoring and managing symptoms"
        ],
        "Additional Resources": [
            {
                "Title": "Mitral Valve Prolapse Information from American Heart Association",
                "Link": "https://www.heart.org/"
            }
        ],
        "SNOMED Code": "251146004",
        "Detailed Description": "A heart valve condition where the mitral valve leaflets bulge (prolapse) into the left atrium during systole, potentially causing mitral regurgitation.",
        "Clinical Findings": [
            "Mid-systolic click on auscultation",
            "Regurgitant flow on echocardiogram"
        ],
        "Associated Conditions": [
            "Mitral regurgitation",
            "Endocarditis"
        ],
        "Treatment Guidelines": [
            "Manage symptoms and complications; surgical intervention for severe cases."
        ]
    },
    "270492004": {
        "Condition Name": "Chronic Obstructive Pulmonary Disease (COPD)",
        "Description": "A progressive lung disease characterized by long-term breathing problems and poor airflow.",
        "Symptoms/Clinical Presentation": [
            "Chronic cough",
            "Shortness of breath",
            "Wheezing",
            "Production of mucus"
        ],
        "Risk Factors": [
            "Smoking",
            "Exposure to air pollutants",
            "Occupational dust and chemicals"
        ],
        "Possible Causes": [
            "Long-term smoking",
            "Environmental exposures"
        ],
        "Diagnostic Criteria": [
            "Spirometry showing reduced FEV1/FVC ratio",
            "Chronic symptoms lasting more than three months"
        ],
        "Treatment Options": {
            "Medication": [
                "Bronchodilators",
                "Inhaled corticosteroids"
            ],
            "Procedures": [
                "Pulmonary rehabilitation",
                "Oxygen therapy in severe cases"
            ],
            "Lifestyle Changes": [
                "Smoking cessation",
                "Avoiding respiratory irritants"
            ]
        },
        "Prognosis": "Progressive disease with worsening symptoms over time; management focuses on symptom relief and improving quality of life.",
        "Prevention": [
            "Avoiding smoking",
            "Reducing exposure to air pollutants"
        ],
        "Additional Resources": [
            {
                "Title": "COPD Information from National Heart, Lung, and Blood Institute",
                "Link": "https://www.nhlbi.nih.gov/"
            }
        ],
        "SNOMED Code": "270492004",
        "Detailed Description": "A progressive disease that causes obstructed airflow from the lungs, leading to difficulty breathing and persistent cough.",
        "Clinical Findings": [
            "Decreased breath sounds",
            "Hyperinflation of the lungs on chest X-ray"
        ],
        "Associated Conditions": [
            "Respiratory infections",
            "Heart disease"
        ],
        "Treatment Guidelines": [
            "Follow COPD management guidelines, including pharmacological therapy and lifestyle modifications."
        ]
    },
    "284470004": {
        "Condition Name": "Hypertension",
        "Description": "A condition characterized by consistently elevated blood pressure levels, which can lead to cardiovascular disease and other complications.",
        "Symptoms/Clinical Presentation": [
            "Headaches",
            "Shortness of breath",
            "Nosebleeds",
            "Dizziness"
        ],
        "Risk Factors": [
            "Obesity",
            "Sedentary lifestyle",
            "High salt intake",
            "Family history"
        ],
        "Possible Causes": [
            "Primary (essential) hypertension with no identifiable cause",
            "Secondary hypertension due to other conditions (e.g., kidney disease)"
        ],
        "Diagnostic Criteria": [
            "Repeatedly elevated blood pressure readings (≥140/90 mmHg)"
        ],
        "Treatment Options": {
            "Medication": [
                "ACE inhibitors",
                "Beta-blockers",
                "Diuretics"
            ],
            "Procedures": [
                "Lifestyle modifications",
                "Renal denervation in resistant cases"
            ],
            "Lifestyle Changes": [
                "Dietary changes",
                "Regular exercise",
                "Weight management"
            ]
        },
        "Prognosis": "Can lead to serious health problems if uncontrolled, including heart attack and stroke; effective management can reduce risks.",
        "Prevention": [
            "Maintain a healthy weight",
            "Regular exercise",
            "Limit salt intake"
        ],
        "Additional Resources": [
            {
                "Title": "Hypertension Information from American Heart Association",
                "Link": "https://www.heart.org/"
            }
        ],
        "SNOMED Code": "284470004",
        "Detailed Description": "A condition where blood pressure is consistently high, which can damage blood vessels and lead to heart disease, stroke, and kidney problems.",
        "Clinical Findings": [
            "Elevated blood pressure readings",
            "Organ damage in severe cases"
        ],
        "Associated Conditions": [
            "Heart disease",
            "Kidney disease"
        ],
        "Treatment Guidelines": [
            "Follow hypertension management guidelines, including lifestyle modifications and pharmacological treatment."
        ]
    },
    "39732003": {
        "Condition Name": "Anterior Myocardial Infarction",
        "Description": "A type of heart attack that affects the front wall of the heart, typically involving the left anterior descending artery.",
        "Symptoms/Clinical Presentation": [
            "Severe chest pain",
            "Shortness of breath",
            "Nausea",
            "Sweating"
        ],
        "Risk Factors": [
            "High blood pressure",
            "Smoking",
            "Diabetes",
            "High cholesterol"
        ],
        "Possible Causes": [
            "Blockage of the left anterior descending artery",
            "Atherosclerosis"
        ],
        "Diagnostic Criteria": [
            "ST elevation in leads V1-V4 on ECG",
            "Elevated cardiac enzymes"
        ],
        "Treatment Options": {
            "Medication": [
                "Antiplatelet agents",
                "Beta-blockers"
            ],
            "Procedures": [
                "Percutaneous coronary intervention (PCI)",
                "Coronary artery bypass grafting (CABG)"
            ],
            "Lifestyle Changes": [
                "Smoking cessation",
                "Dietary changes"
            ]
        },
        "Prognosis": "Depends on the extent of myocardial damage and time to treatment; early intervention improves outcomes.",
        "Prevention": [
            "Control of blood pressure and cholesterol",
            "Healthy lifestyle"
        ],
        "Additional Resources": [
            {
                "Title": "Heart Attack Information from the American Heart Association",
                "Link": "https://www.heart.org/"
            }
        ],
        "SNOMED Code": "39732003",
        "Detailed Description": "A myocardial infarction that occurs due to the blockage of the left anterior descending artery, affecting the front part of the heart.",
        "Clinical Findings": [
            "ST elevation in precordial leads",
            "Elevated troponin levels"
        ],
        "Associated Conditions": [
            "Heart failure",
            "Ventricular arrhythmias"
        ],
        "Treatment Guidelines": [
            "Immediate reperfusion therapy, including PCI or thrombolysis, is recommended."
        ]
    },
    "426177001": {
        "Condition Name": "Incomplete Right Bundle Branch Block",
        "Description": "A delay in the electrical conduction through the right bundle branch, causing a slight alteration in the ECG, but not a full block.",
        "Symptoms/Clinical Presentation": [
            "Often asymptomatic",
            "Mild palpitations",
            "Dizziness"
        ],
        "Risk Factors": [
            "Congenital heart disease",
            "Age-related changes",
            "Hypertension"
        ],
        "Possible Causes": [
            "Structural heart disease",
            "Pulmonary embolism"
        ],
        "Diagnostic Criteria": [
            "QRS complex > 100 ms but < 120 ms on ECG",
            "RSR' pattern in lead V1"
        ],
        "Treatment Options": {
            "Medication": [
                "None usually required unless associated with underlying conditions"
            ],
            "Procedures": [
                "Treatment of underlying conditions if present"
            ],
            "Lifestyle Changes": [
                "Regular monitoring if associated with heart disease"
            ]
        },
        "Prognosis": "Generally benign, but monitoring is recommended if associated with other heart conditions.",
        "Prevention": [
            "Management of underlying heart conditions",
            "Regular cardiovascular check-ups"
        ],
        "Additional Resources": [
            {
                "Title": "Right Bundle Branch Block Information",
                "Link": "https://www.mayoclinic.org/"
            }
        ],
        "SNOMED Code": "426177001",
        "Detailed Description": "A partial blockage of the right bundle branch that causes delayed depolarization of the right ventricle, often detected on an ECG.",
        "Clinical Findings": [
            "RSR' pattern in V1 lead",
            "Prolonged QRS duration"
        ],
        "Associated Conditions": [
            "Pulmonary embolism",
            "Coronary artery disease"
        ],
        "Treatment Guidelines": [
            "Regular monitoring; treatment if associated with other cardiac conditions."
        ]
    },
    "426627000": {
        "Condition Name": "Left Anterior Fascicular Block",
        "Description": "A blockage in one of the branches of the left bundle branch, affecting the electrical conduction to the left ventricle.",
        "Symptoms/Clinical Presentation": [
            "Often asymptomatic",
            "Mild dizziness",
            "Fatigue"
        ],
        "Risk Factors": [
            "Hypertension",
            "Coronary artery disease",
            "Cardiomyopathy"
        ],
        "Possible Causes": [
            "Hypertensive heart disease",
            "Ischemic heart disease"
        ],
        "Diagnostic Criteria": [
            "Left axis deviation on ECG",
            "Small Q waves in leads I and aVL"
        ],
        "Treatment Options": {
            "Medication": [
                "Management of underlying conditions"
            ],
            "Procedures": [
                "None specific for LAFB"
            ],
            "Lifestyle Changes": [
                "Regular monitoring",
                "Healthy diet"
            ]
        },
        "Prognosis": "Generally benign, but may indicate underlying heart disease; regular follow-up is recommended.",
        "Prevention": [
            "Control of blood pressure",
            "Healthy lifestyle"
        ],
        "Additional Resources": [
            {
                "Title": "Fascicular Block Information",
                "Link": "https://www.clevelandclinic.org/"
            }
        ],
        "SNOMED Code": "426627000",
        "Detailed Description": "A conduction abnormality where the anterior fascicle of the left bundle branch is blocked, leading to a delay in the electrical impulses to the left ventricle.",
        "Clinical Findings": [
            "Left axis deviation on ECG",
            "Delayed depolarization of the left ventricle"
        ],
        "Associated Conditions": [
            "Hypertensive heart disease",
            "Left ventricular hypertrophy"
        ],
        "Treatment Guidelines": [
            "Regular monitoring; treatment focused on underlying heart disease."
        ]
    },
    "426783006": {
        "Condition Name": "Left Bundle Branch Block",
        "Description": "A blockage or delay in the pathway that sends electrical impulses to the left side of the heart, affecting the heart's ability to pump efficiently.",
        "Symptoms/Clinical Presentation": [
            "Often asymptomatic",
            "Possible chest pain",
            "Shortness of breath",
            "Fatigue"
        ],
        "Risk Factors": [
            "Hypertension",
            "Coronary artery disease",
            "Cardiomyopathy"
        ],
        "Possible Causes": [
            "Hypertensive heart disease",
            "Aortic stenosis"
        ],
        "Diagnostic Criteria": [
            "Widened QRS complex on ECG",
            "Absence of R waves in V1 and V2 leads"
        ],
        "Treatment Options": {
            "Medication": [
                "Treat underlying conditions",
                "Heart failure medications if needed"
            ],
            "Procedures": [
                "Pacemaker in severe cases"
            ],
            "Lifestyle Changes": [
                "Manage hypertension",
                "Healthy diet"
            ]
        },
        "Prognosis": "Varies depending on underlying conditions; may lead to heart failure if untreated.",
        "Prevention": [
            "Control blood pressure",
            "Regular cardiovascular check-ups"
        ],
        "Additional Resources": [
            {
                "Title": "Left Bundle Branch Block - Health Information",
                "Link": "https://www.healthline.com/"
            }
        ],
        "SNOMED Code": "426783006",
        "Detailed Description": "A delay or block in the electrical impulses that make the heart's left ventricle contract, often indicating underlying heart disease.",
        "Clinical Findings": [
            "Widened QRS complex on ECG",
            "Delayed left ventricular contraction"
        ],
        "Associated Conditions": [
            "Heart failure",
            "Atrial fibrillation"
        ],
        "Treatment Guidelines": [
            "Monitor and treat underlying cardiovascular conditions; consider pacemaker therapy if indicated."
        ]
    },
    "427084000": {
        "Condition Name": "Sinus Tachycardia",
        "Description": "A condition where the heart rate is elevated beyond the normal resting rate due to an increased rate of electrical impulses from the sinus node.",
        "Symptoms/Clinical Presentation": [
            "Rapid heartbeat",
            "Palpitations",
            "Dizziness",
            "Shortness of breath"
        ],
        "Risk Factors": [
            "Fever",
            "Anemia",
            "Hyperthyroidism",
            "Exercise",
            "Anxiety"
        ],
        "Possible Causes": [
            "Increased sympathetic stimulation",
            "Fever",
            "Hypovolemia"
        ],
        "Diagnostic Criteria": [
            "Heart rate greater than 100 beats per minute",
            "Normal P wave preceding every QRS complex on ECG"
        ],
        "Treatment Options": {
            "Medication": [
                "Beta-blockers if symptomatic",
                "Calcium channel blockers"
            ],
            "Procedures": [
                "None typically required unless due to an underlying condition"
            ],
            "Lifestyle Changes": [
                "Manage stress",
                "Stay hydrated"
            ]
        },
        "Prognosis": "Generally benign if associated with physiological stress; may require treatment if symptomatic or due to underlying conditions.",
        "Prevention": [
            "Healthy lifestyle",
            "Manage stress and anxiety"
        ],
        "Additional Resources": [
            {
                "Title": "Understanding Sinus Tachycardia",
                "Link": "https://www.webmd.com/"
            }
        ],
        "SNOMED Code": "427084000",
        "Detailed Description": "An elevated heart rate originating from the sinoatrial node, often in response to stress, exercise, or other physiological stimuli.",
        "Clinical Findings": [
            "Heart rate > 100 bpm",
            "Normal rhythm with P wave preceding each QRS"
        ],
        "Associated Conditions": [
            "Anxiety disorders",
            "Fever",
            "Hyperthyroidism"
        ],
        "Treatment Guidelines": [
            "Address underlying causes such as fever, anemia, or hyperthyroidism; consider beta-blockers for symptomatic relief."
        ]
    },
    "427393009": {
        "Condition Name": "Ventricular Fibrillation",
        "Description": "A life-threatening heart rhythm that results in rapid, erratic electrical impulses causing the ventricles to quiver instead of pumping blood.",
        "Symptoms/Clinical Presentation": [
            "Sudden collapse",
            "No pulse",
            "Loss of consciousness",
            "Sudden cardiac arrest"
        ],
        "Risk Factors": [
            "Previous heart attack",
            "Coronary artery disease",
            "Heart failure",
            "Electrolyte imbalances"
        ],
        "Possible Causes": [
            "Severe heart disease",
            "Electrocution",
            "Drowning",
            "Massive heart attack"
        ],
        "Diagnostic Criteria": [
            "Chaotic, irregular heart rhythm on ECG",
            "No detectable pulse"
        ],
        "Treatment Options": {
            "Immediate": [
                "CPR (Cardiopulmonary Resuscitation)",
                "Defibrillation"
            ],
            "Long-Term": [
                "Implantable cardioverter-defibrillator (ICD)"
            ]
        },
        "Prognosis": "Immediate treatment is critical; without intervention, ventricular fibrillation is fatal.",
        "Prevention": [
            "Management of heart disease",
            "Avoiding situations that can trigger the condition"
        ],
        "Additional Resources": [
            {
                "Title": "Ventricular Fibrillation Information",
                "Link": "https://www.mayoclinic.org/"
            }
        ],
        "SNOMED Code": "427393009",
        "Detailed Description": "A condition characterized by rapid and erratic electrical impulses in the heart's ventricles, leading to ineffective heart contractions and, without treatment, death.",
        "Clinical Findings": [
            "Irregular, rapid heart rhythm on ECG",
            "No effective heartbeat"
        ],
        "Associated Conditions": [
            "Sudden cardiac arrest",
            "Heart failure"
        ],
        "Treatment Guidelines": [
            "Follow advanced cardiac life support (ACLS) protocols immediately."
        ]
    },
    "445118002": {
        "Condition Name": "Myocarditis",
        "Description": "An inflammation of the heart muscle, often caused by viral infections, that can affect the heart's electrical system, reducing its ability to pump blood.",
        "Symptoms/Clinical Presentation": [
            "Chest pain",
            "Fatigue",
            "Shortness of breath",
            "Arrhythmias"
        ],
        "Risk Factors": [
            "Viral infections",
            "Autoimmune diseases",
            "Exposure to certain toxins",
            "Chronic alcohol abuse"
        ],
        "Possible Causes": [
            "Viral infections (e.g., Coxsackievirus)",
            "Bacterial infections",
            "Autoimmune diseases"
        ],
        "Diagnostic Criteria": [
            "Elevated inflammatory markers",
            "Cardiac MRI showing inflammation",
            "Biopsy of heart tissue"
        ],
        "Treatment Options": {
            "Medication": [
                "Anti-inflammatory drugs",
                "Antibiotics if bacterial"
            ],
            "Lifestyle Changes": [
                "Rest",
                "Avoid strenuous activity"
            ]
        },
        "Prognosis": "Varies depending on severity; may recover completely or develop chronic heart conditions.",
        "Prevention": [
            "Avoid viral infections",
            "Manage autoimmune diseases"
        ],
        "Additional Resources": [
            {
                "Title": "Myocarditis Information",
                "Link": "https://www.cdc.gov/"
            }
        ],
        "SNOMED Code": "445118002",
        "Detailed Description": "Inflammation of the heart muscle, which can lead to weakened heart contractions and potentially severe cardiac complications.",
        "Clinical Findings": [
            "Elevated troponin levels",
            "ECG changes indicative of myocarditis"
        ],
        "Associated Conditions": [
            "Dilated cardiomyopathy",
            "Heart failure"
        ],
        "Treatment Guidelines": [
            "Manage underlying cause and provide supportive care; in severe cases, heart failure management may be necessary."
        ]
    },
    "47665007": {
        "Condition Name": "Mitral Valve Prolapse",
        "Description": "A condition in which the two valve flaps of the mitral valve do not close smoothly or evenly but instead bulge (prolapse) upward into the left atrium during the heart's contraction.",
        "Symptoms/Clinical Presentation": [
            "Often asymptomatic",
            "Palpitations",
            "Chest pain",
            "Shortness of breath"
        ],
        "Risk Factors": [
            "Family history of mitral valve prolapse",
            "Connective tissue disorders",
            "Age-related changes"
        ],
        "Possible Causes": [
            "Abnormal mitral valve structure",
            "Connective tissue diseases"
        ],
        "Diagnostic Criteria": [
            "Echocardiogram showing prolapse of the mitral valve",
            "Heart murmur detected during physical exam"
        ],
        "Treatment Options": {
            "Medication": [
                "Beta-blockers for palpitations"
            ],
            "Procedures": [
                "Mitral valve repair or replacement in severe cases"
            ],
            "Lifestyle Changes": [
                "Regular monitoring",
                "Healthy lifestyle"
            ]
        },
        "Prognosis": "Generally good; most people with mitral valve prolapse do not require treatment.",
        "Prevention": [
            "Regular check-ups if there is a family history",
            "Manage associated conditions"
        ],
        "Additional Resources": [
            {
                "Title": "Mitral Valve Prolapse Information",
                "Link": "https://www.heart.org/"
            }
        ],
        "SNOMED Code": "47665007",
        "Detailed Description": "A condition where the mitral valve doesn't close properly, causing a clicking sound or murmur and possibly leading to mitral regurgitation.",
        "Clinical Findings": [
            "Mid-systolic click heard on auscultation",
            "Regurgitant murmur"
        ],
        "Associated Conditions": [
            "Mitral regurgitation",
            "Atrial fibrillation"
        ],
        "Treatment Guidelines": [
            "Monitor for progression; surgical intervention if severe regurgitation develops."
        ]
    },
    "59118001": {
        "Condition Name": "Pericarditis",
        "Description": "An inflammation of the pericardium, the thin sac-like membrane surrounding the heart, often leading to sharp chest pain.",
        "Symptoms/Clinical Presentation": [
            "Sharp, stabbing chest pain",
            "Pain that worsens when lying down",
            "Fever",
            "Shortness of breath"
        ],
        "Risk Factors": [
            "Viral infections",
            "Heart surgery",
            "Trauma to the chest",
            "Autoimmune conditions"
        ],
        "Possible Causes": [
            "Viral infections",
            "Heart attack",
            "Systemic inflammatory disorders"
        ],
        "Diagnostic Criteria": [
            "Pericardial friction rub heard on auscultation",
            "ECG showing diffuse ST elevation",
            "Echocardiogram revealing pericardial effusion"
        ],
        "Treatment Options": {
            "Medication": [
                "NSAIDs for pain and inflammation",
                "Colchicine to reduce recurrence"
            ],
            "Procedures": [
                "Pericardiocentesis if there is significant effusion"
            ],
            "Lifestyle Changes": [
                "Rest",
                "Avoid strenuous activity"
            ]
        },
        "Prognosis": "Generally good with treatment; however, complications such as pericardial effusion or chronic pericarditis may occur.",
        "Prevention": [
            "Prompt treatment of underlying infections",
            "Regular monitoring if at risk"
        ],
        "Additional Resources": [
            {
                "Title": "Pericarditis Information",
                "Link": "https://www.clevelandclinic.org/"
            }
        ],
        "SNOMED Code": "59118001",
        "Detailed Description": "Inflammation of the pericardium, often presenting with sharp chest pain and sometimes leading to complications if untreated.",
        "Clinical Findings": [
            "Pericardial friction rub",
            "Pericardial effusion on imaging"
        ],
        "Associated Conditions": [
            "Cardiac tamponade",
            "Constrictive pericarditis"
        ],
        "Treatment Guidelines": [
            "Manage pain and inflammation, monitor for effusion; consider pericardiocentesis if necessary."
        ]
    },
    "59931005": {
        "Condition Name": "Pulmonary Embolism",
        "Description": "A blockage in one of the pulmonary arteries in the lungs, usually caused by blood clots that travel to the lungs from the legs or other parts of the body (deep vein thrombosis).",
        "Symptoms/Clinical Presentation": [
            "Sudden shortness of breath",
            "Chest pain that worsens with deep breathing",
            "Coughing, sometimes with bloody sputum",
            "Rapid heart rate"
        ],
        "Risk Factors": [
            "Prolonged immobility",
            "Surgery",
            "Cancer",
            "History of deep vein thrombosis"
        ],
        "Possible Causes": [
            "Blood clots traveling to the lungs from deep veins in the legs",
            "Fat embolism"
        ],
        "Diagnostic Criteria": [
            "CT pulmonary angiography showing blockage",
            "D-dimer test indicating clot presence",
            "Ventilation-perfusion scan"
        ],
        "Treatment Options": {
            "Medication": [
                "Anticoagulants",
                "Thrombolytics in severe cases"
            ],
            "Procedures": [
                "Surgical removal of the clot in life-threatening cases",
                "Inferior vena cava (IVC) filter"
            ],
            "Lifestyle Changes": [
                "Regular physical activity",
                "Compression stockings"
            ]
        },
        "Prognosis": "Can be life-threatening if not treated promptly; with treatment, the outlook is generally good, though there is a risk of recurrence.",
        "Prevention": [
            "Avoid prolonged immobility",
            "Use of anticoagulants in high-risk patients"
        ],
        "Additional Resources": [
            {
                "Title": "Pulmonary Embolism Information",
                "Link": "https://www.mayoclinic.org/"
            }
        ],
        "SNOMED Code": "59931005",
        "Detailed Description": "A life-threatening condition where a blood clot blocks an artery in the lungs, leading to impaired oxygenation of blood and potentially fatal outcomes.",
        "Clinical Findings": [
            "Hypoxemia",
            "Tachycardia",
            "Signs of deep vein thrombosis in legs"
        ],
        "Associated Conditions": [
            "Deep vein thrombosis",
            "Right ventricular strain"
        ],
        "Treatment Guidelines": [
            "Immediate anticoagulation therapy; consider thrombolysis or surgery for massive PE."
        ]
    },
    "63593006": {
        "Condition Name": "Myocardial Ischemia",
        "Description": "A condition characterized by reduced blood flow to the heart muscle, often leading to chest pain or discomfort.",
        "Symptoms/Clinical Presentation": [
            "Chest pain (angina)",
            "Shortness of breath",
            "Fatigue",
            "Nausea"
        ],
        "Risk Factors": [
            "Coronary artery disease",
            "Hypertension",
            "Diabetes",
            "Smoking"
        ],
        "Possible Causes": [
            "Atherosclerosis",
            "Blood clot",
            "Coronary artery spasm"
        ],
        "Diagnostic Criteria": [
            "ECG changes (e.g., ST depression)",
            "Elevated cardiac biomarkers",
            "Coronary angiography"
        ],
        "Treatment Options": {
            "Medication": [
                "Nitrates",
                "Beta-blockers",
                "Calcium channel blockers"
            ],
            "Procedures": [
                "Angioplasty",
                "Coronary artery bypass grafting (CABG)"
            ],
            "Lifestyle Changes": [
                "Quit smoking",
                "Healthy diet",
                "Regular exercise"
            ]
        },
        "Prognosis": "Good with proper treatment; however, can lead to heart attack if untreated.",
        "Prevention": [
            "Manage risk factors such as hypertension and cholesterol",
            "Regular cardiovascular check-ups"
        ],
        "Additional Resources": [
            {
                "Title": "Myocardial Ischemia Information",
                "Link": "https://www.mayoclinic.org/"
            }
        ],
        "SNOMED Code": "63593006",
        "Detailed Description": "A condition where the heart muscle receives insufficient oxygen-rich blood due to narrowed coronary arteries.",
        "Clinical Findings": [
            "Chest pain triggered by exertion",
            "ECG showing ST segment depression"
        ],
        "Associated Conditions": [
            "Stable angina",
            "Unstable angina"
        ],
        "Treatment Guidelines": [
            "Guidelines for the management of stable ischemic heart disease."
        ]
    },
    "698252002": {
        "Condition Name": "Supraventricular Tachycardia",
        "Description": "A rapid heart rate originating above the heart's ventricles, typically causing a sudden onset of palpitations.",
        "Symptoms/Clinical Presentation": [
            "Palpitations",
            "Dizziness",
            "Shortness of breath",
            "Chest discomfort"
        ],
        "Risk Factors": [
            "Caffeine or alcohol consumption",
            "Stress",
            "Congenital heart defects"
        ],
        "Possible Causes": [
            "Abnormal electrical pathways in the heart",
            "Wolff-Parkinson-White syndrome"
        ],
        "Diagnostic Criteria": [
            "Rapid heart rate on ECG",
            "Narrow QRS complex"
        ],
        "Treatment Options": {
            "Medication": [
                "Beta-blockers",
                "Calcium channel blockers"
            ],
            "Procedures": [
                "Catheter ablation",
                "Electrical cardioversion"
            ],
            "Lifestyle Changes": [
                "Avoiding stimulants",
                "Stress management"
            ]
        },
        "Prognosis": "Generally good with treatment; can be life-threatening if untreated in certain cases.",
        "Prevention": [
            "Avoid known triggers",
            "Regular follow-ups with a cardiologist"
        ],
        "Additional Resources": [
            {
                "Title": "SVT Information",
                "Link": "https://www.webmd.com/"
            }
        ],
        "SNOMED Code": "698252002",
        "Detailed Description": "A condition characterized by an abnormally fast heart rate that originates above the heart's ventricles, often leading to episodes of rapid heartbeats.",
        "Clinical Findings": [
            "Sudden onset of rapid heartbeat",
            "ECG showing narrow QRS complexes"
        ],
        "Associated Conditions": [
            "Atrial fibrillation",
            "Atrial flutter"
        ],
        "Treatment Guidelines": [
            "Management according to guidelines for supraventricular tachycardia, including rate control and rhythm control strategies."
        ]
    },
    "713426002": {
        "Condition Name": "Inferior Myocardial Infarction",
        "Description": "A type of heart attack that affects the inferior (lower) part of the heart, typically due to blockage of the right coronary artery.",
        "Symptoms/Clinical Presentation": [
            "Chest pain radiating to the back or jaw",
            "Shortness of breath",
            "Nausea",
            "Bradycardia"
        ],
        "Risk Factors": [
            "Atherosclerosis",
            "Smoking",
            "Diabetes",
            "Hypertension"
        ],
        "Possible Causes": [
            "Blockage of the right coronary artery",
            "Thrombosis"
        ],
        "Diagnostic Criteria": [
            "ECG showing ST elevation in leads II, III, and aVF",
            "Elevated cardiac biomarkers"
        ],
        "Treatment Options": {
            "Medication": [
                "Thrombolytics",
                "Antiplatelet agents"
            ],
            "Procedures": [
                "Angioplasty",
                "Coronary artery bypass surgery"
            ],
            "Lifestyle Changes": [
                "Healthy diet",
                "Smoking cessation"
            ]
        },
        "Prognosis": "Varies depending on the extent of the heart muscle damage and the time to treatment.",
        "Prevention": [
            "Managing risk factors such as hypertension, diabetes, and cholesterol levels",
            "Regular exercise"
        ],
        "Additional Resources": [
            {
                "Title": "Inferior Myocardial Infarction Information",
                "Link": "https://www.heart.org/"
            }
        ],
        "SNOMED Code": "713426002",
        "Detailed Description": "A type of myocardial infarction that affects the lower part of the heart, often due to a blockage in the right coronary artery.",
        "Clinical Findings": [
            "ST elevation in leads II, III, and aVF",
            "Bradycardia due to vagal stimulation"
        ],
        "Associated Conditions": [
            "Right ventricular infarction",
            "Heart block"
        ],
        "Treatment Guidelines": [
            "Follow acute coronary syndrome management guidelines specific to inferior myocardial infarction."
        ]
    },
    "713427006": {
        "Condition Name": "Anterior Myocardial Infarction",
        "Description": "A type of heart attack that affects the anterior (front) part of the heart, typically due to blockage of the left anterior descending artery.",
        "Symptoms/Clinical Presentation": [
            "Severe chest pain",
            "Shortness of breath",
            "Sweating",
            "Nausea"
        ],
        "Risk Factors": [
            "High cholesterol",
            "Hypertension",
            "Smoking",
            "Diabetes"
        ],
        "Possible Causes": [
            "Atherosclerosis of the left anterior descending artery",
            "Blood clot"
        ],
        "Diagnostic Criteria": [
            "ECG showing ST elevation in leads V1-V4",
            "Elevated cardiac troponin levels"
        ],
        "Treatment Options": {
            "Medication": [
                "Aspirin",
                "Thrombolytics"
            ],
            "Procedures": [
                "Percutaneous coronary intervention (PCI)",
                "Coronary artery bypass grafting (CABG)"
            ],
            "Lifestyle Changes": [
                "Healthy eating",
                "Regular exercise"
            ]
        },
        "Prognosis": "Depends on the size of the infarct and the timeliness of treatment; anterior MIs are often more severe.",
        "Prevention": [
            "Control risk factors such as hypertension, diabetes, and high cholesterol",
            "Quit smoking"
        ],
        "Additional Resources": [
            {
                "Title": "Anterior Myocardial Infarction Information",
                "Link": "https://www.mayoclinic.org/"
            }
        ],
        "SNOMED Code": "713427006",
        "Detailed Description": "A myocardial infarction that occurs in the anterior part of the heart, often due to a blockage in the left anterior descending artery, leading to significant damage to the heart muscle.",
        "Clinical Findings": [
            "ST elevation in precordial leads (V1-V4)",
            "Signs of left ventricular dysfunction"
        ],
        "Associated Conditions": [
            "Left ventricular aneurysm",
            "Heart failure"
        ],
        "Treatment Guidelines": [
            "Adhere to acute coronary syndrome management protocols, with an emphasis on rapid reperfusion therapy."
        ]
    }
}
