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
    suturing_attendance = forms.ChoiceField(
        label = "I attended this workshop",
        widget = forms.CheckboxInput,
        required = False
    )
    suturing_q1 = forms.ChoiceField(
        label = "Identify components of evaluating lacerations including listing indications for suturing.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    suturing_q2 = forms.ChoiceField(
        label = "Selection of appropriate equipment and anesthesia.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    suturing_q3 = forms.ChoiceField(
        label = "Describe wound care.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    suturing_q4 = forms.ChoiceField(
        label = "Practice and demonstrate simple and advanced suturing.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    suturing_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea,
        required = False
    )
    
    headaches_attendance = forms.ChoiceField(
        label = "I attended this workshop",
        widget = forms.CheckboxInput,
        required = False
    )
    headaches_q1 = forms.ChoiceField(
        label = "Describe diagnostic criteria for different headaches.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    headaches_q2 = forms.ChoiceField(
        label = "Discuss appropriate diagnostic testing and imaging.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    headaches_q3 = forms.ChoiceField(
        label = "Explain pharmaceutical and non-pharmaceutical treatments for headaches.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    headaches_q4 = forms.ChoiceField(
        label = "List challenges encountered when treating pediatric migraines.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    headaches_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea,
        required = False
    )

    bias_bool = forms.ChoiceField(
        label = "Did you find any bias in these lectures?",
        choices = yes_no_choices,
        widget = forms.RadioSelect
    )
    bias_comments = forms.CharField(
        label = "If Yes, what did you consider bias?",
        widget = forms.Textarea,
        required = False
    )
    will_this_info_change_you = forms.ChoiceField(
        label = "Will the information provided change the way you practice?",
        choices = yes_no_choices,
        widget = forms.RadioSelect
    )
    workshop_suggestions = forms.CharField(
        label = "Workshop suggestions for 2023 Lecture at the Beach",
        widget = forms.Textarea,
        required = False
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
                layout.Field(
                    'suturing_attendance',
                    type = 'checkbox',
                    id = 'suturing_attendance',
                    wrapper_class = 'form-switch',
                    data_bs_toggle = 'collapse',
                    data_bs_target = '#collapse_suturing'
                ),
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
                    css_class = 'workshop_flexbox collapse',
                    css_id = 'collapse_suturing'
                )
            ),
            html_separator,
            layout.Fieldset(
                'Heather Norton, ACNP-BC (Headaches - diagnosis and treatment) <hr />',
                layout.Field(
                    'headaches_attendance',
                    type = 'checkbox',
                    id = 'headaches_attendance',
                    wrapper_class = 'form-switch',
                    data_bs_toggle = 'collapse',
                    data_bs_target = '#collapse_headaches'
                ),
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
                    css_class = 'workshop_flexbox collapse',
                    css_id = 'collapse_headaches'
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
                'e_signature'
            ),
            layout.Submit('Submit', 'SUBMIT')
        )

class latbThursForm(forms.Form):
    diabetes_attendance = forms.ChoiceField(
        label = "I attended this workshop",
        widget = forms.CheckboxInput,
        required = False
    )
    diabetes_q1 = forms.ChoiceField(
        label = "List two continuous glucose monitors (CGM) and two insulin pumps available.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    diabetes_q2 = forms.ChoiceField(
        label = "List advantages of utilizing insulin pumps and CGM to mitigate glycemic variability.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    diabetes_q3 = forms.ChoiceField(
        label = "Describe use of reports from these devices in improving glycemic control.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    diabetes_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea,
        required = False
    )

    trafficking_attendance = forms.ChoiceField(
        label = "I attended this workshop",
        widget = forms.CheckboxInput,
        required = False
    )
    trafficking_q1 = forms.ChoiceField(
        label = "Define human trafficking.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    trafficking_q2 = forms.ChoiceField(
        label = "Identify victims of human trafficking.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    trafficking_q3 = forms.ChoiceField(
        label = "List interventions including appropriate reporting of human trafficking.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    trafficking_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea,
        required = False
    )

    hospice_attendance = forms.ChoiceField(
        label = "I attended this workshop",
        widget = forms.CheckboxInput,
        required = False
    )
    hospice_q1 = forms.ChoiceField(
        label = "Discuss the philosophy of hospice.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    hospice_q2 = forms.ChoiceField(
        label = "Cite the four levels of hospice care.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    hospice_q3 = forms.ChoiceField(
        label = "Identify major symptoms of patients in the inpatient and outpatient hospice settings.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    hospice_q4 = forms.ChoiceField(
        label = "Apply pharmacotherapeutics (controlled and noncontrolled) in managing hospice patients with acute and chronic symptoms.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    hospice_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea,
        required = False
    )

    policy_attendance = forms.ChoiceField(
        label = "I attended this workshop",
        widget = forms.CheckboxInput,
        required = False
    )
    policy_q1 = forms.ChoiceField(
        label = "Discuss the legislative process.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    policy_q2 = forms.ChoiceField(
        label = "List the significant changes affecting APRN practice.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    policy_q3 = forms.ChoiceField(
        label = "Describe the requirements for the APRN-physician practice agreement.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    policy_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea,
        required = False
    )

    substance_attendance = forms.ChoiceField(
        label = "I attended this workshop",
        widget = forms.CheckboxInput,
        required = False
    )
    substance_q1 = forms.ChoiceField(
        label = "Define substance use disorder as a treatable disease.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    substance_q2 = forms.ChoiceField(
        label = "List treatments including medication-assisted therapy.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    substance_q3 = forms.ChoiceField(
        label = "Discuss harm reduction interventions.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    substance_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea,
        required = False
    )

    pelvic_attendance = forms.ChoiceField(
        label = "I attended this workshop",
        widget = forms.CheckboxInput,
        required = False
    )
    pelvic_q1 = forms.ChoiceField(
        label = "Differentiate between the main causes of urinary incontinence.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    pelvic_q2 = forms.ChoiceField(
        label = "Outline the treatment pathway of both stress and urgency urinary incontinence.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    pelvic_q3 = forms.ChoiceField(
        label = "Explain the diagnosis and treatment of pelvic organ prolapse.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    pelvic_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea,
        required = False
    )

    bias_bool = forms.ChoiceField(
        label = "Did you find any bias in these lectures?",
        choices = yes_no_choices,
        widget = forms.RadioSelect
    )
    bias_comments = forms.CharField(
        label = "If Yes, what did you consider bias?",
        widget = forms.Textarea,
        required = False
    )
    will_this_info_change_you = forms.ChoiceField(
        label = "Will the information provided change the way you practice?",
        choices = yes_no_choices,
        widget = forms.RadioSelect
    )
    workshop_suggestions = forms.CharField(
        label = "Workshop suggestions for 2023 Lecture at the Beach",
        widget = forms.Textarea,
        required = False
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
                layout.Field(
                    'diabetes_attendance',
                    type = 'checkbox',
                    id = 'diabetes_attendance',
                    wrapper_class = 'form-switch',
                    data_bs_toggle = 'collapse',
                    data_bs_target = '#collapse_diabetes'
                ),
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('diabetes_q1'),
                        bootstrap.InlineRadios('diabetes_q2'),
                        bootstrap.InlineRadios('diabetes_q3'),
                        'diabetes_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox collapse',
                    css_id = 'collapse_diabetes'
                )
            ),
            html_separator,
            layout.Fieldset(
                'Chandra Cleveland, LEO (Human Trafficking) <hr />',
                layout.Field(
                    'trafficking_attendance',
                    type = 'checkbox',
                    id = 'trafficking_attendance',
                    wrapper_class = 'form-switch',
                    data_bs_toggle = 'collapse',
                    data_bs_target = '#collapse_trafficking'
                ),
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('trafficking_q1'),
                        bootstrap.InlineRadios('trafficking_q2'),
                        bootstrap.InlineRadios('trafficking_q3'),
                        'trafficking_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox collapse',
                    css_id = 'collapse_trafficking'
                ),
            ),
            html_separator,
            layout.Fieldset(
                'Stephanie Burgess, PhD, APRN (Hospice) <hr />',
                layout.Field(
                    'hospice_attendance',
                    type = 'checkbox',
                    id = 'hospice_attendance',
                    wrapper_class = 'form-switch',
                    data_bs_toggle = 'collapse',
                    data_bs_target = '#collapse_hospice'
                ),
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
                    css_class = 'workshop_flexbox collapse',
                    css_id = 'collapse_hospice'
                ),
            ),
            html_separator,
            layout.Fieldset(
                'Stephanie Burgess, PhD, APRN (Policy and Political Update) <hr />',
                layout.Field(
                    'policy_attendance',
                    type = 'checkbox',
                    id = 'policy_attendance',
                    wrapper_class = 'form-switch',
                    data_bs_toggle = 'collapse',
                    data_bs_target = '#collapse_policy'
                ),
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('policy_q1'),
                        bootstrap.InlineRadios('policy_q2'),
                        bootstrap.InlineRadios('policy_q3'),
                        'policy_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox collapse',
                    css_id = 'collapse_policy'
                ),
            ),
            html_separator,
            layout.Fieldset(
                'Victor Archambeau, MD (Treating Substance Use Disorder) <hr />',
                layout.Field(
                    'substance_attendance',
                    type = 'checkbox',
                    id = 'substance_attendance',
                    wrapper_class = 'form-switch',
                    data_bs_toggle = 'collapse',
                    data_bs_target = '#collapse_substance'
                ),
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('substance_q1'),
                        bootstrap.InlineRadios('substance_q2'),
                        bootstrap.InlineRadios('substance_q3'),
                        'substance_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox collapse',
                    css_id = 'collapse_substance'
                ),
            ),
            html_separator,
            layout.Fieldset(
                'Annaceci Peacher-Holderied, MD (Female Pelvic Medicine) <hr />',
                layout.Field(
                    'pelvic_attendance',
                    type = 'checkbox',
                    id = 'pelvic_attendance',
                    wrapper_class = 'form-switch',
                    data_bs_toggle = 'collapse',
                    data_bs_target = '#collapse_pelvic'
                ),
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('pelvic_q1'),
                        bootstrap.InlineRadios('pelvic_q2'),
                        bootstrap.InlineRadios('pelvic_q3'),
                        'pelvic_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox collapse',
                    css_id = 'collapse_pelvic'
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
                'e_signature'
            ),
            layout.Submit('Submit', 'SUBMIT')
        )

class latbFriForm(forms.Form):
    newdrug_attendance = forms.ChoiceField(
        label = "I attended this workshop",
        widget = forms.CheckboxInput,
        required = False
    )
    newdrug_q1 = forms.ChoiceField(
        label = "Identify medications that were FDA approved and made available last year.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    newdrug_q2 = forms.ChoiceField(
        label = "List each medication's indication, dosing, potential adverse effects, place in therapy, and unique characteristics.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    newdrug_q3 = forms.ChoiceField(
        label = "Devise a strategy to implement relevant new clinical treatment guidelines that were published last year.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    newdrug_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea,
        required = False
    )

    coding_attendance = forms.ChoiceField(
        label = "I attended this workshop",
        widget = forms.CheckboxInput,
        required = False
    )
    coding_q1 = forms.ChoiceField(
        label = "Know the difference between shared and incident-to visits.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    coding_q2 = forms.ChoiceField(
        label = "State the new quality measures related to care transitions, hypertension management, and ED follow-up.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    coding_q3 = forms.ChoiceField(
        label = "Describe how to correctly document, code, and bill for these services.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    coding_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea,
        required = False
    )
    
    thyroid_attendance = forms.ChoiceField(
        label = "I attended this workshop",
        widget = forms.CheckboxInput,
        required = False
    )
    thyroid_q1 = forms.ChoiceField(
        label = "Differentiate various patterns of thyroid nodules found on ultrasound.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    thyroid_q2 = forms.ChoiceField(
        label = "Apply the Bethesda system of reporting thyroid cytology.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    thyroid_q3 = forms.ChoiceField(
        label = "Discuss the role of molecular markers when treating thyroid disease.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    thyroid_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea,
        required = False
    )

    covid_attendance = forms.ChoiceField(
        label = "I attended this workshop",
        widget = forms.CheckboxInput,
        required = False
    )
    covid_q1 = forms.ChoiceField(
        label = "Discuss the biology of the SARS-CoV-2 virus.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    covid_q2 = forms.ChoiceField(
        label = "List current evidence-based treatments for COVID-19.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    covid_q3 = forms.ChoiceField(
        label = "Explain diagnostic testing.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    covid_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea,
        required = False
    )
    
    bias_bool = forms.ChoiceField(
        label = "Did you find any bias in these lectures?",
        choices = yes_no_choices,
        widget = forms.RadioSelect
    )
    bias_comments = forms.CharField(
        label = "If Yes, what did you consider bias?",
        widget = forms.Textarea,
        required = False
    )
    will_this_info_change_you = forms.ChoiceField(
        label = "Will the information provided change the way you practice?",
        choices = yes_no_choices,
        widget = forms.RadioSelect
    )
    workshop_suggestions = forms.CharField(
        label = "Workshop suggestions for 2023 Lecture at the Beach",
        widget = forms.Textarea,
        required = False
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
                layout.Field(
                    'newdrug_attendance',
                    type = 'checkbox',
                    id = 'newdrug_attendance',
                    wrapper_class = 'form-switch',
                    data_bs_toggle = 'collapse',
                    data_bs_target = '#collapse_newdrug'
                ),
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('newdrug_q1'),
                        bootstrap.InlineRadios('newdrug_q2'),
                        bootstrap.InlineRadios('newdrug_q3'),
                        'newdrug_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox collapse',
                    css_id = 'collapse_newdrug'
                )
            ),
            html_separator,
            layout.Fieldset(
                'Nick Ulmer, MD (Coding) <hr />',
                layout.Field(
                    'coding_attendance',
                    type = 'checkbox',
                    id = 'coding_attendance',
                    wrapper_class = 'form-switch',
                    data_bs_toggle = 'collapse',
                    data_bs_target = '#collapse_coding'
                ),
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('coding_q1'),
                        bootstrap.InlineRadios('coding_q2'),
                        bootstrap.InlineRadios('coding_q3'),
                        'coding_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox collapse',
                    css_id = 'collapse_coding'
                ),
            ),
            html_separator,
            layout.Fieldset(
                'Gauri Dhir, MD (Thyroid Nodules and Molecular Markers) <hr />',
                layout.Field(
                    'thyroid_attendance',
                    type = 'checkbox',
                    id = 'thyroid_attendance',
                    wrapper_class = 'form-switch',
                    data_bs_toggle = 'collapse',
                    data_bs_target = '#collapse_thyroid'
                ),
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('thyroid_q1'),
                        bootstrap.InlineRadios('thyroid_q2'),
                        bootstrap.InlineRadios('thyroid_q3'),
                        'thyroid_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox collapse',
                    css_id = 'collapse_thyroid'
                ),
            ),
            html_separator,
            layout.Fieldset(
                'R. Andrew Philipp, MD (COVID-19 Update) <hr />',
                layout.Field(
                    'covid_attendance',
                    type = 'checkbox',
                    id = 'covid_attendance',
                    wrapper_class = 'form-switch',
                    data_bs_toggle = 'collapse',
                    data_bs_target = '#collapse_covid'
                ),
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('covid_q1'),
                        bootstrap.InlineRadios('covid_q2'),
                        bootstrap.InlineRadios('covid_q3'),
                        'covid_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox collapse',
                    css_id = 'collapse_covid'
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
                'e_signature'
            ),
            layout.Submit('Submit', 'SUBMIT')
        )

class latbSatForm(forms.Form):
    naltrexone_attendance = forms.ChoiceField(
        label = "I attended this workshop",
        widget = forms.CheckboxInput,
        required = False
    )
    naltrexone_q1 = forms.ChoiceField(
        label = "List the indications for prescribing LDN.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    naltrexone_q2 = forms.ChoiceField(
        label = "Discuss the appropriate dosing and pharmacodynamics of LDN.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    naltrexone_q3 = forms.ChoiceField(
        label = "Describe how LDN can act as an immunomodulator.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    naltrexone_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea,
        required = False
    )

    chf_attendance = forms.ChoiceField(
        label = "I attended this workshop",
        widget = forms.CheckboxInput,
        required = False
    )
    chf_q1 = forms.ChoiceField(
        label = "Define the stages of congestive heart failure.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    chf_q2 = forms.ChoiceField(
        label = "List pharmacologic treatments for CHF according to current guidelines.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    chf_q3 = forms.ChoiceField(
        label = "Describe risk factors for developing CHF.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    chf_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea,
        required = False
    )
    
    cancer_attendance = forms.ChoiceField(
        label = "I attended this workshop",
        widget = forms.CheckboxInput,
        required = False
    )
    cancer_q1 = forms.ChoiceField(
        label = "List strategies for improved breast health and cancer prevention.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    cancer_q2 = forms.ChoiceField(
        label = "Discuss the newest surgical strategies for breast lesion.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    cancer_q3 = forms.ChoiceField(
        label = "Discuss the current medical and oncologic treatments for breast cancer.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    cancer_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea,
        required = False
    )

    ptsd_attendance = forms.ChoiceField(
        label = "I attended this workshop",
        widget = forms.CheckboxInput,
        required = False
    )
    ptsd_q1 = forms.ChoiceField(
        label = "List the diagnostic criteria for PTSD.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    ptsd_q2 = forms.ChoiceField(
        label = "Describe how the COVID-19 pandemic has affected the rate and presentation of PTSD.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    ptsd_q3 = forms.ChoiceField(
        label = "Identify pharmaceutical and non-pharmaceutical therapies to treat PTSD.",
        choices = five_point_scale,
        widget = forms.RadioSelect,
        required = False
    )
    ptsd_comments = forms.CharField(
        label = "Comments",
        widget = forms.Textarea,
        required = False
    )
    
    bias_bool = forms.ChoiceField(
        label = "Did you find any bias in these lectures?",
        choices = yes_no_choices,
        widget = forms.RadioSelect
    )
    bias_comments = forms.CharField(
        label = "If Yes, what did you consider bias?",
        widget = forms.Textarea,
        required = False
    )
    will_this_info_change_you = forms.ChoiceField(
        label = "Will the information provided change the way you practice?",
        choices = yes_no_choices,
        widget = forms.RadioSelect
    )
    workshop_suggestions = forms.CharField(
        label = "Workshop suggestions for 2023 Lecture at the Beach",
        widget = forms.Textarea,
        required = False
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
                layout.Field(
                    'naltrexone_attendance',
                    type = 'checkbox',
                    id = 'naltrexone_attendance',
                    wrapper_class = 'form-switch',
                    data_bs_toggle = 'collapse',
                    data_bs_target = '#collapse_naltrexone'
                ),
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('naltrexone_q1'),
                        bootstrap.InlineRadios('naltrexone_q2'),
                        bootstrap.InlineRadios('naltrexone_q3'),
                        'naltrexone_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox collapse',
                    css_id = 'collapse_naltrexone'
                )
            ),
            html_separator,
            layout.Fieldset(
                'Nitesh Ainani, MD (CHF) <hr />',
                layout.Field(
                    'chf_attendance',
                    type = 'checkbox',
                    id = 'chf_attendance',
                    wrapper_class = 'form-switch',
                    data_bs_toggle = 'collapse',
                    data_bs_target = '#collapse_chf'
                ),
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('chf_q1'),
                        bootstrap.InlineRadios('chf_q2'),
                        bootstrap.InlineRadios('chf_q3'),
                        'chf_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox collapse',
                    css_id = 'collapse_chf'
                ),
            ),
            html_separator,
            layout.Fieldset(
                'Craig Brackett, MD/FACS (Advancing Diagnosis and Treatment in Breast Cancer) <hr />',
                layout.Field(
                    'cancer_attendance',
                    type = 'checkbox',
                    id = 'cancer_attendance',
                    wrapper_class = 'form-switch',
                    data_bs_toggle = 'collapse',
                    data_bs_target = '#collapse_cancer'
                ),
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('cancer_q1'),
                        bootstrap.InlineRadios('cancer_q2'),
                        bootstrap.InlineRadios('cancer_q3'),
                        'cancer_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox collapse',
                    css_id = 'collapse_cancer'
                ),
            ),
            html_separator,
            layout.Fieldset(
                'Kelly Holes-Lewis, MD (PTSD and Provider Well-Being) <hr />',
                layout.Field(
                    'ptsd_attendance',
                    type = 'checkbox',
                    id = 'ptsd_attendance',
                    wrapper_class = 'form-switch',
                    data_bs_toggle = 'collapse',
                    data_bs_target = '#collapse_ptsd'
                ),
                layout.Div(
                    five_scale_explanation,
                    layout.Div(
                        bootstrap.InlineRadios('ptsd_q1'),
                        bootstrap.InlineRadios('ptsd_q2'),
                        bootstrap.InlineRadios('ptsd_q3'),
                        'ptsd_comments',
                        css_class = 'workshop_group',
                    ),
                    css_class = 'workshop_flexbox collapse',
                    css_id = 'collapse_ptsd'
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
                'e_signature'
            ),
            layout.Submit('Submit', 'SUBMIT')
        )