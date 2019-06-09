## bot inicia a conversa e a mulher esta gravida
* get_started
  - action_greet_user
* affirm
  - form_initial
  - form{"name": "form_initial"}
  - form{"name": null}
  - utter_ask_me_anything

## bot inicia a conversa e a mulher nao quer responder as perguntas
* get_started
  - action_greet_user
* deny
  - utter_info_later
  - utter_ask_me_anything
* which{"question_entity": "exercicios"}
    - action_get_answer

## a mulher inicia a conversa com apenas 'Oi' e esta gravida
* hello
  - action_greet_user
* affirm
  - form_initial
  - form{"name": "form_initial"}
  - form{"name": null}
  - utter_ask_me_anything

## a mulher inicia a conversa com apenas 'Oi' e quer responder as perguntas
* hello
  - action_greet_user
* deny
  - utter_info_later
  - utter_ask_me_anything

## a mulher inicia a conversa com 'Oi tudo bem?' e esta gravida
* greeting
  - action_greet_user
* greeting_answer
  - utter_ask_info
* affirm
  - form_initial
  - form{"name": "form_initial"}
  - form{"name": null}
  - utter_ask_me_anything

## a mulher inicia a conversa com 'Oi tudo bem?' e nao quer responder as perguntas
* greeting
  - action_greet_user
* greeting_answer
  - utter_ask_info
* deny
  - utter_info_later
  - utter_ask_me_anything

## bot_start
* greeting
    - action_greet_user
* greeting_answer
  - utter_ask_info

## greet_3
* get_started
  - action_greet_user
* greeting_answer
    - utter_ask_info

## action_get_answer
* which{"question_entity": "exercicios"}
    - slot{"last_intent": "which"}
    - action_get_answer
* which_not{"question_entity": "comida"}
    - slot{"last_intent": "which_not"}
    - action_get_answer
* can{"question_entity": "exercicios"}
    - slot{"last_intent": "can"}
    - action_get_answer
* which{"question_entity": "exercicios"}
    - slot{"last_intent": "which"}
    - action_get_answer
* which{"question_entity": "treinos"}
    - slot{"last_intent": "which"}
    - action_get_answer
* which_not{"question_entity": "treinos"}
    - slot{"last_intent": "which_not"}
    - action_get_answer

## action_get_answer_2
* get_started
  - action_greet_user
* which{"question_entity": "exercicios"}
    - slot{"last_intent": "which"}
    - action_get_answer
* which{"question_entity": "treinos"}
    - slot{"last_intent": "which"}
    - action_get_answer

## Generated Story -8569811712381873528
* get_started
    - action_greet_user
* greeting_answer
    - utter_ask_info
* which{"question_entity": "exercicios"}
    - slot{"last_intent": "which"}
    - action_get_answer
* which_not{"question_entity": "alimentos"}
    - slot{"last_intent": "which_not"}
    - action_get_answer

##1233123
* which{"question_entity": "alimentos"}
    - slot{"last_intent": "which"}
    - action_get_answer
* which_not{"question_entity": "exercicio"}
    - slot{"last_intent": "which_not"}
    - action_get_answer
* symptom{"question_entity": "gravidez"}
    - slot{"last_intent": "symptom"}
    - action_get_answer
* prevent{"question_entity": "pre-eclampsia"}
    - slot{"last_intent": "prevent"}
    - action_get_answer
* what_is{"question_entity": "loquio"}
    - slot{"last_intent": "what_is"}
    - action_get_answer
* complain{"question_entity": "costas"}
    - slot{"last_intent": "complain"}
    - action_get_answer
* causes{"question_entity": "pre-eclampsia"}
    - slot{"last_intent": "causes"}
    - action_get_answer
* how_to_know{"question_entity": "bolsa"}
    - slot{"last_intent": "how_to_know"}
    - action_get_answer

##1233123
* which{"question_entity": "alimentos"}
    - action_get_answer
    - slot{"last_intent": "which"}
* last_intent{"question_entity": "exercicio"}
    - slot{"last_intent": "which"}
    - action_get_answer
* symptom{"question_entity": "gravidez"}
    - slot{"last_intent": "symptom"}
    - action_get_answer
* prevent{"question_entity": "pre-eclampsia"}
    - slot{"last_intent": "prevent"}
    - action_get_answer
* what_is{"question_entity": "loquio"}
    - slot{"last_intent": "what_is"}
    - action_get_answer
* last_intent{"question_entity": "puerperio"}
    - slot{"last_intent": "what_is"}
    - action_get_answer
* causes{"question_entity": "pre-eclampsia"}
    - slot{"last_intent": "causes"}
    - action_get_answer
* how_to_know{"question_entity": "bolsa"}
    - slot{"last_intent": "how_to_know"}
    - action_get_answer

## Generated Story 4646674987687058942
* goal_exam{"question_entity": "glicemia"}
    - action_get_answer
* when_exame{"question_entity": "glicemia"}
    - action_get_answer
* what_to_do{"question_entity": "bolsa"}
    - action_get_answer
* complain{"question_entity": "ansia"}
    - action_get_answer
* when{"question_entity": "pre natal"}
    - action_get_answer
* why{"question_entity": "sono"}
    - action_get_answer

## estou gravida
* im_pregnant
    - utter_congrats
    - utter_first_step
    - utter_ask_info
* affirm
  - form_initial
  - form{"name": "form_initial"}
  - form{"name": null}
  - utter_ask_me_anything

## unhappy path: bot inicia a conversa e a mulher esta gravida
* get_started
  - action_greet_user
* affirm
  - form_initial
  - form{"name": "form_initial"}
* what_is{"question_entity":"loquio"}
  - action_get_answer
  - form_initial
  - form{"name": null}
  - utter_ask_me_anything

## unhappy path: a mulher inicia a conversa com apenas 'Oi' e esta gravida
* hello
  - action_greet_user
* affirm
  - form_initial
  - form{"name": "form_initial"}
* why{"question_entity":"sono"}
  - action_get_answer
  - form_initial
  - form{"name": null}
  - utter_ask_me_anything

## unhappy path: bot inicia a conversa e a mulher esta gravida e pede para o bot parar as perguntas
* get_started
  - action_greet_user
* affirm
  - form_initial
  - form{"name": "form_initial"}
* stop
  - action_deactivate_form
  - form{"name": null}
  - utter_ask_me_anything

## unhappy path: a mulher inicia a conversa com apenas 'Oi' e esta gravida e pede para o bot parar as perguntas
* hello
  - action_greet_user
* affirm
  - form_initial
  - form{"name": "form_initial"}
* stop
  - action_deactivate_form
  - form{"name": null}
  - utter_ask_me_anything

## lembrete de remédio
* hello
    - action_greet_user
* set_reminder_medicine    
  - form_medicine
  - form{"name": "form_medicine"}
  - form{"name": null}
* affirm
  - utter_reminder

## lembrete de remédio
* hello
    - action_greet_user
* set_reminder_medicine    
  - form_medicine
  - form{"name": "form_medicine"}
  - form{"name": null}
* deny
  - action_cancel_reminder

## unhappy path: lembrete de remédio
* set_reminder_medicine
  - form_medicine
  - form{"name": "form_medicine"}
  - form{"name": null}
* affirm
  - utter_reminder

## unhappy path: lembrete de remédio
* set_reminder_medicine
  - form_medicine
  - form{"name": "form_medicine"}
* stop
  - action_deactivate_form
  - form{"name": null}
  - utter_help

## Generated Story -1614147544277604422
* hello
    - action_greet_user
* deny
    - utter_info_later
    - utter_ask_me_anything
* set_reminder_medicine
    - form_medicine
    - form{"name": "form_medicine"}
    - slot{"requested_slot": "med_frequency"}
* form: enter_data{"med_frequency": "one_time"}
    - slot{"med_frequency": "one_time"}
    - form: form_medicine
    - slot{"med_frequency": "one_time"}
    - slot{"requested_slot": "med_name"}
* form: enter_data{"med_name": "dorflex"}
    - slot{"med_name": "dorflex"}
    - form: form_medicine
    - slot{"med_name": "dorflex"}
    - slot{"requested_slot": "med_date"}
* form: enter_data{"hour": "10", "time": "2019-06-10T10:00:00.000-07:00"}
    - form: form_medicine
    - slot{"med_date": "2019-06-10T10:00:00.000-07:00"}
    - form{"name": null}
    - slot{"requested_slot": null}    
* affirm
    - utter_reminder    

## Generated Story 4282896163755816122
* hello
    - action_greet_user
* deny
    - utter_info_later
    - utter_ask_me_anything
* set_reminder_medicine
    - form_medicine
    - form{"name": "form_medicine"}
    - slot{"requested_slot": "med_frequency"}
* form: enter_data{"med_frequency": "daily"}
    - slot{"med_frequency": "daily"}
    - form: form_medicine
    - slot{"med_frequency": "daily"}
    - slot{"requested_slot": "med_name"}
* form: enter_data{"med_name": "loratadina"}
    - slot{"med_name": "loratadina"}
    - form: form_medicine
    - slot{"med_name": "loratadina"}
    - slot{"requested_slot": "med_hour"}
* form: enter_data{"hour": "14", "time": "2019-06-09T14:00:00.000-07:00"}
    - form: form_medicine
    - slot{"med_hour": ["9", "14"]}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - action_cancel_reminder

## Generated Story -3021440965482298822
* hello
    - action_greet_user
* deny
    - utter_info_later
    - utter_ask_me_anything
* set_reminder_medicine
    - form_medicine
    - form{"name": "form_medicine"}
    - slot{"requested_slot": "med_frequency"}
* form: enter_data{"med_frequency": "weekly"}
    - slot{"med_frequency": "weekly"}
    - form: form_medicine
    - slot{"med_frequency": "weekly"}
    - slot{"requested_slot": "med_name"}
* form: enter_data{"med_name": "neosaldina"}
    - slot{"med_name": "neosaldina"}
    - form: form_medicine
    - slot{"med_name": "neosaldina"}
    - slot{"requested_slot": "med_week_day"}
* form: enter_data{"time": "2019-06-10T00:00:00.000-07:00"}
    - form: form_medicine
    - slot{"med_week_day": "toda segunda feira"}
    - slot{"requested_slot": "med_hour"}
* form: enter_data{"hour": "10", "time": "2019-06-08T22:00:00.000-07:00"}
    - form: form_medicine
    - slot{"med_hour": "10"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - utter_reminder

## Generated Story 1375328854635215234
* hello
    - action_greet_user
* deny
    - utter_info_later
    - utter_ask_me_anything
* set_reminder_medicine
    - form_medicine
    - form{"name": "form_medicine"}
    - slot{"requested_slot": "med_frequency"}
* form: enter_data{"med_frequency": "one_time"}
    - slot{"med_frequency": "one_time"}
    - form: form_medicine
    - slot{"med_frequency": "one_time"}
    - slot{"requested_slot": "med_name"}
* form: enter_data{"med_name": "dipirona"}
    - slot{"med_name": "dipirona"}
    - form: form_medicine
    - slot{"med_name": "dipirona"}
    - slot{"requested_slot": "med_date"}
* form: enter_data{"time": "2019-06-09T09:00:00.000-07:00"}
    - form: form_medicine
    - slot{"med_date": "2019-06-09T09:00:00.000-07:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - utter_reminder
* thank_you
    - action_thank_you
    - rewind

## Generated Story -4137951915734004051
* hello
    - action_greet_user
* deny
    - utter_info_later
    - utter_ask_me_anything
* set_reminder_medicine
    - form_medicine
    - form{"name": "form_medicine"}
    - slot{"requested_slot": "med_frequency"}
* form: enter_data{"med_frequency": "daily"}
    - slot{"med_frequency": "daily"}
    - form: form_medicine
    - slot{"med_frequency": "daily"}
    - slot{"requested_slot": "med_name"}
* form: enter_data{"med_name": "lufital"}
    - slot{"med_name": "lufital"}
    - form: form_medicine
    - slot{"med_name": "lufital"}
    - slot{"requested_slot": "med_hour"}
* form: enter_data{"time": "2019-06-08T22:20:00.000-07:00", "hour": "20"}
    - form: form_medicine
    - slot{"med_hour": ["10", "20"]}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - action_cancel_reminder

## lembrete de consulta
* hello
    - action_greet_user
* set_reminder_appointment
  - form_appointment
  - form{"name": "form_appointment"}
  - form{"name": null}
* affirm
  - utter_reminder

## lembrete de consulta
* hello
    - action_greet_user
* set_reminder_appointment    
  - form_appointment
  - form{"name": "form_appointment"}
  - form{"name": null}
* deny
  - action_cancel_app_reminder

## unhappy path: lembrete de consulta
* set_reminder_appointment
  - form_appointment
  - form{"name": "form_appointment"}
  - form{"name": null}
* affirm
  - utter_reminder

## unhappy path: lembrete de consulta
* set_reminder_appointment
  - form_medicine
  - form{"name": "form_medicine"}
* stop
  - action_deactivate_form
  - form{"name": null}
  - utter_help
## Generated Story 9034390037895766566
* hello
    - action_greet_user
* deny
    - utter_info_later
    - utter_ask_me_anything
* set_reminder_appointment
    - form_appointment
    - form{"name": "form_appointment"}
    - slot{"requested_slot": "app_doc_name"}
* form: enter_data{"doc_name": "dr eduardo"}
    - form: form_appointment
    - slot{"app_doc_name": "dr eduardo"}
    - slot{"requested_slot": "app_date"}
* form: enter_data{"hour": "10", "time": "2019-06-20T10:00:00.000-07:00"}
    - form: form_appointment
    - slot{"app_date": "2019-06-20T10:00:00.000-07:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - utter_reminder

# perguntar se quer um lembrete de medicamento
* reminder_medicine
    - utter_ask_reminder
* affirm
    - form_medicine
    - form{"name": "form_medicine"}
    - form{"name": null}
* affirm
  - utter_reminder

# perguntar se quer um lembrete de medicamento
* reminder_medicine
    - utter_ask_reminder
* affirm
    - form_medicine
    - form{"name": "form_medicine"}
    - form{"name": null}
* deny
  - utter_cancel_reminder

# perguntar se quer um lembrete de medicamento
* reminder_medicine
    - utter_ask_reminder
* deny
    - utter_okay

# perguntar se quer um lembrete de consulta
* reminder_appointment
    - utter_ask_reminder
* affirm
    - form_appointment
    - form{"name": "form_appointment"}
    - form{"name": null}
* affirm
  - utter_reminder

# perguntar se quer um lembrete de consulta
* reminder_appointment
    - utter_ask_reminder
* affirm
    - form_appointment
    - form{"name": "form_appointment"}
    - form{"name": null}
* deny
  - utter_cancel_reminder

# perguntar se quer um lembrete de consulta
* reminder_appointment
    - utter_ask_reminder
* deny
    - utter_okay
## Generated Story 9121924420816878821
* hello
    - action_greet_user
* deny
    - utter_info_later
    - utter_ask_me_anything
* reminder_appointment
    - utter_ask_reminder
* affirm
    - form_appointment
    - form{"name": "form_appointment"}
    - slot{"requested_slot": "app_doc_name"}
* form: enter_data{"doc_name": "dr carlos"}
    - form: form_appointment
    - slot{"app_doc_name": "dr carlos"}
    - slot{"requested_slot": "app_date"}
* form: enter_data{"week_day": "quarta-feira", "time": "2019-06-12T09:00:00.000-07:00"}
    - form: form_appointment
    - slot{"app_date": "2019-06-12T09:00:00.000-07:00"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - utter_reminder

