## conversa 1
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* have_question
    - utter_ask
* ask_calculate_fertile_period
    - action_get_answer
* ask_late_menstruation
    - action_get_answer
* ask_do_pregnancy_test
    - action_get_answer
* got_it
    - utter_great
* thank_you OR affirm+thank_you
    - utter_welcome
* bye
    - utter_bye

## conversa 2
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything 
* ask_normal_fever_milk_comes_down
    - action_get_answer
* ask_prevent_milk_stumbling
    - action_get_answer
* thank_you OR affirm+thank_you
    - utter_welcome
* bye
    - utter_bye

## conversa 3
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* hello
    - action_greet_user
* greeting_answer
    - utter_great
    - utter_ask_me_anything

## conversa 4
* start
    - action_greet_user
    - slot{"greeted_user": true}
* deny
    - utter_info_later
    - utter_ask_me_anything
* no_question
    - utter_ask_me_later
* bye
    - utter_bye

## conversa 5
* start
    - action_greet_user
    - slot{"greeted_user": true}
* later
    - utter_info_later
    - utter_ask_me_anything
* im_pregnant
    - action_congrats
    - slot{"is_pregnant": true}
    - utter_first_step
    - utter_ask_info
* affirm
  - form_initial
  - form{"name": "form_initial"}
  - form{"name": null}
  - utter_ask_me_anything
* ask_what_is_trichotomy
    - action_get_answer
* ask_what_is_forceps
    - action_get_answer
* ask_what_is_braxton_hicks
    - action_get_answer
* ask_what_is_eclampsia
    - action_get_answer
* ask_what_is_uterine_height
    - action_get_answer
* ask_what_is_amniocentesis
    - action_get_answer

## conversa 6
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* have_question
    - utter_ask

## conversa 7
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* have_question
    - utter_ask
* baby_not_moving
    - utter_baby_not_moving
* affirm+got_it
    - utter_great
* bye
    - utter_bye
* greeting
    - action_greet_user
* greeting_answer
    - utter_great
    - utter_ask_me_anything

## conversa 8
* start
    - action_greet_user
    - slot{"greeted_user": true}
* im_pregnant
    - action_congrats
    - slot{"is_pregnant": true}
    - utter_first_step
    - utter_ask_info
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* ask_what_is_trichotomy
    - action_get_answer
* ask_what_is_forceps
    - action_get_answer
* ask_anesthesia_dentist
    - action_get_answer
* ask_contraceptive_pill_after_birth
    - action_get_answer
* affirm
    - utter_great

## conversa 9
* start
  - action_greet_user
  - slot{"greeted_user": true}
* affirm
  - form_initial
  - form{"name": "form_initial"}
  - form{"name": null}
  - utter_ask_me_anything

## conversa 10
* start
  - action_greet_user
  - slot{"greeted_user": true}
* later
  - utter_info_later
  - utter_ask_me_anything
* affirm
    - utter_ask

## conversa 11
* start
    - action_greet_user
    - slot{"greeted_user": true}
* deny
  - utter_info_later
  - utter_ask_me_anything
* ask_normal_fever_milk_comes_down
    - action_get_answer
* ask_prevent_milk_stumbling
    - action_get_answer
* thank_you OR affirm+thank_you
    - utter_welcome
* bye
    - utter_bye
* start_form_health
    - utter_ask_health_questions
* affirm
    - form_health
    - form{"name": "form_health"}
    - form{"name": null}
* ask_breast_milk_normal_birth
    - action_get_answer
* hello
    - action_greet_user
* have_question
    - utter_ask

## conversa 12
* start
    - action_greet_user
    - slot{"greeted_user": true}
* later
  - utter_info_later
  - utter_ask_me_anything
* ask_normal_fever_milk_comes_down
    - action_get_answer
* ask_prevent_milk_stumbling
    - action_get_answer
* thank_you OR affirm+thank_you
    - utter_welcome
* bye
    - utter_bye
* start_form_personal
    - utter_ask_personal_questions
* affirm
    - form_personal
    - form{"name": "form_personal"}
    - form{"name": null}
* have_question
    - utter_ask
* ask_loose_vagina
    - action_get_answer
* thank_you+bye
    - utter_welcome
    - utter_bye
* start_form_health
    - utter_ask_health_questions
* deny
    - utter_info_later
    - utter_ask_me_anything

## conversa 13
* start
    - action_greet_user
    - slot{"greeted_user": true}
* later
    - utter_info_later
    - utter_ask_me_anything
* ask_normal_fever_milk_comes_down
    - action_get_answer
* ask_prevent_milk_stumbling
    - action_get_answer
* thank_you OR affirm+thank_you
    - utter_welcome
* bye
    - utter_bye
* start_form_pregnancy
    - utter_ask_pregnancy_questions
* affirm
    - form_pregnancy
    - form{"name": "form_pregnancy"}
    - form{"name": null}
* ask_what_is_isthmus_cervical
    - action_get_answer
* bye
    - utter_bye
* hello
    - action_greet_user
* have_question
    - utter_ask

## conversa 14
* ask_what_is_natural_childbirth
    - action_get_answer
* ask_what_is_humanized_childbirth
    - action_get_answer
* ask_who_receive_maternity_leave
    - action_get_answer
* ask_unemployed_receive_maternity_leave
    - action_get_answer
* ask_calculate_fertile_period
    - action_get_answer
* ask_late_menstruation
    - action_get_answer
* ask_do_pregnancy_test
    - action_get_answer

## conversa 15
* start
    - action_greet_user
    - slot{"greeted_user": true}
* ask_can_travel
    - action_get_answer
* welcome
    - utter_welcome

## conversa 16
* start
    - action_greet_user
    - slot{"greeted_user": true}
* later
    - utter_info_later
    - utter_ask_me_anything
* have_question
    - utter_ask
* ask_calculate_fertile_period
    - action_get_answer
* got_it
    - utter_great
* thank_you OR affirm+thank_you
    - utter_welcome
* bye
    - utter_bye
* ask_exam
    - utter_ask_exam
* affirm
    - action_doing_right_exam
* i_know_importance

## conversa 17
* start
    - action_greet_user
    - slot{"greeted_user": true}
* later
    - utter_info_later
    - utter_ask_me_anything
* ask_calculate_fertile_period
    - action_get_answer
* thank_you
    - utter_welcome
* bye
    - utter_bye
* ask_exam
    - utter_ask_exam
* did_exam
    - action_doing_right_exam
* i_know_importance
    - utter_agree

## conversa 18
* start
    - action_greet_user
    - slot{"greeted_user": true}
* later
    - utter_info_later
    - utter_ask_me_anything
* ask_calculate_fertile_period
    - action_get_answer
* thank_you
    - utter_welcome
* bye
    - utter_bye
* ask_exam
    - utter_ask_exam
* did_exam
    - action_doing_right_exam
* i_know_importance
    - utter_agree
* ask_exam
    - utter_ask_exam
* deny
    - action_get_exam
    - utter_is_important_exam
* ill_do_it
    - utter_great
* ask_smell_sweat_stronger
    - action_get_answer

## conversa 19
* start
    - action_greet_user
    - slot{"greeted_user": true}
* later
    - utter_info_later
    - utter_ask_me_anything
* ask_when_go_maternity
    - action_get_answer
* thank_you
    - utter_welcome
* bye
    - utter_bye
* ask_exam
    - utter_ask_exam
* did_exam
    - action_doing_right_exam
* i_know_importance
    - utter_agree
* start_form_pregnancy
    - utter_ask_health_questions
* later
    - utter_info_later
    - utter_ask_me_anything
* no_question
    - utter_ask_me_later

## conversa 20
* start
    - action_greet_user
    - slot{"greeted_user": true}
* later
  - utter_info_later
  - utter_ask_me_anything

## conversa 21
* start
    - action_greet_user
    - slot{"greeted_user": true}
* later
    - utter_info_later
    - utter_ask_me_anything
* out_of_scope
    - utter_canthelp
    - utter_explain_whatspossible

## conversa 22
* start
    - action_greet_user
    - slot{"greeted_user": true}
* ask_diet_breastfeed
    - action_get_answer

## conversa 24
* start
    - action_greet_user
    - slot{"greeted_user": true}
* ask_receive_oral_sex
    - action_get_answer

## conversa 25
* start
    - action_greet_user
    - slot{"greeted_user": true}
* ask_avoid_cleaning_products
    - action_get_answer
* ask_best_position_baby_sleep
    - action_get_answer
* ask_what_vaccines_baby
    - action_get_answer

## conversa 26
* start
    - action_greet_user
    - slot{"greeted_user": true}
* ask_contraceptive_pill_after_birth
    - action_get_answer
* ask_invite_accompany_birth
    - action_get_answer

## conversa 27
* start
    - action_greet_user
    - slot{"greeted_user": true}
* ask_not_allowed_vaccine
    - action_get_answer
* ask_what_is_prenatal
    - action_get_answer
* ask_what_is_postpartum
    - action_get_answer

## conversa 28
* start
    - action_greet_user
    - slot{"greeted_user": true}
* out_of_scope
    - utter_canthelp
    - utter_explain_whatspossible

## conversa 29
* start
    - action_greet_user
    - slot{"greeted_user": true}
* ask_what_is_leboyer_childbirth
    - action_get_answer
* ask_exam
    - utter_ask_exam
* why_i_need_to_answer
    - utter_why_answer
* did_not_exam
    - action_get_exam
    - utter_is_important_exam
* i_know_importance
    - utter_agree

## conversa 30
* start
    - action_greet_user
    - slot{"greeted_user": true}
* ask_pregnant_menopause
    - action_get_answer
* ask_exam
    - utter_ask_exam
* why_i_need_to_answer
    - utter_why_answer
* deny
    - action_get_exam
    - utter_is_important_exam
* got_it
    - utter_great
* start_form_pregnancy
    - utter_ask_pregnancy_questions
* affirm
    - form_pregnancy
    - form{"name": "form_pregnancy"}
* why_i_need_to_answer
    - utter_why_answer
    - form_pregnancy
    - form{"name": null}

## conversa 31
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* im_think_pregnant
    - utter_not_sure_pregnancy
* affirm
    - utter_great

## conversa 32
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* hello+im_think_pregnant
    - utter_hello
    - utter_not_sure_pregnancy
* got_it
    - utter_great
* ask_normal_lose_weight_breastfeed
    - action_get_answer
* thank_you
    - utter_welcome

## conversa 33
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* ask_normal_lose_weight_breastfeed
    - action_get_answer
* start_form_health
    - utter_ask_health_questions
* affirm
    - form_health
    - form{"name": "form_health"}
* stop_form
    - action_deactivate_form
    - form{"name": null}
    - utter_info_later
    - utter_ask_me_anything
* have_question
    - utter_ask
* ask_late_menstruation
    - action_get_answer
* ask_do_pregnancy_test
    - action_get_answer
* thank_you
    - utter_welcome

## conversa 34
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* no_question
    - utter_ask_me_later
* hello+greeting
    - action_greet_user
* greeting_back
    - utter_greet_answer
    - utter_ask_me_anything
* have_question
    - utter_ask
* ask_normal_lose_weight_breastfeed
    - action_get_answer
* ask_late_menstruation
    - action_get_answer
* ask_do_pregnancy_test
    - action_get_answer
* thank_you
    - utter_welcome

## conversa 35
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* welcome
    - utter_great
* hello+greeting
    - action_greet_user
* greeting_answer
    - utter_great
    - utter_ask_me_anything
* ask_sore_sex_after_birth
    - action_get_answer
* thank_you
    - utter_welcome
* bye
    - utter_bye
* ask_exam
    - utter_ask_exam
* did_exam
    - action_doing_right_exam
* i_know_importance
    - utter_agree

## conversa 36
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* start_form_personal
    - utter_ask_personal_questions
* affirm
    - form_personal
    - form{"name": "form_personal"}
    - form{"name": null}
* hello+greeting
    - action_greet_user
* greeting_answer
    - utter_great
    - utter_ask_me_anything
* start_form_health
    - utter_ask_health_questions
* affirm
    - form_health
    - form{"name": "form_health"}
    - form{"name": null}
* ask_exam
    - utter_ask_exam
* affirm
    - action_doing_right_exam

## conversa 37
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* ask_can_sweetener
    - action_get_answer
* ask_can_vaccine
    - action_get_answer
* ask_can_sleep_stomach
    - action_get_answer
* ask_can_hot_wax
    - action_get_answer
* ask_can_pap_smear
    - action_get_answer
* ask_can_drive
    - action_get_answer
* ask_when_start_prenatal
    - action_get_answer
* ask_when_episiotomy
    - action_get_answer
* ask_when_baby_move
    - action_get_answer
* ask_when_start_braxton_hicks
    - action_get_answer
* ask_when_exam_feces
    - action_get_answer
* ask_when_exam_blood_glucose
    - action_get_answer
* ask_when_exam_blood
    - action_get_answer

## conversa 38
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* affirm
    - utter_ask
* ask_can_sweetener
    - action_get_answer
* ask_can_vaccine
    - action_get_answer
* ask_can_sleep_stomach
    - action_get_answer
* ask_can_hot_wax
    - action_get_answer
* bye
    - utter_bye

## conversa 39
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* affirm
    - utter_ask
* ask_when_exam_urine
    - action_get_answer
* bye
    - utter_bye
* start_form_health
    - utter_ask_health_questions
* stop_form
  - utter_info_later
  - utter_ask_me_anything

## conversa 40
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* affirm
    - utter_ask
* ask_when_exam_urine
    - action_get_answer
* bye
    - utter_bye
* start_form_personal
    - utter_ask_personal_questions
* stop_form
  - utter_info_later
  - utter_ask_me_anything

## conversa 41
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* affirm
    - utter_ask
* ask_when_exam_urine
    - action_get_answer
* bye
    - utter_bye
* start_form_pregnancy
    - utter_ask_pregnancy_questions
* stop_form
  - utter_info_later
  - utter_ask_me_anything

## conversa 42
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* no_question
    - utter_ask_me_later
* bye
    - utter_bye
* start_form_health
    - utter_ask_health_questions
* stop_form
    - utter_info_later
    - utter_ask_me_anything
* affirm
    - utter_ask
* ask_when_exam_urine
    - action_get_answer

## conversa 43
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* start_form_health
    - utter_ask_health_questions
* stop_form
    - utter_info_later
    - utter_ask_me_anything
* start_form_pregnancy
    - utter_ask_pregnancy_questions
* stop_form
    - utter_info_later
    - utter_ask_me_anything
* start_form_personal
    - utter_ask_personal_questions
* stop_form
    - utter_info_later
    - utter_ask_me_anything

## conversa 44
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* start_form_health
    - utter_ask_health_questions
* affirm
    - form_health
    - form{"name": "form_health"}
    - form{"name": null}
* start_form_pregnancy
    - utter_ask_pregnancy_questions
* affirm
    - form_pregnancy
    - form{"name": "form_pregnancy"}
    - form{"name": null}
* start_form_personal
    - utter_ask_personal_questions
* affirm
    - form_personal
    - form{"name": "form_personal"}
    - form{"name": null}

## conversa 45
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* start_form_health
    - utter_ask_health_questions
* deny
  - utter_info_later
  - utter_ask_me_anything
* start_form_pregnancy
    - utter_ask_pregnancy_questions
* later
  - utter_info_later
  - utter_ask_me_anything
* start_form_personal
    - utter_ask_personal_questions
* stop_form
  - utter_info_later
  - utter_ask_me_anything

## conversa 46
* start
    - action_greet_user
    - slot{"greeted_user": true}
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - form{"name": null}
    - utter_ask_me_anything
* no_question
    - utter_ask_me_later

## conversa 47
* start
    - action_greet_user
    - slot{"greeted_user": true}
* deny
    - utter_info_later
    - utter_ask_me_anything
* no_question
    - utter_ask_me_later
* ask_exercise_help_normal_birth
    - action_get_answer
* ask_breast_milk_normal_birth
    - action_get_answer
* ask_normal_birth_recovery
    - action_get_answer
* ask_normal_birth_duration
    - action_get_answer
* ask_birth_transmit_disease
    - action_get_answer
* ask_avoid_normal_birth
    - action_get_answer

## conversa 48
* start
    - action_greet_user
    - slot{"greeted_user": true}
* deny
    - utter_info_later
    - utter_ask_me_anything
* no_question
    - utter_ask_me_later
* hello
    - action_greet_user
* ask_how_long_milk_come_down
    - action_get_answer
* thank_you
    - utter_welcome

## conversa 49
* start
    - action_greet_user
    - slot{"greeted_user": true}
* deny
    - utter_info_later
    - utter_ask_me_anything
* hello
    - action_greet_user
* greeting_answer
    - utter_great
    - utter_ask_me_anything
* have_question
    - utter_ask
* ask_back_exercise
    - action_get_answer
* thank_you
    - utter_welcome
* bye
    - utter_bye

## conversa 50
* start
    - action_greet_user
    - slot{"greeted_user": true}
* deny
    - utter_info_later
    - utter_ask_me_anything
* hello
    - action_greet_user
* ask_loss_hair_breastfeed
    - action_get_answer
* thank_you
    - utter_welcome
