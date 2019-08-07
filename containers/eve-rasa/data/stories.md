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
* which_medicine
    - utter_which_medicine

## bot inicia a conversa e o usuário quer responder as perguntas depois
* get_started
  - action_greet_user
* later
  - utter_info_later
  - utter_ask_me_anything
* which{"question_entity": "exercicios"}
    - action_get_answer
* which_medicine
    - utter_which_medicine

## o usuário quer responder as perguntas depois
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
* when_exam{"question_entity": "glicemia"}
    - action_get_answer
* what_to_do{"question_entity": "bolsa"}
    - action_get_answer
* complain{"question_entity": "ansia"}
    - action_get_answer
* when{"question_entity": "pre-natal"}
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

## bot pergunta se quer um lembrete de medicamento (confirmado)
* reminder_medicine
    - utter_ask_reminder
* affirm
    - form_medicine
    - form{"name": "form_medicine"}
    - form{"name": null}
* affirm
  - utter_reminder

## bot pergunta se quer um lembrete de medicamento (cancelado)
* reminder_medicine
    - utter_ask_reminder
* affirm
    - form_medicine
    - form{"name": "form_medicine"}
    - form{"name": null}
* deny
  - utter_cancel_reminder

## bot pergunta se quer um lembrete de medicamento (cancelado)
* reminder_medicine
    - utter_ask_reminder
* deny
    - utter_cancel_reminder

## bot pergunta se quer um lembrete de consulta (confirmado)
* reminder_appointment
    - utter_ask_reminder
* affirm
    - form_appointment
    - form{"name": "form_appointment"}
    - form{"name": null}
* affirm
  - utter_reminder

## bot pergunta se quer um lembrete de consulta (cancelado)
* reminder_appointment
    - utter_ask_reminder
* affirm
    - form_appointment
    - form{"name": "form_appointment"}
    - form{"name": null}
* deny
  - utter_cancel_reminder

## bot pergunta se quer um lembrete de consulta (cancelado)
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

## bot pergunta se fez o exame e o usuário não fez
    - utter_ask_exam  
* deny
    - action_get_exam
    - utter_is_important_exam
* ill_do_it OR affirm
    - utter_great

## bot pergunta se fez o exame e o usuário não fez
    - utter_ask_exam  
* did_not_exam
    - action_get_exam
    - utter_is_important_exam
* ill_do_it OR affirm
    - utter_great

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

## usuario não tem duvidas
* no_question
    - utter_ask_me_later

## usuario tem duvidas
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

## baby_not_moving
* baby_not_moving
    - utter_baby_not_moving

## form_health 1
    - utter_ask_health_questions
* affirm
    - form_health
    - form{"name": "form_health"}
    - form{"name": null}

## form_health 2
    - utter_ask_health_questions
* affirm
    - form_health
    - form{"name": "form_health"}
    - form{"name": null}
* have_question
  - utter_ask

## unhappy path: form_health
    - utter_ask_health_questions
* affirm
  - form_health
  - form{"name": "form_health"}
* what_is{"question_entity":"loquio"}
  - action_get_answer
  - form_health
  - form{"name": null}

## welcome
* welcome
    - utter_great

## Story from conversation with me on July 9th 2019
    - utter_ask_health_questions
* affirm
    - form_health
    - slot{"requested_slot":"regular_medicine"}
* enter_data{"regular_medicine":"False"}
    - slot{"regular_medicine":"False"}
    - form_health
    - slot{"regular_medicine":"False"}
    - slot{"requested_slot":"hypothyroidism"}
* enter_data{"hypothyroidism":"False"}
    - slot{"hypothyroidism":"False"}
    - form_health
    - slot{"hypothyroidism":"False"}
    - slot{"requested_slot":"hyperthyroidism"}
* enter_data{"hyperthyroidism":"False"}
    - slot{"hyperthyroidism":"False"}
    - form_health
    - slot{"hyperthyroidism":"False"}
    - slot{"requested_slot":"diabetes"}
* enter_data{"diabetes":"False"}
    - slot{"diabetes":"False"}
    - form_health
    - slot{"diabetes":"False"}
    - slot{"requested_slot":"drug_use"}
* enter_data{"drug_use":"False"}
    - slot{"drug_use":"False"}
    - form_health
    - slot{"drug_use":"False"}
    - slot{"requested_slot":"autoimmune_disease"}
* enter_data{"autoimmune_disease":"False"}
    - slot{"autoimmune_disease":"False"}
    - form_health
    - slot{"autoimmune_disease":"False"}
    - slot{"requested_slot":"asthma"}
* enter_data{"asthma":"False"}
    - slot{"asthma":"False"}
    - form_health
    - slot{"asthma":"False"}
    - slot{"requested_slot":"seropositive"}
* enter_data{"seropositive":"False"}
    - slot{"seropositive":"False"}
    - form_health
    - slot{"seropositive":"False"}
    - slot{"requested_slot":"high_pressure"}
* enter_data{"high_pressure":"False"}
    - slot{"high_pressure":"False"}
    - form_health
    - slot{"high_pressure":"False"}
    - slot{"requested_slot":null}
* welcome
    - utter_great

## form_personal 1
    - utter_ask_personal_questions
* affirm
    - form_personal
    - form{"name": "form_personal"}
    - form{"name": null}

## form_personal 2
    - utter_ask_personal_questions
* affirm
    - form_personal
    - form{"name": "form_personal"}
    - form{"name": null}
* have_question
  - utter_ask

## unhappy path: form_personal
    - utter_ask_personal_questions
* affirm
  - form_personal
  - form{"name": "form_personal"}
* what_is{"question_entity":"loquio"}
  - action_get_answer
  - form_personal
  - form{"name": null}

## welcome
* welcome
    - utter_great

## Story from conversation with me on July 9th 2019
    - utter_ask_personal_questions
* affirm
    - form_personal
    - slot{"requested_slot":"height"}
* enter_data{"height":"False"}
    - slot{"height":"False"}
    - form_personal
    - slot{"height":"False"}
    - slot{"requested_slot":"weight"}
* enter_data{"weight":"False"}
    - slot{"weight":"False"}
    - form_personal
    - slot{"weight":"False"}
    - slot{"requested_slot":"date_birth"}
* enter_data{"date_birth":"False"}
    - slot{"date_birth":"False"}
    - form_personal
    - slot{"date_birth":"False"}
    - slot{"requested_slot":"state"}
* enter_data{"state":"False"}
    - slot{"state":"False"}
    - form_personal
    - slot{"state":"False"}
    - slot{"requested_slot":null}
* welcome
    - utter_great

## form_pregnancy 1
    - utter_ask_pregnancy_questions
* affirm
    - form_pregnancy
    - form{"name": "form_pregnancy"}
    - form{"name": null}

## form_pregnancy 2
    - utter_ask_pregnancy_questions
* affirm
    - form_pregnancy
    - form{"name": "form_pregnancy"}
    - form{"name": null}
* have_question
  - utter_ask

## unhappy path: form_pregnancy
    - utter_ask_pregnancy_questions
* affirm
  - form_pregnancy
  - form{"name": "form_pregnancy"}
* what_is{"question_entity":"loquio"}
  - action_get_answer
  - form_pregnancy
  - form{"name": null}

## unhappy path: form_pregnancy 2
    - utter_ask_pregnancy_questions
* deny
    - utter_info_later
    - utter_ask_me_anything

## unhappy path: form_personal
    - utter_ask_personal_questions
* deny
    - utter_info_later
    - utter_ask_me_anything

## unhappy path: form_personal
    - utter_ask_health_questions
* deny
    - utter_info_later
    - utter_ask_me_anything

## ask_normal_birth_best
* ask_normal_birth_best
    - utter_normal_birth_best

## ask_normal_birth_pain
* ask_normal_birth_pain
    - utter_normal_birth_pain

## ask_exercise_help_normal_birth
* ask_exercise_help_normal_birth
    - utter_exercise_help_normal_birth

## ask_breast_milk_normal_birth
* ask_breast_milk_normal_birth
    - utter_breast_milk_normal_birth

## ask_normal_birth_recovery
* ask_normal_birth_recovery
    - utter_normal_birth_recovery

## ask_normal_birth_duration
* ask_normal_birth_duration
    - utter_normal_birth_duration

## ask_birth_transmit_disease
* ask_birth_transmit_disease
    - utter_birth_transmit_disease

## ask_avoid_normal_birth
* ask_avoid_normal_birth
    - utter_avoid_normal_birth

## ask_ideal_birth_older_women
* ask_ideal_birth_older_women
    - utter_ideal_birth_older_women

## ask_calculate_fertile_period
* ask_calculate_fertile_period
    - utter_calculate_fertile_period

## ask_late_menstruation
* ask_late_menstruation
    - utter_late_menstruation

## ask_do_pregnancy_test
* ask_do_pregnancy_test
    - utter_do_pregnancy_test

## ask_normal_swollen_foot
* ask_normal_swollen_foot
    - utter_normal_swollen_foot

## ask_how_long_milk_come_down
* ask_how_long_milk_come_down
    - utter_how_long_milk_come_down

## ask_normal_fever_milk_comes_down
* ask_normal_fever_milk_comes_down
    - utter_normal_fever_milk_comes_down

## ask_prevent_milk_stumbling
* ask_prevent_milk_stumbling
    - utter_prevent_milk_stumbling

## ask_pain_breastfeed
* ask_pain_breastfeed
    - utter_pain_breastfeed

## ask_thirst_breastfeed
* ask_thirst_breastfeed
    - utter_thirst_breastfeed

## ask_feeling_sad
* ask_feeling_sad
    - utter_feeling_sad

## ask_diet_breastfeed
* ask_diet_breastfeed
    - utter_diet_breastfeed

## ask_gain_weight_pregnancy
* ask_gain_weight_pregnancy
    - utter_gain_weight_pregnancy

## ask_when_have_sex
* ask_when_have_sex
    - utter_when_have_sex

## ask_stretch_marks
* ask_stretch_marks
    - utter_stretch_marks

## ask_desire_sex
* ask_desire_sex
    - utter_desire_sex

## ask_loose_vagina
* ask_loose_vagina
    - utter_loose_vagina

## ask_sagging_breasts_breastfeed
* ask_sagging_breasts_breastfeed
    - utter_sagging_breasts_breastfeed

## ask_body_back_normal
* ask_body_back_normal
    - utter_body_back_normal

## ask_back_exercise
* ask_back_exercise
    - utter_back_exercise

## ask_loss_hair_breastfeed
* ask_loss_hair_breastfeed
    - utter_loss_hair_breastfeed

## ask_exercise_impair_milk
* ask_exercise_impair_milk
    - utter_exercise_impair_milk

## ask_normal_bleeding_after_birth
* ask_normal_bleeding_after_birth
    - utter_normal_bleeding_after_birth

## ask_normal_menstruation_breastfeed
* ask_normal_menstruation_breastfeed
    - utter_normal_menstruation_breastfeed

## ask_dye_hair_breastfeed
* ask_dye_hair_breastfeed
    - utter_dye_hair_breastfeed

## ask_normal_lose_weight_breastfeed
* ask_normal_lose_weight_breastfeed
    - utter_normal_lose_weight_breastfeed

## ask_normal_feeling_tired
* ask_normal_feeling_tired
    - utter_normal_feeling_tired

## ask_normal_bigger_foot
* ask_normal_bigger_foot
    - utter_normal_bigger_foot

## ask_pregnant_menopause
* ask_pregnant_menopause
    - utter_pregnant_menopause

## ask_sex_bad_pregnancy
* ask_sex_bad_pregnancy
    - utter_sex_bad_pregnancy

## ask_feces_normal_birth
* ask_feces_normal_birth
    - utter_feces_normal_birth

## ask_sore_sex_after_birth
* ask_sore_sex_after_birth
    - utter_sore_sex_after_birth

## ask_have_sex_until_month
* ask_have_sex_until_month
    - utter_have_sex_until_month

## ask_receive_oral_sex
* ask_receive_oral_sex
    - utter_receive_oral_sex

## ask_smell_sweat_stronger
* ask_smell_sweat_stronger
    - utter_smell_sweat_stronger

## ask_normal_discharge_pregnancy
* ask_normal_discharge_pregnancy
    - utter_normal_discharge_pregnancy

## ask_sex_hurt_baby
* ask_sex_hurt_baby
    - utter_sex_hurt_baby

## ask_choose_birth_type_public
* ask_choose_birth_type_public
    - utter_choose_birth_type_public

## ask_pregnant_eat_two
* ask_pregnant_eat_two
    - utter_pregnant_eat_two

## ask_avoid_cleaning_products
* ask_avoid_cleaning_products
    - utter_avoid_cleaning_products

## ask_best_position_baby_sleep
* ask_best_position_baby_sleep
    - utter_best_position_baby_sleep

## ask_what_vaccines_baby
* ask_what_vaccines_baby
    - utter_what_vaccines_baby

## ask_when_go_pediatrician
* ask_when_go_pediatrician
    - utter_when_go_pediatrician

## ask_care_baby_belly_button
* ask_care_baby_belly_button
    - utter_care_baby_belly_button

## ask_birth_control_difficult_pregnancy
* ask_birth_control_difficult_pregnancy
    - utter_birth_control_difficult_pregnancy

## ask_normal_headache_pregnancy
* ask_normal_headache_pregnancy
    - utter_normal_headache_pregnancy

## ask_how_many_pounds_pregnancy
* ask_how_many_pounds_pregnancy
    - utter_how_many_pounds_pregnancy

## ask_how_long_breastfeed
* ask_how_long_breastfeed
    - utter_how_long_breastfeed

## ask_how_long_healthy_pregnant
* ask_how_long_healthy_pregnant
    - utter_how_long_healthy_pregnant

## Story from conversation with me on July 31st 2019

* ask_choose_birth_type_public
    - utter_choose_birth_type_public
* ask_choose_birth_type_public
    - utter_choose_birth_type_public
* ask_loose_vagina
    - utter_loose_vagina

## Story from conversation with me on July 31st 2019

* ask_choose_birth_type_public
    - utter_choose_birth_type_public
* ask_choose_birth_type_public
    - utter_choose_birth_type_public
* ask_loose_vagina
    - action_default_fallback
* ask_loose_vagina
    - utter_loose_vagina
* ask_feces_normal_birth
    - utter_feces_normal_birth
* ask_sex_hurt_baby
    - utter_sex_hurt_baby
* ask_normal_discharge_pregnancy
    - utter_normal_discharge_pregnancy
* ask_smell_sweat_stronger
    - utter_smell_sweat_stronger
* ask_receive_oral_sex
    - utter_receive_oral_sex
* ask_have_sex_until_month
    - utter_have_sex_until_month
* ask_sore_sex_after_birth
    - utter_sore_sex_after_birth
## Generated Story -4178839390444423351
* hello
    - action_greet_user

## Generated Story -6771195614729549971
* can{"question_entity": "raio x"}
    - action_get_answer
    - slot{"last_intent": "can"}
* im_pregnant{"time": "2019-08-06T19:19:35.000-07:00"}
    - utter_congrats
    - utter_first_step
    - utter_ask_info

## Generated Story 2621393950485477002
* can{"question_entity": "cabelo"}
    - action_get_answer
    - slot{"last_intent": "can"}
* can{"question_entity": "dentista"}
    - action_get_answer
    - slot{"last_intent": "can"}
* can{"question_entity": "sexo"}
    - action_get_answer
    - slot{"last_intent": "can"}
* can{"question_entity": "rela\u00e7\u00f5es sexuais"}
    - action_get_answer
    - slot{"last_intent": "can"}
* im_pregnant{"time": "2019-08-06T20:44:28.000-07:00"}
    - utter_congrats
    - utter_first_step
    - utter_ask_info

## Generated Story 1492885391058787124
* can{"question_entity": "salto alto"}
    - action_get_answer
    - slot{"last_intent": "can"}
* can{"question_entity": "cigarro"}
    - action_get_answer
    - slot{"last_intent": "can"}
* can{"question_entity": "sexo"}
    - action_get_answer
    - slot{"last_intent": "can"}
* can{"question_entity": "sexo"}
    - action_get_answer
    - slot{"last_intent": "can"}
* can{"question_entity": "sexo"}
    - action_get_answer
    - slot{"last_intent": "can"}
* can{"question_entity": "exercicios"}
    - action_get_answer
    - slot{"last_intent": "can"}
* ask_feces_normal_birth
    - utter_feces_normal_birth
* ask_loose_vagina
    - utter_loose_vagina
* ask_smell_sweat_stronger
    - utter_smell_sweat_stronger
* ask_receive_oral_sex
    - utter_receive_oral_sex
* ask_have_sex_until_month
    - utter_have_sex_until_month
* ask_sore_sex_after_birth
    - utter_sore_sex_after_birth

## Generated Story 4782866021833329566
* ask_receive_oral_sex
    - utter_receive_oral_sex
* ask_smell_sweat_stronger
    - utter_smell_sweat_stronger
* ask_normal_discharge_pregnancy
    - utter_normal_discharge_pregnancy
* ask_loose_vagina
    - utter_loose_vagina

## Generated Story 3897647428770637518
* can{"question_entity": "dirigir"}
    - action_get_answer
    - slot{"last_intent": "can"}
* which{"question_entity": "parto"}
    - action_get_answer
    - slot{"last_intent": "which"}

## Generated Story -4846044068828919887
* which{"question_entity": "parto"}
    - action_get_answer
    - slot{"last_intent": "which"}
* ask_normal_discharge_pregnancy
    - utter_normal_discharge_pregnancy
* can{"question_entity": "cigarro"}
    - action_get_answer
    - slot{"last_intent": "can"}
* can{"question_entity": "sexo"}
    - action_get_answer
    - slot{"last_intent": "can"}

## Generated Story 7789138662663016432
* can{"question_entity": "cigarro"}
    - action_get_answer
    - slot{"last_intent": "can"}
* which{"question_entity": "parto"}
    - action_get_answer
    - slot{"last_intent": "which"}
* can{"question_entity": "sexo"}
    - action_get_answer
    - slot{"last_intent": "can"}

## Generated Story 8778707381967773006
* can{"question_entity": "sexo"}
    - action_get_answer
    - slot{"last_intent": "can"}
* which{"question_entity": "parto"}
    - action_get_answer
    - slot{"last_intent": "which"}

