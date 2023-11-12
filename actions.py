from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionUtterGreet(Action):
    def name(self) -> Text:
        return "utter_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hi! Do you need help?")
        return []

class ActionUtterAffirm(Action):
    def name(self) -> Text:
        return "utter_affirm"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="How can I help you?")
        return []

class ActionUtterDeny(Action):
    def name(self) -> Text:
        return "utter_deny"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="I'm sorry, it seems I didn't understand your request.")
        return []

class ActionUtterDidThatHelp(Action):
    def name(self) -> Text:
        return "utter_did_that_help"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Did that information help you?")
        return []
    
class ActionUtterAuthorizationInfo(Action):
    def name(self) -> Text:
        return "utter_authorization_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="To authorize another person to act on your behalf, please follow the steps outlined on this page: https://www.gov.gr/en/ipiresies/polites-kai-kathemerinoteta/psephiaka-eggrapha-gov-gr/ekdose-exousiodoteses.")
        return []
    
class ActionUtterVaccinationInfo(Action):
    def name(self) -> Text:
        return "utter_vaccination_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="For information regarding the COVID-19 vaccination process, please visit the official government page: https://www.gov.gr/en/ipiresies/ugeia-kai-pronoia/koronoios-covid-19/pistopoietiko-emboliasmou.")
        return []

class ActionUtterBirthCertificate(Action):
    def name(self) -> Text:
        return "utter_birth_certificate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="For obtaining a birth certificate, please refer to the page: https://www.gov.gr/en/ipiresies/oikogeneia/gennese/pistopoietiko-genneses.")
        return []
    
class ActionUtterCheckDocumentValidity(Action):
    def name(self) -> Text:
        return "utter_check_document_validity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="To check the validity of documents, visit the official government page: https://www.gov.gr/en/ipiresies/polites-kai-kathemerinoteta/psephiaka-eggrapha-gov-gr/elegkhos-egkurotetas-eggraphon-gov-gr.")
        return []

class ActionUtterThanks(Action):
    def name(self) -> Text:
        return "utter_thanks"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="You're welcome!")
        return []

class ActionUtterGoodbye(Action):
    def name(self) -> Text:
        return "utter_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="It was my pleasure to serve you, bye!")
        return []