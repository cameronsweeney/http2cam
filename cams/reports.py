from urllib import response
from django.template.response import TemplateResponse
from django.http import JsonResponse
from rest_framework import generics
from .models import CamsFormResponse
from .permissions import CamsAppPermission

workshop_slugs = {
    'suturing': [
        "Angel Sheridan, FNP (Suturing)",
        "Identify components of evaluating lacerations including listing indications for suturing.",
        "Selection of appropriate equipment and anesthesia.",
        "Describe wound care.",
        "Practice and demonstrate simple and advanced suturing."
    ],
    'headaches': [
        "Heather Norton, ACNP-BC (Headaches - diagnosis and treatment)",
        "Describe diagnostic criteria for different headaches.",
        "Discuss appropriate diagnostic testing and imaging.",
        "Explain pharmaceutical and non-pharmaceutical treatments for headaches.",
        "List challenges encountered when treating pediatric migraines.",
    ],
    'diabetes': [
        "Eileen Egan, DNP (Diabetes)",
        "List two continuous glucose monitors (CGM) and two insulin pumps available.",
        "List advantages of utilizing insulin pumps and CGM to mitigate glycemic variability.",
        "Describe use of reports from these devices in improving glycemic control.",
    ],
    'trafficking': [
        "Chandra Cleveland, LEO (Human Trafficking)",
        "Define human trafficking.",
        "Identify victims of human trafficking.",
        "List interventions including appropriate reporting of human trafficking.",
    ],
    'hospice': [
        "Stephanie Burgess, PhD, APRN (Hospice)",
        "Discuss the philosophy of hospice.",
        "Cite the four levels of hospice care.",
        "Identify major symptoms of patients in the inpatient and outpatient hospice settings.",
        "Apply pharmacotherapeutics (controlled and noncontrolled) in managing hospice patients with acute and chronic symptoms.",
    ],
    'policy': [
        "Stephanie Burgess, PhD, APRN (Policy and Political Update)",
        "Discuss the legislative process.",
        "List the significant changes affecting APRN practice.",
        "Describe the requirements for the APRN-physician practice agreement.",
    ],
    'substance': [
        "Victor Archambeau, MD (Treating Substance Use Disorder)",
        "Define substance use disorder as a treatable disease.",
        "List treatments including medication-assisted therapy.",
        "Discuss harm reduction interventions.",
    ],
    'pelvic': [
        "Annaceci Peacher-Holderied, MD (Female Pelvic Medicine)",
        "Differentiate between the main causes of urinary incontinence.",
        "Outline the treatment pathway of both stress and urgency urinary incontinence.",
        "Explain the diagnosis and treatment of pelvic organ prolapse.",
    ],
    'newdrug': [
        "Andrew Mardis, PharmD (New Drug Update)",
        "Identify medications that were FDA approved and made available last year.",
        "List each medication's indication, dosing, potential adverse effects, place in therapy, and unique characteristics.",
        "Devise a strategy to implement relevant new clinical treatment guidelines that were published last year.",
    ],
    'coding': [
        "Nick Ulmer, MD (Coding)",
        "Know the difference between shared and incident-to visits.",
        "State the new quality measures related to care transitions, hypertension management, and ED follow-up.",
        "Describe how to correctly document, code, and bill for these services.",
    ],
    'thyroid': [
        "Gauri Dhir, MD (Thyroid Nodules and Molecular Markers)",
        "Differentiate various patterns of thyroid nodules found on ultrasound.",
        "Apply the Bethesda system of reporting thyroid cytology.",
        "Discuss the role of molecular markers when treating thyroid disease.",
    ],
    'covid': [
        "R. Andrew Philipp, MD (COVID-19 Update)",
        "Discuss the biology of the SARS-CoV-2 virus.",
        "List current evidence-based treatments for COVID-19.",
        "Explain diagnostic testing.",
    ],
    'naltrexone': [
        "Yusuf Saleeby, MD (Low Dose Naltrexone)",
        "List the indications for prescribing LDN.",
        "Discuss the appropriate dosing and pharmacodynamics of LDN.",
        "Describe how LDN can act as an immunomodulator.",
    ],
    'chf': [
        "Nitesh Ainani, MD (CHF)",
        "Define the stages of congestive heart failure.",
        "List pharmacologic treatments for CHF according to current guidelines.",
        "Describe risk factors for developing CHF.",
    ],
    'cancer': [
        "Craig Brackett, MD/FACS (Advancing Diagnosis and Treatment in Breast Cancer)",
        "List strategies for improved breast health and cancer prevention.",
        "Discuss the newest surgical strategies for breast lesion.",
        "Discuss the current medical and oncologic treatments for breast cancer.",
    ],
    'ptsd': [
        "Kelly Holes-Lewis, MD (PTSD and Provider Well-Being)",
        "List the diagnostic criteria for PTSD.",
        "Describe how the COVID-19 pandemic has affected the rate and presentation of PTSD.",
        "Identify pharmaceutical and non-pharmaceutical therapies to treat PTSD.",
    ],
}

def intOrNone(possible_int):
    if possible_int is None:
        return 0
    else:
        return int(possible_int)

def prep_workshop_evals(workshop_name, response_data):
    response_data[workshop_name] = {
        'workshop_title': workshop_slugs[workshop_name][0],
        'comments': [],
        'questions': [{}]
    }
    for question_no in range(1, len(workshop_slugs[workshop_name])):
        response_data[workshop_name]['questions'].append({
            'objective': workshop_slugs[workshop_name][question_no],
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0
        })
    return response_data

def parse_workshop_evals(workshop_name, form_response, response_data):
    if not form_response.get(workshop_name+'_attendance'):
        return response_data
    if form_response.get(workshop_name+'_comments'):
        response_data[workshop_name]['comments'].append(form_response[workshop_name+'_comments'])
    for question_no in range(1, len(workshop_slugs[workshop_name])):
        score = intOrNone(form_response.get(workshop_name+'_q'+str(question_no)))
        response_data[workshop_name]['questions'][question_no][score] += 1
    return response_data

def calculate_average(question_dict):
    score_sum = question_dict[1] + 2*question_dict[2] + 3*question_dict[3] + 4*question_dict[4] + 5*question_dict[5]
    total = question_dict[1] + question_dict[2] + question_dict[3] + question_dict[4] + question_dict[5]
    return (score_sum / total)

class LatbEvalReportView(generics.ListAPIView):
    queryset = CamsFormResponse.objects.all()
    permission_classes = [CamsAppPermission]

    def get(self, request, *args, **kwargs):
        self.check_object_permissions(self.request, 'latb22')

        response_data = {}
        
        general_data = {
            'bias_bool': [0, 0],
            'bias_comments': [],
            'will_this_info_change_you': [0, 0],
            'workshop_suggestions': [],
        }

        for workshop in workshop_slugs.keys():
            response_data = prep_workshop_evals(workshop, response_data)

        for form_response_dict in self.queryset.values():
            form_response = form_response_dict['response_data']
            #print(form_response_dict)

            for workshop in workshop_slugs.keys():
                response_data = parse_workshop_evals(workshop, form_response, response_data)

            if form_response.get('bias_comments'):
                general_data['bias_comments'].append(form_response['bias_comments'])

            if form_response.get('workshop_suggestions'):
                general_data['workshop_suggestions'].append(form_response['workshop_suggestions'])

            if form_response.get('bias_bool') is not None:
                general_data['bias_bool'][int(form_response['bias_bool'])] += 1

            if form_response.get('will_this_info_change_you') is not None:
                general_data['will_this_info_change_you'][int(form_response['will_this_info_change_you'])] += 1

        general_data['bias'] = general_data['bias_bool'][0] / (general_data['bias_bool'][0] + general_data['bias_bool'][1])              
        for workshop in workshop_slugs.keys():
            for question_no in range(1, len(workshop_slugs[workshop])):
                response_data[workshop]['questions'][question_no]['average'] = calculate_average(response_data[workshop]['questions'][question_no])
        
        data_to_return = {
            'workshops': response_data,
            'other': general_data
        }

        if 'json' in request.GET:
            return JsonResponse(data_to_return, safe=False)
        return TemplateResponse(request, 'evaluation_data.html', data_to_return)