## bot inicia a conversa e o usuário (gestante)
* get_started
  - action_greet_user
* affirm
  - form_initial
  - form{"name": "form_initial"}
  - form{"name": null}
  - utter_ask_me_anything

## bot inicia a conversa e o usuário nao quer responder as perguntas
* get_started
  - action_greet_user
* deny
  - utter_info_later
  - utter_ask_me_anything
* which{"question_entity": "exercicios"}
    - action_get_answer

## bot inicia a conversa e o usuário quer responder as perguntas depois
* get_started
  - action_greet_user
* later
  - utter_info_later
  - utter_ask_me_anything
* which{"question_entity": "exercicios"}
    - action_get_answer

# o usuário quer responder as perguntas depois
* later
  - utter_info_later

## o usuário inicia a conversa com apenas 'Oi' (gestante)
* hello
  - action_greet_user
* affirm
  - form_initial
  - form{"name": "form_initial"}
  - form{"name": null}
  - utter_ask_me_anything

## o usuário inicia a conversa com apenas 'Oi' e não quer responder as perguntas
* hello
  - action_greet_user
* deny
  - utter_info_later
  - utter_ask_me_anything

## o usuário inicia a conversa com apenas 'Oi' e quer responder as perguntas depois
* hello
  - action_greet_user
* later
  - utter_info_later
  - utter_ask_me_anything

## o usuário inicia a conversa com 'Oi tudo bem?' (gestante)
* greeting
  - action_greet_user
* greeting_answer
  - utter_ask_info
* affirm
  - form_initial
  - form{"name": "form_initial"}
  - form{"name": null}
  - utter_ask_me_anything

## o usuário inicia a conversa com 'Oi tudo bem?' e nao quer responder as perguntas
* greeting
  - action_greet_user
* greeting_answer
  - utter_ask_info
* deny
  - utter_info_later
  - utter_ask_me_anything

## o usuário inicia a conversa com 'Oi tudo bem?' e quer responder as perguntas depois
* greeting
  - action_greet_user
* greeting_answer
  - utter_ask_info
* later
  - utter_info_later
  - utter_ask_me_anything

## 'Oi tudo bem?'
* greeting
    - action_greet_user
* greeting_answer
  - utter_ask_info

## perguntas aleatórias 1
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

## perguntas aleatórias 2
* get_started
  - action_greet_user
* which{"question_entity": "exercicios"}
    - slot{"last_intent": "which"}
    - action_get_answer
* which{"question_entity": "treinos"}
    - slot{"last_intent": "which"}
    - action_get_answer

## perguntas aleatórias 3
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

## perguntas aleatórias 4
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

## perguntas aleatórias 5
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

## perguntas aleatórias 6
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

## unhappy path: bot inicia a conversa (gestante)
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

## unhappy path: o usuário inicia a conversa com apenas 'Oi' (gestante)
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

## unhappy path: o usuário inicia a conversa com apenas 'Oi' (gestante)
* hello
  - action_greet_user
* affirm
  - form_initial
  - form{"name": "form_initial"}
* why_i_need_to_answer
  - utter_why_answer
  - form_initial
  - form{"name": null}
  - utter_ask_me_anything

## unhappy path: bot inicia a conversa e o usuário e pede para o bot parar as perguntas (gestante)
* get_started
  - action_greet_user
* affirm
  - form_initial
  - form{"name": "form_initial"}
* stop
  - action_deactivate_form
  - form{"name": null}
  - utter_ask_me_anything

## unhappy path: o usuário inicia a conversa com apenas 'Oi' e pede para o bot parar as perguntas (gestante)
* hello
  - action_greet_user
* affirm
  - form_initial
  - form{"name": "form_initial"}
* stop
  - action_deactivate_form
  - form{"name": null}
  - utter_ask_me_anything

## lembrete de remédio confirmado
* hello
    - action_greet_user
* set_reminder_medicine    
  - form_medicine
  - form{"name": "form_medicine"}
  - form{"name": null}
* affirm
  - utter_reminder

## lembrete de remédio confirmado 2
* set_reminder_medicine
  - form_medicine
  - form{"name": "form_medicine"}
  - form{"name": null}
* affirm
  - utter_reminder

## lembrete de remédio cancelado
* hello
    - action_greet_user
* set_reminder_medicine    
  - form_medicine
  - form{"name": "form_medicine"}
  - form{"name": null}
* deny
  - action_cancel_reminder

## unhappy path: lembrete de remédio cancelado
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

## lembrete de consulta confirmado
* hello
    - action_greet_user
* set_reminder_appointment
  - form_appointment
  - form{"name": "form_appointment"}
  - form{"name": null}
* affirm
  - utter_reminder

## lembrete de consulta confirmado 2
* set_reminder_appointment
  - form_appointment
  - form{"name": "form_appointment"}
  - form{"name": null}
* affirm
  - utter_reminder

## lembrete de consulta cancelado
* hello
    - action_greet_user
* set_reminder_appointment    
  - form_appointment
  - form{"name": "form_appointment"}
  - form{"name": null}
* deny OR stop
  - action_cancel_app_reminder

## unhappy path: lembrete de consulta cancelado
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

# bot pergunta se quer um lembrete de medicamento (confirmado)
* reminder_medicine
    - utter_ask_reminder
* affirm
    - form_medicine
    - form{"name": "form_medicine"}
    - form{"name": null}
* affirm
  - utter_reminder

# bot pergunta se quer um lembrete de medicamento (cancelado)
* reminder_medicine
    - utter_ask_reminder
* affirm
    - form_medicine
    - form{"name": "form_medicine"}
    - form{"name": null}
* deny
  - utter_cancel_reminder

# bot pergunta se quer um lembrete de medicamento (cancelado)
* reminder_medicine
    - utter_ask_reminder
* deny
    - utter_cancel_reminder

# bot pergunta se quer um lembrete de consulta (confirmado)
* reminder_appointment
    - utter_ask_reminder
* affirm
    - form_appointment
    - form{"name": "form_appointment"}
    - form{"name": null}
* affirm
  - utter_reminder

# bot pergunta se quer um lembrete de consulta (cancelado)
* reminder_appointment
    - utter_ask_reminder
* affirm
    - form_appointment
    - form{"name": "form_appointment"}
    - form{"name": null}
* deny
  - utter_cancel_reminder

# bot pergunta se quer um lembrete de consulta (cancelado)
* reminder_appointment
    - utter_ask_reminder
* deny
    - utter_cancel_reminder

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

## bot pergunta se fez o exame e o usuário fez
    - utter_ask_exam
* affirm
    - action_doing_right_exam

## bot pergunta se fez o exame e o usuário fez
    - utter_ask_exam
* did_exam
    - action_doing_right_exam

## bot pergunta se fez o exame e o usuário não fez
    - utter_ask_exam  
* deny
    - action_get_exam
    - utter_is_important_exam

## bot pergunta se fez o exame e o usuário não fez
    - utter_ask_exam  
* did_not_exam
    - action_get_exam
    - utter_is_important_exam

## bot pergunta se fez o exame, o usuário fez mas quer saber o motivo da pergunta
    - utter_ask_exam  
* why_i_need_to_answer
    - utter_why_answer
* did_exam
    - action_doing_right_exam

## bot pergunta se fez o exame, o usuário fez mas quer saber o motivo da pergunta
    - utter_ask_exam  
* why_i_need_to_answer
    - utter_why_answer
* affirm
    - utter_ask_exam
* did_exam
    - action_doing_right_exam

## bot pergunta se fez o exame, o usuário fez mas quer saber o motivo da pergunta
    - utter_ask_exam  
* why_i_need_to_answer
    - utter_why_answer
* affirm
    - utter_ask_exam
* affirm
    - action_doing_right_exam

## bot pergunta se fez o exame, o usuário não fez mas quer saber o motivo da pergunta
    - utter_ask_exam  
* why_i_need_to_answer
    - utter_why_answer
* affirm
    - utter_ask_exam
* deny
    - action_get_exam
    - utter_is_important_exam

## bot pergunta se fez o exame, o usuário não fez mas quer saber o motivo da pergunta
    - utter_ask_exam  
* why_i_need_to_answer
    - utter_why_answer
* affirm
    - utter_ask_exam
* did_not_exam
    - action_get_exam
    - utter_is_important_exam

## bot pergunta se fez o exame, o usuário fez e sabe a importância do exame
    - utter_ask_exam
* affirm
    - action_doing_right_exam
* i_know_importance
    - utter_agree

## bot pergunta se fez o exame, o usuário fez e sabe a importância do exame
    - utter_ask_exam
* did_exam
    - action_doing_right_exam
* i_know_importance
    - utter_agree

## sabe a importancia dos exames e do pré-natal
* i_know_importance
    - utter_agree

## o usuário inicia a conversa com apenas 'Oi' e quer saber o motivo das perguntas (gestante)
* hello
  - action_greet_user
* why_i_need_to_answer
  - utter_why_answer
* affirm
  - form_initial
  - form{"name": "form_initial"}
  - form{"name": null}
  - utter_ask_me_anything

## o usuário inicia a conversa com apenas 'Oi' e quer saber o motivo das perguntas (gestante)
* hello
  - action_greet_user
* affirm
  - form_initial
  - form{"name": "form_initial"}
* why_i_need_to_answer
  - utter_why_answer
  - form_initial
  - form{"name": null}
  - utter_ask_me_anything

## Generated Story -2517970030274559833
* hello
    - action_greet_user
* why_i_need_to_answer
    - utter_why_answer
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - slot{"requested_slot": "is_pregnant"}
* form: enter_data{"is_pregnant": "False"}
    - slot{"is_pregnant": "False"}
    - form: form_initial
    - slot{"is_pregnant": "False"}
    - slot{"requested_slot": "is_trying"}
* form: enter_data{"is_trying": "True"}
    - slot{"is_trying": "True"}
    - form: form_initial
    - slot{"is_trying": "True"}
    - slot{"requested_slot": "is_planning"}
* form: enter_data{"is_planning": "False"}
    - slot{"is_planning": "False"}
    - form: form_initial
    - slot{"is_planning": "False"}
    - slot{"requested_slot": "has_children"}
* form: enter_data{"has_children": "False"}
    - slot{"has_children": "False"}
    - form: form_initial
    - slot{"has_children": "False"}
    - slot{"requested_slot": "health_plan"}
* form: enter_data{"health_plan": "False"}
    - slot{"health_plan": "False"}
    - form: form_initial
    - slot{"health_plan": "False"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_me_anything
* reminder_medicine
    - utter_ask_reminder
* deny
    - utter_cancel_reminder

# usuario não tem duvidas
* no_question
    - utter_ask_me_later

# usuario tem duvidas
* have_question
    - utter_ask

## o usuário inicia a conversa com apenas 'Oi' (gestante) e não tem duvidas
* hello
  - action_greet_user
* affirm
  - form_initial
  - form{"name": "form_initial"}
  - form{"name": null}
  - utter_ask_me_anything
* no_question
  - utter_ask_me_later

## o usuário inicia a conversa com apenas 'Oi' (gestante) e tem duvidas
* hello
  - action_greet_user
* affirm
  - form_initial
  - form{"name": "form_initial"}
  - form{"name": null}
  - utter_ask_me_anything
* have_question
  - utter_ask

## Generated Story 4935868663189737503
* hello
    - action_greet_user
* affirm
    - form_initial
    - form{"name": "form_initial"}
    - slot{"requested_slot": "is_pregnant"}
* form: enter_data{"is_pregnant": "True"}
    - slot{"is_pregnant": "True"}
    - form: form_initial
    - slot{"is_pregnant": "True"}
    - slot{"requested_slot": "pregnancy_weeks"}
* form: enter_data{"pregnancy_weeks": "6"}
    - slot{"pregnancy_weeks": "6"}
    - form: form_initial
    - slot{"pregnancy_weeks": "6"}
    - slot{"requested_slot": "planned_pregnancy"}
* form: enter_data{"planned_pregnancy": "False"}
    - slot{"planned_pregnancy": "False"}
    - form: form_initial
    - slot{"planned_pregnancy": "False"}
    - slot{"requested_slot": "first_pregnancy"}
* form: enter_data{"first_pregnancy": "True"}
    - slot{"first_pregnancy": "True"}
    - form: form_initial
    - slot{"first_pregnancy": "True"}
    - slot{"requested_slot": "health_plan"}
* form: enter_data{"health_plan": "False"}
    - slot{"health_plan": "False"}
    - form: form_initial
    - slot{"health_plan": "False"}
    - slot{"requested_slot": "pre_natal"}
* form: enter_data{"pre_natal": "False"}
    - slot{"pre_natal": "False"}
    - form: form_initial
    - slot{"pre_natal": "False"}
    - form{"name": null}
    - slot{"requested_slot": null}

