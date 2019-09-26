# got_it
* got_it OR affirm+got_it
    - utter_great

# got_it
* affirm+got_it+thank_you OR got_it+thank_you
    - utter_great
    - utter_welcome

# thank_you
* thank_you OR affirm+thank_you
    - utter_welcome

# thank_you+bye
* thank_you+bye OR bye+thank_you
    - utter_welcome
    - utter_bye

# bye
* bye
    - utter_bye

<!-- ## i_know_importance
* i_know_importance
    - utter_agree

## later
* later
  - utter_info_later -->

## 'Oi tudo bem?'
* greeting OR hello+greeting OR hello
    - action_greet_user
    - slot{"greeted_user": true}
* greeting_answer
    - utter_great
    - utter_ask_me_anything

## 'Oi tudo bem?'
* greeting OR hello+greeting OR hello
    - action_greet_user
    - slot{"greeted_user": true}
* greeting_back
    - utter_greet_answer
    - utter_ask_me_anything

## baby_not_moving
* baby_not_moving
    - utter_baby_not_moving

## usuario não tem duvidas
* no_question
    - utter_ask_me_later

## usuario não tem duvidas
* no_question
    - utter_ask_me_later
* affirm OR affirm+thank_you
    - utter_great

## usuario tem duvidas
* have_question OR affirm+have_question
    - utter_ask

## usuario tem duvidas
    - utter_ask_me_anything
* have_question OR affirm+have_question
    - utter_ask

## ok
    - action_get_answer
* affirm
    - utter_great

## estou gravida
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

## Oi, estou gravida
* hello+im_pregnant
    - utter_hello
    - action_congrats
    - slot{"is_pregnant": true}
    - utter_first_step
    - utter_ask_info
* affirm
  - form_initial
  - form{"name": "form_initial"}
  - form{"name": null}
  - utter_ask_me_anything

## start 1
* start
  - action_greet_user
  - slot{"greeted_user": true}
* affirm
  - form_initial
  - form{"name": "form_initial"}
  - form{"name": null}
  - utter_ask_me_anything 

## start 2
* start
  - action_greet_user
  - slot{"greeted_user": true}
* deny OR later
  - utter_info_later
  - utter_ask_me_anything

## start 3
* start
  - action_greet_user
  - slot{"greeted_user": true}
* affirm
  - form_initial
  - form{"name": "form_initial"}
* why_i_need_to_answer
  - utter_why_answer
  - form_initial
  - form{"name": null}
  - utter_ask_me_anything

## start 4
* start
  - action_greet_user
  - slot{"greeted_user": true}
* affirm
  - form_initial
  - form{"name": "form_initial"}
* stop
  - action_deactivate_form
  - form{"name": null}
  - utter_info_later
  - utter_ask_me_anything

## utter_ask_me_anything
    - utter_ask_me_anything
* affirm
    - utter_ask

## bot pergunta se fez o exame e o usuário fez
* ask_exam
    - utter_ask_exam
* affirm OR affirm+did_exam OR did_exam
    - action_doing_right_exam

## bot pergunta se fez o exame e o usuário fez
    - utter_ask_exam
* affirm OR affirm+did_exam OR did_exam
    - action_doing_right_exam

## bot pergunta se fez o exame e o usuário fez
* ask_exam
    - utter_ask_exam
* deny OR did_not_exam OR deny+did_not_exam
    - action_get_exam
    - utter_is_important_exam

## bot pergunta se fez o exame e o usuário fez
    - utter_ask_exam
* deny OR did_not_exam OR deny+did_not_exam
    - action_get_exam
    - utter_is_important_exam

## exame
    - utter_is_important_exam
* affirm+ill_do_it OR affirm OR ill_do_it
    - utter_great

## bot pergunta se fez o exame, o usuário fez mas quer saber o motivo da pergunta
    - utter_ask_exam  
* why_i_need_to_answer
    - utter_why_answer
* affirm OR affirm+did_exam OR did_exam
    - action_doing_right_exam

## bot pergunta se fez o exame, o usuário fez mas quer saber o motivo da pergunta
    - utter_ask_exam  
* why_i_need_to_answer
    - utter_why_answer
* deny OR did_not_exam OR deny+did_not_exam
    - action_get_exam
    - utter_is_important_exam

<!-- ## bot pergunta se fez o exame, o usuário fez e sabe a importância do exame
    - utter_ask_exam
* affirm OR affirm+did_exam OR did_exam
    - action_doing_right_exam
* i_know_importance
    - utter_agree -->

## form_health 1
* start_form_health
    - utter_ask_health_questions
* affirm
    - form_health
    - form{"name": "form_health"}
    - form{"name": null}

## form_health 2
* start_form_health
  - utter_ask_health_questions
* deny OR later
  - utter_info_later
  - utter_ask_me_anything

## form_health 3
* start_form_health
  - utter_ask_health_questions
* affirm
  - form_health
  - form{"name": "form_health"}
* why_i_need_to_answer
  - utter_why_answer
  - form_health
  - form{"name": null}

## form_health 4
* start_form_health
  - utter_ask_health_questions
* affirm
  - form_health
  - form{"name": "form_health"}
* stop OR stop_form
  - action_deactivate_form
  - form{"name": null}
  - utter_info_later
  - utter_ask_me_anything

## form_personal 1
* start_form_personal
    - utter_ask_personal_questions
* affirm
    - form_personal
    - form{"name": "form_personal"}
    - form{"name": null}

## form_personal 2
* start_form_personal
  - utter_ask_personal_questions
* deny OR later
  - utter_info_later
  - utter_ask_me_anything

## form_personal 3
* start_form_personal
  - utter_ask_personal_questions
* affirm
  - form_personal
  - form{"name": "form_personal"}
* why_i_need_to_answer
  - utter_why_answer
  - form_personal
  - form{"name": null}

## form_personal 4
* start_form_personal
  - utter_ask_personal_questions
* affirm
  - form_personal
  - form{"name": "form_personal"}
* stop OR stop_form
  - action_deactivate_form
  - form{"name": null}
  - utter_info_later
  - utter_ask_me_anything

## form_pregnancy 1
* start_form_pregnancy
    - utter_ask_pregnancy_questions
* affirm
    - form_pregnancy
    - form{"name": "form_pregnancy"}
    - form{"name": null}

## form_pregnancy 2
* start_form_pregnancy
  - utter_ask_pregnancy_questions
* deny OR later
  - utter_info_later
  - utter_ask_me_anything

## form_pregnancy 3
* start_form_pregnancy
  - utter_ask_pregnancy_questions
* affirm
  - form_pregnancy
  - form{"name": "form_pregnancy"}
* why_i_need_to_answer
  - utter_why_answer
  - form_pregnancy
  - form{"name": null}

## form_pregnancy 4
* start_form_pregnancy
  - utter_ask_pregnancy_questions
* affirm
  - form_pregnancy
  - form{"name": "form_pregnancy"}
* stop OR stop_form
  - action_deactivate_form
  - form{"name": null}
  - utter_info_later
  - utter_ask_me_anything

## welcome
* welcome
    - utter_great

## out_of_scope
* out_of_scope
    - utter_canthelp
    - utter_explain_whatspossible

## welcome
* welcome
    - utter_great

## Generated Story -4178839390444423351
* hello
    - action_greet_user
    - slot{"greeted_user": true}

## ask_normal_birth_pain
* ask_normal_birth_pain
    - action_get_answer

## ask_exercise_help_normal_birth
* ask_exercise_help_normal_birth
    - action_get_answer

## ask_breast_milk_normal_birth
* ask_breast_milk_normal_birth
    - action_get_answer

## ask_normal_birth_recovery
* ask_normal_birth_recovery
    - action_get_answer

## ask_normal_birth_duration
* ask_normal_birth_duration
    - action_get_answer

## ask_birth_transmit_disease
* ask_birth_transmit_disease
    - action_get_answer

## ask_avoid_normal_birth
* ask_avoid_normal_birth
    - action_get_answer

## ask_ideal_birth_older_women
* ask_ideal_birth_older_women
    - action_get_answer

## ask_calculate_fertile_period
* ask_calculate_fertile_period
    - action_get_answer

## ask_late_menstruation
* ask_late_menstruation
    - action_get_answer

## ask_do_pregnancy_test
* ask_do_pregnancy_test
    - action_get_answer

## ask_normal_swollen_foot
* ask_normal_swollen_foot
    - action_get_answer

## ask_how_long_milk_come_down
* ask_how_long_milk_come_down
    - action_get_answer

## ask_normal_fever_milk_comes_down
* ask_normal_fever_milk_comes_down
    - action_get_answer

## ask_prevent_milk_stumbling
* ask_prevent_milk_stumbling
    - action_get_answer

## ask_pain_breastfeed
* ask_pain_breastfeed
    - action_get_answer

## ask_thirst_breastfeed
* ask_thirst_breastfeed
    - action_get_answer

## ask_feeling_sad
* ask_feeling_sad
    - action_get_answer

## ask_diet_breastfeed
* ask_diet_breastfeed
    - action_get_answer

## ask_gain_weight_pregnancy
* ask_gain_weight_pregnancy
    - action_get_answer

## ask_when_have_sex
* ask_when_have_sex
    - action_get_answer

## ask_stretch_marks
* ask_stretch_marks
    - action_get_answer

## ask_desire_sex
* ask_desire_sex
    - action_get_answer

## ask_loose_vagina
* ask_loose_vagina
    - action_get_answer

## ask_sagging_breasts_breastfeed
* ask_sagging_breasts_breastfeed
    - action_get_answer

## ask_body_back_normal
* ask_body_back_normal
    - action_get_answer

## ask_back_exercise
* ask_back_exercise
    - action_get_answer

## ask_loss_hair_breastfeed
* ask_loss_hair_breastfeed
    - action_get_answer

## ask_exercise_impair_milk
* ask_exercise_impair_milk
    - action_get_answer

## ask_normal_bleeding_after_birth
* ask_normal_bleeding_after_birth
    - action_get_answer

## ask_normal_menstruation_breastfeed
* ask_normal_menstruation_breastfeed
    - action_get_answer

## ask_dye_hair_breastfeed
* ask_dye_hair_breastfeed
    - action_get_answer

## ask_normal_lose_weight_breastfeed
* ask_normal_lose_weight_breastfeed
    - action_get_answer

## ask_normal_feeling_tired
* ask_normal_feeling_tired
    - action_get_answer

## ask_normal_bigger_foot
* ask_normal_bigger_foot
    - action_get_answer

## ask_pregnant_menopause
* ask_pregnant_menopause
    - action_get_answer

## ask_sex_bad_pregnancy
* ask_sex_bad_pregnancy
    - action_get_answer

## ask_feces_normal_birth
* ask_feces_normal_birth
    - action_get_answer

## ask_sore_sex_after_birth
* ask_sore_sex_after_birth
    - action_get_answer

## ask_have_sex_until_month
* ask_have_sex_until_month
    - action_get_answer

## ask_receive_oral_sex
* ask_receive_oral_sex
    - action_get_answer

## ask_smell_sweat_stronger
* ask_smell_sweat_stronger
    - action_get_answer

## ask_sex_hurt_baby
* ask_sex_hurt_baby
    - action_get_answer

## ask_choose_birth_type_public
* ask_choose_birth_type_public
    - action_get_answer

## ask_pregnant_eat_two
* ask_pregnant_eat_two
    - action_get_answer

## ask_avoid_cleaning_products
* ask_avoid_cleaning_products
    - action_get_answer

## ask_best_position_baby_sleep
* ask_best_position_baby_sleep
    - action_get_answer

## ask_what_vaccines_baby
* ask_what_vaccines_baby
    - action_get_answer

## ask_when_go_pediatrician
* ask_when_go_pediatrician
    - action_get_answer

## ask_care_baby_belly_button
* ask_care_baby_belly_button
    - action_get_answer

## ask_birth_control_difficult_pregnancy
* ask_birth_control_difficult_pregnancy
    - action_get_answer

## ask_how_many_pounds_pregnancy
* ask_how_many_pounds_pregnancy
    - action_get_answer

## ask_how_long_breastfeed
* ask_how_long_breastfeed
    - action_get_answer

## ask_how_long_healthy_pregnant
* ask_how_long_healthy_pregnant
    - action_get_answer

## ask_high_risk_normal_birth 
* ask_high_risk_normal_birth
    - action_get_answer

## ask_ultrasound_hurt_baby
* ask_ultrasound_hurt_baby
    - action_get_answer

## ask_baby_feel_sex
* ask_baby_feel_sex
    - action_get_answer

## ask_how_many_weeks_sex_baby
* ask_how_many_weeks_sex_baby
    - action_get_answer

## ask_how_long_pregnancy_last
* ask_how_long_pregnancy_last
    - action_get_answer

## ask_dont_know_who_father_is
* ask_dont_know_who_father_is
    - action_get_answer

## ask_how_calculate_fertilization_date
* ask_how_calculate_fertilization_date
    - action_get_answer

## ask_food_desire_baby_appearance
* ask_food_desire_baby_appearance
    - action_get_answer

## ask_anesthesia_dentist
* ask_anesthesia_dentist
    - action_get_answer

## ask_contraceptive_pill_after_birth
* ask_contraceptive_pill_after_birth
    - action_get_answer

## ask_invite_accompany_birth
* ask_invite_accompany_birth
    - action_get_answer

## ask_cesarean_can_normal_birth
* ask_cesarean_can_normal_birth
    - action_get_answer

## ask_main_exams_prenatal
* ask_main_exams_prenatal
    - action_get_answer

## ask_allowed_exercises
* ask_allowed_exercises
    - action_get_answer

## ask_allowed_depilation
* ask_allowed_depilation
    - action_get_answer

## ask_needed_feed
* ask_needed_feed
    - action_get_answer

## ask_needed_vaccine
* ask_needed_vaccine
    - action_get_answer

## ask_signs_labor
* ask_signs_labor
    - action_get_answer

## ask_ideal_weight
* ask_ideal_weight
    - action_get_answer

## ask_best_sleeping_position
* ask_best_sleeping_position
    - action_get_answer

## ask_best_childbirth
* ask_best_childbirth
    - action_get_answer

## ask_cases_forceps
* ask_cases_forceps
    - action_get_answer

## ask_medicine
* ask_medicine
    - action_get_answer

## ask_not_allowed_exercises
* ask_not_allowed_exercises
    - action_get_answer

## ask_not_allowed_food
* ask_not_allowed_food
    - action_get_answer

## ask_not_allowed_vaccine
* ask_not_allowed_vaccine
    - action_get_answer

## ask_what_is_prenatal
* ask_what_is_prenatal
    - action_get_answer

## ask_what_is_postpartum
* ask_what_is_postpartum
    - action_get_answer

## ask_what_is_loco
* ask_what_is_loco
    - action_get_answer

## ask_what_is_miscarriage
* ask_what_is_miscarriage
    - action_get_answer

## ask_what_is_amniotic_fluid
* ask_what_is_amniotic_fluid
    - action_get_answer

## ask_what_is_pre_eclampsia
* ask_what_is_pre_eclampsia
    - action_get_answer

## ask_what_is_folic_acid
* ask_what_is_folic_acid
    - action_get_answer

## ask_what_is_episiotomy
* ask_what_is_episiotomy
    - action_get_answer

## ask_what_is_trichotomy
* ask_what_is_trichotomy
    - action_get_answer

## ask_what_is_forceps
* ask_what_is_forceps
    - action_get_answer

## ask_what_is_braxton_hicks
* ask_what_is_braxton_hicks
    - action_get_answer

## ask_what_is_eclampsia
* ask_what_is_eclampsia
    - action_get_answer

## ask_what_is_uterine_height
* ask_what_is_uterine_height
    - action_get_answer

## ask_what_is_amniocentesis
* ask_what_is_amniocentesis
    - action_get_answer

## ask_what_is_bcf
* ask_what_is_bcf
    - action_get_answer

## ask_what_is_term_baby
* ask_what_is_term_baby
    - action_get_answer

## ask_what_is_deflected_baby
* ask_what_is_deflected_baby
    - action_get_answer

## ask_what_is_pelvic
* ask_what_is_pelvic
    - action_get_answer

## ask_what_is_choric
* ask_what_is_choric
    - action_get_answer

## ask_what_is_beta_hcg
* ask_what_is_beta_hcg
    - action_get_answer

## ask_what_is_colostrum
* ask_what_is_colostrum
    - action_get_answer

## ask_what_is_pdd
* ask_what_is_pdd
    - action_get_answer

## ask_what_is_hyperemesis_gravidarum
* ask_what_is_hyperemesis_gravidarum
    - action_get_answer

## ask_what_is_isthmus_cervical
* ask_what_is_isthmus_cervical
    - action_get_answer

## ask_what_is_nesting
* ask_what_is_nesting
    - action_get_answer

## ask_what_is_oxytocin
* ask_what_is_oxytocin
    - action_get_answer

## ask_what_is_previous_placenta
* ask_what_is_previous_placenta
    - action_get_answer

## ask_what_is_epidural_anesthesia
* ask_what_is_epidural_anesthesia
    - action_get_answer

## ask_what_is_cephalic_perimeter
* ask_what_is_cephalic_perimeter
    - action_get_answer

## ask_what_is_spinal_anesthesia
* ask_what_is_spinal_anesthesia
    - action_get_answer

## ask_what_is_basal_temperature
* ask_what_is_basal_temperature
    - action_get_answer

## ask_what_is_nuchal_translucency
* ask_what_is_nuchal_translucency
    - action_get_answer

## ask_can_paint_nails
* ask_can_paint_nails
    - action_get_answer

## ask_can_treatment_varicose_veins
* ask_can_treatment_varicose_veins
    - action_get_answer

## ask_can_seabathe
* ask_can_seabathe
    - action_get_answer

## ask_can_lymphatic_drainage
* ask_can_lymphatic_drainage
    - action_get_answer

## ask_can_almond_oil
* ask_can_almond_oil
    - action_get_answer

## ask_can_sick_friend
* ask_can_sick_friend
    - action_get_answer

## ask_when_pregnant_again
* ask_when_pregnant_again
    - action_get_answer

## ask_diet_after_delivery
* ask_diet_after_delivery
    - action_get_answer

## ask_when_start_breastfeeding
* ask_when_start_breastfeeding
    - action_get_answer

## ask_pregnant_takes_pill
* ask_pregnant_takes_pill
    - action_get_answer

## ask_can_pregnant_anal_sex
* ask_can_pregnant_anal_sex
    - action_get_answer

## ask_necessary_condom_pregnant
* ask_necessary_condom_pregnant
    - action_get_answer

## ask_can_pregnant_orgasm
* ask_can_pregnant_orgasm
    - action_get_answer

## ask_when_period_return
* ask_when_period_return
    - action_get_answer

## ask_consult_after_childbirth
* ask_consult_after_childbirth
    - action_get_answer

## ask_normal_birth_better_mother
* ask_normal_birth_better_mother
    - action_get_answer

## ask_normal_birth_better_baby
* ask_normal_birth_better_baby
    - action_get_answer

## ask_when_go_maternity
* ask_when_go_maternity
    - action_get_answer

## ask_while_breastfeeding_pregnant
* ask_while_breastfeeding_pregnant
    - action_get_answer

## ask_can_paint_hair
* ask_can_paint_hair
    - action_get_answer

## ask_types_childbirth
* ask_types_childbirth
    - action_get_answer

## ask_what_is_forceps_childbirth
* ask_what_is_forceps_childbirth
    - action_get_answer

## ask_what_is_leboyer_childbirth
* ask_what_is_leboyer_childbirth
    - action_get_answer

## ask_what_is_squatting_childbirth
* ask_what_is_squatting_childbirth
    - action_get_answer

## ask_what_is_water_childbirth
* ask_what_is_water_childbirth
    - action_get_answer

## ask_what_is_natural_childbirth
* ask_what_is_natural_childbirth
    - action_get_answer

## ask_what_is_humanized_childbirth
* ask_what_is_humanized_childbirth
    - action_get_answer

## ask_who_receive_maternity_leave
* ask_who_receive_maternity_leave
    - action_get_answer

## ask_unemployed_receive_maternity_leave
* ask_unemployed_receive_maternity_leave
    - action_get_answer

## ask_pregnant_women_fired
* ask_pregnant_women_fired
    - action_get_answer

## ask_what_is_maternity_pay
* ask_what_is_maternity_pay
    - action_get_answer

## ask_how_much_salary_maternity_leave
* ask_how_much_salary_maternity_leave
    - action_get_answer

## ask_how_apply_maternity_leave
* ask_how_apply_maternity_leave
    - action_get_answer

## ask_how_long_maternity_leave
* ask_how_long_maternity_leave
    - action_get_answer

## ask_when_maternity_leave_start
* ask_when_maternity_leave_start
    - action_get_answer

## ask_add_vacation_maternity_leave
* ask_add_vacation_maternity_leave
    - action_get_answer

## ask_father_have_paternity_leave
* ask_father_have_paternity_leave
    - action_get_answer

## ask_what_is_maternity_leave
* ask_what_is_maternity_leave
    - action_get_answer

## ask_what_is_maternity_leave
* ask_what_is_maternity_leave
    - action_get_answer

## ask_what_is_cesarean_childbirth
* ask_what_is_cesarean_childbirth
    - action_get_answer

## ask_can_discolor_hair
* ask_can_discolor_hair
    - action_get_answer

## ask_can_ride_motorcycle
* ask_can_ride_motorcycle
    - action_get_answer

## ask_can_horseback_riding
* ask_can_horseback_riding
    - action_get_answer

## ask_can_ride_bike
* ask_can_ride_bike
    - action_get_answer

## ask_can_take_laxative
* ask_can_take_laxative
    - action_get_answer

## ask_can_take_bath
* ask_can_take_bath
    - action_get_answer

## ask_can_steam_room
* ask_can_steam_room
    - action_get_answer

## ask_can_chili
* ask_can_chili
    - action_get_answer

## ask_can_coffee
* ask_can_coffee
    - action_get_answer

## ask_can_sunbathe
* ask_can_sunbathe
    - action_get_answer

## ask_can_moisturizer
* ask_can_moisturizer
    - action_get_answer

## ask_can_travel
* ask_can_travel
    - action_get_answer

## ask_can_ladder
* ask_can_ladder
    - action_get_answer

## ask_can_high_heels
* ask_can_high_heels
    - action_get_answer

## ask_can_japanese_food
* ask_can_japanese_food
    - action_get_answer

## ask_can_dentist
* ask_can_dentist
    - action_get_answer

## ask_can_exercise
* ask_can_exercise
    - action_get_answer

## ask_can_alcohol
* ask_can_alcohol
    - action_get_answer

## ask_can_drugs
* ask_can_drugs
    - action_get_answer

## ask_can_smoke
* ask_can_smoke
    - action_get_answer

## ask_can_x_ray
* ask_can_x_ray
    - action_get_answer

## ask_can_sex
* ask_can_sex
    - action_get_answer

## ask_can_raw_meat
* ask_can_raw_meat
    - action_get_answer

## ask_can_soda
* ask_can_soda
    - action_get_answer

## ask_can_sweetener
* ask_can_sweetener
    - action_get_answer

## ask_can_vaccine
* ask_can_vaccine
    - action_get_answer

## ask_can_sleep_stomach
* ask_can_sleep_stomach
    - action_get_answer

## ask_can_hot_wax
* ask_can_hot_wax
    - action_get_answer

## ask_can_pap_smear
* ask_can_pap_smear
    - action_get_answer

## ask_can_drive
* ask_can_drive
    - action_get_answer

## ask_when_start_prenatal
* ask_when_start_prenatal
    - action_get_answer

## ask_when_episiotomy
* ask_when_episiotomy
    - action_get_answer

## ask_when_baby_move
* ask_when_baby_move
    - action_get_answer

## ask_when_start_braxton_hicks
* ask_when_start_braxton_hicks
    - action_get_answer

## ask_when_exam_feces
* ask_when_exam_feces
    - action_get_answer

## ask_when_exam_blood_glucose
* ask_when_exam_blood_glucose
    - action_get_answer

## ask_when_exam_blood
* ask_when_exam_blood
    - action_get_answer

## ask_when_exam_urine
* ask_when_exam_urine
    - action_get_answer

## ask_when_exam_intravaginal_ultrasound
* ask_when_exam_intravaginal_ultrasound
    - action_get_answer

## ask_when_exam_nuchal_translucency_ultrasound
* ask_when_exam_nuchal_translucency_ultrasound
    - action_get_answer

## ask_when_exam_screening_gestational_diabetes
* ask_when_exam_screening_gestational_diabetes
    - action_get_answer

## ask_when_exam_screening_beta_hermolytic_streptococcus
* ask_when_exam_screening_beta_hermolytic_streptococcus
    - action_get_answer

## ask_when_exam_third_trimester_ultrasound
* ask_when_exam_third_trimester_ultrasound
    - action_get_answer

## ask_when_stop_nausea
* ask_when_stop_nausea
    - action_get_answer

## ask_symptom_miscarriage
* ask_symptom_miscarriage
    - action_get_answer

## ask_symptom_pregnancy
* ask_symptom_pregnancy
    - action_get_answer

## ask_symptom_premature_birth
* ask_symptom_premature_birth
    - action_get_answer

## ask_symptom_pre_eclampsia
* ask_symptom_pre_eclampsia
    - action_get_answer

## ask_why_sleep
* ask_why_sleep
    - action_get_answer

## ask_why_nausea
* ask_why_nausea
    - action_get_answer

## ask_risk_factor_pregnancy
* ask_risk_factor_pregnancy
    - action_get_answer

## ask_risk_factor_premature_birth
* ask_risk_factor_premature_birth
    - action_get_answer

## ask_causes_pre_eclampsia
* ask_causes_pre_eclampsia
    - action_get_answer

## ask_causes_premature_birth
* ask_causes_premature_birth
    - action_get_answer

## ask_what_to_do_bag
* ask_what_to_do_bag
    - action_get_answer

## ask_what_to_do_bleeding
* ask_what_to_do_bleeding
    - action_get_answer

## ask_importance_breast_feeding
* ask_importance_breast_feeding
    - action_get_answer

## ask_how_to_know_bag_burst
* ask_how_to_know_bag_burst
    - action_get_answer

## ask_how_to_know_childbirth
* ask_how_to_know_childbirth
    - action_get_answer

## ask_how_to_know_pregnancy
* ask_how_to_know_pregnancy
    - action_get_answer

## ask_prevent_premature_birth
* ask_prevent_premature_birth
    - action_get_answer

## ask_prevent_pre_eclampsia
* ask_prevent_pre_eclampsia
    - action_get_answer

## complain_nauseas
* complain_nauseas
    - action_get_answer

## complain_heartburn
* complain_heartburn
    - action_get_answer

## complain_salivation
* complain_salivation
    - action_get_answer

## complain_weakness
* complain_weakness
    - action_get_answer

## complain_flatulence
* complain_flatulence
    - action_get_answer

## complain_constipation
* complain_constipation
    - action_get_answer

## complain_discharge
* complain_discharge
    - action_get_answer

## complain_urine
* complain_urine
    - action_get_answer

## complain_breasts
* complain_breasts
    - action_get_answer

## complain_varicose_veins
* complain_varicose_veins
    - action_get_answer

## complain_body
* complain_body
    - action_get_answer

## complain_headache
* complain_headache
    - action_get_answer

## complain_cramps
* complain_cramps
    - action_get_answer

## complain_stretch_marks
* complain_stretch_marks
    - action_get_answer

## complain_melasma
* complain_melasma
    - action_get_answer

## complain_gums
* complain_gums
    - action_get_answer

## complain_shortness_breath
* complain_shortness_breath
    - action_get_answer

## complain_bleeding
* complain_bleeding
    - action_get_answer

## complain_colic
* complain_colic
    - action_get_answer

## ask_goal_exam_feces
* ask_goal_exam_feces
    - action_get_answer

## ask_goal_exam_blood_glucose
* ask_goal_exam_blood_glucose
    - action_get_answer

## ask_goal_exam_blood
* ask_goal_exam_blood
    - action_get_answer

## ask_goal_exam_urine
* ask_goal_exam_urine
    - action_get_answer

## ask_goal_exam_intravaginal_ultrasound
* ask_goal_exam_intravaginal_ultrasound
    - action_get_answer

## ask_goal_exam_nuchal_translucency_ultrasound
* ask_goal_exam_nuchal_translucency_ultrasound
    - action_get_answer

## ask_goal_exam_screening_gestational_diabetes
* ask_goal_exam_screening_gestational_diabetes
    - action_get_answer

## ask_goal_exam_screening_beta_hermolytic_streptococcus
* ask_goal_exam_screening_beta_hermolytic_streptococcus
    - action_get_answer

## ask_goal_exam_third_trimester_ultrasound
* ask_goal_exam_third_trimester_ultrasound
    - action_get_answer

## ask_how_works_prenatal
* ask_how_works_prenatal
    - action_get_answer
