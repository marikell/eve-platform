## conversa 15
* start
    - action_greet_user
    - slot{"greeted_user": true}
* ask_can_travel
    - action_get_answer
* welcome
    - utter_welcome   <!-- predicted: utter_great -->


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
* thank_you
    - utter_welcome
* bye
    - utter_bye
* ask_exam
    - utter_ask_exam
* affirm
    - action_doing_right_exam
* i_know_importance
    - action_listen   <!-- predicted: utter_agree -->


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
* affirm+thank_you
    - utter_welcome
* bye
    - utter_bye
* ask_exam
    - utter_ask_exam
* affirm
    - action_doing_right_exam
* i_know_importance
    - action_listen   <!-- predicted: utter_agree -->


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
    - utter_ask_health_questions   <!-- predicted: utter_ask_pregnancy_questions -->
* later
    - utter_info_later
    - utter_ask_me_anything
* no_question
    - utter_ask_me_later


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
* form: why_i_need_to_answer
    - form: utter_why_answer   <!-- predicted: form_pregnancy -->
    - form: form_pregnancy
    - form{"name": null}


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
* form: stop_form
    - form: action_deactivate_form   <!-- predicted: form_health -->
    - form{"name": null}
    - utter_info_later   <!-- predicted: action_listen -->
    - utter_ask_me_anything
* have_question
    - utter_ask
* ask_late_menstruation
    - action_get_answer
* ask_do_pregnancy_test
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
    - utter_ask_me_anything   <!-- predicted: action_listen -->
* have_question
    - utter_ask
* ask_back_exercise
    - action_get_answer
* thank_you
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
    - utter_ask_me_anything   <!-- predicted: action_listen -->


