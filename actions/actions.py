# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union, Optional

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType


class ValidateGetusernameForm(FormValidationAction):
    ''' Exemple of validation action'''
    print('----------------------------')

    def name(self) -> Text:
        return "validate_getusername_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        return []

    def validate_nom_personne(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        '''
            Validate nom_personne
        '''
        myintent = Tracker.latest_message['intent'].get('name')

        print("slot_value ------" + slot_value)
        print("myintent --------" + myintent)

        if(myintent == 'greet' or myintent == "bojour"):
            return {"nom_personne": None}

        if slot_value is not None:
            return {"nom_personne", slot_value}
        else:
            return {"nom_personne", None}


class ValidateRegisterForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_register_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        return []

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""

        myintent = Tracker.latest_message['intent'].get('name')

        print("slot_value ------" + slot_value)
        print("myintent --------" + myintent)

        if not slot_value:
            return {"registeremail": None}
        else:
            return {"registeremail": slot_value}


class ActionSubmitProject(Action):
    def name(self) -> Text:
        return "action_submitregister"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        user_name = tracker.get_slot("registeremail")
        print("email id  is  : ", user_name)

        dispatcher.utter_message(template="utter_details_thanks")
        return[]
