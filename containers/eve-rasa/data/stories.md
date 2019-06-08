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
* which{"question_entity": "exercicios"}
    - get_answer

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
* which{"question_entity": "exercicios"}
    - get_answer

## a mulher inicia a conversa com 'Oi tudo bem?' e nao quer responder as perguntas
* greeting
  - action_greet_user
* greeting_answer
  - utter_ask_info
* deny
  - utter_info_later
  - utter_ask_me_anything

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

## bye
* bye
- utter_bye

## thank_you
* thank_you
- utter_welcome

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
* thank_you
    - utter_welcome
    - utter_help

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

## Generated Story 6158015074139116326
* im_pregnant
    - utter_congrats
    - utter_first_step
    - utter_ask_info
* affirm
  - initial_form
  - form{"name": "initial_form"}
  - form{"name": null}
  - utter_ask_me_anything

## bot inicia a conversa e a mulher esta gravida
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

## a mulher inicia a conversa com apenas 'Oi' e esta gravida
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
* which{"question_entity": "exercicios"}
    - get_answer

## bot inicia a conversa e a mulher esta gravida e pede para o bot parar as perguntas
* get_started
  - action_greet_user
* affirm
  - initial_form
  - form{"name": "initial_form"}
* stop
  - action_deactivate_form
  - form{"name": null}
  - utter_ask_me_anything

## a mulher inicia a conversa com apenas 'Oi' e esta gravida e pede para o bot parar as perguntas
* hello
  - action_greet_user
* affirm
  - initial_form
  - form{"name": "initial_form"}
* stop
  - action_deactivate_form
  - form{"name": null}
  - utter_ask_me_anything
* which{"question_entity": "exercicios"}
    - get_answer

## Story from conversation with me on June 4th 2019

* hello
    - action_greet_user
* affirm
    - initial_form
    - slot{"requested_slot":"is_pregnant"}

## Story from conversation with me on June 4th 2019

* hello
    - action_greet_user
* affirm
    - initial_form
    - slot{"requested_slot":"is_pregnant"}
* enter_data{"is_pregnant":"False"}
    - slot{"is_pregnant":"False"}
    - initial_form
    - slot{"is_pregnant":"False"}
    - slot{"requested_slot":"is_trying"}
* can{"question_entity":"vacinas"}
    - get_answer
    - initial_form
    - slot{"requested_slot":"is_trying"}
