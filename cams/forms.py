from django import forms
from crispy_forms import helper, layout, bootstrap

five_point_scale = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)

five_scale_explanation = layout.HTML("""
    <div class="five_scale_explanation card">
    <div class="card-header">How well did the lecturer accomplish their objectives?</div>
    <div class="card-body">
        <p>1 = Did not accomplish</p>
        <p>2 = Poor</p>
        <p>3 = OK</p>
        <p>4 = Very Good</p>
        <p>5 = Excellent</p>
    </div>
    </div>""")

html_separator = layout.HTML("""<div class="separator"><hr /></div>""")

id_field = layout.HTML("""<input type="hidden" name="contact_uuid" value="{{ contact_uuid }}" />""")

yes_no_choices = (
    ("1", "Yes"),
    ("0", "No")
)

class latbWedForm(forms.Form):
    suturing_q1 = forms.ChoiceField(
        label = "Identify components of evaluating lacerations including listing indications for suturing.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    suturing_q2 = forms.ChoiceField(
        label = "Selection of appropriate equipment and anesthesia.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    suturing_q3 = forms.ChoiceField(
        label = "Describe wound care.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    suturing_q4 = forms.ChoiceField(
        label = "Practice and demonstrate simple and advanced suturing.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    suturing_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea
    )
    
    headaches_q1 = forms.ChoiceField(
        label = "Describe diagnostic criteria for different headaches.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    headaches_q2 = forms.ChoiceField(
        label = "Discuss appropriate diagnostic testing and imaging.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    headaches_q3 = forms.ChoiceField(
        label = "Explain pharmaceutical and non-pharmaceutical treatments for headaches.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    headaches_q4 = forms.ChoiceField(
        label = "List challenges encountered when treating pediatric migraines.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    headaches_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea
    )

    bias_bool = forms.ChoiceField(
        label = "Did you find any bias in these lectures?",
        choices = yes_no_choices,
        widget = forms.RadioSelect
    )
    bias_comments = forms.CharField(
        label = "If Yes, what did you consider bias?",
        widget = forms.Textarea
    )
    will_this_info_change_you = forms.ChoiceField(
        label = "Will the information provided change the way you practice?",
        choices = yes_no_choices,
        widget = forms.RadioSelect
    )
    workshop_suggestions = forms.CharField(
        label = "Workshop suggestions for 2023 Lecture at the Beach",
        widget = forms.Textarea
    )
    e_signature = forms.CharField(
        label = "Signature of Attendee (please type in your name)",
        required = True
    )
    day = forms.CharField(initial="Wednesday")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = helper.FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit'
        self.helper.field_class = 'form-control'
        self.helper.layout = layout.Layout(
            layout.Field('day', type="hidden"),
            id_field,
            layout.Fieldset(
                'Angel Sheridan, FNP (Suturing) <hr />',
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('suturing_q1'),
                        bootstrap.InlineRadios('suturing_q2'),
                        bootstrap.InlineRadios('suturing_q3'),
                        bootstrap.InlineRadios('suturing_q4'),
                        'suturing_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox'
                )
            ),
            html_separator,
            layout.Fieldset(
                'Heather Norton, ACNP-BC (Headaches - diagnosis and treatment) <hr />',
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('headaches_q1'),
                        bootstrap.InlineRadios('headaches_q2'),
                        bootstrap.InlineRadios('headaches_q3'),
                        bootstrap.InlineRadios('headaches_q4'),
                        'headaches_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox'
                ),
            ),
            html_separator,
            layout.Fieldset(
                'Other remarks',
                bootstrap.InlineRadios('bias_bool'),
                'bias_comments',
                bootstrap.InlineRadios('will_this_info_change_you'),
                'workshop_suggestions'
            ),
            layout.Fieldset(
                'Signature',
                layout.HTML("<p>By signing, I attest that I have attended the above programs in full, or for time indicated if I did not attend the full session."),
                'e_signature',
                layout.HTML("<p>A certificate will be emailed to {{ user.content.email }}.<p>")
            ),
            layout.Submit('Submit', 'SUBMIT')
        )

class latbThursForm(forms.Form):
    diabetes_q1 = forms.ChoiceField(
        label = "List two continuous glucose monitors (CGM) and insulin pumps available.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    diabetes_q2 = forms.ChoiceField(
        label = "List advantages of utilizing insulin pumps and CGM to mitigate glycemic variability.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    diabetes_q3 = forms.ChoiceField(
        label = "Describe use of reports from these devices in improving glycemic control.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    diabetes_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea
    )

    trafficking_q1 = forms.ChoiceField(
        label = "Define human trafficking.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    trafficking_q2 = forms.ChoiceField(
        label = "Identify victims of human trafficking.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    trafficking_q3 = forms.ChoiceField(
        label = "List interventions including appropriate reporting of human trafficking.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    trafficking_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea
    )

    hospice_q1 = forms.ChoiceField(
        label = "Discuss the philosophy of hospice.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    hospice_q2 = forms.ChoiceField(
        label = "Cite the four levels of hospice care.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    hospice_q3 = forms.ChoiceField(
        label = "Identify major symptoms of patients in the inpatient and outpatient hospice settings.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    hospice_q4 = forms.ChoiceField(
        label = "Apply pharmacotherapeutics (controlled and noncontrolled) in managing hospice patients with acute and chronic symptoms.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    hospice_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea
    )

    policy_q1 = forms.ChoiceField(
        label = "Discuss the legislative process.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    policy_q2 = forms.ChoiceField(
        label = "List the significant changes affecting APRN practice.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    policy_q3 = forms.ChoiceField(
        label = "Describe the requirements for the APRN-physician practice agreement.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    trafficking_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea
    )

    substance_q1 = forms.ChoiceField(
        label = "Define substance use disorder as a treatable disease.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    substance_q2 = forms.ChoiceField(
        label = "List treatments including medication-assisted therapy.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    substance_q3 = forms.ChoiceField(
        label = "Discuss harm reduction interventions.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    substance_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea
    )

    pelvic_q1 = forms.ChoiceField(
        label = "Differentiate between the main causes of urinary incontinence.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    pelvic_q2 = forms.ChoiceField(
        label = "Outline the treatment pathway of both stress and urgency urinary incontinence.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    pelvic_q3 = forms.ChoiceField(
        label = "Explain the diagnosis and treatment of pelvic organ prolapse.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    pelvic_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea
    )

    bias_bool = forms.ChoiceField(
        label = "Did you find any bias in these lectures?",
        choices = yes_no_choices,
        widget = forms.RadioSelect
    )
    bias_comments = forms.CharField(
        label = "If Yes, what did you consider bias?",
        widget = forms.Textarea
    )
    will_this_info_change_you = forms.ChoiceField(
        label = "Will the information provided change the way you practice?",
        choices = yes_no_choices,
        widget = forms.RadioSelect
    )
    workshop_suggestions = forms.CharField(
        label = "Workshop suggestions for 2023 Lecture at the Beach",
        widget = forms.Textarea
    )
    e_signature = forms.CharField(
        label = "Signature of Attendee (please type in your name)",
        required = True
    )
    day = forms.CharField(initial="Thursday")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = helper.FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit'
        self.helper.field_class = 'form-control'
        self.helper.layout = layout.Layout(
            layout.Field('day', type="hidden"),
            id_field,
            layout.Fieldset(
                'Eileen Egan, DNP (Diabetes) <hr />',
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('diabetes_q1'),
                        bootstrap.InlineRadios('diabetes_q2'),
                        bootstrap.InlineRadios('diabetes_q3'),
                        'diabetes_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox'
                )
            ),
            html_separator,
            layout.Fieldset(
                'Chandra Cleveland, LEO (Human Trafficking) <hr />',
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('trafficking_q1'),
                        bootstrap.InlineRadios('trafficking_q2'),
                        bootstrap.InlineRadios('trafficking_q3'),
                        'trafficking_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox'
                ),
            ),
            html_separator,
            layout.Fieldset(
                'Stephanie Burgess, PhD, APRN (Hospice) <hr />',
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('hospice_q1'),
                        bootstrap.InlineRadios('hospice_q2'),
                        bootstrap.InlineRadios('hospice_q3'),
                        bootstrap.InlineRadios('hospice_q4'),
                        'hospice_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox'
                ),
            ),
            html_separator,
            layout.Fieldset(
                'Stephanie Burgess, PhD, APRN (Policy and Political Update) <hr />',
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('policy_q1'),
                        bootstrap.InlineRadios('policy_q2'),
                        bootstrap.InlineRadios('policy_q3'),
                        'policy_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox'
                ),
            ),
            html_separator,
            layout.Fieldset(
                'Victor Archambeau, MD (Treating Substance Use Disorder) <hr />',
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('substance_q1'),
                        bootstrap.InlineRadios('substance_q2'),
                        bootstrap.InlineRadios('substance_q3'),
                        'substance_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox'
                ),
            ),
            html_separator,
            layout.Fieldset(
                'Annaceci Peacher-Holderied, MD (Female Pelvic Medicine) <hr />',
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('pelvic_q1'),
                        bootstrap.InlineRadios('pelvic_q2'),
                        bootstrap.InlineRadios('pelvic_q3'),
                        'pelvic_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox'
                ),
            ),
            html_separator,
            layout.Fieldset(
                'Other remarks',
                bootstrap.InlineRadios('bias_bool'),
                'bias_comments',
                bootstrap.InlineRadios('will_this_info_change_you'),
                'workshop_suggestions'
            ),
            layout.Fieldset(
                'Signature',
                layout.HTML("<p>By signing, I attest that I have attended the above programs in full, or for time indicated if I did not attend the full session."),
                'e_signature',
                layout.HTML("<p>A certificate will be emailed to {{ user.content.email }}.<p>")
            ),
            layout.Submit('Submit', 'SUBMIT')
        )

class latbFriForm(forms.Form):
    newdrug_q1 = forms.ChoiceField(
        label = "Identify medications that were FDA approved and made available last year.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    newdrug_q2 = forms.ChoiceField(
        label = "List each medication's indication, dosing, potential adverse effects, place in therapy, and unique characteristics.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    newdrug_q3 = forms.ChoiceField(
        label = "Devise a strategy to implement relevant new clinical treatment guidelines that were published last year.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    newdrug_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea
    )


    coding_q1 = forms.ChoiceField(
        label = "Know the difference between shared and incident-to visits.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    coding_q2 = forms.ChoiceField(
        label = "State the new quality measures related to care transitions, hypertension management, and ED follow-up.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    coding_q3 = forms.ChoiceField(
        label = "Describe how to correctly document, code, and bill for these services.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    coding_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea
    )
    
    thyroid_q1 = forms.ChoiceField(
        label = "Differentiate various patterns of thyroid nodules found on ultrasound.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    thyroid_q2 = forms.ChoiceField(
        label = "Apply the Bethesda system of reporting thyroid cytology.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    thyroid_q3 = forms.ChoiceField(
        label = "Discuss the role of molecular markers when treating thyroid disease.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    thyroid_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea
    )

    covid_q1 = forms.ChoiceField(
        label = "Discuss the biology of the SARS-CoV-2 virus.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    covid_q2 = forms.ChoiceField(
        label = "List current evidence-based treatments for COVID-19.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    covid_q3 = forms.ChoiceField(
        label = "Explain diagnostic testing.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    covid_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea
    )
    
    bias_bool = forms.ChoiceField(
        label = "Did you find any bias in these lectures?",
        choices = yes_no_choices,
        widget = forms.RadioSelect
    )
    bias_comments = forms.CharField(
        label = "If Yes, what did you consider bias?",
        widget = forms.Textarea
    )
    will_this_info_change_you = forms.ChoiceField(
        label = "Will the information provided change the way you practice?",
        choices = yes_no_choices,
        widget = forms.RadioSelect
    )
    workshop_suggestions = forms.CharField(
        label = "Workshop suggestions for 2023 Lecture at the Beach",
        widget = forms.Textarea
    )
    e_signature = forms.CharField(
        label = "Signature of Attendee (please type in your name)",
        required = True
    )
    day = forms.CharField(initial="Friday")
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = helper.FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit'
        self.helper.field_class = 'form-control'
        self.helper.layout = layout.Layout(
            layout.Field('day', type="hidden"),
            id_field,
            layout.Fieldset(
                'Andrew Mardis, PharmD (New Drug Update)<hr />',
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('newdrug_q1'),
                        bootstrap.InlineRadios('newdrug_q2'),
                        bootstrap.InlineRadios('newdrug_q3'),
                        'newdrug_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox'
                )
            ),
            html_separator,
            layout.Fieldset(
                'Nick Ulmer, MD (Coding) <hr />',
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('coding_q1'),
                        bootstrap.InlineRadios('coding_q2'),
                        bootstrap.InlineRadios('coding_q3'),
                        'coding_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox'
                ),
            ),
            html_separator,
            layout.Fieldset(
                'Gauri Dhir, MD (Thyroid Nodules and Molecular Markers) <hr />',
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('thyroid_q1'),
                        bootstrap.InlineRadios('thyroid_q2'),
                        bootstrap.InlineRadios('thyroid_q3'),
                        'thyroid_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox'
                ),
            ),
            html_separator,
            layout.Fieldset(
                'R. Andrew Philipp, MD (COVID-19 Update) <hr />',
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('covid_q1'),
                        bootstrap.InlineRadios('covid_q2'),
                        bootstrap.InlineRadios('covid_q3'),
                        'covid_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox'
                ),
            ),
            html_separator,
            layout.Fieldset(
                'Other remarks',
                bootstrap.InlineRadios('bias_bool'),
                'bias_comments',
                bootstrap.InlineRadios('will_this_info_change_you'),
                'workshop_suggestions'
            ),
            layout.Fieldset(
                'Signature',
                layout.HTML("<p>By signing, I attest that I have attended the above programs in full, or for time indicated if I did not attend the full session."),
                'e_signature',
                layout.HTML("<p>A certificate will be emailed to {{ user.content.email }}.<p>")
            ),
            layout.Submit('Submit', 'SUBMIT')
        )



class latbSatForm(forms.Form):
    naltrexone_q1 = forms.ChoiceField(
        label = "List the indications for prescribing LDN.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    naltrexone_q2 = forms.ChoiceField(
        label = "Discuss the appropriate dosing and pharmacodynamics of LDN.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    naltrexone_q3 = forms.ChoiceField(
        label = "Describe how LDN can act as an immunomodulator.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    naltrexone_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea
    )


    chf_q1 = forms.ChoiceField(
        label = "Define the stages of congestive heart failure.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    chf_q2 = forms.ChoiceField(
        label = "List pharmacologic treatments for CHF according to current guidelines.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    chf_q3 = forms.ChoiceField(
        label = "Describe risk factors for developing CHF.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    chf_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea
    )
    
    cancer_q1 = forms.ChoiceField(
        label = "List strategies for improved breast health and cancer prevention.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    cancer_q2 = forms.ChoiceField(
        label = "Discuss the newest surgical strategies for breast lesion.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    cancer_q3 = forms.ChoiceField(
        label = "Discuss the current medical and oncologic treatments for breast cancer.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    cancer_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea
    )

    ptsd_q1 = forms.ChoiceField(
        label = "List the diagnostic criteria for PTSD.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    ptsd_q2 = forms.ChoiceField(
        label = "Describe how the COVID-19 pandemic has affected the rate and presentation of PTSD.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    ptsd_q3 = forms.ChoiceField(
        label = "Identify pharmaceutical and non-pharmaceutical therapies to treat PTSD.",
        choices = five_point_scale,
        widget = forms.RadioSelect
    )
    ptsd_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea
    )
    
    bias_bool = forms.ChoiceField(
        label = "Did you find any bias in these lectures?",
        choices = yes_no_choices,
        widget = forms.RadioSelect
    )
    bias_comments = forms.CharField(
        label = "If Yes, what did you consider bias?",
        widget = forms.Textarea
    )
    will_this_info_change_you = forms.ChoiceField(
        label = "Will the information provided change the way you practice?",
        choices = yes_no_choices,
        widget = forms.RadioSelect
    )
    workshop_suggestions = forms.CharField(
        label = "Workshop suggestions for 2023 Lecture at the Beach",
        widget = forms.Textarea
    )
    e_signature = forms.CharField(
        label = "Signature of Attendee (please type in your name)",
        required = True
    )
    day = forms.CharField(initial="Friday")
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = helper.FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit'
        self.helper.field_class = 'form-control'
        self.helper.layout = layout.Layout(
            layout.Field('day', type="hidden"),
            id_field,
            layout.Fieldset(
                'Yusuf Saleeby, MD (Low Dose Naltrexone) <hr />',
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('naltrexone_q1'),
                        bootstrap.InlineRadios('naltrexone_q2'),
                        bootstrap.InlineRadios('naltrexone_q3'),
                        'naltrexone_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox'
                )
            ),
            html_separator,
            layout.Fieldset(
                'Nitesh Ainani, MD (CHF) <hr />',
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('chf_q1'),
                        bootstrap.InlineRadios('chf_q2'),
                        bootstrap.InlineRadios('chf_q3'),
                        'chf_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox'
                ),
            ),
            html_separator,
            layout.Fieldset(
                'Craig Brackett, MD/FACS (Advancing Diagnosis and Treatment in Breast Cancer) <hr />',
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('cancer_q1'),
                        bootstrap.InlineRadios('cancer_q2'),
                        bootstrap.InlineRadios('cancer_q3'),
                        'cancer_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox'
                ),
            ),
            html_separator,
            layout.Fieldset(
                'Kelly Holes-Lewis, MD (PTSD and Provider Well-Being) <hr />',
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('ptsd_q1'),
                        bootstrap.InlineRadios('ptsd_q2'),
                        bootstrap.InlineRadios('ptsd_q3'),
                        'ptsd_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox'
                ),
            ),
            html_separator,
            layout.Fieldset(
                'Other remarks',
                bootstrap.InlineRadios('bias_bool'),
                'bias_comments',
                bootstrap.InlineRadios('will_this_info_change_you'),
                'workshop_suggestions'
            ),
            layout.Fieldset(
                'Signature',
                layout.HTML("<p>By signing, I attest that I have attended the above programs in full, or for time indicated if I did not attend the full session."),
                'e_signature',
                layout.HTML("<p>A certificate will be emailed to {{ user.content.email }}.<p>")
            ),
            layout.Submit('Submit', 'SUBMIT')
        )