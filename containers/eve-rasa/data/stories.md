## bot inicia a conversa e a mulher esta gravida
* get_started
  - action_greet_user
* affirm
  - utter_ask_is_pregnant
* affirm
  - utter_congrats
  - initial_form
  - form{"name": "initial_form"}
  - form{"name": null}
  - utter_thank_you
  - utter_first_help
* which{"question_entity": "exercicios"}
    - get_answer

## bot inicia a conversa e a mulher não esta gravida mas esta tentando engravidar
* get_started
  - action_greet_user
* affirm
  - utter_ask_is_pregnant
* deny
  - utter_ask_trying_pregnant
* affirm
  - utter_trying_pregnant
  - utter_first_help
* which{"question_entity": "exercicios"}
    - get_answer

## bot inicia a conversa e a mulher nao esta gravida e nao esta tentando engravidar
* get_started
  - action_greet_user
* affirm
  - utter_ask_is_pregnant
* deny
  - utter_ask_trying_pregnant
* deny
  - utter_first_help
* which{"question_entity": "exercicios"}
    - get_answer

## bot inicia a conversa e a mulher nao quer responder as perguntas
* get_started
  - action_greet_user
* deny
  - utter_info_later
  - utter_first_help
* which{"question_entity": "exercicios"}
    - get_answer

## a mulher inicia a conversa com apenas 'Oi' e esta gravida
* hello
  - action_greet_user
* affirm
  - utter_ask_is_pregnant
* affirm
  - utter_congrats
  - initial_form
  - form{"name": "initial_form"}
  - form{"name": null}
  - utter_thank_you
  - utter_first_help
* which{"question_entity": "exercicios"}
    - get_answer

## a mulher inicia a conversa com apenas 'Oi' e nao esta gravida mas esta tentando engravidar
* hello
  - action_greet_user
* affirm
  - utter_ask_is_pregnant
* deny
  - utter_ask_trying_pregnant
* affirm
  - utter_trying_pregnant
  - utter_first_help
* which{"question_entity": "exercicios"}
    - get_answer

## a mulher inicia a conversa com apenas 'Oi' e nao esta gravida e nao esta tentando engravidar
* hello
  - action_greet_user
* affirm
  - utter_ask_is_pregnant
* deny
  - utter_ask_trying_pregnant
* deny
  - utter_thank_you
  - utter_first_help

## a mulher inicia a conversa com apenas 'Oi' e quer responder as perguntas
* hello
  - action_greet_user
* deny
  - utter_info_later
  - utter_first_help

## a mulher inicia a conversa com 'Oi tudo bem?' e esta gravida
* greeting
  - action_greet_user
* greeting_answer
  - utter_ask_info
* affirm
  - utter_ask_is_pregnant
* affirm
  - utter_congrats
  - initial_form
  - form{"name": "initial_form"}
  - form{"name": null}
  - utter_thank_you
  - utter_first_help
* which{"question_entity": "exercicios"}
    - get_answer

## a mulher inicia a conversa com 'Oi tudo bem?' e nao esta gravida mas esta tentando engravidar
* greeting
  - action_greet_user
* greeting_answer
  - utter_ask_info
* affirm
  - utter_ask_is_pregnant
* deny
  - utter_ask_trying_pregnant
* affirm
  - utter_trying_pregnant
  - utter_first_help
* which{"question_entity": "exercicios"}
    - get_answer

## a mulher inicia a conversa com 'Oi tudo bem?' e nao esta gravida e nao esta tentando engravidar
* greeting
  - action_greet_user
* greeting_answer
  - utter_ask_info
* affirm
  - utter_ask_is_pregnant
* deny
  - utter_ask_trying_pregnant
* deny
  - utter_thank_you
  - utter_first_help
* which{"question_entity": "exercicios"}
    - get_answer

## a mulher inicia a conversa com 'Oi tudo bem?' e nao quer responder as perguntas
* greeting
  - action_greet_user
* greeting_answer
  - utter_ask_info
* deny
  - utter_info_later
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

## Generated Story 707944168274727227
* hello
    - action_greet_user
* affirm
    - utter_ask_is_pregnant
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
  - utter_thank_you
  - utter_first_help

## Generated Story -8676088873807953507
* hello
    - action_greet_user
* affirm
    - utter_ask_is_pregnant
* affirm
    - utter_congrats
    - initial_form
    - form{"name": "initial_form"}
    - slot{"requested_slot": "pregnancy_weeks"}
* form: enter_data{"pregnancy_weeks": "10"}
    - slot{"pregnancy_weeks": "10"}
    - form: initial_form
    - slot{"pregnancy_weeks": "10"}
    - slot{"requested_slot": "planned_pregnancy"}
## Generated Story -9169979720908617369
* hello
    - action_greet_user
* affirm
    - utter_ask_is_pregnant
* affirm
    - utter_congrats
    - initial_form
    - form{"name": "initial_form"}
    - slot{"requested_slot": "pregnancy_weeks"}
* form: enter_data{"pregnancy_weeks": "12"}
    - slot{"pregnancy_weeks": "12"}
    - form: initial_form
    - slot{"pregnancy_weeks": "12"}
    - slot{"requested_slot": "planned_pregnancy"}
* form: enter_data
    - form: initial_form
    - slot{"planned_pregnancy": "1"}
    - slot{"requested_slot": "first_pregnancy"}
* form: enter_data
    - form: initial_form
    - slot{"first_pregnancy": "1"}
    - slot{"requested_slot": "health_plan"}
* form: enter_data
    - form: initial_form
    - slot{"health_plan": "1"}
    - slot{"requested_slot": "pre_natal"}
* form: enter_data
    - form: initial_form
    - slot{"pre_natal": "1"}
    - form{"name": null}
    - slot{"requested_slot": null}

