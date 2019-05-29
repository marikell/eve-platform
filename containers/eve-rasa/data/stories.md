## greet
* get_started
  - action_greet_user
* greeting_answer_back
  - utter_greet_answer
  - utter_first_help

## canthelp
* canthelp
    - utter_canthelp

## ask_howold
* ask_howold
    - utter_ask_howold

## ask_howold
* ask_howold
    - utter_ask_howold
* ask_isbot
    - utter_ask_isbot

## ask_isbot
* ask_isbot
    - utter_ask_isbot

## ask_wherefrom
* ask_wherefrom
    - utter_ask_wherefrom

## ask_wherefrom
* ask_wherefrom
    - utter_ask_wherefrom
* ask_isbot
    - utter_ask_isbot

## ask_wherefrom
* ask_wherefrom
    - utter_ask_wherefrom
* ask_howold
    - utter_ask_howold

## whoisit
* ask_whoisit
    - utter_introduce

## whoisit
* ask_whoisit
    - utter_introduce
* ask_wherefrom
    - utter_ask_wherefrom

## whoisit
* ask_whoisit
    - utter_introduce
* ask_wherefrom
    - utter_ask_wherefrom
* ask_howold
    - utter_ask_howold

## greet
* get_started
  - action_greet_user
* greeting_answer_back
  - utter_greet_answer
  - utter_first_help
* canthelp
    - utter_canthelp
* ask_whoisit
    - utter_introduce

## user_info
* get_info
  - utter_ask_info_user
* affirm
  - utter_ask_city
* enter_data{"user_city": "Sorocaba"}
  - action_city_user
  - utter_great
  - utter_ask_state
* enter_data{"user_state": "SP"}
    - action_state_user
  - utter_great
  - utter_ask_age
* enter_data{"user_age": "20"}
    - action_age_user
    - utter_great
* ask_whoisit
    - utter_introduce


## greet
* get_started
  - action_greet_user
* greeting_answer
  - utter_first_help

## bot_start
* hello
    - action_greet_user
* greeting_answer_back
  - utter_greet_answer
  - utter_first_help

## bot_start
* greet
    - action_greet_user
* greeting_answer
  - utter_great
  - utter_first_help

## greet_3
* get_started
  - action_greet_user
* greeting_answer
    - utter_great
    - utter_first_help

## bye
* bye
- utter_bye

## thank_you
* thank_you
- utter_welcome

## get_answer
* get_started
  - action_greet_user
* greeting_answer
    - utter_great
    - utter_first_help
* which{"question_entity": "exercicios"}
    - get_answer
* which_not{"question_entity": "comida"}
    - get_answer
* can{"question_entity": "exercicios"}
    - get_answer
* which{"question_entity": "exercicios"}
    - get_answer
* which{"question_entity": "treinos"}
    - get_answer
* which_not{"question_entity": "treinos"}
    - get_answer

## get_answer_2
* get_started
  - action_greet_user
* which{"question_entity": "exercicios"}
    - get_answer
* which{"question_entity": "treinos"}
    - get_answer

## Generated Story -8569811712381873528
* get_started
    - action_greet_user
* greeting_answer
    - utter_first_help
* which{"question_entity": "exercicios"}
    - get_answer
* which_not{"question_entity": "alimentos"}
    - get_answer
* thank_you
    - utter_welcome
    - utter_help

## med_reminder_1
* get_started
  - action_greet_user
* greeting_answer
    - utter_first_help
* set_reminder_med
    - medicine_form
    - form{"name": "medicine_form"}
    - form{"name": null}
* affirm
    - utter_med_done
* thank_you
    - utter_welcome
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_help

## med_reminder_1
* greeting
  - utter_introduce
  - utter_greet_back
* greeting_answer
    - utter_first_help
* set_reminder_med
    - medicine_form
    - form{"name": "medicine_form"}
    - form{"name": null}
* affirm
    - utter_med_done
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup
    - utter_help
* thank_you
    - utter_welcome

## Generated Story 1673752282302648423
* hello
    - action_greet_user
* greeting_answer
    - utter_great
    - utter_first_help
* set_reminder_med
    - medicine_form
    - form{"name": "medicine_form"}
    - slot{"requested_slot": "med_name"}
* form: enter_data{"med_name": "dipirona"}
    - slot{"med_name": "dipirona"}
    - form: medicine_form
    - slot{"med_name": "dipirona"}
    - slot{"requested_slot": "med_frequency"}
* form: enter_data
    - form: medicine_form
    - slot{"med_frequency": "1"}
    - slot{"requested_slot": "med_frequency_day"}
* form: enter_data{"med_frequency_day": "3"}
    - slot{"med_frequency_day": "3"}
    - form: medicine_form
    - slot{"med_frequency_day": "3"}
    - slot{"requested_slot": "med_hours"}
* form: enter_data{"med_hours": "9"}
    - slot{"med_hours": "9"}
    - form: medicine_form

## Generated Story 1025067352679099485
* hello
    - action_greet_user
* greeting_answer
    - utter_great
    - utter_first_help
* set_reminder_med
    - medicine_form
    - form{"name": "medicine_form"}
    - slot{"requested_slot": "med_name"}
* form: enter_data{"med_name": "dipirona"}
    - slot{"med_name": "dipirona"}
    - form: medicine_form
    - slot{"med_name": "dipirona"}
    - slot{"requested_slot": "med_frequency"}
* form: enter_data
    - form: medicine_form
    - slot{"med_frequency": "1"}
    - slot{"requested_slot": "med_frequency_day"}
* form: enter_data
    - form: medicine_form
    - slot{"med_frequency_day": "3"}
    - slot{"requested_slot": "med_hours"}
* form: enter_data{"med_hours": "9"}
    - slot{"med_hours": "9"}
    - form: medicine_form
    - slot{"med_hours": null}
    - slot{"requested_slot": "med_hours"}
* form: enter_data{"med_hours": "10"}
    - slot{"med_hours": "10"}
    - form: medicine_form
    - slot{"med_hours": null}
    - slot{"requested_slot": "med_hours"}
* form: enter_data
    - form: medicine_form
    - slot{"med_hours": null}
    - slot{"requested_slot": "med_hours"}

## Generated Story 3143580898074990559
* hello
    - action_greet_user
* greeting_answer
    - utter_great
    - utter_first_help
* set_reminder_med
    - medicine_form
    - form{"name": "medicine_form"}
    - slot{"requested_slot": "med_name"}
* form: enter_data{"med_name": "lufital"}
    - slot{"med_name": "lufital"}
    - form: medicine_form
    - slot{"med_name": "lufital"}
    - slot{"requested_slot": "med_frequency"}
* form: enter_data
    - form: medicine_form
    - slot{"med_frequency": "1"}
    - slot{"requested_slot": "med_frequency_day"}
* form: enter_data
    - form: medicine_form
    - slot{"med_frequency_day": "2"}
    - slot{"requested_slot": "med_hours"}
* form: enter_data{"med_hours": "3"}
    - slot{"med_hours": "3"}
    - form: medicine_form
    - slot{"med_hours": null}
    - slot{"requested_slot": "med_hours"}
* form: enter_data{"med_hours": "7"}
    - slot{"med_hours": "7"}
    - form: medicine_form
    - slot{"med_hours": ["3", "7"]}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - utter_med_done
    - utter_ask_feedback

## Generated Story 35854981849600683
* hello
    - action_greet_user
* greeting_back
    - utter_greet_answer
    - utter_first_help
* which_not{"question_entity": "alimentos"}
    - get_answer
* which_not{"question_entity": "exercicio"}
    - get_answer
* set_reminder_med
    - medicine_form
    - form{"name": "medicine_form"}
    - slot{"requested_slot": "med_name"}
* form: enter_data{"med_name": "dipirona"}
    - slot{"med_name": "dipirona"}
    - form: medicine_form
    - slot{"med_name": "dipirona"}
    - slot{"requested_slot": "med_frequency"}
* form: enter_data
    - form: medicine_form
    - slot{"med_frequency": "1"}
    - slot{"requested_slot": "med_frequency_day"}
* form: enter_data
    - form: medicine_form
    - slot{"med_frequency_day": "2"}
    - slot{"requested_slot": "med_hours"}
* form: enter_data{"med_hours": "9"}
    - slot{"med_hours": "9"}
    - form: medicine_form
    - slot{"med_hours": null}
    - slot{"requested_slot": "med_hours"}
* form: enter_data{"med_hours": "19"}
    - slot{"med_hours": "19"}
    - form: medicine_form
    - slot{"med_hours": ["9", "19"]}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - utter_med_done

## Generated Story 707944168274727227
* hello
    - action_greet_user
* greeting_answer
    - utter_great
    - utter_first_help
* which{"question_entity": "exercicio"}
    - get_answer
* which{"question_entity": "alimentos"}
    - get_answer
* which_not{"question_entity": "exercicio"}
    - get_answer
* symptom{"question_entity": "gravidez"}
    - get_answer
* prevent{"question_entity": "pre-eclampsia"}
    - get_answer
* risk_factor{"question_entity": "gravidez"}
    - get_answer

#1233123
* which{"question_entity": "alimentos"}
    - get_answer
* which_not{"question_entity": "exercicio"}
    - get_answer
* symptom{"question_entity": "gravidez"}
    - get_answer
* prevent{"question_entity": "pre-eclampsia"}
    - get_answer
* what_is{"question_entity": "loquio"}
    - get_answer
* causes{"question_entity": "pre-eclampsia"}
    - get_answer
* how_to_know{"question_entity": "bolsa"}
    - get_answer

## Generated Story 6967894117882910328
* set_reminder_med
    - medicine_form
    - form{"name": "medicine_form"}
    - slot{"requested_slot": "med_name"}
* form: enter_data{"med_name": "lufital"}
    - slot{"med_name": "lufital"}
    - form: medicine_form
    - slot{"med_name": "lufital"}
    - slot{"requested_slot": "med_frequency"}
* form: enter_data
    - form: medicine_form
    - slot{"med_frequency": "1"}
    - slot{"requested_slot": "med_frequency_day"}
* form: enter_data
    - form: medicine_form
    - slot{"med_frequency_day": "2"}
    - slot{"requested_slot": "med_hours"}
* form: enter_data{"med_hours": "9"}
    - slot{"med_hours": "9"}
    - form: medicine_form
    - slot{"med_hours": null}
    - slot{"requested_slot": "med_hours"}
* form: enter_data{"med_hours": "14"}
    - slot{"med_hours": "14"}
    - form: medicine_form
    - slot{"med_hours": ["9", "14"]}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story -7753515448056614684
* set_reminder_med{"med_name": "dipirona"}
    - slot{"med_name": "dipirona"}
    - medicine_form
    - form{"name": "medicine_form"}
    - slot{"med_name": "dipirona"}
    - slot{"med_name": "dipirona"}
    - slot{"requested_slot": "med_frequency"}
* form: enter_data
    - form: medicine_form
    - slot{"med_frequency": "1"}
    - slot{"requested_slot": "med_frequency_day"}
* form: enter_data
    - form: medicine_form
    - slot{"med_frequency_day": "3"}
    - slot{"requested_slot": "med_hours"}
* form: enter_data
    - form: medicine_form
    - slot{"med_hours": null}
    - slot{"requested_slot": "med_hours"}
* form: enter_data{"med_hours": "9"}
    - slot{"med_hours": "9"}
    - form: medicine_form
    - slot{"med_hours": null}
    - slot{"requested_slot": "med_hours"}
* form: enter_data{"med_hours": "20"}
    - slot{"med_hours": "20"}
    - form: medicine_form
    - slot{"med_hours": null}
    - slot{"requested_slot": "med_hours"}
* form: enter_data{"med_hours": "15"}
    - slot{"med_hours": "15"}
    - form: medicine_form
    - slot{"med_hours": ["9", "20", "15"]}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - utter_med_done
    - utter_ask_feedback
* enter_data
    - utter_thumbsup
    - utter_help
* set_reminder_med
    - medicine_form

## Generated Story 4646674987687058942
* greeting
    - utter_introduce
    - utter_greet_back
* greeting_answer
    - utter_first_help
* can{"question_entity": "bicicleta"}
    - get_answer
* can{"question_entity": "moto"}
    - get_answer
* what_is{"question_entity": "puerperio"}
    - get_answer
* ask_isbot
    - utter_ask_isbot
* ask_whoisit
    - utter_introduce

## Generated Story 4646674987687058942
* greeting
    - utter_introduce
    - utter_greet_back
* greeting_answer
    - utter_first_help
* goal_exam{"question_entity": "glicemia"}
    - get_answer
* when_exame{"question_entity": "glicemia"}
    - get_answer
* what_to_do{"question_entity": "bolsa"}
    - get_answer
* when{"question_entity": "pre natal"}
    - get_answer
* why{"question_entity": "sono"}
    - get_answer
* hello
    - action_greet_user
* greeting_back
    - utter_greet_answer
    - utter_first_help

## Generated Story 6158015074139116326
* hello
    - action_greet_user
* greeting_answer
    - utter_great
    - utter_first_help
* which{"question_entity": "exerc\u00edcios"}
    - get_answer
* bye
    - utter_bye

