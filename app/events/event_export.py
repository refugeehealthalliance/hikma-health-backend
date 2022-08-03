from events.event import Event
from admin_api.patient_data_import import PatientDataRow
import json


def get_field(data, field):
    if data.get(field) is None:
        return None
    return 'Yes' if data.get(field) else 'No'

def get_text_field(data, field, text_field):
    if data.get(field) is None:
        return None
    if data.get(field) is not None and not data.get(text_field):
        return 'Yes' if data.get(field) else 'No'
    return data.get(text_field) if data.get(field) else 'No'

def write_vitals_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.height = data.get('height')
    row.weight = data.get('weight')
    row.bmi = data.get('bmi')
    row.waist_circumference = data.get('waistCircumference')
    if data.get('systolic') and data.get('diastolic'):
        row.blood_pressure = f"{data.get('systolic')}/{data.get('diastolic')}"
    row.pulse = data.get('pulse')


def write_medical_hx_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.allergies = data.get('allergies')
    row.surgery_hx = data.get('surgeryHx')
    row.chronic_conditions = data.get('chronicConditions')
    row.current_medications = data.get('currentMedications')
    row.vaccinations = data.get('vaccinations')

def write_examination_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.examination_complaint = data.get('examinationComplaint')
    row.active_conditions = data.get('activeConditions')
    row.inactive_conditions = data.get('inactiveConditions')
    row.illness_history = data.get('treatment')

def write_med1_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.medication_1 = data.get('medication')
    row.type_1 = data.get('type')
    row.dosage_1 = data.get('dosage')
    row.days_1 = data.get('days')

def write_med2_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.medication_2 = data.get('medication')
    row.type_2 = data.get('type')
    row.dosage_2 = data.get('dosage')
    row.days_2 = data.get('days')

def write_med3_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.medication_3 = data.get('medication')
    row.type_3 = data.get('type')
    row.dosage_3 = data.get('dosage')
    row.days_3 = data.get('days')
		
def write_med4_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.medication_4 = data.get('medication')
    row.type_4 = data.get('type')
    row.dosage_4 = data.get('dosage')
    row.days_4 = data.get('days')

def write_med5_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.medication_5 = data.get('medication')
    row.type_5 = data.get('type')
    row.dosage_5 = data.get('dosage')
    row.days_5 = data.get('days')

def write_physiotherapy_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.previous_treatment = get_text_field(data, 'previousTreatment', 'previousTreatmentText')
    row.complaint_p = data.get('complaint')
    row.findings = data.get('findings')
    row.treatment_plan = data.get('treatmentPlan')
    row.treatment_session = data.get('treatmentSession')
    row.recommendations = data.get('recommendations')
    row.referral = get_text_field(data, 'referral', 'referralText')

def write_covid_19_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    if data.get('seekCare'):
        row.covid_19_result = 'Seek Emergency Care and Isolate'
    elif data.get('testAndIsolate'):
        row.covid_19_result = 'Test/Isolate Patient'  
    else:
        row.covid_19_result = 'No Action Necessary'    


def write_medicines_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.on_stain = data.get('onStain')
    row.stain_name_dose = data.get('stainNameDose')
    row.diabetes = data.get('diabetes')
    row.htn = data.get('htn')
    row.family_history = data.get('familyHistory')


def write_dm_history_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.diagnosis_age = data.get('diagnosisAge')
    row.dm_duration = data.get('dmDuration')
    row.diabetes_type = data.get('diabetesType')
    row.management = data.get('management')
    row.family_history = data.get('familyHistory')
    row.smoker = data.get('smoker')
    row.alcohol = data.get('alcohol')
    row.cardiac_problem = data.get('cardiacProblem')
    row.hf_sign = data.get('hfSign')
    row.hypertension = data.get('hypertension')
    row.renal_problem = data.get('renalProblem')
    row.eye_problem = data.get('eyeProblem')
    row.hypoglycemia_requiring = data.get('hypoglycemiaRequiring')
    row.dka = data.get('dka')
    row.myocardial = data.get('myocardial')
    row.cerebral_stroke = data.get('cerebral_stroke')
    row.limb_amputation = data.get('limb_amputation')
    row.erectile_dysfunction = data.get('erectile_dysfunction')
    row.retinal_examination = data.get('retinal_examination')


def write_clinical_examination_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.respiratory_system = data.get('respiratorySystem')
    row.respiratory_system_note = data.get('respiratorySystemNote')
    row.cvs = data.get('cvs')
    row.cvs_note = data.get('cvsNote')
    row.abdomen = data.get('abdomen')
    row.abdomen_note = data.get('abdomenNote')
    row.musculoskeletal = data.get('musculoskeletal')
    row.musculoskeletal_note = data.get('musculoskeletalNote')
    row.cns = data.get('cns')
    row.cns_note = data.get('cnsNote')


def write_foot_examination_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.rt_vibration = data.get('rtVibration')
    row.rt_monofilament = data.get('rtMonofilament')
    row.rt_distal_pulse = data.get('rtDistalPulse')
    row.rt_dorsalis_pulse = data.get('rtDorsalisPulse')
    row.rt_posterior_pulse = data.get('rtPosteriorPulse')
    row.left_vibration = data.get('leftVibration')
    row.left_monofilament = data.get('leftMonofilament')
    row.left_distal_pulse = data.get('leftDistalPulse')
    row.left_dorsalis_pulse = data.get('leftDorsalisPulse')
    row.left_posterior_pulse = data.get('leftPosteriorPulse')

def write_lab_investigation_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.hb_a1c = data.get('hbA1c')
    row.fating_glucose = data.get('fatingGlucose')
    row.random_glucose = data.get('randomGlucose')
    row.post_meal_glucose = data.get('postMealGlucose')
    row.creatinine = data.get('creatinine')
    row.egfr = data.get('egfr')
    row.total_cholesterol = data.get('totalCholesterol')
    row.ldl_cholesterol = data.get('ldlCholesterol')
    row.hdl = data.get('hdl')
    row.tg = data.get('tg')
    row.sodium = data.get('sodium')
    row.potassium = data.get('potassium')
    row.haemoglobin = data.get('haemoglobin')
    row.urinary_acr = data.get('urinaryAcr')
    row.dipstick_protein = data.get('dipstickProtein')
    row.urine_protein = data.get('urineProtein')
    row.urine_sugar = data.get('urineSugar')
    row.urine_microalbuminuria = data.get('urineMicroalbuminuria')
    row.urine_ketones = data.get('urineKetones')
    row.ecg = data.get('ecg')
    row.other_investigations = data.get('otherInvestigations')

def write_ophthalmology_examination_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.rt_dilated_fundoscopy = data.get('rtDilatedFundoscopy')
    row.rt_ophthalmologist = data.get('rtOphthalmologist')
    row.rt_retinal_camera = data.get('rtRetinalCamera')
    row.rt_findings = data.get('rtFindings')
    row.left_dilated_fundoscopy = data.get('leftDilatedFundoscopy')
    row.left_ophthalmologist = data.get('leftOphthalmologist')
    row.left_retinal_camera = data.get('leftRetinalCamera')
    row.left_findings = data.get('leftFindings')


def write_endocrinologist_cases_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.indications = data.get('indications')
    row.feedback = data.get('feedback')
    row.diabetes_education = data.get('diabetesEducation')


def write_referrals_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.diabetic_educator = data.get('diabeticEducator')
    row.dietitian = data.get('dietitian')
    row.ophthalmologist = data.get('ophthalmologist')
    row.foot_care_clinic = data.get('footCareClinic')
    row.social_services = data.get('socialServices')
    row.psychologist = data.get('psychologist')


