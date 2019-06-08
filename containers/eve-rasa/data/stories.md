## bot inicia a conversa e a mulher esta gravida
* get_started
  - action_greet_user
* affirm
  - initial_form
  - form{"name": "initial_form"}
  - form{"name": null}
  - utter_ask_me_anything

## bot inicia a conversa e a mulher nao quer responder as perguntas
* get_started
  - action_greet_user
* deny
  - utter_info_later
  - utter_ask_me_anything
* which{"question_entity": "exercicios"}
    - get_answer

## a mulher inicia a conversa com apenas 'Oi' e esta gravida
* hello
  - action_greet_user
* affirm
  - initial_form
  - form{"name": "initial_form"}
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
  - initial_form
  - form{"name": "initial_form"}
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

## get_answer
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
    - utter_ask_info
* which{"question_entity": "exercicios"}
    - get_answer
* which_not{"question_entity": "alimentos"}
    - get_answer

##1233123
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
* complain{"question_entity": "costas"}
    - get_answer
* causes{"question_entity": "pre-eclampsia"}
    - get_answer
* how_to_know{"question_entity": "bolsa"}
    - get_answer

## Generated Story 4646674987687058942
* goal_exam{"question_entity": "glicemia"}
    - get_answer
* when_exame{"question_entity": "glicemia"}
    - get_answer
* what_to_do{"question_entity": "bolsa"}
    - get_answer
* complain{"question_entity": "ansia"}
    - get_answer
* when{"question_entity": "pre natal"}
    - get_answer
* why{"question_entity": "sono"}
    - get_answer

## estou gravida
* im_pregnant
    - utter_congrats
    - utter_first_step
    - utter_ask_info
* affirm
  - initial_form
  - form{"name": "initial_form"}
  - form{"name": null}
  - utter_ask_me_anything

## unhappy path: bot inicia a conversa e a mulher esta gravida
* get_started
  - action_greet_user
* affirm
  - initial_form
  - form{"name": "initial_form"}
* what_is{"question_entity":"loquio"}
  - get_answer
  - initial_form
  - form{"name": null}
  - utter_ask_me_anything

## unhappy path: a mulher inicia a conversa com apenas 'Oi' e esta gravida
* hello
  - action_greet_user
* affirm
  - initial_form
  - form{"name": "initial_form"}
* why{"question_entity":"sono"}
  - get_answer
  - initial_form
  - form{"name": null}
  - utter_ask_me_anything

## unhappy path: bot inicia a conversa e a mulher esta gravida e pede para o bot parar as perguntas
* get_started
  - action_greet_user
* affirm
  - initial_form
  - form{"name": "initial_form"}
* stop
  - action_deactivate_form
  - form{"name": null}
  - utter_ask_me_anything

## unhappy path: a mulher inicia a conversa com apenas 'Oi' e esta gravida e pede para o bot parar as perguntas
* hello
  - action_greet_user
* affirm
  - initial_form
  - form{"name": "initial_form"}
* stop
  - action_deactivate_form
  - form{"name": null}
  - utter_ask_me_anything

## lembrete de remédio
* hello
    - action_greet_user
* set_reminder_med    
  - medicine_form
  - form{"name": "medicine_form"}
  - form{"name": null}
* thank_you
  - utter_help

## unhappy path: a mulher inicia a conversa com apenas 'Oi' e esta gravida e pede para o bot parar as perguntas
* set_reminder_med
  - medicine_form
  - form{"name": "medicine_form"}
  - form{"name": null}
  - utter_help

## asd
* set_reminder_med
  - medicine_form
  - form{"name": "medicine_form"}
* stop
  - action_deactivate_form
  - form{"name": null}
  - utter_help

## Story from conversation with me on June 8th 2019

* hello
    - action_greet_user
* affirm
    - initial_form
    - slot{"requested_slot":"is_pregnant"}
* enter_data{"is_pregnant":"True"}
    - slot{"is_pregnant":"True"}
    - initial_form
    - slot{"is_pregnant":"True"}
    - slot{"requested_slot":"pregnancy_weeks"}
* enter_data{"pregnancy_weeks":"15"}
    - slot{"pregnancy_weeks":"15"}
    - initial_form
    - slot{"pregnancy_weeks":"15"}
    - slot{"requested_slot":"planned_pregnancy"}
* enter_data{"planned_pregnancy":"False"}
    - slot{"planned_pregnancy":"False"}
    - initial_form
    - slot{"planned_pregnancy":"False"}
    - slot{"requested_slot":"first_pregnancy"}
* enter_data{"first_pregnancy":"True"}
    - slot{"first_pregnancy":"True"}
    - initial_form
    - slot{"first_pregnancy":"True"}
    - slot{"requested_slot":"health_plan"}
* enter_data{"health_plan":"True"}
    - slot{"health_plan":"True"}
    - initial_form
    - slot{"health_plan":"True"}
    - slot{"requested_slot":"pre_natal"}
* enter_data{"pre_natal":"False"}
    - slot{"pre_natal":"False"}
    - initial_form
    - slot{"pre_natal":"False"}
    - slot{"requested_slot":null}
    - utter_ask_me_anything
* can{"question_entity":"exercicios"}
    - get_answer
