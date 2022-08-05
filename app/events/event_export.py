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
    row.heart_rate = data.get('heartRate')
    if data.get('systolic') and data.get('diastolic'):
        row.blood_pressure = f"{data.get('systolic')}/{data.get('diastolic')}"
    row.sats = data.get('sats')
    row.temp = data.get('temp')
    row.respiratory_rate = data.get('respiratoryRate')
    row.weight = data.get('weight')
    row.blood_glucose = data.get('bloodGlucose')

def write_medical_hx_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.allergies = data.get('allergies')
    row.surgery_hx = data.get('surgeryHx')
    row.chronic_conditions = data.get('chronicConditions')
    row.current_medications = data.get('currentMedications')
    row.vaccinations = data.get('vaccinations')

def write_examination_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.examination = data.get('examination')
    row.general_observations = data.get('generalObservations')
    row.diagnosis = data.get('diagnosis')
    row.treatment = data.get('treatment')
    row.covid_19 = get_field(data, 'covid19')
    row.referral = get_text_field(data, 'referral', 'referralText')

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

def write_mental_health_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.in_person = data.get('InPerson')
    row.tele = data.get('tele')
    row.female_only = data.get('femaleOnly')
    row.go_clinic = data.get('goClinic')
    row.mental_other = data.get('mentalOther')
    row.acupuncture = data.get('acupuncture')
    row.send_audio = data.get('sendAudio')
    row.psychiatry = data.get('psychiatry')
    row.refill = data.get('refill')
    row.taking_regularly = data.get('takingRegularly')
    row.concerns_followup = data.get('concernsFollowup')
    row.last_follow_up_date = data.get('lastFollowUpDate')
    row.feeling_nervous = data.get('feelingNervous')
    row.no_control_worrying = data.get('noControlWorrying')
    row.little_interest = data.get('littleInterest')
    row.feeling_down = data.get('feelingDown')
    row.cant_sleep = data.get('cantSleep')
    row.dont_feel_safe_living = data.get('dontFeelSafeLiving')
    row.how_you_feel = data.get('howYouFeel')
    row.child_body_feeling = data.get('childBodyFeeling')
    row.child_away_from_people = data.get('childAwayFromPeople')
    row.child_feeling_happy = data.get('childFeelingHappy')
    row.child_trouble_sleeping = data.get('childTroubleSleeping')
    row.child_hard_pay_attention = data.get('childHardPayAttention')
    row.child_feels_alone = data.get('childFeelsAlone')
    row.body_feelings = data.get('bodyFeelings')
    row.away_from_people = data.get('awayFromPeople')
    row.feeling_happy = data.get('feelingHappy')
    row.trouble_sleeping = data.get('troubleSleeping')
    row.hard_pay_attention = data.get('hardPayAttention')
    row.feel_alone = data.get('feelAlone')
    row.past_week_stress = data.get('pastWeekStress')


def write_interventions_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.resource_connection = data.get('resourceConnection')
    row.resource_connection_specify = data.get('resourceConnectionSpecify')
    row.active_listening = data.get('activeListening')
    row.psychoeducation = data.get('psychoeducation')
    row.sleep_hygiene = data.get('sleepHygiene')
    row.safe_space_imagine = data.get('safeSpaceImagine')
    row.muscle_relaxation = data.get('muscleRelaxation')
    row.behavioral_activation = data.get('behavioralActivation')
    row.grief_letter = data.get('griefLetter')
    row.changing_thoughts = data.get('changingThoughts')
    row.senses = data.get('senses')
    row.distraction_techniques = data.get('distractionTechniques')
    row.diary_yourself = data.get('diaryYourself')
    row.chair_technique = data.get('chairTechnique')
    row.build_strengths = data.get('buildStrengths')
    row.motivational_interviewing = data.get('motivationalInterviewing')
    row.diaphragmatic_breathing = data.get('diaphragmaticBreathing')
    row.safety_plan = data.get('safetyPlan')
    row.interpersonal_communication = data.get('interpersonalCommunication')
    row.prayer = data.get('prayer')
    row.supportive_people = data.get('supportivePeople')
    row.other_strategies = data.get('otherStrategies')
    row.psychiatric_medications = data.get('psychiatricMedications')


def write_common_problems_event(row: PatientDataRow, event):
    data = json.loads(event.event_metadata)
    row.difficulty_eating = data.get('difficultyEating')
    row.suicidal_ideation = data.get('suicidalIdeation')
    row.difficulty_sleeping = data.get('difficultySleeping')
    row.hours_slept = data.get('hoursSlept')
    row.sleeping_night = data.get('sleepingNight')
    row.sleeping_falling = data.get('sleepingFalling')
    row.sleeping_walking = data.get('sleepingWalking')
    row.restless = data.get('restless')
    row.difficulty_stopping_worrying = data.get('difficultyStoppingWorrying')
    row.body_aches = data.get('bodyAches')
    row.body_aches_where = data.get('bodyAchesWhere')
    row.low_energy = data.get('lowEnergy')
    row.no_interest = data.get('noInterest')
    row.guilt = data.get('guilt')
    row.hopeless = data.get('hopeless')
    row.flashbacks = data.get('flashbacks')
    row.hypervigilance = data.get('hypervigilance')
    row.sad_irritable = data.get('sadIrritable')
    row.hallucinations = data.get('hallucinations')
    row.potential_diagnosis = data.get('potentialDiagnosis')
    row.other_symptom = data.get('otherSymptom')
    row.bed_wetting = data.get('bedWetting')
    row.defiant = data.get('defiant')
    row.separation_anxiety = data.get('separationAnxiety')
    row.communication_difficulties = data.get('communicationDifficulties')
