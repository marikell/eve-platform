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
    - slot{"last_intent": "which"}
    - get_answer
* which_not{"question_entity": "comida"}
    - slot{"last_intent": "which_not"}
    - get_answer
* can{"question_entity": "exercicios"}
    - slot{"last_intent": "can"}
    - get_answer
* which{"question_entity": "exercicios"}
    - slot{"last_intent": "which"}
    - get_answer
* which{"question_entity": "treinos"}
    - slot{"last_intent": "which"}
    - get_answer
* which_not{"question_entity": "treinos"}
    - slot{"last_intent": "which_not"}
    - get_answer

## get_answer_2
* get_started
  - action_greet_user
* which{"question_entity": "exercicios"}
    - slot{"last_intent": "which"}
    - get_answer
* which{"question_entity": "treinos"}
    - slot{"last_intent": "which"}
    - get_answer

## Generated Story -8569811712381873528
* get_started
    - action_greet_user
* greeting_answer
    - utter_ask_info
* which{"question_entity": "exercicios"}
    - slot{"last_intent": "which"}
    - get_answer
* which_not{"question_entity": "alimentos"}
    - slot{"last_intent": "which_not"}
    - get_answer

##1233123
* which{"question_entity": "alimentos"}
    - slot{"last_intent": "which"}
    - get_answer
* which_not{"question_entity": "exercicio"}
    - slot{"last_intent": "which_not"}
    - get_answer
* symptom{"question_entity": "gravidez"}
    - slot{"last_intent": "symptom"}
    - get_answer
* prevent{"question_entity": "pre-eclampsia"}
    - slot{"last_intent": "prevent"}
    - get_answer
* what_is{"question_entity": "loquio"}
    - slot{"last_intent": "what_is"}
    - get_answer
* complain{"question_entity": "costas"}
    - slot{"last_intent": "complain"}
    - get_answer
* causes{"question_entity": "pre-eclampsia"}
    - slot{"last_intent": "causes"}
    - get_answer
* how_to_know{"question_entity": "bolsa"}
    - slot{"last_intent": "how_to_know"}
    - get_answer

##1233123
* which{"question_entity": "alimentos"}
    - get_answer
    - slot{"last_intent": "which"}
* last_intent{"question_entity": "exercicio"}
    - slot{"last_intent": "which"}
    - get_answer
* symptom{"question_entity": "gravidez"}
    - slot{"last_intent": "symptom"}
    - get_answer
* prevent{"question_entity": "pre-eclampsia"}
    - slot{"last_intent": "prevent"}
    - get_answer
* what_is{"question_entity": "loquio"}
    - slot{"last_intent": "what_is"}
    - get_answer
* last_intent{"question_entity": "puerperio"}
    - slot{"last_intent": "what_is"}
    - get_answer
* causes{"question_entity": "pre-eclampsia"}
    - slot{"last_intent": "causes"}
    - get_answer
* how_to_know{"question_entity": "bolsa"}
    - slot{"last_intent": "how_to_know"}
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

## unhappy path: lembrete de remédio
* set_reminder_med
  - medicine_form
  - form{"name": "medicine_form"}
  - form{"name": null}
  - utter_help

## unhappy path: lembrete de remédio
* set_reminder_med
  - medicine_form
  - form{"name": "medicine_form"}
* stop
  - action_deactivate_form
  - form{"name": null}
  - utter_help
